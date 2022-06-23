from src.api.books_api import BooksAPI
from unittest.mock import patch

class TestBooksAPI: 

    def test_books_api_should_call_books_api_client(self):
        with patch('src.api_clients.books_api_client.BooksAPIClient._get_books') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            BooksAPI().get_books()
            mocked_get.assert_called_once()

    def test_books_api_should_call_books_api_client_with_limit_and_offset(self):
        with patch('src.api_clients.books_api_client.BooksAPIClient._get_books') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            BooksAPI().get_books(limit=1, offset=2)
            mocked_get.assert_called_with(1, 1, 2)

    

