# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    Accepts three params: title(str), genre(str), rating(float)
    Returns movie(dict), or None if any param is missing
    '''
    # empty dictionary to create movie
    movie = {}
    # if title, genre, and rating are Truthy, add to dictionary
    if title and genre and rating:
        movie.update({"title": title, "genre": genre, "rating": rating})
        return movie
    # otherwise return None
    else:
        return None


def add_to_watched(user_data, movie):
    '''
    Accepts two params: user_data(dictionary) and movie(dictionary)
    Returns an updated user_data containing the movie
    '''
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    '''
    Accepts two params: user_data(dict), movie(dict)
    returns user_data(dict) updated with new movies
    '''
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    '''
    Accepts two params: user_data(dict) and title(str)
    Returns: user_data(dict), updated to remove a movie from
    watchlist and place into watched
    '''
    # Iterate through user_data
    for movie in user_data["watchlist"]:

        # If the movie's title is already in watched
        if movie["title"] == title:
            user_data["watchlist"].remove(movie) # Remove from watchlist
            user_data["watched"].append(movie) # Add to watched

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    '''
    Accepts one param: user_data(dictionary)
    Returns: average_rating(float)
    '''
    ratings_total = 0
    num_ratings = 0

    # if watched list is empty, return 0.0
    if not user_data["watched"]:
        return 0.0

    # Loop through watched ratings, add to the ratings_total and increase num_ratings
    for dict in user_data["watched"]:
        rating = dict["rating"]
        ratings_total += rating
        num_ratings += 1

    # Calculate average using ratings_total and dividing by num_ratings
    average_rating = float(ratings_total/num_ratings)

    return average_rating


def get_most_watched_genre(user_data):
        '''
        Accepts one param: user_data(dict)
        Returns most_watched_genre(str), or None
        if watched is an empty list.
        '''
        place_for_genres = []
        genre_freq_count = {}
        count = 0
        most_watched_genre = ""

        #if the value of "watched" is an empty list, return None
        if user_data["watched"] == []:
            return None

        #put genre titles in a list
        for movie in user_data["watched"]:
                if "genre" in movie:
                    genre_title = movie["genre"]
                    place_for_genres.append(genre_title)

        #make a dictionary with freq count based on list
        for i in place_for_genres:
            if i not in genre_freq_count:
                genre_freq_count[i] = 1
            else:
                genre_freq_count[i] += 1

        #find the most freq genre
        for i in genre_freq_count:
            if genre_freq_count[i] > count:
                most_watched_genre = i
                count = genre_freq_count[i]
        #return
        return(most_watched_genre)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    '''
    Accepts one param: user_data(dictionary)
    Returns: a list of dictionaries(represents a list of movies)
    '''
    unique_watched = []
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]# Access the friends list of movies

    # Iterate through all movies in user_data
    for movie in user_watched: # Look at movie data in user_watched
        found_movie = False

        for friend in friends_watched:
            for friend_movie in friend["watched"]:
                if movie["title"] == friend_movie["title"]: # If the title is found, boolean is True
                    found_movie = True

        if not found_movie and movie["title"] not in unique_watched: # Else it's a unique movie, append to unique_watched
            unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    '''
    Accepts one param: user_data(dict)
    Returns unique_watched(dict)
    '''
    unique_watched = []
    user_watched = user_data["watched"] # Access the watched list of movies
    friend_list = user_data["friends"]# Access the friends list of movies

    # Iterate through all movies
    for movie_data in friend_list: # Looping through inner loop of friends
        for friends_watched in movie_data["watched"]: # Checking each movie inside of watched
            if friends_watched not in user_watched and friends_watched not in unique_watched:
                unique_watched.append(friends_watched)

    return(unique_watched)

        
'''
for movie in user_watched: # Look at movie data in user_watched
    if movie not in friends_watched: # If the title is found, boolean is True
        unique_watched.append(movie)
    {
    'watched':
        [{'title': 'The Lord of the Functions: The Fellowship of the Function','genre': 'Fantasy','rating': 4.8},
        {'title': 'The Lord of the Functions: The Two Parameters','genre': 'Fantasy','rating': 4.0},
        {'title': 'The Lord of the Functions: The Return of the Value','genre': 'Fantasy','rating': 4.0},
        {'title': 'The JavaScript and the React','genre': 'Action', rating': 2.2},
        {'title': 'Recursion','genre': 'Intrigue', 'rating': 2.0},
        {'title': 'Instructor Student TA Manager','genre': 'Intrigue','rating': 4.5}],

    'friends':
        [{'watched':
            [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8},
            {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0},
            {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0},
            {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]},
        {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8},
        {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2},
        {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0},
        {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0}]}]
    }
'''

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    '''
    Accepts one param: user_data(dict)
    and returns recommended_movies(list)
    '''

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    '''
    Accepts one param: user_data(dict)
    Returns recommended_movies(list)
    '''

def get_rec_from_favorites(user_data):
    '''
    Accepts one param: user_data(dict)
    Returns recommended_movies(list) or
    None if none of the user's friends have watched
    '''
