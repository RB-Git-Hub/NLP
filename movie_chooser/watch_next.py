# Import Library
import spacy
nlp = spacy.load('en_core_web_md')

# Hulk text to compare movies with
hulk = "Will he save their world or destroy it? When the Hulk becomes too \
dangerous for the Earth, the Illuminati trick Hulk into a shuttle and \
launch him into space to a planet where the Hulk can live in peace. \
Unfortunately, Hulk lands on the planet Sakaar where he is sold \
into slavery and trained as a gladiator."
current = nlp(hulk)

# Variables set
highest=0
best_movie=""

# text file opened and data extracted and compared to Hulk text
with open("movies.txt", "r") as movie:
    for line in movie: 
        new_movie = nlp(line)
        rank=(current.similarity(new_movie))

        # If score is highest it is saved in variable along with movie text
        if rank>highest:
            highest = rank
            best_movie = line
    
    # Result displayed
    print(f"\nThe recommended movie to watch next is {best_movie[0:7]}\n")

    

