import json

import requests

from src.common.base_api_client import BaseAPIClient

class QuotesAPIClient(BaseAPIClient): 
    def get_quotes(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """Return all movie quotes in the Lord of the Rings API
        
        :param int limit: Specify upper limit of movies that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """
        quotes = requests.get(
            f"{self._base_url}/quote", 
            params={"limit": limit, 'page': page, 'offset': offset},
            headers=self._headers)

        return quotes.json()

    def get_quote(self, quote_id: str) -> json:
        """Return specific movie quote in the Lord of the Rings API
        
        :param str quote_id: Specify quote id
        :return: JSON object 
        """
        quote = requests.get(
            f"{self._base_url}/quote/{quote_id}", 
            headers=self._headers)

        return quote.json()