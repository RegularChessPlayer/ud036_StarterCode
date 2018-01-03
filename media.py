import webbrowser


# noinspection PyInterpreter
class Movie(object):
    """This is a example showing init class

    Attributes:
        title (str): title movie .
        storyline (str): this a brief about movie history
        poster_image_url (str): url who show the image poster movie
        trailer_youtube_url (str): rl who show the trailer movie

    """

    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """This function call the webPage who contains the movie trailer"""
        webbrowser.open(self.url_trailler)
