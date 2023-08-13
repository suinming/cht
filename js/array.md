# Array.prototype.shift()

## Description

1. The shift() method removes the first element from an array and ==returns that removed element==.
   This method changes the length of the array.

## Syntax

shift()

## Return value

The removed element from the array; undefined if the array is empty.

## Example

```js
// EX1: removed the element from the array
const myFish = ["angel", "clown", "mandarin", "surgeon"];

console.log("myFish before:", myFish);
// myFish before: ['angel', 'clown', 'mandarin', 'surgeon']

const shifted = myFish.shift();

console.log("myFish after:", myFish);
// myFish after: ['clown', 'mandarin', 'surgeon']

console.log("Removed this element:", shifted);
// Removed this element: angel
```

```js
// EX2: using shift method in while loop
const names = ["Andrew", "Tyrone", "Paul", "Maria", "Gayatri"];

while (typeof (i = names.shift()) !== "undefined") {
  console.log(i);
}
// Andrew, Tyrone, Paul, Maria, Gayatri
```

=======================================================================

# Array.prototype.unshift()

## Description

The unshift() method adds the specified elements to the beginning of an array and returns the new length of the array.
Please note that, if multiple elements are passed as parameters, they're inserted in chunk at the beginning of the object, in the exact same order they were passed as parameters.
Hence, calling unshift() with n arguments once, or calling it n times with 1 argument (with a loop, for example), don't yield the same results.

## Syntax

unshift()
unshift(element0)
unshift(element0, element1)
unshift(element0, element1, /_ … ,_/ elementN)

## Return value

The new length property of the object upon which the method was called.

## Example

```js
// EX1:
const arr = [1, 2];

arr.unshift(0); // result of the call is 3, which is the new array length
// arr is [0, 1, 2]

arr.unshift(-2, -1); // the new array length is 5
// arr is [-2, -1, 0, 1, 2]

arr.unshift([-4, -3]); // the new array length is 6
// arr is [[-4, -3], -2, -1, 0, 1, 2]

arr.unshift([-7, -6], [-5]); // the new array length is 8
// arr is [ [-7, -6], [-5], [-4, -3], -2, -1, 0, 1, 2 ]
```

=======================================================================

# Array.prototype.slice()

## Description

1. The slice() method ==returns a shallow copy== of a portion of an array into a new array object selected from start to end (end not included)

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

```js
// EX1: Return a portion of an existing array
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1, 3);

// fruits contains ['Banana', 'Orange', 'Lemon', 'Apple', 'Mango']
// citrus contains ['Orange','Lemon']
```

=======================================================================

# Array.prototype.splice()

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

```js
// EX1: Remove 0 (zero) elements before index 2, and insert "drum" and "guitar"
// 當 deleteCount 為 0 時，將 element 在 target element 前塞入
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
```

=======================================================================

# Array.from()

## Description

The Array.from() static method creates a new, shallow-copied "Array instance" from an iterable or array-like object.

## Syntax

Array.from(arrayLike)
Array.from(arrayLike, mapFn)
Array.from(arrayLike, mapFn, thisArg)

1. arrayLike
   An iterable or array-like object to convert to an array.

2. mapFn Optional
   A function to call on every element of the array.
   If provided, every value to be added to the array is first passed through this function,
   and mapFn's return value is added to the array instead.
   The function is called with the following arguments:

- element
  The current element being processed in the array.
- index
  The index of the current element being processed in the array.

3. thisArg Optional
   Value to use as this when executing mapFn.

## Return value

A new Array instance.

## Example

```js
// EX1: make sequence array from the array-like object
Array.from({ length: 4 }, (value, index) => value); // [0,1,2,3]

// EX2: make range function
const rangeFunction = (start, stop, step) => Array.from({length: (stop - start / step + 1)}, (_, index) => start + step \* index)
```

=======================================================================

# Array.prototype.every()

## Description

The every() method tests whether all elements in the array pass the test implemented by the provided function.
It returns a Boolean value.

The every() method is an iterative method.
It calls a provided callbackFn function once for each element in an array,
until the callbackFn returns a falsy value.
If such an element is found, every() immediately returns false and stops iterating through the array.
Otherwise, if callbackFn returns a truthy value for all elements, every() returns true.

every acts like the "for all" quantifier in mathematics.
In particular, for an empty array, it returns true.
(It is vacuously true that all elements of the empty set satisfy any given condition.)

## Syntax

```js
every(callbackFn);
every(callbackFn, thisArg);
```

1. callbackFn
   A function to execute for each element in the array.
   It should return a truthy value to indicate the element passes the test,
   and a falsy value otherwise.
   The function is called with the following arguments:

- element
  The current element being processed in the array.

- index
  The index of the current element being processed in the array.

- array
  The array every() was called upon.

2. thisArg Optional
   A value to use as this when executing callbackFn. See iterative methods.

## Return value

true if callbackFn returns a truthy value for every array element. Otherwise, false.

## Example

