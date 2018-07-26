$(document).ready(function(){

  const app = document.getElementById('container-fluid');

  const logo = document.createElement('img');
  logo.src = 'images/star-wars-logo.png';
  logo.setAttribute('class', 'title')

  const h1 = document.createElement('h1');
  h1.textContent = "Star Wars Assignment";

  const charContainer = document.createElement('div');
  charContainer.setAttribute('class', 'starwars');

  const statContainer = document.createElement('div');
  statContainer.setAttribute('class', 'starwars-people');

  app.appendChild(h1);
  app.appendChild(logo);
  app.appendChild(charContainer);
  app.appendChild(statContainer);

  // set root portion of media/img URL here
  const imgBaseUrl = 'http://swapi.co/media/img/'
  // talk to the API and retrieve the first ten characters information
  // once a response is received, display their names in a business card
  for(let i = 1; i <= 10; i++){
    $.get("https://swapi.co/api/people/"+i, function(response) {
      let charName = response.name;
      let imgAlt = response.name;
      // set variable to pull in specific Star Wars character ID (from URL) here,
      // get subtring value from the API endpoint for results.url
      // let url = response.url.split('/');
      // let charID = url[url.length - 2];
      // this is another method to parse out unique character ID values from JSON
      let charID = response.url.split('/')[5];

      // this logs each value uniquely => great
      console.log(charID);

      let htmlStr = `<div><h1>${charName}</h1></div>`;
      $('.starwars').append(htmlStr);
      // this is not pullind down unique charID variables into the data-id attribute => bad juju...
      $('.starwars>div').attr('data-id', charID);

      // $('#starwars-people>div').append(`<img alt="${imgAlt}" id="${pokemonCharID}" src="${pokemonCharFullPath}" />`);
    }, "json");
  }

  // if the business card is clicked, show that particular characters stats
  // in the starwars-people container
  $('.starwars').on('click', 'div', function() {
    // to do this, we need to send another request to the API.
    var id = $(this).attr('data-id');
    $.get("https://swapi.co/api/people/"+id, function(response) {
      let charHairColor = response.hair_color;
      let charEyeColor = response.eye_color;
      let charHeight = response.height;
      let charGender = response.gender;
      let charID = response.url.split('/')[5];

      let htmlStr = `<div><ul><li><span class="strong">Hair color:</span> ${charHairColor}</li><li><span class="strong">Eye color:</span> ${charEyeColor}</li><li><span class="strong">Height:</span> ${charHeight} cm</li><li><span class="strong">Gender:</span> ${charGender}</li></ul></div>`;
      // $('.starwars-people').append(htmlStr);
      $('.starwars-people').show().attr('style', 'display: inline-block;').html(htmlStr);
    }, "json");
  });

  // when an individual pokemon image is hovered over, 
  // toggle the hidden div on/off
  // $('').click(function(){
  //   $('').show();
  // });

});