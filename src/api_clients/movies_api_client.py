import json

import requests

from src.common.base_api_client import BaseAPIClient

class MoviesAPIClient(BaseAPIClient): 
    def _get_movies(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """Return all the movies in the Lord of the Rings API
        
        :param int limit: Specify upper limit of movies that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """
        movies = requests.get(
            f"{self._base_url}/movie", 
            params={"limit": limit, 'page': page, 'offset': offset},
            headers=self._headers)

        return movies.json()

    def _get_movie(self, movie_id: str) -> json: 
        """Return movie by id
        
        :param str movie_id: Specify id of movie to be returned
        :return: JSON object 
        """
        movie = requests.get(
            f"{self._base_url}/movie/{movie_id}", 
            headers=self._headers)

        return movie.json()

    def _get_movie_quotes(self, movie_id: str, limit: int = 100, page: int = 1, offset: int = 0) -> json: 
        """Return all the movie quotes in the Lord of the Rings API
        
        :param str movie_id: Specify movie id 
        :param int limit: Specify upper limit of quotes that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """
        quotes = requests.get(
            f"{self._base_url}/movie/{movie_id}/quote",
            params={"limit": limit, 'page': page, 'offset': offset},
            headers=self._headers)

        return quotes.json()