# EA1 - Overview

## 1. Which Package/Library did I select?

I chose the PyQt6 library for Python as my main exploration focus, as well as the pendulum library to support it in making this application.

## 2. What is the Package/Library?

PyQt6 is a library for developing GUI's within Python. It works very similarly to JavaFX for Java, having things like generic buttons, labels, VBoxes, etc. Since it's such a large library, it would have been impossible to use all of the built in functions within this project. I also did not want to import the entirety of PyQt6, and so I imported features I needed as they came up.

To use it, you have to think of it in 3 steps:
1. The Application
    - First you have to actually create the application, this is where everything will be displayed
    - You have to think about things like how big you want your application to be, do you want it full screened all the time, do you want a minimum/maximum size, do you want the elements in your application to grow/shrink as you change the size of your application window?
2. The Windows
    - Windows are essentially like scenes in JavaFX, each window will serve a purpose. In this program, I used 3 windows, one for Home, one for View Transactions, and one for Plan Trip.
3. The Elements
    - You now need to populate your window with various elements, whether it be labels for texts, buttons that do various things, different layout elements, whatever you need for your application.

## 3. What are the functionalities of the Package/Library?

There are way too many to list them all, but I will go over some of the ones I utilized the most:

- QApplication
    - This is arguably the most important function, simply creates the application screen
- QToolBar
    - This was used to create the ToolBar on the top of the application. Alternatively you can go with a MenuBar which would create a single button called "Menu" which can be clicked to view the buttons that are on the ToolBar.
- QPushButton
    - This creates a button. You can give it a string as a parameter which will use that string as text within the button.
- QComboBox
    - Drop down box full of items that must be added into it. Using a simple for loop to iterate through a list of strings is a quick and simple way to fill it up. Can be seen in View Timezones as the list of timezones.
- QVBoxLayout & QHBoxLayout
    - Used to store elements in either a vertical or horizontal manner
- QWidget
    - Elements such as QPushButtons and QComboBox, essentially anything that's interactable is considered a QWidget, and can all be styles with basic CSS.
- QLabel
    - Basic text, takes in a string and outputs that string on screen.

## 4. When was it created?

The original release of PyQt was in 1998, but PyQt6 was released in January of 2021. It was last updated as recently as Decemeber 2023, so it's still being maintained.

## 5. Why did I select this Package/Library?

I had a very hard time using JavaFX, I think the documentation for it was very poor, and outdated, so I wanted to find some kind of library that focused on GUIs. Octave and Racket were not great languages for this, and I had already known about the pendulum library so choosing to look for a GUI library within Python made more sense than within Javascript.

## 6. How did learning the Package/Library influence my learning?

If I'm being honest, I don't think it had much of an impact on my learning. As I found it very similar to JavaFX, I took a lot of core concepts from how I would write a program with that into consideration, and simply used PyQt6 as a base to do it with. If anything, I think it's made me appreciate good documentation more, because there wasn't a single problem that didn't have an answer for me within documentation itself.

## 7. How was my overall experience with the Package/Library?

Overall I enjoyed it. I think it's very easy to pick up and use, even with minor knowledge of Python as a language you can grasp how to use things just by playing around with the different functions. I think the most challenging aspect was honestly formatting. When I first changed the background for one of the windows, I then noticed that it changed the background for buttons too, so then I had to adjust that, and it always felt like if you were changing the formatting of one thing, you had to do it for a few others too.

I would definitely recommend this to anyone looking to make any sort of application with a GUI in Python. I know there's also tkinter as an option for GUIs, however I can't really say which one would be better to use as I've not really looked into it. I would definitely use it again if I needed to make a project like this again.