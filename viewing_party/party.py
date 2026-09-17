# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
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
    user_data["watchlist"].append(movie)
    return user_data

    # user_data = {watchlist: [{title : "title", "genre": "genre", "rating": "rating"}, {}, {}]}
    # user_data = {watchlist: []} <<<< the user has no movies they want to watch
    # movie = {"title": "Title A","genre": "Horror",rating": 3.5}

    #user_data(watchlist).update({movie})

def watch_movie(user_data, title):
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
    user_watched = user_data["watched"] # Access the watched list of movies
    friends_watched = user_data["friends"] # Access the friends list of movies
    found_movie = False # Use to determine if a movie has been found

    # Iterate through all movies in user_data
    for movie in user_watched: # Look at movie data in user_watched
        for friend in friends_watched: # Go through each friend in the friends list
            for friend_movie in friend["watched"]: # Check each of the watched movies for that friend
                if movie["title"] == friend_movie["title"]: # If the title is found, boolean is True
                    found_movie = True

            if not found_movie: # Else it's a unique movie, append to unique_watched
                unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    '''
  - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
    - This represents that the user has a list of watched movies and a list of friends
    - The value of `"friends"` is a list
    - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
    - Each movie dictionary has a `"title"`.
- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
- Return a list of dictionaries, that represents a list of movies
user_data = {"watched":xxxxxx, "friends":xxxxxx}
    '''
    pass
    # user_data is a dict with 'watched' list of movie dicts and 'friends' list of friend dicts
    # each friend has a 'watched' key
    # each movie dict has a 'title' key
    # find movies that at least one friend has watched but user has NOT watched
    # return a list of movie dicts

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
