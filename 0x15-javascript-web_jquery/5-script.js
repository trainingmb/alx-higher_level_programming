//Adds a <li> element to a list when the user clicks on the tag DIV#add_item
$(document).ready(function () {
  $('div#add_item').click(function () {
  	$('UL.my_list').append('<li>Item</li>');
  });
});
