# This class will create objects with general media attributes
class Video():
        def __init__(self, title, trailer, story, ratings, poster):
                self.title = title
                self.trailer = trailer
                self.story = story
                self.ratings = ratings
                self.poster = poster

# Create objects that are specific to having attributes for a TV Show                
class TvShow(Video):
    def __init__(self, title, trailer, story, ratings, poster,
                 seasons, episodes, status):
        self.title = title
        self.trailer = trailer
        self.story = story
        self.ratings = ratings
        self.poster = poster
        self.seasons = seasons
        self.episodes = episodes
        self.status = status

        
