//Change the color of the header text on clicking DIV tag 
$(document).ready(function () {
  $('div#red_header').click(function () {
    $('header').css('color', '#FF0800');
  });
});
