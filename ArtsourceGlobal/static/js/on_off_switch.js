$(document).ready(function() {
	$("#checkArtist").on('click', function(){
		clickSwitch()
	});

	var clickSwitch = function() {
		var refereeMenu=document.getElementById('refereeMenu');
		if ($("#checkArtist").is(':checked')) {
			console.log("on sate");
			refereeMenu.style.display="block";
		} else {
			refereeMenu.style.display="none";
			console.log("off state");
		}
	};
});
