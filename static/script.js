$("document").ready(function(){

$("#food-div").hide();
$("#places-div").hide();
$("#info-div").hide();

		
	

	$("#info").click(function () { 
			$("#info-div").show(); 
	}
	);
	$("#food").click(function () { 
			$("#food-div").show(); 
		
		
	}
	);
	$("#place").click(function () { 
			$("#places-div").show(); 

	}
	);

});

