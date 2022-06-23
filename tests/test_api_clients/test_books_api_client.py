import vcr 
from src.api_clients.books_api_client import BooksAPIClient

class TestBooksAPIClient:

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/get_books.yml")
    def test_get_books(self):
        response = BooksAPIClient()._get_books()
        response['docs'] == [{'_id': '5cf5805fb53e011a64671582', 'name': 'The Fellowship Of The Ring'}, 
                             {'_id': '5cf58077b53e011a64671583', 'name': 'The Two Towers'}, 
                             {'_id': '5cf58080b53e011a64671584', 'name': 'The Return Of The King'}]
       
    
    @vcr.use_cassette("tests/fixtures/vcr_cassettes/get_book.yml")
    def test_get_book(self):
        response = BooksAPIClient()._get_book('5cf5805fb53e011a64671582')
        response['docs'] == [{'_id': '5cf5805fb53e011a64671582', 'name': 'The Fellowship Of The Ring'}] 

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/get_book_chapters.yml")
    def test_get_book_chapters_with_limit(self):
        response = BooksAPIClient()._get_book_chapters('5cf5805fb53e011a64671582', limit=2)
        response['docs'] == [{'_id': '6091b6d6d58360f988133b8b', 'chapterName': 'A Long-expected Party'}, 
                             {'_id': '6091b6d6d58360f988133b8c', 'chapterName': 'The Shadow of the Past'}]

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/get_all_chapters.yml")
    def test_get_all_chapters_with_limit_and_offset(self):
        response = BooksAPIClient()._get_chapters(limit=3, offset=1)
        response['docs'] == [{'_id': '6091b6d6d58360f988133b8c', 'chapterName': 'The Shadow of the Past', 'book': '5cf5805fb53e011a64671582'}, 
                            {'_id': '6091b6d6d58360f988133b8d', 'chapterName': 'Three is Company', 'book': '5cf5805fb53e011a64671582'}, 
                            {'_id': '6091b6d6d58360f988133b8e', 'chapterName': 'A Short Cut to Mushrooms', 'book': '5cf5805fb53e011a64671582'}]

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/get_chapter.yml")
    def test_get_chapter(self):
        response = BooksAPIClient()._get_chapter('6091b6d6d58360f988133b8c')
        response['docs'] == [{'_id': '6091b6d6d58360f988133b8c', 'chapterName': 
                              'The Shadow of the Past', 'book': '5cf5805fb53e011a64671582'}]