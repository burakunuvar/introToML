### <u> Errors and Exceptions </u>

-   **Syntax errors** occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

-   **Exceptions** occur when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.
    -   ValueError
    -   AssertionError
    -   IndexError
    -   KeyError
    -   TypeError

#### Try Statement

-   We can use try statements to handle exceptions. There are four clauses:

    -   **try:** This is the only mandatory clause in a `try` statement. The code in this block is the first thing that Python runs in a `try` statement.

    -   **except:** If Python runs into an exception while running the `try` block, it will jump to the except block that handles that exception.

    -   **else:** If Python runs into no exceptions while running the `try` block, it will run the code in this block after running the try block.
    -   **finally:** Before Python leaves this `try` statement, it will run the code in this `finally` block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the `except` or `else` block, this finally block will still be executed before stopping the program.

```Python
while True :
    try:
        x=int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number')
    else:
        print('no exceptions - running well ')
    finally:
        print('\n**right input provided**\n ')
```


- You can still access its error message :

 ```python
try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))   
 ```

 - When you don't have a specific error you're handling:

 ```python
 try:
     # some code
 except Exception as e:
    # some code
    print("Exception occurred: {}".format(e))
```
