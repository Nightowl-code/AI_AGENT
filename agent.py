Here is a simple Python function that does exactly that:

```python
def print_greeting():
    print("Hello world Laxman")

# Call the function 
print_greeting()
```

This function, when called, prints the string "Hello world Laxman" to the console. If you want to make it more dynamic to greet different people, you could modify the function like so:

```python
def print_greeting(name):
    print("Hello world " + name)

# Call the function 
print_greeting("Laxman")
```
This version of the function takes an argument that it adds to the end of the greeting. Calling `print_greeting("Laxman")` would produce the same output as before. Calling `print_greeting("John")` would instead print "Hello world John".