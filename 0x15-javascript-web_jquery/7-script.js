//Fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$(document).ready(function () {
  $.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(result){
    $('div#character').text(result.name);
  });
});
