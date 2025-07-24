# PyGrps: A Python-based Fun Programming Language
<p align="center">
  <img src="https://example.com/pygrps-logo.png" alt="PyGrps Logo">
</p>

PyGrps is a programming language developed using Python, designed to provide a simplified syntax for easier programming. It aims to offer a beginner-friendly approach while maintaining the power and versatility of Python.

## Features

- **Easy Syntax**: PyGrps offers a simplified syntax that reduces the learning curve.

- **Python Compatibility**: PyGrps is built on Python, allowing seamless integration with existing Python code and libraries.

- **Core Concepts**: Supports many core concepts like variables, datatype, conditional statements, FOR loop, WHIILE loop, functions, keywords (20+), modules (random, maths etc.), in-built modules (100+), PYTHON module support and much more.

- **.grps Extension**: Special .grps extension for PyGrps programs

## Installation

To use PyGrps, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/code-with-rajeev/PyGrps.git


## How to use this programming language?

for running - run "grps.py"
best if you have Tkinter installed.

## 📚 Table of Contents

1. [Basics](#basics)
2. [Print Statement](#print-statement)
3. [Basic Operation](#print-statement)
4. [Data Types](#data-types)

   * [Number](#number)
   * [String](#string)

     * [Slicing](#slicing)
     * [Operations](#operations)
     * [Methods](#methods)

---

## Basics

* `;` - **newline separator**
  Optional (like Python), but required in **inline multiple statements**.

* **Comments**:

```pygrps
-- This is inline-comment --

---
This is
multi-line comment
---
```
---

## 🔨 Print Statement

* **in-built method**: `show()`
* **Arguments**:
  * Type: Expression or Identifier

### Example:

```pygrps
a, b = 2, 4
show( (a + b)^2 == (a^2 + b^2 + 2*(a * b)) )
```

#### Output:

```
True
```

---

## Data Types

### Number

```pygrps
-- Inline declaration --
a, b = 2, 8

show(x^y)
show(type(a))
```

#### Output:

```
256
GRPS OBJ <class 'int'>
```

---

### 🌤️ String

#### Datatype:
```
GRPS OBJ <class 'str'>
```

#### 🧪 Slicing

##### STR[start:stop:skip] all these parameters are optional.


```pygrps
STR = "_h_e_l_l_o_ _w_o_r_l_d_"
show(STR[1::2])
```

#### Output:

```
hello world
```

---

### 🔗 Operations

#### Concatenation:

```pygrps
greet = 'hello ' + 'World!'
show(greet)
```

> Output: `hello World!`

#### Repetition:

```pygrps
text = 'Well '
show(text * 3)
```

> Output: `Well Well Well`

---

### 🛠️ Methods

#### 🔍 Search Methods

```pygrps
STR = 'can you find x here'
show(STR.find('x'))           -- Output: 13

STR = 'a b c a b c'
show(STR.rfind('b'))          -- Output: 8

STR = 'apple app pple '
show(STR.count('app'))        -- Output: 2

STR = 'HELLOWORLD'
show(STR.startswith('HELLO')) -- Output: True
show(STR.endswith('WORLD'))   -- Output: True
```

---

#### 👁️ Case Conversion

```pygrps
txt = 'hEllo PYgrps'

show(txt.lower())      # hello pygrps
show(txt.upper())      # HELLO PYGRPS
show(txt.capitalize()) # Hello pygrps
show(txt.title())      # Hello Pygrps
show(txt.swapcase())   # HeLLO pyGRPS
```

#### ✔️ Character Checks

```pygrps
s = 'Python3'

show(s.isalpha())       -- False
show(s.isdigit())       -- False
show(s.isalnum())       -- True
show(' '.isspace())     -- True
show(s.isupper())       -- False
show(s.istitle())       -- True
show('123'.isnumeric()) -- True
show('123'.isdecimal()) -- True
```

---

#### Split & Join

```pygrps
text = 'a,b,c'
parts = text.split(',')           -- ['a', 'b', 'c']
joined = '*'.join(parts)
show(joined)                      -- a*b*c
```

---

#### Strip & Replace

```pygrps
s = '   Hello GRPS   '
s1 = s.strip()                    -- 'Hello GRPS'
s2 = s.replace('GRPS', 'World')
show(s1 + '; ' + s2)              -- Hello GRPS; Hello World
```

---

> ✅ **Next Sections** (To Be Added):
>
> * Control Flow (if/else)
> * Loops (for, while)
> * Functions
> * Error Handling
> * Custom Features / Built-in Modules
> * Real Project Examples
