// JavaScript object notes

var jeremy = {
  age: 43,
  first_name: "Jeremy",
  last_name: "Wilson",
  eye_color: "hazel",
  height: 69,
  year: 1975,
  month: 6,
  day: 26
}
console.log(jeremy.age)
// console.log(this.jeremy);
jeremy.age = 30;
jeremy.hobby = "Skiing";
// console.log(jeremy);
console.log("Jeremy's birthday is:" + jeremy.month + '/' + jeremy.day + '/' + jeremy.year);

// for(var key in jeremy){
//   console.log(jeremy[key]);
// }
// console.dir(document);
// document.title = "HEYOOOO";
// console.dir(document);
// console.log(document.getElementById('home'));
// document.getElementById('home').innerHTML = "Hello Dawg Fans";
// document.getElementById('home').style.color = "#F00";

var bod = document.body;
for (var i = 0; i < 5; i ++){
  bod.innerHTML += "<p>This has gone through the loop completely: " +i+ " times</p>";
}

var paragraphs = document.getElementsByTagName('p');
console.log(paragraphs);
for (var i = 0; i < paragraphs.length; i ++){
  // console.log(paragraphs[i].addEventListener);
  paragraphs[i].addEventListener('click', function(){
    this.style.background='blue';
  console.log(this);
  });
}