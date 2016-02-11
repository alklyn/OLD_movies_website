# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

#__name __ , __module__ & __doc__ are examples of predefined class variables
#they are available for all classes

import webbrowser

class Movie():
	""" This class provides a way to store movie related information """
	#class variables are the smae for all instances of a class.
	VALID_RATINGS = ["G", "PG", "PG-13", "R"] #this is a class variable.
	#Since we don't intend to change VALID_RATINGS it s a constant
	#In python constants are written in all caps
	
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		# initialize instance of class Movie. This is a constructor
		#self is the object being created
		self.title = movie_title #this is an example of an instance variable.
		self.storyline = movie_storyline #an instance variable is unique to each instance
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
        

	def show_trailer(self):
		#plays trailer for movie
		#A function defined inside a class and is associated an instance is
		#called an instance method.
		webbrowser.open(self.trailer_youtube_url)
