from django.shortcuts import render
from .models import FullForms
from .forms import FullformForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail


def index(request):
    ff = FullForms.objects.all().order_by('shortForm')
    ff_filtered = []
    for i in ff:
        if i.approve:
            ff_filtered.append(i)

    return render(request, 'fullforms/index.html',
                  {
                      'ff': ff_filtered

                  })


@login_required
def addfullform(request):
    form_class = FullformForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            usr = User.objects.get(username=request.user)
            fullform = form.save(commit=False)
            fullform.user = request.user
            usr.points += 1
            usr.save()
            fullform.save()
            send_mail(
                'Your fullform has been added',
                'Thank you for contributing to full forms.',
                'admins@thepcstudio.com',
                [usr.email],
                fail_silently=False,
            )
            return redirect(index)

    elif request.method == 'GET':
        form = form_class()

    return render(request, 'fullforms/add_fullform.html', {
        'form': form,
    })


def profile(request, uname):
    
    if User.objects.filter(username=uname).exists():
        isExists = True
        ff = FullForms.objects.filter(user__username=uname).order_by('shortForm')
        ff_filtered = []
        for i in ff:
            if i.approve:
                ff_filtered.append(i)
    else:
        isExists = False
        ff_filtered = []
    return render(request, 'registration/user_profile.html', {
        'username': uname, 'isExists': isExists, 'ff': ff_filtered,
    })


def leaderboard(request):
    usr = User.objects.all().order_by('-points')
    return render(request, 'fullforms/leaderboard.html', {
        'usr': usr
    })