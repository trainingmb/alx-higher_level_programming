//Add red to the class of the header text on clicking DIV tag 
$(document).ready(function () {
  $('div#red_header').click(function () {
    $('header').addClass('red');
  });
});
