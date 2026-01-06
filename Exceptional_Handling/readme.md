* Exception/Error Handling

> avoid shutting dowm the hole code
> we should handle error graceful
 
* what is error ?

if we write code then we will face have errors
    > syntax error/compile error : during complilation
    > exceptions/runtime error : during execution

Syntax error :
    - a syntax errors occurs when python interpreter finds something wrong with the structure of the code
        > not following rules if language
        > program fails to run and will show message explaining the error 
        > ex : parentheses , undefined variables , indendation , :[colon]


* what is exception/runtime error ?
exception is the error that occur during the execution of the program

> it doesnot prevent program from running but cause it to crash if not handled normally faced when something happens
> raised by python runtime
> ex > division by zero , database connection , memory overflow

🔹 Why Exception Handling?

Prevents program crashes

Handles unexpected inputs

Improves user experience

Useful in real-world apps (APIs, DB, files, user input)

| Keyword   | Purpose                   |
| --------- | ------------------------- |
| `try`     | Code that may cause error |
| `except`  | Handles the error         |
| `else`    | Runs if no error          |
| `finally` | Always executes           |
| `raise`   | Manually raise exception  |


| Do                   | Don’t                |
| -------------------- | -------------------- |
| Use meaningful names | Catch all exceptions |
| Add messages         | Ignore exceptions    |
| Create hierarchy     | Raise generic errors |
| Handle properly      | Crash program        |

