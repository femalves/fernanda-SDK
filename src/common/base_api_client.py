import os

from dotenv import load_dotenv

load_dotenv()

class BaseAPIClient: 
    def __init__(self) -> None: 
        self._token = os.environ.get('API_TOKEN')
        self._base_url = os.environ.get('BASE_URL')
        self._headers = {"Authorization": f"Bearer {self._token}"}
    
   

    

    

    
