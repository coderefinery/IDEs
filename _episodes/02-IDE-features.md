---
layout: episode
title: "PyCharm features"
teaching: 30
exercises: 
questions:
  - "Does an IDE actually help me?"
objectives:
  - "How can I debug?"
keypoints:
---

# PyCharm Coding && debugging

### A small coding example

Code to type (from the matplotlib gallery):
```python
  """
  ===================
  A simple fill plot
  ===================
  This example showcases the most basic fill plot a user can do with matplotlib
  """

  import numpy as np
  import matplotlib.pyplot as plt

  x = np.linspace(0,1,500)
  y = np.sin(4 * np.pi * x)*np.exp(-5*x)

  fig, ax = plt.subplots()

  ax.fill(x,y,zorder=10)
  ax.grid(True, zorder=5)
  plt.show()

```
Create new file. As we type, we get support from PyCharm - it completes quite a few of our intentions.
 - ```import``` help with what to import (Most frequent first?)
 - Quick documentation for functions
 - External documentation available, and you can add your own through "Preferences" (Search doc)
 - Help you with regular expressions. Test this code in a new file
 
 ``` python
import re

p=re.compile('[A-Za-z0-9._%+-].+@[A-Za-z0-9.-]+\.[A-Za-z]{3,4}')
```
#### Enabling Version Control
Select "VCS" -> "Version Control Integration...". Select Git from the list. Note that the colors
of the file names changed from black to red.
Add files to version control, and colors change to green.
Commit the files. Colors change from green to black. These colors changes applies also to the
project area.

Close project. The state of the project is preserved.


### Debugging
Select ```calcpi.py```. Scroll down to line 84. On the left side of the source, push the mouse
such that you get a red bullet point. This a break point at line 84.

Select "Run"->"Debug". Make sure it is calcpi.py which is executed by the debugger. The program
is now executed until the break point.

On the left you see the current call stack with each stack frame. In middle you see the state of
the variables, and on left there is the state of the watch points. Currently there is no watch
points set

#### Stepping
By pressing "Step into my code", we can step through the code and watch the state of the
variables. When a function is being called, the call stack increases with a new stack frame.
The set of variables we watch is the variables which lives in the new function scope.


#### TODOs
At bottom we have a TODO list. Select #FIXME.
Go to circsq() and add a comment ```#TODO: Replace circsq() with Radovan's Fortran implementation.```

Add your own Todo comment in the Preferences.
Select "Preferences"->Search for ToDo-> Add ```\bdeprecated\b```

