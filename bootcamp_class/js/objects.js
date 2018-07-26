var glazedDonuts = [
  {
    frosting: 'glazed',
    style: 'cake',
    type: 'old fashioned',
    age: '45',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'regular',
    age: '5',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'jelly filled',
    age: '1',
    time: 'seconds'
  }
];

var purchase;
var numPurchase = 0;
//You
for(var donut in glazedDonuts){
  console.log(glazedDonuts[donut].type);
  if((glazedDonuts[donut].age < 25 && glazedDonuts[donut].time == 'minutes') || glazedDonuts[donut].time == 'seconds'){
    //shop owner
    purchase = glazedDonuts[donut];
    // console.log(purchase);
    numPurchase++;
  }
  else {
    console.log('sorry it has been out a bit longer');
  }
}
console.log(numPurchase);

var Jon = {
  first_name: 'Jon', 
  last_name: 'Snow', 
  age: 25, 
  house: 'House Stark', 
  ancestry: 'Andals', 
  titles: ['Bastard', 'Snow', 'King in the North', 'the Resurrected', 'Lord Commander of the Night\'s Watch', 'Defender of the Reals of Men']
};

console.log(Jon.last_name); // Expected result => Snow