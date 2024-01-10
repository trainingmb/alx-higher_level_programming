//Toogle class between red and green for header text on clicking DIV tag 
$(document).ready(function () {
  $('div#toggle_header').click(function () {
  	if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
    else {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
  });
});
