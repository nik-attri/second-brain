---
author: SELVASUNDAR RAJAN
fetched_at: '2026-11-13T10:20:01.320938Z'
id: acda4243d72d
lane: lead
published: ''
source: linkedin
title: '*CODING INTERVIEW SERIES – PART 2*


  Let''s continue our Coding Interview Series. In Part 1, we covered the basic programm'
url: https://www.linkedin.com/posts/selvasundar-rajan-788a0330a_coding-interview-series-part-2-lets-activity-7526946945110593536-zsxx
---

*CODING INTERVIEW SERIES – PART 2*

Let's continue our Coding Interview Series. In Part 1, we covered the basic programming concepts. Today, let's explore 10 important interview questions about variables, data types, and operators.

*1. What is the difference between a variable and a constant?*

* Variable: A named storage location whose value can change during program execution.

* Constant: A value that should not change once defined.

Example (Python):

``` 
age = 25
age = 30

PI = 3.14159
```

Here, `age` changes, while `PI` is conventionally treated as a constant.

*2. What are primitive data types?*

Primitive data types are the basic types used to represent simple values.

Common examples include:

* Integer

* Float

* Character

* Boolean

The exact primitive types depend on the programming language.

*3. What is the difference between Integer and Float?*

* Integer: Stores whole numbers without decimal points.

* Float: Stores numbers with decimal points.

Example:

``` 
age = 25
price = 99.99
```

*4. What is Type Casting?*

Type casting is the process of converting a value from one data type to another.

Example:

``` 
num = "100"
result = int(num)

print(result)
```

Output:
```
100
```

*5. What is the difference between Implicit and Explicit Type Conversion?*

* Implicit conversion: Automatically performed by the programming language.

* Explicit conversion: Manually performed by the programmer.

Example:

``` 
# Implicit
a = 10
b = 2.5
c = a + b

# Explicit
x = int(10.8)
```

*6. What are Arithmetic Operators?*

Arithmetic operators are used to perform mathematical operations.

| Operator | Operation      |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| %        | Modulus        |
| //       | Floor division |
| **       | Exponentiation |

*7. What is the difference between = and ==?*

* `=` is an assignment operator used to assign a value.

* `==` is a comparison operator used to check whether two values are equal.

Example:

``` 
x = 10

print(x == 10)
```

Output:

``` 
True
```

*8. What are Logical Operators?*

Logical operators are used to combine or modify conditional expressions.

Three common logical operators:

* AND – True if both conditions are true.

* OR – True if at least one condition is true.

* NOT – Reverses the Boolean result.

Example:

``` 
age = 25

print(age > 18 and age < 60)
```

Output:

``` 
True
```

*9. What is the Modulus Operator (%)?*

The modulus operator returns the remainder after division.

Example:

``` 
print(10 % 3)
```

Output:

``` 
1
```

It is commonly used to check whether a number is even or odd.

*10. How do you swap two variables without using a third variable?*

In Python, you can use tuple unpacking.

``` 
a = 10
b = 20

a, b = b, a

print(a, b)
```

Output:

``` 
20 10
```
