---
layout: episode
title: "PyCharm setup"
teaching: 15
exercises: 20
questions:
  - "How to install PyCharm?"
objectives:
  - "The project is imported into PyCharm"
  - "PyCharm installation is verified"
  - "Student is aware of the supporting materials locations"
keypoints:
  - "It is easy and fun to start with the IDE"
---

# PyCharm setup

During this lesson the typical IDE installation process is completed. Session aims to expose ease of beginning with IDE, point to sources of information as well as guide towards having a verified valid installation on a local machine (OS agnostic). 

## PyCharm

motivation for choosing PyCharm is quite simple: 
- Python language is more or less familiar to the majority of the workshop's audience
- PyCharm belongs to JetBrains' IDE product family, which is considered to be one of the best ranges of developer tools exists
- there are similar IDEs for different technologies:

<br/>
<table style="width:100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:50%"> technology </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:50%"> IDE </th> 
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Python </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> PyCharm / Edu </td> 
  </tr>  
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> C / C++ </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> CLion </td> 
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> C++ </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ReSharper C++ as Visual Studio Extension </td> 
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> SQL (Databases) </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> DataGrip </td> 
  </tr>
</table>

PyCharm comes in 3 (three) flavours:
- community edition (the one we are going to mainly use during the session)
- educational edition (open source, good for learning purposes)
- commercial edition (a tool for serious adventures)

as a notice: there is a way to get commercial edition licenses for [open source projects](https://www.jetbrains.com/buy/opensource/#application-rules) and [students](https://www.jetbrains.com/student/) for free

## Installation and support

- [download](https://www.jetbrains.com/pycharm/download) the bundle if not done yet
- start installation and follow the software installer guide

while the installer is running, let's take a look at support materials:
- [video tutorials](https://www.youtube.com/playlist?list=PLQ176FUIyIUZ1mwB-uImQE-gmkwzjNLjP)
- [latest docs](https://www.jetbrains.com/help/pycharm/2017.1/meet-pycharm.html)
- [Mac default keymap](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard_mac.pdf) / [generic default keymap (Win/Linux)](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)

try using the following key combination to find the function desired:

<table style="width:100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:50%"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Find Action </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Shift + A </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⇧ A  </td>
  </tr>
</table>

## Setup & intro

```shell
$ git clone https://github.com/coderefinery/IDEs.git
```
now press key combination:

<table style="width:100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:50%"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Find Action </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Shift + A </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ ⇧ A  </td>
  </tr>
</table>

and start typing **Open**, find and import pulled project. Once the project is loaded let's look around, there are several working areas of the window or panes (list of them can also be found by **View -> Tool Windows -> ...**):

- project 
- code
- control menus and buttons
- tool windows like terminal and VCS, run/debug panes _etc._, try switching between the tabs with 

<table style="width:100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:50%"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Open Corresponding Tool Window </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Alt + #[0-9] </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ 0 ... ⌘ 9 </td>
  </tr>
</table>

tools can be also called by **Find Action** key combination, just start typing in the pane/tool name. another useful part of the UI is the buttons ribbon, let's extend the default a little:

- select **View -> ...** and check all the options in the section starting with **Toolbar**, or alternatively use the **Find Action** approach

before we complete this part, let's tune the look and feel too, do: 

<br/>
<table style="width:100%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:50%"> Action </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Win/Lin keys </th> 
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:25%"> Mac keys </th>
  </tr>
  <tr>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Open Settings Dialog </td>
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> Ctrl + Alt + S </td> 
    <td style="text-align: center; border: 1px solid black; padding: 3px;"> ⌘ , </td>
  </tr>
</table>

and type word **Size** into the search field, among the results, find and adjust **Console font size** and check **Change font size (Zoom) with Ctrl+Mouse Wheel**

now lets finalize the setup by running a test script [verification script](https://github.com/coderefinery/IDEs/blob/gh-pages/verify.py)
- **Run -> ...** or **Find Action** + **Run** or right click on the file tab and select **Run**
(if asked by **Run/Debug** configuration dialog, then select the script location and other option as like python version and more... (anaconda package is advisable))

> ## Environment
> If You want to preserve Your existing environment by creating a separate VirtualEnv, please take a look [here]({{site.baseurl}}/03-features/#virtualenv-7) for guindance. And "Yes", it is also embedded into PyCharm.
>
> {: .solution }
{: .challenge :}