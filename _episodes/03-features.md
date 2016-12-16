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
- Code completion [1]
- On-the-fly error highlighting [2]
- Fast and Safe Refactorings [3]

## Built-in Developer Tools
- Visual Debugger [4]
- VCS + Local History [5]
- Profiler [6]
- Vagrant [7]

## Customizable and Cross-platform IDE
- Plugins [8]

## Intelligent Coding Assistance

### [Navigation](https://www.jetbrains.com/help/pycharm/2016.1/navigation-in-source-code.html?search=navigation) & [Code completion](https://www.jetbrains.com/help/pycharm/2016.1/code-completion.html?search=code%20comple) [1]

<table>
  <tr>
    <th> Action </th>
    <th> Win/Lin keys </th> 
    <th> Mac keys </th>
  </tr>
  <tr>
    <td> To find any action inside the IDE use Find Action </td>
    <td> Ctrl + Shift + A </td> 
    <td> ⌘ ⇧ A  </td>
  </tr>
    <tr>
    <td> Show intention actions and quick-fixes </td>
    <td> Alt + Enter </td> 
    <td> ⌥ Enter </td>
  </tr>
  <tr>
    <td> Basic code completion (the name of any class, method or variable) </td>
    <td> Ctrl + Space </td> 
    <td> ⌃ Space  </td>
  </tr>
  <tr>
    <td> Go to declaration (the name of any class, method or variable) </td>
    <td> Ctrl + B , Ctrl + Click </td> 
    <td> ⌘ B , ⌘ Click </td>
  </tr>
  <tr>
    <td> Find/Replace </td>
    <td> Ctrl + F / Ctrl +  </td> 
    <td> ⌘ F, ⌘ R </td>
  </tr>
  <tr>
    <td> Go to class </td>
    <td> Ctrl + N </td> 
    <td> ⌘ O </td>
  </tr>
  <tr>
    <td> Go to line </td>
    <td> Ctrl + G </td> 
    <td> ⌘ L </td>
  </tr>
</table>

---

## Intelligent Coding Assistance

### [On-the-fly error highlighting]() [2]

- concept : [**_PEP8 (style guides)_**](https://www.python.org/dev/peps/pep-0008/#introduction) - is a StyleGuide for Python. A tool that validates code against it goes by the same name. (Python wiki)
- concept : [**_Pylint (style guides)_**](https://pylint.readthedocs.io/en/latest/intro.html) - iPylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code’s complexity. (Pylint wiki)

<table>
  <tr>
    <th> Action </th>
    <th> Win/Lin keys </th> 
    <th> Mac keys </th>
  </tr>
  <tr>
    <td> Reformat code </td>
    <td> Ctrl + Alt + L </td> 
    <td> ⌘ ⌥ L </td>
  </tr>
</table>


- code analysis : **Code -> Inspect Code**
- errors highlighting

---

## Intelligent Coding Assistance

### [Fast and Safe Refactorings](https://www.jetbrains.com/help/pycharm/2016.1/refactoring.html?search=refac) [3]

<table>
  <tr>
    <th> Action </th>
    <th> Win/Lin keys </th> 
    <th> Mac keys </th>
  </tr>
  <tr>
    <td> Change Signature </td>
    <td> Ctrl + F6 </td> 
    <td> ⌘ F6 </td>
  </tr>
  <tr>
    <td> Surround with... </td>
    <td> Ctrl + Alt + T </td> 
    <td> ⌘ ⌥ T </td>
  </tr>
  <tr>
    <td> Extract Constant </td>
    <td> Ctrl + Alt + C </td> 
    <td> ⌘ ⌥ C </td>
  </tr>
  <tr>
    <td> Extract Method </td>
    <td> Ctrl + Alt + M </td> 
    <td> ⌘ ⌥ M </td>
  </tr>
  <tr>
    <td> Safe delete </td>
    <td> Alt + Enter </td> 
    <td> ⌘ Delete </td>
  </tr>
</table>

---

## Built-in Developer Tools

### [Visual Debugger](https://www.jetbrains.com/help/pycharm/2016.1/debugger.html?search=debugger) [4]

- concept : [**_breakpoint_**](https://en.wikipedia.org/wiki/Breakpoint) - a breakpoint is an intentional stopping or pausing place in a program, put in place for debugging purposes. (Wikipedia)

- run in debug mode : **Run -> Debug '...'**
- take a look
- remove debugging

<table>
  <tr>
    <th> Action </th>
    <th> Win/Lin keys </th> 
    <th> Mac keys </th>
  </tr>
  <tr>
    <td> Resume program </td>
    <td> F9 </td> 
    <td> F9 </td>
  </tr>
  <tr>
    <td> Step over/into </td>
    <td> F8 / F7 </td> 
    <td> F8 / F7 </td>
  </tr>
  <tr>
    <td> Step out </td>
    <td> Shift + F8 </td> 
    <td> ⇧ F8 </td>
  </tr>
  <tr>
    <td> Evaluate expression </td>
    <td> Alt + F8 </td> 
    <td> ⌥ F8 </td>
  </tr>
  <tr>
    <td> View breakpoints </td>
    <td> Ctrl + Shift + F8 </td> 
    <td> ⌘ ⇧ F8 </td>
  </tr>
</table>


- set value

---

## Built-in Developer Tools

### [VCS](https://www.jetbrains.com/help/pycharm/2016.1/version-control-with-pycharm.html) + [Local history](https://www.jetbrains.com/help/pycharm/2016.1/local-history.html?search=local%20history) [5]

- VCS integration (not limited to Git)
- Local History

---

## Built-in Developer Tools

### [Profiler](https://www.jetbrains.com/help/pycharm/2016.1/profiler.html) [6]

- run in debug mode : **Run -> Profile '...'**
- take a look at results

---

## Built-in Developer Tools

### [Vagrant](https://www.jetbrains.com/help/pycharm/2016.1/vagrant.html?search=vagrant) [7]

- demo : **Tools -> Vagrant -> ...** (PyCharm Professional only)

---

## Customizable and Cross-platform IDE

### [Plugins](https://www.jetbrains.com/help/pycharm/2016.1/plugins.html?search=plugins) [8]

<table>
  <tr>
    <th> Action </th>
    <th> Win/Lin keys </th> 
    <th> Mac keys </th>
  </tr>
  <tr>
    <td> Open Settings dialog </td>
    <td> Ctrl + Alt + S </td> 
    <td> ⌘ , </td>
  </tr>
</table>


- Plugins, plugins are everywhere... 

___

1. Python Wiki - http://python.wikia.com/wiki/PEP8
2. Wikipedia - https://en.wikipedia.org/wiki/Breakpoint
3. Pylint - https://pylint.readthedocs.io/en/latest/intro.html