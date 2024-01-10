//Fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$(document).ready(function () {
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(result){
  results = result.results;
    $.each(results, function(i, field){
      $("UL#list_movies").append($('<li></li').text(field.title));
    });
  });
});
