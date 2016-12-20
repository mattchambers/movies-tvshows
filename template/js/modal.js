$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
            $('.content-ratings').empty();
            $('.content-story').empty();
            $('.content-seasons').empty();
            $('.content-episodes').empty();
            $('.content-status').empty();

        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.content-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var ratings = $(this).attr('data-movie-ratings');
            var story = $(this).attr('data-movie-story'); 

            var tvRatings = $(this).attr('data-tvshow-ratings');
            var tvStory = $(this).attr('data-tvshow-story');
            var seasons = $(this).attr('data-tvshow-seasons');
            var episodes = $(this).attr('data-tvshow-episodes');
            var status = $(this).attr('data-tvshow-status');

            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));

            if (ratings) {
                $('.content-ratings').append(ratings);
            }else if(tvRatings){
                $('.content-ratings').append(tvRatings);
                
            }

            if (story) {
                $('.content-story').append(story);
            }else if(tvStory){
                $('.content-story').append(tvStory);
                console.log(tvStory);
            }

            
            $('.content-seasons').append(seasons);
            $('.content-episodes').append(episodes);
            $('.content-status').append(status)
        });
