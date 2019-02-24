function closeWarning() {
	var x = document.getElementById("warning");
	x.style.display = "none";
}

/**
$(document).ready(function(){
	//'use strict';

	$('#search_autocomplete').swiftypeSearch({
  		resultContainingElement: '#search-container',
  		engineKey: 'H2-SAPvc79Up6eeAkona'
	});


	var searchArray = $.map(search, function (value, key) { return { value: value, data: key };});
	
	// Initialize autocomplete
	$('#search_autocomplete').autocomplete({
		lookup: searchArray,
		appendTo: '#suggestions-container'
	});

}); //Document Ready End
 **/