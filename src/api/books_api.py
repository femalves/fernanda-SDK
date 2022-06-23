import json

from src.api_clients.books_api_client import BooksAPIClient

class BooksAPI:
    def __init__(self): 
        self.books_api_client = BooksAPIClient() 

    def get_books(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """Return all the books in the Lord of the Rings API
        
        :param int limit: Specify upper limit of books that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.books_api_client._get_books(limit, page, offset)
        """
        
        return self.books_api_client._get_books(limit, page, offset)

    def get_book(self, book_id: str) -> json:
        """Return book by id
        
        :param str book_id: Specify id of book to be returned
        :return: JSON object 
        
        :example:
        
        >>> result = self.books_api_client._get_book(book_id)
        """

        return self.books_api_client._get_book(book_id)

    def get_book_chapters(self, book_id: str, limit: int = 100, page: int = 1, offset: int = 0) -> json: 
        """Return all the chapters of a book
        
        :param str book_id: Specify book id 
        :param int limit: Specify upper limit of chapters that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.books_api_client._get_book_chapters(book_id, limit, page, offset)
        """
       
        return self.books_api_client._get_book_chapters(book_id, limit, page, offset)

    def get_chapters(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """
        Return all the chapters of all books
        
        :param int limit: Specify upper limit of chapters that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.books_api_client._get_chapters(limit, page, offset)
        """
        return self.books_api_client._get_chapters(limit, page, offset)

    def get_chapter(self, chapter_id: str) -> json:
        """
        Return a chapter of a book
        
        :param int chapter_id: Specify chapter id
        :return: JSON object 
        
        :example:
        
        >>> result = self.books_api_client._get_chapter(chapter_id)
        """
        return self.books_api_client._get_chapter(chapter_id)
    