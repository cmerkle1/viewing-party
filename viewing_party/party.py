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
    pass

def get_most_watched_genre(user_data):
    pass


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
