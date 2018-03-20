---
layout: episode
title: "Getting to know PyCharm"
teaching: 20
exercises: 10
questions:
  - "What is an IDE?"
  - "Why to use an IDE?"
objectives:
  - "Basic concept of IDE is introduced"
  - "Main IDE usage benefits explained"
  - "Managing Virtual Environments with PyCharm"
keypoints:
  - "IDEs are helpful, really..."
---
# What is an Integrated Development Environment (IDE)
![](../img/PYC_IDE.png)

An Integrated Development Environment (IDE) brings you "everything" you need to be a productive programmer to your finger tips. Does this make sense in when working with research software? Take a look
at Bjarne Stroustrup's general statements about Software Development and Design. 

###  Bjarne Stroustrup writing about Development and Design (The Programming Language C++, edition 3)
  - Design and programming are iterative activities
  - The systems we construct tend to be at the limit of the complexity that  we and our tools can handle
  - There are no "cookbook" methods that can replace intelligence,experience, and good taste in design and programming  
  - Successful software development is a long-term activity
  - The most important single aspect of software development is to be clear about what you are trying to build
  - **The different phases of a software project, such as design, programming, and testing, cannot be strictly separated**
  - Programming and design cannot be considered without also considering the management of these activities.

The value proposition of an IDE is to make this process more efficient.
![](../img/PyC_process.png)

The plausibility of this value proposition very much depend upon your line of work;
 - How much software development you do?
 - How large code base you depend upon?
 - Do you share code with others and so on.

The pro is that an IDE really integrates features you need. The cons is that you need to learn the in-and-outs of the IDE,
especially the keyboard shortcuts, to reap the benefits.    

## Introduction to PyCharm

We will go through the main parts of PyCharm. We have selected PyCharm as the tool to demonstrate,
and at the same time motivating the use of Integrated Development Environments. We want to show you why
IDEs are useful.

We start by creating a project.
 - Start PyCharm
 - In the dialog "Welcome to PyCharm", choose "Create New Project"
 - Give the project directory an appropriate name, like "Introduction_to_IDE"
 - Note: You can configure line separators between functions, line numbers, white spaces via (configure -> editor -> general -> appearance)
![PyCharm Project Dialog](../img/PyC_proj_dialog.png)



### PyCharm environment
The screen is divided in a project area and a gray canvas.
![PyCharm Project Area](../img/ide_introduction.png)

This is currently an empty project. It contains the default setup for a project with a Python Interpreter.
If you double click on "External Libraries", you will see your Python Environment.

![PyCharm Interpreter Expanded](../img/ide_introduction_libraries.png)

Note, if you want to remove a view select the "Black&&White"-vertical bar. For a horizontal view,
there will be a corresonding horizontal bar.

### Executing a Python File

Create a python file by selecting a "File"->"New"->"Python File". Call the file `hello`, and add the following
Python code to the file:

```python
from __future__ import print_function

print('Hello World!')
```

The file can be excuted by selecting "Run"->"Run". The output from the execution will disappear
by select the "Red X".

![](../img/ide_program_hello.png)

It is also possible to execute the code in a terminal which is part of PyCharm.

![](../img/ide_execute_program_from_terminal.png)
### PyCharm Settings/Preferences dialog {#Configure}

- **Windows and Linux** - *File -> Settings* 
- **macOS** - *PyCharm -> Preferences*

