$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (content) => {
  $('DIV#character').text(content.name);
});
