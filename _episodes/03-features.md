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
    <tr>
    <td style="text-align: center; border: 1px solid black; "> Show intention actions and quick-fixes </td>
    <td style="text-align: center; border: 1px solid black; "> Alt + Enter </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌥ Enter </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Basic code completion (the name of any class, method or variable) </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Space </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌃ Space  </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Go to declaration (the name of any class, method or variable) </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + B , Ctrl + Click </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ B , ⌘ Click </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Select successively increasing code blocks </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + W </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌥ ↑ </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Find/Replace </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + F / Ctrl + R </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ F, ⌘ R </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Go to class </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + N </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ O </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Go to line </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + G </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ L </td>
  </tr>
</table>

---

## Intelligent Coding Assistance

### [On-the-fly error highlighting]() [1]

- concept : [**_PEP8 (style guides)_**](https://www.python.org/dev/peps/pep-0008/#introduction) - is a StyleGuide for Python. A tool that validates code against it goes by the same name. (Python wiki)
- concept : [**_Pylint (style guides)_**](https://pylint.readthedocs.io/en/latest/intro.html) - Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code’s complexity. (Pylint wiki)

<table style="width=100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; "> Action </th>
    <th style="text-align: center; border: 1px solid black; "> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; "> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Reformat code </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Alt + L </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ ⌥ L </td>
  </tr>
</table>


- code analysis : **Code -> Inspect Code**
- errors highlighting

---

## Intelligent Coding Assistance

### [Fast and Safe Refactorings](https://www.jetbrains.com/help/pycharm/2016.1/refactoring.html?search=refac) [2]

<table style="width=100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; "> Action </th>
    <th style="text-align: center; border: 1px solid black; "> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; "> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Change Signature </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + F6 </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ F6 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Surround with... </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Alt + T </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ ⌥ T </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Extract Constant </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Alt + C </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ ⌥ C </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Extract Method </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Alt + M </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ ⌥ M </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Safe delete </td>
    <td style="text-align: center; border: 1px solid black; "> Alt + Delete </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ Delete </td>
  </tr>
</table>

---

## Built-in Developer Tools

### [Visual Debugger](https://www.jetbrains.com/help/pycharm/2016.1/debugger.html?search=debugger) [3]

- concept : [**_breakpoint_**](https://en.wikipedia.org/wiki/Breakpoint) - a breakpoint is an intentional stopping or pausing place in a program, put in place for debugging purposes. (Wikipedia)

- run in debug mode : **Run -> Debug '...'**
- take a look
- remove debugging

<table style="width=100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; "> Action </th>
    <th style="text-align: center; border: 1px solid black; "> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; "> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Resume program </td>
    <td style="text-align: center; border: 1px solid black; "> F9 </td> 
    <td style="text-align: center; border: 1px solid black; "> F9 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Step over/into </td>
    <td style="text-align: center; border: 1px solid black; "> F8 / F7 </td> 
    <td style="text-align: center; border: 1px solid black; "> F8 / F7 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Step out </td>
    <td style="text-align: center; border: 1px solid black; "> Shift + F8 </td> 
    <td style="text-align: center; border: 1px solid black; "> ⇧ F8 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Evaluate expression </td>
    <td style="text-align: center; border: 1px solid black; "> Alt + F8 </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌥ F8 </td>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> View breakpoints </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Shift + F8 </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ ⇧ F8 </td>
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

### [VirtualEnv](https://virtualenv.pypa.io/en/stable/) [7]

- creating virtual environments

---

## Customizable and Cross-platform IDE

### [Plugins](https://www.jetbrains.com/help/pycharm/2016.1/plugins.html?search=plugins)

<table style="width=100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; "> Action </th>
    <th style="text-align: center; border: 1px solid black; "> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; "> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; "> Open Settings dialog </td>
    <td style="text-align: center; border: 1px solid black; "> Ctrl + Alt + S </td> 
    <td style="text-align: center; border: 1px solid black; "> ⌘ , </td>
  </tr>
</table>
<br/>

- Plugins, plugins are everywhere... 

___

1. Python Wiki - http://python.wikia.com/wiki/PEP8
2. Wikipedia - https://en.wikipedia.org/wiki/Breakpoint
3. Pylint - https://pylint.readthedocs.io/en/latest/intro.html