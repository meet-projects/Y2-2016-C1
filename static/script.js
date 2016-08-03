$("document").ready(function(){

$("#food-div").hide();
$("#places-div").hide();
$("#info-div").hide();

		
	

	$("#info").change(function () { 
		console.log('click');
		console.log($('#info'));
		if ($("#info").is(":checked") ){
			$("#info-div").show(); 
		
			console.log('should hide');
		}
	}
	);
	$("#food").change(function () { 
		console.log('click');
		console.log($('#food'));
		if ($("#food").is(":checked") ){
			$("#food-div").show(); 
		
			console.log('should hide');
		}
	}
	);
	$("#place").change(function () { 
		console.log('click');
		console.log($('#place'));
		if ($("#place").is(":checked") ){
			$("#places-div").show(); 
		
			console.log('should hide');
		}
	}
	);

});

