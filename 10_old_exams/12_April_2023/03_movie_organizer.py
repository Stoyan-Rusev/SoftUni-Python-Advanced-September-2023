def movie_organizer(*args):
    organizer_dict = {}

    for info in args:
        movie_name = info[0]
        genre = info[1]
        if genre not in organizer_dict.keys():
            organizer_dict[genre] = []
        organizer_dict[genre].append(movie_name)
    organizer_dict = sorted(organizer_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for current_genre, movie_list in organizer_dict:
        movie_list = sorted(movie_list)
        result += f'{current_genre} - {len(movie_list)}\n'
        for current_movie in movie_list:
            result += f'* {current_movie}\n'
    return result


# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))

# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
