# Eamonn Patterson 100954660
# ICE1
# 1/20/24
# this is the first assignment for ice, the movie budget calculator


##############################################
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]


# defining functions to find th average, add the new movies to the list and ask for user input
def new_movie():
    movie_title = input('Enter the title of the new movie: ')
    movie_budget = int(input('What is the budget of the new movie? '))
    movies.append((movie_title, movie_budget))
    return movie_title, movie_budget


def average_budget(movies):
    total_budget = 0
    for movie in movies:
        total_budget += movie[1]

    if len(movies) > 0:
        average = total_budget / len(movies)
        return average


# all awnsers/ everthing being printed after the user inputs
def prints():
    average = average_budget(movies)
    print(f'{average_budget(movies)} is the average movie budget\n')
    count = 0
    for movie in movies:
        if movie[1] > average:
            count += 1
            above_by = movie[1] - average
            print(f"{movie[0]}'s budget was {movie[1]} which is {above_by} above average")
    print(f'{count} movies were above budget')


# initial prompt
num_movies_to_add = int(input('How many movies would you like to add? '))
for n in range(num_movies_to_add):
    new_movie()
prints()
