'''Create a function named get_most_watched_genre. This function should take one parameter: user_data
the value of user_data will be a dictionary with a "watched" list of movie dictionaries.
Each movie dictionary has a key "genre".
This represents that the user has a list of watched movies. Each watched movie has a genre.
The values of "genre" is a string.
Determine which genre is most frequently occurring in the watched list
return the genre that is the most frequently watched
If the value of "watched" is an empty list, get_most_watched_genre should return None.'''
def get_most_watched_genre(user_data):

        place_for_genres = []
        genre_freq_count = {}
        count = 0
        most_watched_genre = ""

        for movie in user_data["watched"]:
                if "genre" in movie:
                    genre_title = movie["genre"]
                    place_for_genres.append(genre_title)
                else:
                    return None

        for i in place_for_genres:
            if i not in genre_freq_count:
                genre_freq_count[i] = 1
            elif i in genre_freq_count:
                genre_freq_count[i] += 1

        for i in genre_freq_count:
            if genre_freq_count[i] > count:
                most_watched_genre = i
                count = genre_freq_count[i]

        return(most_watched_genre)


INTRIGUE_1 = {"watched": [{
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}, {
    "title": "Instructor Student TA Manager",
    "genre": "Horror",
    "rating": 4.5
}, {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}]}
#print(INTRIGUE_1)


get_most_watched_genre(INTRIGUE_1)
