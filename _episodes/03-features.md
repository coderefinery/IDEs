---
layout: episode
title: "PyCharm features"
teaching: 15
exercises: 30
questions:
  - "How to ease Your life?"
objectives:
  - "Some of the main features of PyCharm are introduced."
---

# PyCharm setup

In this part basic functionality of IDE is demonstrated and gone through.

## Intelligent Coding Assistance
- Code completion [0]
- On-the-fly error highlighting [1]
- Fast and Safe Refactorings [2]

## Built-in Developer Tools
- Visual Debugger [3]
- VCS + Local History [4]
- Profiler [5]
- Vagrant [6]
- VirtualEnv [7]

## Customizable and Cross-platform IDE
- Plugins

## Intelligent Coding Assistance

### [Navigation](https://www.jetbrains.com/help/pycharm/2016.1/navigation-in-source-code.html?search=navigation) & [Code completion](https://www.jetbrains.com/help/pycharm/2016.1/code-completion.html?search=code%20comple) [0]

<table style="width:70%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> To find any action inside the IDE use Find Action </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Shift + A </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⇧ A  </td>
  </tr>
    <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Show intention actions and quick-fixes </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Alt + Enter </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌥ Enter </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Basic code completion (the name of any class, method or variable) </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Space </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌃ Space  </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Go to declaration (the name of any class, method or variable) </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + B , Ctrl + Click </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ B , ⌘ Click </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Select successively increasing code blocks </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + W </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌥ ↑ </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Find/Replace </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + F / Ctrl + R </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ F, ⌘ R </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Go to class </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + N </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ O </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Go to line </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + G </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ L </td>
  </tr>
</table>

---

## Intelligent Coding Assistance

### [On-the-fly error highlighting]() [1]

- concept : [**_PEP8 (style guides)_**](https://www.python.org/dev/peps/pep-0008/#introduction) - is a StyleGuide for Python. A tool that validates code against it goes by the same name. (Python wiki)
- concept : [**_Pylint (style guides)_**](https://pylint.readthedocs.io/en/latest/intro.html) - Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code’s complexity. (Pylint wiki)

<table style="width:70%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Reformat code </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Alt + L </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⌥ L </td>
  </tr>
</table>


- code analysis : **Code -> Inspect Code**
- errors highlighting

---

## Intelligent Coding Assistance

### [Fast and Safe Refactorings](https://www.jetbrains.com/help/pycharm/2016.1/refactoring.html?search=refac) [2]

<table style="width:70%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Change Signature </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + F6 </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ F6 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Surround with... </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Alt + T </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⌥ T </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Extract Constant </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Alt + C </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⌥ C </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Extract Method </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Alt + M </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⌥ M </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Safe delete </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Alt + Delete </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ Delete </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Create test </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Shift + T </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⇧ T </td>
  </tr>
</table>

---

## Built-in Developer Tools

### [Visual Debugger](https://www.jetbrains.com/help/pycharm/2016.1/debugger.html?search=debugger) [3]

- concept : [**_breakpoint_**](https://en.wikipedia.org/wiki/Breakpoint) - a breakpoint is an intentional stopping or pausing place in a program, put in place for debugging purposes. (Wikipedia)

- run in debug mode : **Run -> Debug '...'**
- take a look
- remove debugging

<table style="width:70%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Resume program </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> F9 </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> F9 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Step over/into </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> F8 / F7 </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> F8 / F7 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Step out </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Shift + F8 </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⇧ F8 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Evaluate expression </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Alt + F8 </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌥ F8 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> View breakpoints </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Shift + F8 </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⇧ F8 </td>
  </tr>
</table>
<br/>

- set value

---

## Built-in Developer Tools

### [VCS](https://www.jetbrains.com/help/pycharm/2016.1/version-control-with-pycharm.html) + [Local history](https://www.jetbrains.com/help/pycharm/2016.1/local-history.html?search=local%20history) [4]

- VCS integration (not limited to Git)
- Local History

---

## Built-in Developer Tools

### [Profiler](https://www.jetbrains.com/help/pycharm/2016.1/profiler.html) [5]

- run in debug mode : **Run -> Profile '...'**
- take a look at results

---

## Built-in Developer Tools

### [Vagrant](https://www.jetbrains.com/help/pycharm/2016.1/vagrant.html?search=vagrant) [6]

- demo : **Tools -> Vagrant -> ...** (PyCharm Professional only)

### [VirtualEnv](https://www.jetbrains.com/help/pycharm/2016.3/creating-virtual-environment.html) [7]

- creating [virtual environments](https://virtualenv.pypa.io/en/stable/)

---

## Customizable and Cross-platform IDE

### [Plugins](https://www.jetbrains.com/help/pycharm/2016.1/plugins.html?search=plugins)

<table style="width:70%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px;"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Open Settings dialog </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Alt + S </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ , </td>
  </tr>
</table>
<br/>

- Plugins, plugins are everywhere... 

___

1. Python Wiki - http://python.wikia.com/wiki/PEP8
2. Wikipedia - https://en.wikipedia.org/wiki/Breakpoint
3. Pylint - https://pylint.readthedocs.io/en/latest/intro.html