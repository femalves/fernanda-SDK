# Lord of the Rings (LOTR) SDK

Interact with the [LOTR API](https://the-one-api.dev) in a seamless way.

## First step 

Visit [API Website](https://the-one-api.dev/sign-up) to obtain token necessary for authorization 

## Virtual environment
``` 
mkdir new_project 
cd new_project 
python3 -m venv myvenv 
source myvenv/bin/activate
```

## Set up environment variables
.env 
```
API_TOKEN=<your-api-token> 
BASE_URL=https://the-one-api.dev/v2/
```

## Install 
```sh
pip install lotrsdkbyfernanda
```

### Fetch all books
```sh 
get_books() 
``` 

### Fetch one book by book ID 
```sh
get_book(book_id)
```

### Fetch book chapters by book ID
```sh 
get_book_chapters(book_id)
```

### Fetch book chapters by book ID
```sh 
get_book_chapters(book_id)
```

### Fetch chapter by chapter ID 
```sh
get_chapter(chapter_id)
```
___ 

### Adding different params 
```sh 
get_books(limit=1, page=2, offset=1) 
``` 

___

### Fetch characters 
```sh 
get_characters() 
```

### Fetch character 
```sh 
get_character(character_id) 
```

### Fetch character quote
```sh 
get_characters_quote(character_id) 
```

--- 
Extra params 

### Fetch characters with filters
```sh 
get_characters(race="Human", gender="Female", name="Adanel") 
```

___ 
### Fetch movies 

```sh
get_movies() 
```

### Fetch movie
```sh
get_movie(movie_id) 
```

### Fetch movie quotes
```sh
get_movie_quotes(movie_id) 
```

___ 
### Fetch quotes 
```sh 
get_quotes() 
``` 

### Fetch quote 
```sh
get_quote(quote_id)
```

---

## Running tests 
```sh
python -m pytest -s 
```

