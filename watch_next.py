# importing spacy
import spacy

# specify the model
nlp = spacy.load('en_core_web_md')

# text to compare
planet_hulk = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

def next_movie(mov):
    # initialise variable to keep track of the best match
    highest_score = 0
    # open text file to read movies
    with open("movies.txt") as f:
        lines = f.readlines()

        # loop through the movies and strip/split the lines on the : to separate the movie name and description
        for movie in lines:
            temp = movie.strip()
            temp = movie.split(":")

            # compare the similarities and store in a variable
            similarity = nlp(temp[1]).similarity(mov)

            # check to see if it is more similar than the previous highest similarity
            # save the highest scoring match and the corresponding movie_name 
            if similarity > highest_score:
                highest_score = similarity
                movie_name = temp[0]
        
        # return
        return(movie_name)

# display a message to the user calling the next_movie function to find the most similar movie
print(f"Suggested next movie based on highest similarity: {next_movie(planet_hulk)}")


