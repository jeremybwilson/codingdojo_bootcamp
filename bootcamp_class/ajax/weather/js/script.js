$(document).ready(function(){
  const baseUrl = "http://api.openweathermap.org/data/2.5/weather?";
  // let cityId = "5809844";
  const apiKey = "35ed712f5f8848d1811811c457093d67";
  // api.openweathermap.org/data/2.5/weather?q=Seattle&APPID=35ed712f5f8848d1811811c457093d67

  $('form').submit(function(){
    let cityId = $('#city').val();
    // let city = $('input[type=text]').val();
    // console.log('city is: ' + city);
    $.get(baseUrl + "q=" + cityId + "&APPID=" + apiKey, function(response){

      let htmlStr = `<h4>Weather in ${cityId} is: `;
      for(let i = 0; i < response.weather.length; i++){
        let weatherDescription = response.weather[i].main;
        htmlStr += `${weatherDescription} skies. `;
      }
      let weatherDegreesKel = response.main.temp;
      function stripDecimals(num){
        return num | 1;
      }
      let weatherDegreesFahr = ((9 / 5) * (weatherDegreesKel - 273) + 32);
      let weatherDegrees = stripDecimals(weatherDegreesFahr);

      htmlStr += `${weatherDegrees} degrees.</h4>`;

      $('.weather-display').show();
      $('.weather-display').html(htmlStr);
    }, "json");

    return false;
  });
});