//Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
$(document).ready(function () {
  $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(result){
  $('DIV#hello').text(result.hello);
  });
});
