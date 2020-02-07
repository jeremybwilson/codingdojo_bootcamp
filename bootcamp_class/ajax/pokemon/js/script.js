$(document).ready(function(){

  const app = document.getElementById('container-fluid');

  const containerCharacter = document.getElementById('pokemon');
  // containerCharacter.setAttribute('id', 'pokemon');

  const containerStats = document.getElementById('pokemon-display');
  // containerStats.setAttribute('id', 'pokemon-display');

  const logo = document.createElement('img');
  logo.src = 'images/pokemon-title.jpg';
  logo.setAttribute('class', 'title')

  const h1 = document.createElement('h1');
  h1.textContent = "Pokemon Assignment";

  $('.heading').prepend(logo);
  $('.heading').prepend(h1);

  // set base URL for Pokemon API character info
  const baseUrl = "https://pokeapi.co/api/v2/pokemon/";
  
  // set root portion of media/img URL here
  // const imgBaseUrl = 'https://pokeapi.co/media/sprites/pokemon/';  // this seems to be deprecated 
  const imgBaseUrl = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/';

  // embed opening <div> tag for .row container
  // $('#pokemon').append('<div class="row">');

  $.get("https://pokeapi.co/api/v2/pokemon/?limit=51", function(response) {
    for(let i = 0; i < response.results.length; i++){
      
      let url = response.results[i].url.split('/');
      let pokemonCharID = response.results[i].url.split('/')[6];
      
      let imgAlt = response.results[i].name;
      let pokemonCharName = response.results[i].name;
      // set variable to pull in specific Pokemon character ID (from URL) here,
      // get subtring value from the API endpoint for results.url

      const pokeID = response.results[i];
      console.log('Here is the charID response', pokeID);
      
      // create imagePath URL here
      const pokemonCharFullPath = imgBaseUrl + pokemonCharID + '.png';
      console.log('Here is the Image URI', pokemonCharFullPath);

      // let htmlStr = `<div data-id="${pokemonCharID}" data-title="${pokemonCharName}"><img alt="${imgAlt}" id="${pokemonCharID}" src="${pokemonCharFullPath}" /></div>`;
      let htmlStr = `<img alt="${imgAlt}" data-id="${pokemonCharID}" src="${pokemonCharFullPath}" />`;
      $('#pokemon').append(htmlStr);
    }
  }, "json");

  // if the business card is clicked, show that particular characters stats
  // in the starwars-people container
  $('#pokemon').on('click', 'img', function() {
    // to do this, we need to send another request to the API.
    let id = $(this).attr('data-id');

    $.get(baseUrl+id, function(response){
      // return character info from the JSON response;
      let pokemonCharID   = id;
      let pokemonCharName = response.name;
      let pokemonImgURL   = response.sprites.front_default;
      let pokemonHeight   = response.height;
      let pokemonWeight   = response.weight;

      let htmlStr = `<div><h4 class="strong">${pokemonCharName}</h4><img src="${pokemonImgURL}" alt="${pokemonCharName}" /><ul>`;
      for(let i = 0; i < response.types.length; i++){
        let pokemonType = response.types[i].type.name;
        htmlStr += `<li><span class="strong">Types:</span> ${pokemonType}</li>`;
      }
      htmlStr += `<li><span class="strong">Height:</span> ${pokemonHeight}</li><li><span class="strong">Weight:</span> ${pokemonWeight} cm</li>
      </ul></div>`;

      // $('#pokemon-display').show().attr('style', 'display: inline-block;').html(htmlStr);
      $('#pokemon-display').show().html(htmlStr);
    }, "json");
  });
});