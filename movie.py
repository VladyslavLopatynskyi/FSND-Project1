class Movie(object):
	"""Movie class is used to describe your favorite movie. It contains title, poster_image_url and trailer_youtube_url properties"""
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		