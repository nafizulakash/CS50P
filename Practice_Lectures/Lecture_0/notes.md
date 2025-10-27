Lecture_0 Notes: Python Fundamentals (Under development)

> **Note**: These notes were AI-generated based on my personal CS50P practice files containing my code and rough comments. They represent my learning journey and are provided as a study reference.
> 
> - **Original Content**: My code and personal observations
> - **AI Assistance**: Organization, formatting, and clarity improvement
> - **Purpose**: Personal study and knowledge sharing


📚 Topics Covered
Basic Output & Input

String Formatting & Methods

Function Definitions & Parameters

Variable Scope

Recursion Concepts

Return Statements

Type Conversion & Rounding

Number Formatting



Basic Output & Input
Print Function
Basic print statement: print("text")

Default behavior: ends with newline \n

Can override default parameters:

end parameter controls line ending

sep parameter controls separator between items

python
print("Hello")  # Ends with newline
print("Hello", end="")  # No newline
print("Hello", "World", sep="???")  # Custom separator
User Input
input() function captures user input as string

Always returns string type, needs conversion for numbers

python
name = input("What's your name? ")
String Formatting & Methods
String Formatting Options
Concatenation: "Hello, " + name

Comma separation: print("Hi,", name)

f-strings (recommended): Embed variables directly with f"Hello {name}"

python
print(f"Hello, {name}")  # f-string format
String Methods
.strip(): Removes whitespace from both ends

.capitalize(): Capitalizes first letter only

.title(): Capitalizes first letter of each word

Method chaining: Multiple methods in one line

python
name = input("Name? ").strip().title()  # Chain methods
String Manipulation
Split strings: first, last = name.split()

Escape characters: Use \ for special characters

Quotes in strings: Use different quote types or escape characters

python
first, last = name.split()  # Split into parts
print('Hello "Friend"')  # Mixing quote types
print("Hello \"Friend\"")  # Escape characters
Functions
Function Definition
Use def keyword to define functions

Functions must be defined before calling

Parameters can have default values

python
def hello(to="World"):  # Default parameter
    print(f"Hello, {to}")
Function Organization
Define main() function for program structure

Call main() at the end to start program

Organize functions logically

python
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print(f"Hello, {to}")

main()  # Program entry point
Return Values
return statement sends value back from function

Functions can return calculated results

Return values can be used directly in f-strings

python
def square(n):
    return n * n  # Return calculated value

# Usage:
print(f"Square: {square(5)}")  # Direct usage
Variable Scope
Local variables: Defined inside functions

Global variables: Defined outside functions

Functions can access global variables

python
name2 = "Global"  # Global variable

def main():
    name1 = input("Name? ")  # Local variable
    hello(name1, name2)  # Using both local and global
Advanced Concepts
Recursion
Function that calls itself

Requires base case to avoid infinite recursion

Python has recursion depth limit (~1000)

python
def main():
    # ... code ...
    main()  # Recursive call - creates infinite loop!
Alternative Square Methods
python
def square(n):
    return n * n      # Multiplication
    return n ** 2     # Exponentiation
    return pow(n, 2)  # Power function
Calculator & Number Operations
Type Conversion
input() always returns string

Convert to numbers: int() for integers, float() for decimals

Essential for mathematical operations

python
x = int(input("Enter x: "))    # Integer conversion
y = float(input("Enter y: "))  # Float conversion
Mathematical Operations
Basic arithmetic: +, -, *, /

Without conversion: string concatenation occurs

With conversion: proper mathematical operations

python
z = x + y  # Mathematical addition (with conversion)
Rounding & Formatting
round(number, digits): Rounds to specified decimal places

f-string formatting: {variable:.2f} formats to 2 decimal places

Thousands separator: {variable:,} adds commas

python
z = round(x / y, 2)          # Round to 2 decimal places
print(f"Result: {z:.2f}")    # Format to 2 decimal places
print(f"Number: {z:,}")      # Add thousands separators
Key Syntax Patterns
Print Function Parameters
python
print("text")                 # Basic
print("text", end="")         # No newline
print("a", "b", sep="---")    # Custom separator
String Methods
python
text.strip()                  # Remove whitespace
text.capitalize()             # Capitalize first letter
text.title()                  # Title case
text.strip().title()          # Method chaining
Function Patterns
python
def function_name(parameter=default):
    # code
    return value
Type Conversion
python
int(string)    # Convert to integer
float(string)  # Convert to float
str(number)    # Convert to string