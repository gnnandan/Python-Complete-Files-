<!-- markdownlint-disable -->


** Syntax ** - The rules how each instruction is written
**Semantics** - The effects the instructions have

**Script** - a program that's short, simple and can be write very quickly 

**Automation** - replacing **manual step ** with one that happens automatically

**interpreter** - interpreter is the program that reads and executes code

**What is Python**
    - General purpose scripting language

**functions** - piece of code that perform specific task

**keywords**- reserved words to construct instructions

**keywords list**
-------
False | class | finally | is | return
------|-------|---------|----|-------
None | continue | for | lambda | try
True | def | from | nonlocal | while
and | del | global | not | with
as | elif | if | or | yield
assert | else | import | pass | 
break | except | in | raise | 

___________________________________________________________

## **Datatypes** *Use type() to know the type of data*
1. **String** - collection of character
2. **int** - integer
3. **float** - real number
4. **boolean** - True or False




___________________________________________________________
## **Variables**
    - It's name used as a reference
    - '=' is used to as assignment
### Rules
- don't use reserved keywords or functions as avariable name 
- names should't have space between them
- variable name must start with letter or _ (underscore)
- variable names can be made up with only alphabet/letter/number/_
    - I_am_a_variable is the **valid**
    - I_am_a_variable2 is also a **valid**
    - Apples_&_oranges is **invalid**
```
Python variables are case sensitive, so capitalization matters. Lowercase name, uppercase name and all caps name are all valid and different variable names, and that rule on variables is invariable.
```

## conversions
- **implicit conversion** - interpreter automatically convert one datatype to another.
- **explit conversion** - user forcefully covert one datatype to another.

## functions
- 1. defining functions 
    - a building block of program
    - to define a function we use `def` keyword 
    - we can add parameters also in like this `_(parameters_here)_`
       - defining and adding parameter def(name):

- 2. calling a functions 
    - while calling a functions the number of parameter should be same as number of parameters used

- 3. returning values
    - it returns some value and this can be used as reusability when return is not used means it will return _None_

## Coding style
- **self-documenting code**- a code should be written in such a way that it should be easily understandable.
    - variable_name,function_name etc........
    - use comment when every necessary to explain the purpose of the code.

## operator 
- ### Comparison Operator
Note= "=" is not "==", "=" is assignment operator and "==" is equal to operator
    - **>** : Greaterthan
    - **<** : lesserthan
    - **==** : equals to
    -  **!=** : not equal
    - **>=** : Greaterthan or equalto
    -  **<=** : lesserthan or equalto

- ### Logical Operators
    - **and** :and operator, _both sides of the statement being evaluated must be true_ for the whole statement to be true
    -  **or** :or operator, if _either side of the comparison is true_, then the whole statement is true
    -  **not** : not operator _simply inverts the value of the statement_ immediately following it 
_________________________________________________________
## Statements
- ### **1. Branching Statements** (The ability of program to alter its execution sequence)
    - **if** : If the comparison is True, the code inside the if body is executed. If the comparison evaluates to False, then the code block is skipped and will not be run.
    - **if else** : when if block false it go to else block
    - **elif** : same as if block 
        - Syntax 
            ```
            if condition1:
                if-block
            elif condition2:
                elif-block
            else:
                else-block
            
            ```
- **while loop**
    - A while loop will _continuously execute_ code depending on the value of a condition.
- **for loop**
    - it is mainly used to iterate characters in string,list, tuples etc...

- **recursion**
    - it is a repeated application of same procedure to a smaller problem.
    - **Document recursion**
        ```
        def recursive_function(parameters):
            if base_case_condition(parameters):
                return base_case_value
            recursive_function(modified_parameters)
        ```
- **common errors**
    - variables used without initialization (_NameError:_ name 'var_name' is not defined)
    - the loop may never finish and we get what's called an _infinite loop_


___________________________________________________________
- **String " "**
