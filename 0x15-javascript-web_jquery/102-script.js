//Fetches from https://hellosalut.stefanbohacek.dev/?lang=<> and displays the value of hello from that fetch in the HTML tag DIV#hello.
$(document).ready(function () {
  $('input#btn_translate').click(function () {
    console.log($('input#language_code').val());
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + $('input#language_code').val(),
      function(result){
        $('DIV#hello').text(result.hello);
      });
  });
});