### Creating tasks and tracking unfinished work
- How do you track tasks that require feedback/attention from other researchers?
- We can add `#TODO` or `#FIXME` before code to track unfinshed work
- The TODO tool window lists all the tasks marked as TODO or FIXME (case insensitive)
- For example, add TODO: add documentation 
- You can add a custom pattern via [Settings/Preferences](#Configure) -> editor -> TODO


### The Project Interpreter
Under [Settings/Preferences](#Configure)->Project:IDEprep->Project Interpreter-> "Add local" (the mechanical wheel) it is possible
to configure your interpreter environment. Once you select "Add local", you get a dialog where you can
select type of interpreter and type of package manager you want to use (if you have both a regular Python 
and Python from Anaconda.org installed)
![](../img/PyC_local_py_interpreter.png)
#### Create environment
![](../img/ide_add_interpreter.png)

We will change the Project Interpreter.
Select "[Settings/Preferences](#Configure)->Project:<project-name>->ProjectInterpreter"
Here we can select our preferred Python Environment.

We create a new Python virtual environment, and this is established in our project area under
the venv sub-directory:

### Manage dependencies
Python Code often comes with a list of required modules which is installed with pip. Here we show you
how you can install necessary modules. In python, requirements.txt is commonly used for managing dependencies. 

#### Create requirements.txt file in the root directory of the project {#dependecies}

To configure this as default requirements file, go to [Settings/Preferences](#Configure) -> Tools in PyCharm
![](../img/ide_add_requirements.png)

Add requirements.txt as the default requirements file.

Now add some requirements to `requirements.txt`
```txt
jupyter
numpy
scipy
```
Open a Python file, you will see notifications on top about requirements that has to be installed.
The event log will state that the packages are installed succesfully.
![](../img/ide_update_requirements_file.png)


### Enabling Version Control
When you start a new project Version Control, you must enable your preferred Version Control system.
You do this by selecting "VCS"->"Enable Version Control Integration". Here you can select Git.
![](../img/PyC-vc_enable.png)

Notice how the colors of the file name in project view changes from black to red:
 - Files with red filenames are not tracked by git
 - Files with green filenames are added to git but not committed
 - Files with black filenames are commited and are unmodified.
 - Files with blue filenames are tracked by git and are modified.

The version control dialog let you add and commit the files, similar to git on the command line. To commit
`hello.py` select "VCS -> Git -> Add" and then "VCS->Commit":
![](../img/PyC_commit.png)

There is a short-cut to the version control log at the bottom edge of the PyCharm Window. The log is also
accessible from "VCS"->"Git"->"Show History"

- Make changes and see the differences between working directory and last commit. 
- You can see the git branch history and log from the Version Control tool window. 

#### Checking out a project from GitHub or another public Git Repository
From the "VCS" menu it also possible to check-out source code from Github or other repositories. Here is an
example, choose "VCS"->"Checkout from Version Control"->"Github". You will get a dialog look like:

![](../img/ide_checkout_github.png)

The address to the repository is

```
https://github.com/Vathasav/ide-examples.git
```

Choose a project name for the cloned source. PyCharm opens the cloned repository as a separate project.

Open `RomanNumberConverter.py`. This file defines a class and some test cases. Based on the naming it seems
that this is class which can convert Roman Numbers to integers. The different tests supports also this.

The tests are written with pytest. To run this tests you will need pytest installed. 

If you don't have pytest, add pytest to the requirements file as [mentioned earlier](#dependecies)

PyCharm will recognize the tests as written according to pytest. If you select "Run"->"Run", you will have
"py.test in RomanNumberConverter.py" as one execution option.

![](../img/ide_test_run_configuration.png)

After executing the pytest, you should get a result something like this, all test passed.
![](../img/ide_test_pass.png)

How will it look if test fails? Add the following code at the bottom of the source code.

```python
def test_parsing_one():
    value = RomanNumeralConverter("I")
    assert value.convert_to_decimal() == 2
```
You get a red result. Select "test_parsing_one" and the view shows you what went wrong with this one test.
![](../img/ide_test_fail.png)

Let us correct it and try to add a commit: 
  - PyCharm shows the differences between the last commit and local file
  - Checks if any TODO tasks that are left -> Helps us to track unfinished work

### Code Inspection
We will do Code Inspection to see how well this code adheres to the [PEP8 Style Guide for Python code](https://www.python.org/dev/peps/pep-0008/).
By default PyCharm have set violations of the PEP8 Style Guide to 'weak warning'. We will modify
the setting such that violations of the PEP 8 Style Guide is more pronounced.

Open [Settings/Preferences](#Configure) and search for `pep8`. Change the severity regarding violation of PEP8
coding style and naming convention from `weak warning` to `warning`.
![](../img/ide_pep8_warnings.png)

Having done that, do the code inspection by selecting "Code"->"Code Inspection". PyCharm produce 
a view with the individual violations. The source code is also colored in areas where the 
violations happen.
![](../img/ide_pep8_inspection.png)

You can select the each warning and reformat the file, removing the PEP8-violations. 

### You should use an IDE because...
it alleviates the process of instantiating your abstract ideas:
- decreases pain
- boosts effectiveness
- best-practice

- ±multi functional
- ±need to learn new tool
 
