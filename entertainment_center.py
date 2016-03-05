# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!
# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

riddick = media.Movie("Riddick",
"Escaped criminal Riddick is left stranded on an alien planet",
"https://upload.wikimedia.org/wikipedia/en/6/69/Riddick_poster.jpg",
"https://www.youtube.com/watch?v=zH3O-CeZckE",
"September 4, 2013",
[
"Vin Diesel",
"Jordi Molla",
"Matt Nable",
"Katee Sackhoff",
"Dave Bautista",
"Bokeem Woodbine",
"Raoul Trujillo",
"Karl Urban"
]
)

avatar = media.Movie("Avatar",
"A Marine on an alien planet.",
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.youtube.com/watch?v=cRdxXPV9GNQ",
"December 18, 2009",
[
"Sam Worthington",
"Zoe Saldana",
"Stephen Lang",
"Michelle Rodriguez",
"Sigourney Weaver"
]
)

cloverfield = media.Movie("Cloverfield",
"A monster goes rampaging through New York.",
"https://upload.wikimedia.org/wikipedia/en/f/f1/Cloverfield_theatrical_poster.jpg",
"https://www.youtube.com/watch?v=M1XEriXzNik",
"January 18, 2008",
[
"Lizzy Caplan",
"Jessica Lucas",
"T. J. Miller",
"Michael Stahl-David",
"Mike Vogel",
"Odette Yustman    "
]
)


guardians_of_the_galaxy = media.Movie("Guardians Of The Galaxy",
"A group of intergalactic criminals are forced to work together.",
"https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
"https://www.youtube.com/watch?v=d96cjJhvlMA",
"August 1, 2014",
[
"Chris Pratt",
"Zoe Saldana",
"Dave Bautista",
"Vin Diesel",
"Bradley Cooper",
"Lee Pace",
"Michael Rooker",
"Karen Gillan",
"Djimon Hounsou",
"John C. Reilly",
"Glenn Close",
"Benicio del Toro"
]
)

pacific_rim = media.Movie("Pacific Rim",
"A war between humankind and monstrous sea creatures..",
"https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
"https://www.youtube.com/watch?v=5guMumPFBag",
"July 12, 2013",
[
"Charlie Hunnam",
"Idris Elba",
"Rinko Kikuchi",
"Charlie Day",
"Ron Perlman",
]
)

three_hundred = media.Movie("300",
"300 spartan soldiers battle the Persian army.",
"https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
"https://www.youtube.com/watch?v=UrIbxk7idYA",
"March 9, 2007",
[
"Gerard Butler",
"Lena Headey",
"David Wenham"
"Dominic West"
"Rodrigo Santoro"
]
)



movies = [riddick, avatar, cloverfield, guardians_of_the_galaxy, pacific_rim, three_hundred]
fresh_tomatoes.open_movies_page(movies)