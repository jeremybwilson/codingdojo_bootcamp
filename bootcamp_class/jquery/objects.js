// why use objects
// How do we use them?

var person = {
  name: "jeremy",
  age: 42,
  location: "Pyuallup",
  ability: function(){
    console.log('Hello');
  },
  canDrive: true,
  doesCode: true
}
// if(person.age === 42 && person.canDrive == true){
//   console.log('You are ' + person.age + ' and old enough to drive!');
// }
// console.log(person.doesCode);
// person.ability();

// for(var key in person){
//   console.log(person[key]);
// }