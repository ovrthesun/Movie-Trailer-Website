import webbrowser

class Movie():
    """This class provides a way to store move-related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #initializing the instance with its details
    def __init__(self, title, storyline, image, trailer): #the constructor
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    #opens the url of the trailer to view
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
