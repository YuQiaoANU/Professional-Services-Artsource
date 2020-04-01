$(document).ready(function() {
	$("#checkArtist").on('click', function(){
		clickArtistSwitch()
	});

	$("#interest_switch").on('click', function(){
		clickInterestSwitch()
	});

	$("#addition_switch").on('click', function(){
		clickAdditionSwitch()
	});

	var clickArtistSwitch = function() {
		var refereeMenu=document.getElementById('refereeMenu');
		if ($("#checkArtist").is(':checked')) {
			refereeMenu.style.display="block";
		} else {
			refereeMenu.style.display="none";
		}
	};

	var clickInterestSwitch = function() {
		var interestList=document.getElementById('interest');
		var arrow=document.getElementById('interest_arrow');
		if ($("#interest_switch").is(':checked')) {
			interestList.style.display="block";
			arrow.className='arrow-top';
		} else {
			interestList.style.display="none";
			arrow.className='arrow-bottom';
		}
	};

	var clickAdditionSwitch = function() {
		var additionalInfo=document.getElementById('additionalInfo');
		var arrow=document.getElementById('addition_arrow');
		if ($("#addition_switch").is(':checked')) {
			additionalInfo.style.display="block";
			arrow.className='arrow-top';
		} else {
			additionalInfo.style.display="none";
			arrow.className='arrow-bottom';
		}
	};


});


