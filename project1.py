import movie
import fresh_tomatoes

# Creating objects with different movies
police_academy = movie.Movie(
    "Fresh cadets need to protect citizens",
    "http://www.impawards.com/1984/posters/police_academy.jpg",
    "https://www.youtube.com/watch?v=FebYWUGucpA")

matrix = movie.Movie(
    "Everything you have heard before is a lie and this is a lie too",
    "https://c1.staticflickr.com/9/8819/17072638696_f871731849_b.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

fifth_element = movie.Movie(
    "Dive into nearest future to get a sneak peak what to expect from it",
    "http://img.moviepostershop.com/the-fifth-element-movie-poster-1997-1010473456.jpg",
    "https://www.youtube.com/watch?v=199EvXTKucc")

# Generate html page with your favorite movies
fresh_tomatoes.open_movies_page([police_academy, matrix, fifth_element])
