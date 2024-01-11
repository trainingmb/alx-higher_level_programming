//Fetches from https://hellosalut.stefanbohacek.dev/?lang=<> and displays the value of hello from that fetch in the HTML tag DIV#hello.
$(document).ready(function () {
  $('input#btn_translate').click(function () {
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + $('input#language_code').val(),
      function(result){
        $('DIV#hello').text(result.hello);
      });
  });
  $('input#language_code').keypress(function (e) {
    if (e.which == 13) {
      $('input#btn_translate').click();
    }
  });
});
