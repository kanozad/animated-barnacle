const request = require("request");

//1b1622efeb0246ac386dcfe73a7bb44c
//http://api.weatherstack.com

const url = 'http://api.weatherstack.com/current?access_key=1b1622efeb0246ac386dcfe73a7bb44c&query=37.8267,-122.4233';

request({ url: url }, (error, response) => {
    const data = JSON.parse(response.body);
    console.log(data.current);
});