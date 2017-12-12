---
layout: episode
title: "Getting to know PyCharm"
teaching: 30
exercises: 0
questions:
  - "What is an IDE?"
  - "Why to use an IDE?"
objectives:
  - "Basic concept of IDE is introduced"
  - "Main IDE usage benefits explained"
keypoints:
  - "IDEs are helpful, really..."
---

# Introduction to PyCharm

In this lesson main concepts of IDE are explained. One will learn about the benefits and motivation to start using it.

We start by downloading a project.
 - Start PyCharm
 - In the dialog "Welcome to PyCharm", choose "Checkout from Version Control"
 - Select Github
 - Use the following for "Git Repository URL":
 ```shell
 https://source.coderefinery.org/bjornlin/calculate_pi.git
```
- Give the project directory a appropriate name

### PyCharm environment
The screen is divided in a project area and a gray canvas. The project shows our files and
Python Interpreter PyCharm has selected for us.

Note, if you want to remove a view select the "Black&&White"-vertical bar, for a vertical view,
and the same but horizontal symbol for a horizontal view.

### The Project Interpreter
We will change the Project Interpreter.
Select "PyCharm->Preferences->Project:<project-name>->ProjectInterpreter"
Here we can select our preferred  Python Environment.

We create a new Python virtual environment, and this is established in our project area under
the venv sub-directory:

```shell
dhcp-86-124:calculate_pi171212 bjorn$ ls
calcpi.py                       requirements.txt                venv
calculate_pi_functions.py       test_pi_functions.py
dhcp-86-124:calculate_pi171212 bjorn$
```

### Requirements.txt

### Installing and upgrade numpy

### Running Pytest

### Code Inspection
Select "Code"->"Code Inspection". As we see, there is a lot of PEP8 code warnings. On right side
of the source code, the PEP-8 warnings are shown.

We will change the preferences such that PEP8 warnings get more pronounced.
Select "PyCharm"->"Preferences". Search for PEP8. Select "PEP8 coding style violation" and change
it from "Weak Warning" to "Warning" (Yellow color). Do the same for "PEP8 naming convention".

Select a warning-> select the light bulb -> Rename element -> Rename all occurrences
Select expression with parenthesis -> Remove redundant parenthesis


### PyCharm integrates many Version Control Systems
This exampled is enabled with Git and we can browse the commit log.

Define a new remote and push the code.

##  Why to use and IDE?

The keyword is: **INTEGRATED**
 
###  Bjarne Stroustrup writing about Development and Design (The Programming Language C++, edition 3)
  - Design and programming are iterative activities
  - The systems we construct tend to be at the limit of the complexity that  we and our tools can handle
  - There are no "cookbook" methods that can replace intelligence,experience, and good taste in design and programming  
  - Successful software development is a long-term activity
  - The most important single aspect of software development is to be clear about what you are trying to build
  - **The different phases of a software project, such as design, programming, and testing, cannot be strictly separated**
  - Programming and design cannot be considered without also considering the management of these activities.

"It is easy - typically expensive - to underestimate any of these points. It is hard to transform the abstract ideas they embody into practice. The need for experience should be noted. Like boat building, bicycling, and programming, design is not a skill that can be mastered through theoretical study alone."


Remember, you never see the scaffolding!!

### You should use an IDE because...
it alleviates the process of instantiating your abstract ideas:
- decreases pain
- boosts effectiveness
- best-practice

- ±multi functional
- ±need to learn new tool
 
