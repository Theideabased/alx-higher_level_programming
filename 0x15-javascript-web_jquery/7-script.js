$.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
  // Extract the 'name' field from the JSON data
  var name = data.name;

  // Insert the 'name' into the DIV with id 'character'
  $("DIV#character").text(name);
});

