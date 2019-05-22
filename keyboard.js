$(function(){
	var $textarea = $('#textarea'),
		shift = false,
		capslock = false;
	
	$('#keyboard li').click(function(){
		var $this = $(this),
			character = $this.html(); // If it's a lowercase letter, nothing happens to this variable
		
		// Delete
		if ($this.hasClass('delete')) {
			var html = $textarea.html();
			
			$textarea.html(html.substr(0, html.length - 1));
			return false;
		}
    
		// Special characters
		if ($this.hasClass('symbol')) character = $('span:visible', $this).html();
			
		// Add the character
		$textarea.html($textarea.html() + character);
	});
});