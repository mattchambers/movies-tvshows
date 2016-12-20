from Classes import media
import mediacenter

dory = media.Video('Finding Dory',
                   'https://www.youtube.com/watch?v=AMjMFbhyhwY',
                   'Dory finds her parents',
                   'Ratings - 5/5',
                   'https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg')

brave = media.Video('Brave',
                    'https://www.youtube.com/watch?v=TEHWDA_6e3M',
                    'Journay of a very brave girl',
                    'Ratings - 4.5/5',
                    'http://t0.gstatic.com/images?q=tbn:ANd9GcSuKUcpKMfuY1En5kWsJB2Xe-dqu-yYrQM6KTps3-Mti04lgmSY')

frozen = media.Video('Frozen',
                     'https://www.youtube.com/watch?v=FLzfXQSPBOg',
                     'Journey to bring back summer from a long winter period',
                     'Ratings - 5/5',
                     'https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg')

movies = [brave, frozen, dory]
# list of all movies Objects containing their Title, Youtube Trailer,
# Brief description, Movie's Rating, Poster Image 

modernFamily = media.TvShow('Modern Family',
                            'https://www.youtube.com/watch?v=U7dLXjZfXV8',
                            'Mockumentary Sitcom',
                            'Ratings - 5/5',
                            'https://s-media-cache-ak0.pinimg.com/originals/51/0e/2c/510e2c3e6685885ab9eedaafb8f8b747.jpg',
                            'Number of Seasons - 8',
                            'Number of Episodes - 175',
                            'Status - Current')

newGirl = media.TvShow('New Girl',
                       'https://www.youtube.com/watch?v=gP1Rp87_M6U',
                       'Sitcom about an offbeat teacher and her new roomates',
                       'Ratings - 5/5',
                       'http://www.finalreel.co.uk/wp-content/uploads/2014/08/New-Girl-Season-4-Poster.jpg',
                       'Number of Seasons - 6',
                       'Number of Episodes - 126',
                       'Status - Current')

HalfMen = media.TvShow('Two and a Half Men',
                       'https://www.youtube.com/watch?v=FtYVJTUvjEU',
                       'Sitcom about a father and his teenage boy moving in with his brother',
                       'Ratings - 5/5',
                       'http://www.tvposter.net/posters/two_and_a_half_men_2003_4196_poster.jpg',
                       'Number of Seasons - 12',
                       'Number of Episodes - 262',
                       'Status - Cancelled')

seriesList = [modernFamily, newGirl, HalfMen]
# list of all the TV Show objects created with the following attributes: Title, YouTube Trailer, Brief Description, TV Show's Ratings, Poster Image, Number of Seasons, Number of Episodes, Status of Tv Show

# This function takes the list of obejects and create the output files
mediacenter.open_page(movies, seriesList)

