import vcr
from src.api_clients.characters_api_client import CharactersAPIClient


class TestCharactersAPIClient:

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/get_characters.yml")
    def test_get_characters_with_race_gender_and_limit(self):
        response = CharactersAPIClient()._get_characters(race="Human", gender="Female", limit=2)
        response['docs'] == [{'_id': '5cd99d4bde30eff6ebccfbbe', 'height': '', 'race': 'Human', 'gender': 'Female', 'birth': '', 
        'spouse': 'Belemir', 'death': '', 'realm': '', 'hair': '', 'name': 'Adanel', 'wikiUrl': 'http://lotr.wikia.com//wiki/Adanel'}, 
        {'_id': '5cd99d4bde30eff6ebccfbc2', 'height': '', 'race': 'Human', 'gender': 'Female', 'birth': 'Mid ,First Age', 'spouse': 'Brodda', 'death': 'FA 495', 'realm': '', 'hair': '', 'name': 'Aerin', 'wikiUrl': 'http://lotr.wikia.com//wiki/Aerin'}]
