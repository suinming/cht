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
// EX1:
const object1 = {
  a: "somestring",
  b: 42,
  c: false,
};

console.log(Object.keys(object1));
// Expected output: Array ["a", "b", "c"]
```

=======================================================================

# Object.hasOwn()

## Description

The Object.hasOwn() static method returns true if the specified object has the indicated property as its own property
even if the property value is null or undefined.
If the property is _inherited_, or does not exist, the method returns false.

## Syntax

Object.hasOwn(obj, prop)

1. obj
   The JavaScript object instance to test.
2. prop
   The String name or Symbol of the property to test.

## Return value

true if the specified object has directly defined the specified property. Otherwise false

## Example

```js
// EX1: Direct vs. inherited properties
const example = {};
example.prop = "exists";

// `hasOwn` will only return true for direct properties:
Object.hasOwn(example, "prop"); // true
Object.hasOwn(example, "toString"); // false
Object.hasOwn(example, "hasOwnProperty"); // false

// The `in` operator will return true for direct or inherited properties:
"prop" in example; // true
"toString" in example; // true
"hasOwnProperty" in example; // true
```

=======================================================================

# Object.defineProperty()

## Description

The Object.defineProperty() static method defines a new property directly on an object, or modifies an existing property on an object,
and returns the object.

## Syntax

Object.defineProperty(obj, prop, descriptor)

1. obj
   The object on which to define the property.
2. prop
   A string or Symbol specifying the key of the property to be defined or modified.
3. descriptor
   Property descriptors present in objects come in two main flavors: data descriptors and accessor descriptors.

   - A _data descriptor_ is a property with a value that may or may not be writable.

     - configurable
     - enumerable
     - value
     - writable

   - An _accessor descriptor_ is a property described by a getter-setter pair of functions.
     - configurable
     - enumerable
     - get
     - set

   A descriptor must be one of these two flavors; it cannot be both.

## Return value

The object that was passed to the function(before you add the prop)

## Example

```js
// EX1: use defineProperty to define the props in person object
const person = {
  name: "frank",
};
// use the data descriptor
Object.defineProperty(person, "gender", {
  configurable: true,
  enumerable: true,
  writable: true,
  value: "male",
});
console.log(person);
// use the accessor descriptor
Object.defineProperty(person, "age", {
  configurable: true,
  enumerable: true,
  get: () => this.value,
  set: (_value) => (this.value = _value),
});
// use setter to set the age
person.age = 25;
console.log(person);
console.log(person.age);
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
