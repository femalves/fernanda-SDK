from unittest.mock import patch
from src.api.movies_api import MoviesAPI

class TestMoviesAPI: 

    def test_movies_api_should_call_movies_api_client(self):
        with patch('src.api_clients.movies_api_client.MoviesAPIClient._get_movie') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Book 1"


            MoviesAPI().get_movie('123')
            mocked_get.assert_called_once()

    