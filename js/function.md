# Function.prototype.bind()

## Description

The bind() method creates a new ==function== that, when called,
has its this keyword set to the provided value,
with a given sequence of arguments preceding any provided when the new function is called.

## Syntax

bind(thisArg)
bind(thisArg, arg1, arg2, /_ …, _/ argN)

1. thisArg
   The value to be passed as the this parameter to the target function func when the bound function is called.
   If the function is not in strict mode, null and undefined will be replaced with the global object,
   and primitive values will be converted to objects.
   The value is ignored if the bound function is constructed using the new operator.

2. arg1, …, argN ( Optional )
   Arguments to prepend to arguments provided to the bound function when invoking func.

## Return value

A copy of the given function with the specified this value, and initial arguments (if provided).

## Example

```js
// EX1: create a bound function
// Top-level 'this' is bound to 'globalThis' in scripts.
this.x = 9;
const module = {
  x: 81,
  getX() {
    return this.x;
  },
};

// The 'this' parameter of 'getX' is bound to 'module'.
console.log(module.getX()); // 81

const retrieveX = module.getX;
// The 'this' parameter of 'retrieveX' is bound to 'globalThis' in non-strict mode.
console.log(retrieveX()); // 9

// Create a new function 'boundGetX' with the 'this' parameter bound to 'module'.
const boundGetX = retrieveX.bind(module);
console.log(boundGetX()); // 81
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
