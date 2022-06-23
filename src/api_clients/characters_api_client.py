import json

import requests


from src.common.base_api_client import BaseAPIClient

class CharactersAPIClient(BaseAPIClient): 
    def _get_characters(self, limit: int = 100, page: int = 1, offset: int = 0, name: str = "", race: str = "", gender: str = "") -> json:
        """Return all the characters in the Lord of the Rings API
        
        :param int limit: Specify upper limit of characters that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """

        characters = requests.get(
            f"{self._base_url}/character",
            params={"limit": limit, 'page': page, 'offset': offset, 'name': name, 'race': race, 'gender': gender},
            headers=self._headers)

        return characters.json()

    def _get_character(self, character_id: str) -> json: 
        """Return all character in the Lord of the Rings API
        
        :param str character_id: Specify character id
        :return: JSON object 
        """
        character = requests.get(
            f"{self._base_url}/character/{character_id}", 
            headers=self._headers)

        return character.json()

    def _get_character_quotes(self, character_id: str, limit: int = 100, page: int = 1, offset: int = 0) -> json: 
        """Return all the character quotes in the Lord of the Rings API
        
        :param str character_id: Specify character id
        :param int limit: Specify upper limit of quotes that should be returned
        :param int page: Specify the page to retrieve
        :param int offset: Specify the offset of the first hit to return 
        :return: JSON object 
        """
        quotes = requests.get(
            f"{self._base_url}/character/{character_id}/quote", 
            params={"limit": limit, 'page': page, 'offset': offset},
            headers=self._headers)

        return quotes.json()