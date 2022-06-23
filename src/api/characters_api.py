import json

from src.api_clients.characters_api_client import CharactersAPIClient

class CharactersAPI: 
    def __init__(self): 
        self.characters_api_client = CharactersAPIClient() 

    def get_characters(self, limit: int = 100, page: int = 1, offset: int = 0, name: str = "", race: str = "", gender: str = "") -> json:
        """Return all the characters in the Lord of the Rings API
        
        :param int limit: Specify upper limit of characters that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.characters_api_client._get_characters(limit, page, offset, name, race, gender)
        """
        return self.characters_api_client._get_characters(limit, page, offset, name, race, gender)

    def get_character(self, character_id: str) -> json: 
        """Return all character in the Lord of the Rings API
        
        :param str character_id: Specify character id
        :return: JSON object 
        
        :example:
        
        >>> result = LotrAPIClient.get_character() 
        """
        return self.characters_api_client._get_character(character_id)

    def get_character_quotes(self, character_id: str, limit: int = 100, page: int = 1, offset: int = 0) -> json: 
        """Return all the character quotes in the Lord of the Rings API
        
        :param str character_id: Specify character id
        :param int limit: Specify upper limit of quotes that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        
        :example:
        
        >>> result = self.characters_api_client._get_character_quotes(character_id, limit, page, offset)
        """

        return self.characters_api_client._get_character_quotes(character_id, limit, page, offset)
    