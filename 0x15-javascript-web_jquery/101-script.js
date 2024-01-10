//Adds, removes and clears LI elements from a list when the user clicks:
$(document).ready(function () {
  $('div#add_item').click(function () {
        $('UL.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function () {
  	$('UL.my_list li:last-child').remove();
  });
  $('div#clear_list').click(function () {
  	$('UL.my_list').text('');
  });
});
