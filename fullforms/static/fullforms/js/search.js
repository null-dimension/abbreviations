var searchText;
function move()
{

  searchText = '#' + document.getElementById('textBox').value;
  searchText = searchText.toUpperCase();
  //document.getElementById("bSearch").setAttribute('href', '#' + searchText);
  if(searchText.length > 1)
  {
        document.getElementById('searchMsg').innerHTML = '';
        try
        {
           $("html, body").animate({
                scrollTop: $(searchText).offset().top
            }, 1000);
        }
        catch(err)
        {
            document.getElementById('searchMsg').innerHTML = 'No results.';

        }
  }
  else
    document.getElementById('searchMsg').innerHTML = 'Search box is empty.';

   searchText = '';
}

