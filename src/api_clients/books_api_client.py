import json

import requests
 
from src.common.base_api_client import BaseAPIClient


class BooksAPIClient(BaseAPIClient):
    def _get_books(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """Return all the books in the Lord of the Rings API
        
        :param int limit: Specify upper limit of books that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """
        books = requests.get(
            f"{self._base_url}/book",
            params={"limit": limit, 'page': page, 'offset': offset})

        return books.json()

    def _get_book(self, book_id: str) -> json:
        """Return book by id
        
        :param str book_id: Specify id of book to be returned
        :return: JSON object 
        """

        book = requests.get(
            f"{self._base_url}/book/{book_id}")

        return book.json()

    def _get_book_chapters(self, book_id: str, limit: int = 100, page: int = 1, offset: int = 0) -> json: 
        """Return all the chapters of a book
        
        :param str book_id: Specify book id 
        :param int limit: Specify upper limit of chapters that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """

        chapters = requests.get(
            f"{self._base_url}/book/{book_id}/chapter", 
            params={"limit": limit, 'page': page, 'offset': offset},
            headers=self._headers)

        return chapters.json()

    def _get_chapters(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """
        Return all the chapters of all books
        
        :param int limit: Specify upper limit of chapters that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """
        chapters = requests.get(
            f"{self._base_url}/chapter", 
            params={"limit": limit, 'page': page, 'offset': offset},
            headers=self._headers)

        return chapters.json()

    def _get_chapter(self, chapter_id: str) -> json:
        """
        Return a chapter of a book
        
        :param int chapter_id: Specify chapter id
        :return: JSON object 
        """
        chapter = requests.get(
            f"{self._base_url}/chapter/{chapter_id}",
            headers=self._headers)

        return chapter.json()
    