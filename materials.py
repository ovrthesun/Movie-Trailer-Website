import movie
import fresh_tomatoes

#creating an instance of the class Movie called "If Only"
the_little_prince = movie.Movie("The Little Prince",
                        "An adventure of a lifetime",
                        "http://www.impawards.com/intl/france/2015/posters/little_prince.jpg",
                        "https://www.youtube.com/watch?v=fEPqgSNLfK8")

the_secret_life_of_walter_mitty = movie.Movie("The Secret Life of Walter Mitty",
                     "One frame at a time",
                     "http://www.impawards.com/2013/posters/secret_life_of_walter_mitty_ver8.jpg",
                     "https://www.youtube.com/watch?v=kGWO2w0H2V8")

ex_machina = movie.Movie("Ex Machina",
                         "The ultimate Turing Test",
                         "http://i62.tinypic.com/ml6trr.jpg",
                         "https://www.youtube.com/watch?v=EoQuVnKhxaM")

movies = [the_little_prince, the_secret_life_of_walter_mitty, ex_machina]

#opening the movie page with the movies in the array
fresh_tomatoes.open_movies_page(movies)
