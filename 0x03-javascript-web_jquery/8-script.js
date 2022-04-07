$.get('https://swapi-api.hbtn.io/api/films/?format=json', (content) => {
  const movies = content.results;
  for (const movie in movies) {
    $('#list_movies').append('<li>' + movies[movie].title + '</li>');
  }
});
