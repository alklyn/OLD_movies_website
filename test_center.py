# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

riddick = media.Movie("Riddick",
						"Escaped criminal Riddick is left stranded on an alien planet",
						"https://upload.wikimedia.org/wikipedia/en/6/69/Riddick_poster.jpg",
						"https://www.youtube.com/watch?v=zH3O-CeZckE"
						)

avatar = media.Movie("Avatar",
					 "A Marine on an alien planet.",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
					)

pitch_black = media.Movie("Pitch Black",
						"A spaceship crash lands on a planet full of bloodthirsty creatures.",
						"https://upload.wikimedia.org/wikipedia/en/2/26/Pitch_Black_poster.JPG",
						"https://www.youtube.com/watch?v=fIeSV4i7bxQ"
					)

cloverfield = media.Movie("Cloverfield",
					 "A monster goes rampaging through New York.",
					 "https://upload.wikimedia.org/wikipedia/en/f/f1/Cloverfield_theatrical_poster.jpg",
					 "https://www.youtube.com/watch?v=M1XEriXzNik"
					)

guardians_of_the_galaxy = media.Movie("Guardians Of The Galaxy",
					 "A group of intergalactic criminals are forced to work together.",
					 "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
					 "https://www.youtube.com/watch?v=d96cjJhvlMA"
					)

pacific_rim = media.Movie("Pacific Rim",
					 "A war between humankind and monstrous sea creatures..",
					 "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
					 "https://www.youtube.com/watch?v=5guMumPFBag"
					)

monsters_vs_aliens = media.Movie("Monsters Vs Aliens",
					 "The world's most unlikely heroes are on a mission to save the Earth.",
					 "https://upload.wikimedia.org/wikipedia/en/7/76/Monsters-vs-aliens-poster.jpg",
					 "https://www.youtube.com/watch?v=76XkslTbkjU"
					)

pirates_of_the_caribbean = media.Movie("Pirates Of The Caribbean",
					 "The world's most unlikely heroes are on a mission to save the Earth.",
					 "https://upload.wikimedia.org/wikipedia/en/0/0e/Pirates_of_the_Caribbean_movie.jpg",
					 "https://www.youtube.com/watch?v=naQr0uTrH_s"
					)

three_hundred = media.Movie("300",
					 "300 spartan soldiers battle the Persian army.",
					 "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
					 "https://www.youtube.com/watch?v=UrIbxk7idYA"
					)



#avatar.show_trailer()
#riddick.show_trailer()
#pacific_rim.show_trailer()

#movies = [riddick, avatar, cloverfield, guardians_of_the_galaxy, pacific_rim, pitch_black, monsters_vs_aliens, pirates_of_the_caribbean, three_hundred]
#fresh_tomatoes.open_movies_page(movies)

print riddick.VALID_RATINGS
print three_hundred.VALID_RATINGS
print media.Movie.VALID_RATINGS
print media.Movie.__doc__
