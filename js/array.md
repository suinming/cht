# shift

## Description

1. The shift() method removes the first element from an array and returns that removed element.
   This method changes the length of the array.

## Syntax

shift()

## Return value

The removed element from the array; undefined if the array is empty.

## Example

// EX1: removed the element from the array
const myFish = ["angel", "clown", "mandarin", "surgeon"];

console.log("myFish before:", myFish);
// myFish before: ['angel', 'clown', 'mandarin', 'surgeon']

const shifted = myFish.shift();

console.log("myFish after:", myFish);
// myFish after: ['clown', 'mandarin', 'surgeon']

console.log("Removed this element:", shifted);
// Removed this element: angel

// EX2: using shift method in while loop
const names = ["Andrew", "Tyrone", "Paul", "Maria", "Gayatri"];

while (typeof (i = names.shift()) !== "undefined") {
console.log(i);
}
// Andrew, Tyrone, Paul, Maria, Gayatri

=======================================================================

# slice

## Description

1. The slice() method returns a shallow copy of a portion of an array into a new array object selected from start to end (end not included)

2. The slice() method is a copying method.
   It does not alter this but instead returns a shallow copy that contains some of the same elements as the ones from the original array.

## Syntax

slice()
slice(start)
slice(start, end)

1. start (optional)
   Zero-based index at which to start extraction, converted to an integer.
   Negative index counts back from the end of the array — if start < 0, start + array.length is used.
   If start < -array.length or start is omitted, 0 is used.
   If start >= array.length, nothing is extracted.

2. end (optional)
   Zero-based index at which to end extraction, converted to an integer. slice() extracts up to but not including end.
   Negative index counts back from the end of the array — if end < 0, end + array.length is used.
   If end < -array.length, 0 is used.
   If end >= array.length or end is omitted, array.length is used, causing all elements until the end to be extracted.
   If end is positioned before or at start after normalization, nothing is extracted.

## Return value

A new array containing the extracted elements.

## Example

// EX1: Return a portion of an existing array
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1, 3);

// fruits contains ['Banana', 'Orange', 'Lemon', 'Apple', 'Mango']
// citrus contains ['Orange','Lemon']

=======================================================================

# splice

## Description

1. The splice() method "changes the contents of an array" by removing or
   replacing existing elements and/or adding new elements in place.

2. The splice() method is generic. It only expects the this value to have a length property and integer-keyed properties.
   Although strings are also array-like, this method is not suitable to be applied on them, as strings are immutable.

## Syntax

splice(start)
splice(start, deleteCount)
splice(start, deleteCount, item1)
splice(start, deleteCount, item1, item2, itemN)

1. start
   Zero-based index at which to start changing the array, converted to an integer.
   Negative index counts back from the end of the array — if start < 0, start + array.length is used.
   If start < -array.length, 0 is used.
   If start >= array.length, no element will be deleted, but the method will behave as an adding function,
   adding as many elements as provided.
   If start is omitted (and splice() is called with no arguments), nothing is deleted.
   This is different from passing undefined, which is converted to 0.

2. deleteCount (optional)
   An integer indicating the number of elements in the array to remove from start.
   If deleteCount is omitted, or if its value is greater than or equal to the number of elements after the position specified by start,
   then all the elements from start to the end of the array will be deleted.
   However, if you wish to pass any itemN parameter, you should pass Infinity as deleteCount to delete all elements after start,
   because an explicit undefined gets converted to 0.
   If deleteCount is 0 or negative, no elements are removed. In this case, you should specify at least one new element (see below).

3. item1, …, itemN (optional)
   The elements to add to the array, beginning from start.
   If you do not specify any elements, splice() will only remove elements from the array.

## Return value

An array containing the deleted elements.
If only one element is removed, an array of one element is returned.
If no elements are removed, an empty array is returned.

## Example

// EX1: Remove 0 (zero) elements before index 2, and insert "drum" and "guitar"
const myFish = ["angel", "clown", "mandarin", "sturgeon"];
const removed = myFish.splice(2, 0, "drum", "guitar");

// myFish is ["angel", "clown", "drum", "guitar", "mandarin", "sturgeon"]
// removed is [], no elements removed

// EX2: Remove 1 element at index 3
const myFish = ["angel", "clown", "drum", "mandarin", "sturgeon"];
const removed = myFish.splice(3, 1);

// myFish is ["angel", "clown", "drum", "sturgeon"]
// removed is ["mandarin"]

// EX3: Remove 1 element at index 2, and insert "trumpet"
const myFish = ["angel", "clown", "drum", "sturgeon"];
const removed = myFish.splice(2, 1, "trumpet");

// myFish is ["angel", "clown", "trumpet", "sturgeon"]
// removed is ["drum"]

// EX4: Remove all elements, starting from index 2
const myFish = ["angel", "clown", "mandarin", "sturgeon"];
const removed = myFish.splice(2);

// myFish is ["angel", "clown"]
// removed is ["mandarin", "sturgeon"]

=======================================================================

#

## Description

## Syntax

## Return value

## Example

=======================================================================
