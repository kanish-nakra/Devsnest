//  Write a JavaScript program to find the most frequent item of an array
// Sample array : var arr1=[3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3];
// Sample Output : a ( 5 times )

var arr1 = [3, "a", "a", "a", 2, 3, "a", 3, "a", 2, 4, 9, 3];

var freqMap = {};
for (let i = 0; i < arr1.length; i++) {
  if (arr1[i] in freqMap) {
    freqMap[arr1[i]] += 1;
  } else {
    freqMap[arr1[i]] = 1;
  }
}

console.log(freqMap);

var maxFreq = arr1[0];
for (let i = 0; i < arr1.length; i++) {
  if (freqMap[arr1[i]] > freqMap[maxFreq]) {
    maxFreq = arr1[i];
  }
}

console.log(maxFreq);
