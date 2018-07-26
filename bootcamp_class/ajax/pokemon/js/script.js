$(document).ready(function(){

  const app = document.getElementById('pokemon');

  const logo = document.createElement('img');
  logo.src = 'images/pokemon-title.jpg';

  const container = document.createElement('div');
  container.setAttribute('class', 'container-fluid');

  app.appendChild(logo);
  app.appendChild(container);



  // $.get("https://pokeapi.co/api/v2/pokemon/?limit=1", function(res) {
    for(let i = 0; i < res.results.length; i++){
      console.log(res.results[i].name);
      // set root portion of media/img URL here
      var imgBaseUrl = 'http://pokeapi.co/media/img/'
      // set variable to pull in specific Pokemon character ID (from URL) here
      var pokemonCharNo = $(this)
      // var pokemonCharNo = res.results.url.substr(34, 37); => this isn't working as expected
      console.log(pokemonCharNo);
      // create imagePath URL here
      var pokemonCharFullPath = imgBaseUrl + pokemonCharNo + '.png';
    }
    
  // }, "json");


  // var request = new XMLHttpRequest();
  // request.open('GET', 'https://pokeapi.co/api/v2/pokemon/?limit=20', true);
  // request.onload = function () {

    // Begin accessing JSON data here
    // var data = JSON.parse(this.response);

    // if (request.status >= 200 && request.status < 400) {
      // console.log(this.response);
      // data.forEach(pokemon => {
      // console.log(results.url);

        // const card = document.createElement('div');
        // card.setAttribute('class', 'card');

        // const img = document.createElement('img');
        // img.textContent = `${result.url}`;
        // $imgUrl = 'http://pokeapi.co/media/img/';
        // $imgPokemonNo = pokemon.results.url.substring(34, 37);
        // $imgFullPath = $imgUrl + $imgPokemonNo + '.png';

        // container.appendChild(card);
        // card.appendChild(img);
        // card.appendChild(a);
        // p.appendChild(span);

      // });
    // } else {
    //   const errorMessage = document.createElement('marquee');
    //   errorMessage.textContent = `Gah, it's not working!`;
    //   app.appendChild(errorMessage);
    // }
  // }

  // request.send();

});