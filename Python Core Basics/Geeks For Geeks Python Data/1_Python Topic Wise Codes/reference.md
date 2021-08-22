<!-- markdownlint-disable -->
### Level 1 Topics
- **Keywords** = reserve words used to perform specific tasks
- **variables** = user defined words used to store some data and these data can be access
    - using variables without assigning a variable cause **NameError**
    - **None** can be used when the we don't know the answer or when we want to **reset the variables**
- **functions**= sequence of instructions used to perform specific tasks
- **class**= A Class is like an object constructor, or a "blueprint" for creating objects.
- **object**= instance of class is called object
- **modules**= Modules refer to a file containing Python statements and definitions and/or classes
- **packages**= Python files and a file with the name __init__ . ... This means that every directory inside of the Python path, which contains a file named __init__ . py, will be treated as a package by Python
- **id()**= it provides unique identifier for every object.
- **is()**= checks the identity of 2 operands are similar or not 
- **in**= tells whether item is present or not

### Level 2 Topics
- **list[ ]** 
  - mutable
  - it is collection of items(container)
  - it can have different items as well

- **tuple( )** 
  - immutable
  - it is ordered and indexed
  - tuple won't create for single element irrespective of ','

- **sets{ }**
  - Distinct/can have any element type
  - unordered
  - no-indexing
  - union, intersection, set difference are fast
  - uses hashing internally 

- **Dictionary{Key:Value}**
  - collection of key-value pairs
  - unordered
  - all key must be distinct 
  - values may be repeated 
  - uses hashing internally

#### Operators
- **operator**
  - Associative & Precedence
  
**|Operator |Precedence|Associative|**
|---------|----------|-----------|
|+ -      |   low    |left-right |
|* / //   |   high   |left-right |
|**       |   highest|right-left |

- **arithmetic operator**
  - +,-,*,/,%,**,//

- **logical operator**
  - and,or,not

- **identity comparision operator**
  - is, is not

- **Membership Operator**
  - in 
    - **string**= check for substring
    - **dictionary**= check for key
    - **list, set & tuple**=check for memberships
  - not in  

- **Bitwise Operator**
  - & "and"
  - | "or"
  - ^ "xor"
  - <<  "leftshift"
  - >>  "rightshift"
  - ~ "Negation"

### statements
#### condition statements

- if,else, elif statment statements
  1. if and else condition:
     1. """
        [Syntax]
        if condition:
            // execute the statements
        else:
            // comes out of the statement
        """
  2. if,else, elif statment statements
     1. [Syntax]
        if condition:
            // execute the if part of statements
        elif:
            // execute the elif part of statements
        else:
            // execute else part of statements
        """
#### looping statements
- **while**
  1. [Syntax]
      while condition:
          statement 1
          .
          .
          .
          statement n
- **for loop**
  1. [Syntax]
      for x in seq:
          statement 1
          .
          .
          .
          statement n