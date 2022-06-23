## Design

- While thinking about how to design this I kept KISS (Keep It Simple Stupid) in mind. I wanted to keep it as simple as possible while also prioritizing modularity to try to make it super testable

- I decided to do this in layers and what actually happens in the client layers is completely abstracted from the user, that way the SDK becomes extremely easy to use as the complexity is hidden 

## Error handling 
- Time constraints didn't allow me to implement error handling, which of course is an important factor when dealing with API calls 

## Security 

- Since the Token was necessary for authentication, I created a .env file to keep all environmental variables isolated and protected, as it is recommended by the twelve-factor methodology 

## API Endpoints 
- I tried to mirror as many API endpoints as possible, but unfortunately I ran out of time on the last ones 

## Testing 
- Since most of the code repeated, I implemented sample tests for some of the classes. All the other classes should follow the same patterns, so I didn't feel it was necessary to keep repeating myself. I do understand that if the code was meant for production, good code coverage would be necessary 

## Clean Code 
- I tried to observe some of the clean code principles by obeying the single-responsibility principle, naming conventions, implementing test cases, adding documentation etc. 

## Documentation 
- I tried to add documentation to all endpoints 

## Disclaimer 

- Since time was of the essence, I tried to keep everything very simple. Some of the requirements were only implemented partially to give an idea of how I would handle them in a real scenario. Some of the things I would also do, like error handling, were not done at all in order to prioritize other items, like testing, which I felt was more important for the task at hand
