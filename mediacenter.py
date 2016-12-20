import webbrowser
import os
import re

# Main HTML ouput of the final results
htmlcontent = '''
<!DOCTYPE html PUBLIC"-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!--CSS Responsbile for Background Video-->
<link rel="stylesheet" href="css/video.css">
<link rel="stylesheet" href="css/videomodal.css">

<link href='http://fonts.googleapis.com/css?family=Buenard:700' rel='stylesheet' type='text/css'>

<!--Google jQuery API-->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<!--jScript Responsible for Playing Video-->
<script src="http://pupunzi.com/mb.components/mb.YTPlayer/demo/inc/jquery.mb.YTPlayer.js"></script>

<!--jScript Responsible for calling mb.YTPlayer-->
<script type="text/javascript" src="js/video.js"></script>

<!--Jscript responsible for loading AJAX Content-->
<script type="text/javascript" src="js/content.js"></script>

<!--jScript for Animation and Modal-->
<script type="text/javascript" src="js/animate.js"></script>
<script type="text/javascript" src="js/modal.js"></script>


<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>




	<title>Matthew's Movies & TV Shows</title>
</head>
<body>

<!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>

          <div>
          	<center>
          		<b>STORY LINE</b>
          		<p class="content-story"></p>
          	</center>
          	<p class="content-ratings"></p>
          	<p class="content-seasons"></p>
          	<p class="content-episodes"></p>
          	<p class="content-status"></p>
          	
          </div>
        </div>
      </div>
    </div>

<section class="content-section video-section">
  <div class="pattern-overlay">
  <a id="bgndVideo" class="player" data-property="{videoURL:'https://www.youtube.com/watch?v=QRmKa7vvct4',containment:'.video-section', quality:'large', autoPlay:true, mute:true, opacity:1}">bg</a>
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
        <h1>Movies & TV Shows</h1>  
        <h3><button onclick="movies()" type="button" class="btn btn-success btn-lg">Movies</button> <button onclick="tvshows()" class="btn btn-danger btn-lg">TV Shows</button></h3>
     </div>
      </div>
    </div>
  </div>
</section>

<br><br><br>


    <div class="container" id="content">

      <div class="starter-template">
        <h1>Welcome</h1>
        <p class="lead">Here you'll see a collection of my favorite Movies and TV Shows.</p>
      </div>

    </div>
<!-- /.container -->

  
  </body>



</body>
</html>
'''

# HTML Layout of a Movie Object
movie_tile_content = '''
<div class="col-md-6 col-lg-4 content-tile text-center"
data-movie-story="{movieStory}" data-movie-ratings="{movieRatings}"
data-trailer-youtube-id="{movieTrailer}" data-toggle="modal"
data-target="#trailer">
    <img src="{moviePoster}" width="220" height="342"></img>
    <h2>{movieTitle}</h2>
</div>
'''
# HTML layput of a TV Show Object
tvshow_tile_content = '''
<div class="col-md-6 col-lg-4 content-tile text-center" data-trailer-youtube-id="{tvTrailer}" data-tvshow-story="{tvStory}" data-tvshow-ratings="{tvRatings}" data-tvshow-seasons="{tvSeasons}" data-tvshow-episodes="{tvEpisodes}" data-tvshow-status="{tvStatus}" data-toggle="modal" data-target="#trailer">
    <img src="{tvPoster}" width="220" height="342"></img>
    <h2>{tvTitle}</h2>
</div>
'''

# This method will loop through a list of movie objects and append the
# appropriate values from an object to a movie HTML layout 
def create_movie_tiles_content(movies):
	content = ''
	for movie in movies:
		youtubeID = re.search(r'(?<=v=)[^&#]+', movie.trailer)
		youtubeID = youtubeID or re.search(r'(?<=be/)[^&#]+', movie.trailer)
		trailerID = youtubeID.group(0) if youtubeID else None

		content +=movie_tile_content.format(
			movieTitle = movie.title,
			moviePoster = movie.poster,
			movieTrailer = trailerID,
                        movieStory = movie.story,
                        movieRatings = movie.ratings
			)

	return content

# This method will loop through a list of TV Show objects and append
# the appropriate values from the objects into the TV Show HTML layout
def create_tv_tiles_content(seriesList):
        content = ''
        for series in seriesList:
                youtubeID = re.search(r'(?<=v=)[^&#]+', series.trailer)
                youtubeID = youtubeID or re.search(r'(?<=be/)[^&#]+', series.trailer)
                trailerID = youtubeID.group(0) if youtubeID else None

                content +=tvshow_tile_content.format(
                        tvTitle = series.title,
                        tvPoster = series.poster,
                        tvTrailer = trailerID,
                        tvStory = series.story,
                        tvRatings = series.ratings,
                        tvSeasons = series.seasons,
                        tvEpisodes = series.episodes,
                        tvStatus = series.status
                        )

        return content

# This method is responsible for creating the output HTML files
# from the input of TV Show and Movie obejcts 
def open_page(movies, seriesList):
	movie_output_file = open('template/ajax/movies.html', 'w')
	rendered_movie_content = create_movie_tiles_content(movies)
	movie_output_file.write(rendered_movie_content)
	movie_output_file.close()

	tv_output_file = open('template/ajax/tvshows.html', 'w')
	rendered_tv_content = create_tv_tiles_content(seriesList)
	tv_output_file.write(rendered_tv_content)
	tv_output_file.close()

	main_output = open('template/index.html', 'w')
	main_output.write(htmlcontent)
	main_output.close()

	#url = os.path.abspath(main_output.name)
	#webbrowser.open('file://'+url,new=2)
	url = os.system('python -m SimpleHTTPServer 8080')
	



