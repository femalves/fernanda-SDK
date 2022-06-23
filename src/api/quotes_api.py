import json

from src.api_clients.quotes_api_client import QuotesAPIClient

class QuotesAPI: 
    def __init__(self): 
        self.quotes_api_client = QuotesAPIClient() 

    def get_quotes(self, limit: int = 100, page: int = 1, offset: int = 0) -> json:
        """Return all movie quotes in the Lord of the Rings API
        
        :param int limit: Specify upper limit of movies that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.quotes_api_client._get_quotes(limit, page, offset)
        """
        return self.quotes_api_client._get_quotes(limit, page, offset)

    def get_quote(self, quote_id: str) -> json:
        """Return specific movie quote in the Lord of the Rings API
        
        :param str quote_id: Specify quote id
        :return: JSON object 
        
        :example:
        
        >>> result = self.quotes_api_client._get_quote(quote_id)
        """
        return self.quotes_api_client._get_quote(quote_id)