```js
// EX1: Check if one array is a subset of another array
const isSubset = (array1, array2) =>
  array2.every((element) => array1.includes(element));

console.log(isSubset([1, 2, 3, 4, 5, 6, 7], [5, 7, 6])); // true
console.log(isSubset([1, 2, 3, 4, 5, 6, 7], [5, 8, 7])); // false

// EX2: using every on spare array
console.log([1, , 3].every((x) => x !== undefined)); // true
console.log([2, , 2].every((x) => x === 2)); // true

// EX3: effecting the existing array(modifying, appending, deleting)
// ---------------
// Modifying items
// ---------------
let arr = [1, 2, 3, 4];
arr.every((elem, index, arr) => {
  arr[index + 1]--;
  console.log(`[${arr}][${index}] -> ${elem}`);
  return elem < 2;
});

// Loop runs for 3 iterations, but would
// have run 2 iterations without any modification
//
// 1st iteration: [1,1,3,4][0] -> 1
// 2nd iteration: [1,1,2,4][1] -> 1
// 3rd iteration: [1,1,2,3][2] -> 2

// ---------------
// Appending items
// ---------------
arr = [1, 2, 3];
arr.every((elem, index, arr) => {
  arr.push("new");
  console.log(`[${arr}][${index}] -> ${elem}`);
  return elem < 4;
});

// Loop runs for 3 iterations, even after appending new items
//
// 1st iteration: [1, 2, 3, new][0] -> 1
// 2nd iteration: [1, 2, 3, new, new][1] -> 2
// 3rd iteration: [1, 2, 3, new, new, new][2] -> 3

// ---------------
// Deleting items
// ---------------
arr = [1, 2, 3, 4];
arr.every((elem, index, arr) => {
  arr.pop();
  console.log(`[${arr}][${index}] -> ${elem}`);
  return elem < 4;
});

// Loop runs for 2 iterations only, as the remaining
// items are `pop()`ed off
//
// 1st iteration: [1,2,3][0] -> 1
// 2nd iteration: [1,2][1] -> 2
```

=======================================================================

# Array.prototype.find()

## Description

The find() method returns the first element in the provided array that satisfies the provided testing function.
If no values satisfy the testing function, undefined is returned.
callbackFn is invoked for every index of the array, not just those with assigned values.
Empty slots in sparse arrays behave the same as undefined.

## Syntax

find(callbackFn)
find(callbackFn, thisArg)

1. callbackFn
   A function to execute for each element in the array.
   It should return a truthy value to indicate a matching element has been found, and a falsy value otherwise.
   The function is called with the following arguments:

- element
  The current element being processed in the array.

- index
  The index of the current element being processed in the array.

- array
  The array find() was called upon.

2. thisArg Optional
   A value to use as this when executing callbackFn.

## Return value

The first element in the array that satisfies the provided testing function. Otherwise, undefined is returned.

## Example

```js
// EX1: using find on sparse array
// Declare array with no elements at indexes 2, 3, and 4
const array = [0, 1, , , , 5, 6];

// Shows all indexes, not just those with assigned values
array.find((value, index) => {
  console.log("Visited index", index, "with value", value);
});
// Visited index 0 with value 0
// Visited index 1 with value 1
// Visited index 2 with value undefined
// Visited index 3 with value undefined
// Visited index 4 with value undefined
// Visited index 5 with value 5
// Visited index 6 with value 6

// EX2: Calling find() on non-array objects
const arrayLike = {
  length: 3,
  "-1": 0.1, // ignored by find() since -1 < 0
  0: 2,
  1: 7.3,
  2: 4,
};
console.log(Array.prototype.find.call(arrayLike, (x) => !Number.isInteger(x)));
// 7.3
```

=======================================================================

# Array.prototype.indexOf()

## Description

The indexOf() method returns the first index at which a given element can be found in the array, or -1 if it is not present.

## Syntax

indexOf(searchElement)
indexOf(searchElement, fromIndex)

1. searchElement
   Element to locate in the array.
2. fromIndex(optional)
   Zero-based index at which to start searching, converted to an integer.
   - Negative index counts back from the end of the array — if fromIndex < 0, fromIndex + array.length is used. Note, the array is still searched from front to back in this case.
   - If fromIndex < -array.length or fromIndex is omitted, 0 is used, causing the entire array to be searched.
   - If fromIndex >= array.length, the array is not searched and -1 is returned.ero-based index at which to start searching, converted to an integer.

## Return value

The first index of the element in the array; -1 if not found.

## Example

```js
// EX1: using indexOf
const array = [2, 9, 9];
array.indexOf(2); // 0
array.indexOf(7); // -1
array.indexOf(9, 2); // 2
array.indexOf(2, -1); // -1
array.indexOf(2, -3); // 0

// EX2: Finding all the occurrences of an element
const indices = [];
const array = ["a", "b", "a", "c", "a", "d"];
const element = "a";
let idx = array.indexOf(element);
while (idx !== -1) {
  indices.push(idx);
  idx = array.indexOf(element, idx + 1);
}
console.log(indices);
// [0, 2, 4]
```

=======================================================================

#

## Description

## Syntax

## Return value

## Example

```js
// EX1:
```

=======================================================================

#

## Description

## Syntax

## Return value

## Example

```js
// EX1:
```

=======================================================================

#

## Description

## Syntax

## Return value

## Example

```js
// EX1:
```

=======================================================================

#

## Description

## Syntax

## Return value

## Example

```js
// EX1:
```

=======================================================================

#

## Description

## Syntax

## Return value

## Example

```js
// EX1:
```

=======================================================================

#

## Description

## Syntax

## Return value

## Example

```js
// EX1:
```

=======================================================================
