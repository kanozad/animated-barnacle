// // ninja.js
// console.log('shit');

// var n = {};

// var i = [];

// i.push('crap');

// n.name = 'Bubba';
// n.att = i;

// n.func = console.log;

// n.func(n);

// /**
//  *
//  * @param first
//  * @param remaining - a rest parameter gathering all the remaining arguments
//  * @returns {number}
//  */
// function multimax(first, ...remaining) {
//     var sorted = remaining.sort(function(a, b) {
//         return b - a;
//     });

//     return first * sorted[0];
// }

// console.log(multimax(4, 9, 11, 3, 1, 6));

// function* genetal() {
//     yield 1
// }

// function abc() {
//     console.log("boo");
// }

// n.genetal = genetal;

// n.func(n.genetal());

// console.log(genetal());

// function* fibonacci(n) {
//     const infinite = !n && n !== 0;
//     let current = 0;
//     let next = 1;

//     while (infinite || n--) {
//         yield current;
//         [current, next] = [next, current + next];
//     }
// }

// function performAction(ninja, action="skulking") {
//     console.log(ninja + " " + action);
// }


// performAction("Dickhead");
// performAction("Buttwad", "doinking");

// abc(1, "two", "three");

var re = /^[A-Za-z]{2,2}$/

console.log('123'.match(re));
console.log('A'.match(re));

console.log('1a'.match(re));
console.log('a1'.match(re));

console.log('ba'.match(re));
console.log('BA'.match(re));
console.log('BAAAAAA'.match(re));

console.log('fuck you');
