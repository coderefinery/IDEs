---
layout: episode
title: "PyCharm setup"
teaching: 15
exercises: 15
questions:
  - "How to install PyCharm?"
objectives:
  - "PyCharm is installed."
  - "The project is imported into PyCharm."
  - "The cheat sheet is downloaded."
keypoints:
  - "It is easy to start with IDE."
---

# PyCharm setup

In this lesson the typical IDE installation process is completed. This session aims to expose ease of beginning with IDE, point to sources of information.
explained main concepts of IDE, learn about its benefits and motivation to start using it. The goal is to provide basic understanding of what IDEs are and which functions they contain. You will also get a generic idea about the variety of tools available, in next lesson you will get to know some of the tools a bit better. 

## Installation and setup

- follow the software installer guide
- open our exiting project: **File -> Open -> ...** (or download from: https://github.com/coderefinery/IDEs )

<table style="width=100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; "> Action </th>
    <th style="text-align: center; border: 1px solid black; "> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; "> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> To find any action inside the IDE use Find Action </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Shift + A </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ ⇧ A  </td>
  </tr>
</table>
<br/>

- google for "hotkeys pycharm" for **default** Win/Lin keymap: https://resources.jetbrains.com/assets/products/pycharm/PyCharm_ReferenceCard.pdf , 
- google for "hotkeys pycharm" for **default** Mac keymap: https://resources.jetbrains.com/assets/products/pycharm/PyCharm_ReferenceCard_mac.pdf
- latest docs: https://www.jetbrains.com/help/pycharm/2016.3/
- slide...


## Clone a repository with PyCharm

- The repository to clone:  https://github.com/kjam/wswp
- Add a new if statement on line 39 in the file advanced_link_crawler.py
- Revert change
- Create branch && checkout branch
- Add the if statment
- Commit the change

## Start new project
- Create a simple program (main)
- Create class
- Create class.method
- Import package and look at documentation

## Change appearance and PEP8 warnings
- Import old Python file

## Debugging
The code we will use (taken from Jet Brains Help pages)


```python
import math

class Solver:

    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        elif d == 0:
            return -b / ( 2 * a )
        else:
            return "This equation has no roots"

if __name__ == '__main__':
    solver = Solver()

while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    result = solver.demo(a,b,c)
    print(result)

```

- Add breakpoints
- Inspect variables