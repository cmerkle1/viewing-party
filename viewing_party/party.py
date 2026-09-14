# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # empty dictionary to create movie
    movie = {}
    # if title, genre, and rating are Truthy, add to dictionary
    if title and genre and rating:
        movie.update({"title": title, "genre": genre, "rating": rating})
    # otherwise return None
    else:
        return None


def add_to_watched(user_data, movie):
    pass

    # if user_data = None, we get -> []
    # user_data = {watched: [{title: "title", "genre": "genre", "rating": "rating"}, {}, {}]}
    # user_data = {watched: []} <<<< the user has no movies in their watched list
    # movie = {"title": "Title A","genre": "Horror",rating": 3.5}

    #user_data(watched).update({movie})

    #return user_data

def add_to_watchlist(user_data, movie):
    pass

    # user_data = {watchlist: [{title : "title", "genre": "genre", "rating": "rating"}, {}, {}]}
    # user_data = {watchlist: []} <<<< the user has no movies they want to watch
    # movie = {"title": "Title A","genre": "Horror",rating": 3.5}

    #user_data(watchlist).update({movie})

def watch_movie(user_data, title):
    pass

    # user_data = {watchlist: [{}, {}, {}], watched: [{}, {}, {}]}
    # if title in user_data(watchlist):
        #user_data(watchlist).remove(title)
        #user_data(watched).update(title) ???what about genrea and rating?
    #return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
