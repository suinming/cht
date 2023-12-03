## description

Set objects are collections of values. A value in the set may only occur once; it is unique in the set's collection.
You can iterate through the elements of a set in insertion order.
The Set object lets you store unique values of any type, whether primitive values or object references.

## performance

The has method checks if a value is in the set, using an approach that is, on average,
quicker than testing most of the elements that have previously been added to the set.
In particular, it is, on average, faster than the Array.prototype.includes method when an array has a length equal to a set's size.

## properties

- Set.prototype.size()
  - The size accessor property of Set instances returns the number of (unique) elements in this set.

```js
const set1 = new Set();
const object1 = {};

set1.add(42);
set1.add("forty two");
set1.add("forty two");
set1.add(object1);

console.log(set1.size);
// Expected output: 3
```

## methods

- Set.prototype.add()
- Set.prototype.delete()
- Set.prototype.has()
- Set.prototype.forEach()
- Set.prototype.values()
- Set.prototype.clear()

```js
const set = new Set();
// Set.prototype.add()
console.log("==add");
set.add(1);
set.add("one");
set.add({ name: "one", id: 1 });
// 需要替deletObj宣告一個變數，後續才能刪除
// 因為Set刪除元素是by reference
const deleteObj = { name: "deleteObj", id: 2 };
set.add(deleteObj);
console.log(set);
// Set.prototype.delete()
console.log("==delete");
set.delete(deleteObj);
console.log(set);
// Set.prototype.has()
console.log("==has");
console.log(set.has(1));
console.log(set.has("one"));
console.log(set.has(deleteObj));
// Set.prototype.foreach()
console.log("==foreach");
set.forEach((val) => {
  console.log(val);
});
// Set.prototype.values()
console.log("==create iterator by using values method");
const iterator = set.values();
console.log(iterator.next().value);
console.log(iterator.next().value);
console.log(iterator.next().value);
// Set.prototype.clear()
console.log("==clear");
set.clear();
console.log(set);
```
