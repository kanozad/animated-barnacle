const fs = require('fs');

// const book = {
//     title: 'Watchmen',
//     author: 'Alan Moore'
// }
//
// var gumby = JSON.stringify(book);
// fs.writeFileSync('1-json.json', gumby);

// console.log(gumby)
//
// var parsed = JSON.parse(gumby);
//
// console.log(parsed.title);

const dataBuffer = fs.readFileSync('1-json.json');
const dataJson = dataBuffer.toString();
const data = JSON.parse(dataJson);
console.log(data);

data.name="Lard Ass"
data.planet="Planet Fart Fart Hat"
data.age=33

var poop = JSON.stringify(data);
console.log(poop);
fs.writeFileSync('1-json.json', poop);


