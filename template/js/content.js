
function movies(){

	$.ajax({
		url: 'ajax/movies.html',
		type: 'GET',
		dataType: 'HTML',
		success: function(response){
			$('#content').html(response);

			window.location.hash = 'content';
		}
	})



}

function tvshows(){

	$.ajax({
		url: 'ajax/tvshows.html',
		type: 'GET',
		dataType: 'HTML',
		success: function(response){
			$('#content').html(response);

			window.location.hash = 'content';
		}
	})
}