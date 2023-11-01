// Use jQuery to fetch the movie data
$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
      // Extract the movie titles
      const movies = data.results;

      // Create an empty UL to list the movie titles
      const ul = $("<ul>");

      // Loop through the movies and add each title to the UL
      $.each(movies, function(index, movie) {
        var li = $("<li>").text(movie.title);
        ul.append(li);
      });

      // Append the UL to the element with id 'list_movies'
      $("UL#list_movies").replaceWith(ul);
});
