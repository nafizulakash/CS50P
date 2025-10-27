
# Lecture 0 Notes: Python Fundamentals

> **Note**: These notes were AI-generated based on my personal CS50P practice files containing my code and rough comments.  
> They represent my learning journey and are provided as a study reference.
>
> - **Original Content**: My code and personal observations
> - **AI Assistance**: Organization, formatting, and clarity improvement
> - **Purpose**: Personal study and knowledge sharing




# 📚 Topics Covered

1. [Basic Output & Input](#basic-output--input)
2. [String Formatting & Methods](#string-formatting--methods)
3. [Function Definitions & Parameters](#function-definitions--parameters)
4. [Variable Scope](#variable-scope)
5. [Recursion Concepts](#recursion-concepts)
6. [Return Statements](#return-statements)
7. [Type Conversion & Rounding](#type-conversion--rounding)
8. [Number Formatting](#number-formatting)

# CS50P Lecture Notes: Python Fundamentals

## 📋 Table of Contents
- [Basic I/O Operations](#basic-io-operations)
- [String Manipulation](#string-manipulation)
- [Function Implementation](#function-implementation)
- [Recursion Concepts](#recursion-concepts)
- [Return Statements](#return-statements)
- [Type Conversion & Arithmetic](#type-conversion--arithmetic)
- [Number Formatting](#number-formatting)

---

## Basic I/O Operations

### **Print Function Fundamentals**
- Basic output: `print("text")`
- Default behavior: Automatically adds newline (`\n`)
- Parameter types:
  - **Positional parameters**: Standard arguments
  - **Named parameters**: `end` and `sep`

```python
# Default behavior
print("Hello")
print("World")  # Prints on new line

# Override default parameters
print("Hello", end="")  # No newline
print("World")          # Continues on same line

print("Hello", "World", sep="???")  # Custom separator

## Basic Output & Input

### Print Function
```python


