import json

from src.api_clients.movies_api_client import MoviesAPIClient

class MoviesAPI: 
    def __init__(self):
        self.movies_api_client = MoviesAPIClient()

    def get_movies(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """Return all the movies in the Lord of the Rings API
        
        :param int limit: Specify upper limit of movies that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.movies_api_client._get_movies(limit, page, offset)

        """
        return self.movies_api_client._get_movies(limit, page, offset)

    def get_movie(self, movie_id: str) -> json: 
        """Return movie by id
        
        :param str movie_id: Specify id of movie to be returned
        :return: JSON object 
        
        :example:
        
        >>> result = self.movies_api_client._get_movie(movie_id)
        """
        return self.movies_api_client._get_movie(movie_id)

    def get_movie_quotes(self, movie_id: str, limit: int = 100, page: int = 1, offset: int = 0) -> json: 
        """Return all the movie quotes in the Lord of the Rings API
        
        :param str movie_id: Specify movie id 
        :param int limit: Specify upper limit of quotes that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.movies_api_client._get_movie_quotes(movie_id, limit, page, offset)
        """
        return self.movies_api_client._get_movie_quotes(movie_id, limit, page, offset)