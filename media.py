# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    """ This class provides a way to store and display movie related information """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, 
                 release_date, actors):
        """ Initialize instance of class Movie."""
        self.title = movie_title
        self.storyline = movie_storyline 
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.actors = list(actors)
        

    def show_trailer(self):
        """Play trailer for movie"""
        webbrowser.open(self.trailer_youtube_url)
