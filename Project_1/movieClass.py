"""
This python file contains a single class named Movie with below attributes.

1. title - string input of the movie title.
2. summary - string input of summary of the movie.
3. poster_image_url - string input of valid url(a) to the movie poster.
4. trailer_youtube_url - string input of valid youtube trailer url(a).

a. Valid url - it should contains the complete web address.
ex:
https://image.tmdb.org/t/p/w370_and_h556_bestv2//67NXPYvK92oQgEQvLppF2Siol9q.jpg

same goes for the youtube url
ex:https://www.youtube.com/watch?v=tquIfapGVqs.
"""
class Movies:

    def __init__(self,titles,summary,image,url):
        self.title=titles
        self.storyline = summary
        self.poster_image_url=image
        self.trailer_youtube_url=url
