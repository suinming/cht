# Object.entries()

## Description

The Object.entries() static method returns an array of a given object's
own enumerable string-keyed property key-value pairs.

## Syntax

Object.entries(obj)

## Return value

An array of the given object's own enumerable string-keyed property key-value pairs.
Each key-value pair is an array with two elements:
the first element is the property key (which is always a string),
and the second element is the property value.

## Example

```js
// EX:1 iterating through the object
// first solution
const obj = { a: 5, b: 7, c: 9 };
for (const [key, value] of Object.entries(obj)) {
  console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
}
// second solution
Object.entries(obj).forEach(([key, value]) => {
  console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
});
```

=======================================================================

# Object.assign()

## Description

Properties in the target object are overwritten by properties in the sources if they have the same key.
Later sources' properties overwrite earlier ones.

The Object.assign() method only copies enumerable and own properties from a source object to a target object.
It uses [[Get]] on the source and [[Set]] on the target, so it will invoke getters and setters.
Therefore it assigns properties, versus copying or defining new properties.
This may make it unsuitable for merging new properties into a prototype if the merge sources contain getters.
//白話文就是 object 合併的概念

## Syntax

Object.assign(target, ...sources)

1. target
   The target object — what to apply the sources' properties to, which is returned after it is modified.

2. sources
   The source object(s) — objects containing the properties you want to apply.

## Return value

the target object

## Example

```js
// EX:1 cloning the object
const obj = { a: 1 };
const copy = Object.assign({}, obj);
console.log(copy); // { a: 1 }

// EX:2 deep copy the object
// For deep cloning, we need to use alternatives like structuredClone(),
// because Object.assign() copies property values.

If the source value is a reference to an object, it only copies the reference value.
const obj1 = { a: 0, b: { c: 0 } };
const obj2 = Object.assign({}, obj1);
console.log(obj2); // { a: 0, b: { c: 0 } }

obj1.a = 1;
console.log(obj1); // { a: 1, b: { c: 0 } }
console.log(obj2); // { a: 0, b: { c: 0 } }

obj2.a = 2;
console.log(obj1); // { a: 1, b: { c: 0 } }
console.log(obj2); // { a: 2, b: { c: 0 } }

obj2.b.c = 3;
console.log(obj1); // { a: 1, b: { c: 3 } }
console.log(obj2); // { a: 2, b: { c: 3 } }

// Deep Clone
const obj3 = { a: 0, b: { c: 0 } };
const obj4 = structuredClone(obj3);
obj3.a = 4;
obj3.b.c = 4;
console.log(obj4); // { a: 0, b: { c: 0 } }
```

=======================================================================

# Object.keys()

## Description

The Object.keys() static method returns an array of a given object's own enumerable string-keyed property names.
This is the same as iterating with a for...in loop,
==except that a for...in loop enumerates properties in the prototype chain as well.==

## Syntax

Object.keys(obj)

## Return value

An array of strings representing the given object's own enumerable string-keyed property keys.

## Example

```js

```

=======================================================================

#

## Description

## Syntax

## Return value

## Example

=======================================================================
