# Blackjack Game by Arafat Rahaman & Aiah Aly
Hey guys, my partner and I decided for our final project for our CIS 1051, Introductory to Python class, we would attempt to create Blackjack, and this how it went...

# Original Goal:
Our original goal was to go all out. We were hungry, young, and ambitious CS students that wanted most to blow the roof of our wonderful professor’s and TA's heads. We decided what  better game than the infamous Blackjack to do that. We wanted to create a full out GUI that allowed for the game to be fully played just on the GUI. In essence, you could play the game by simply entering the bet amount in an input box, and the game would be simulated, and the cards would fly out of the deck one-by-one. We envisioned buttons that you could press to "hit", "stand", or "play again!". In the best cases of scenarios, we even wanted music and cool animations. Alas, as ambitious as we were, we may have been just a little too ambitious.

# Challenges:
We thought that because it was just a game, like any game we built in our introductory class, we could quickly code it, and move on to working on the GUI. Boy, were we wrong! There is a lot of logic behind Blackjack that made the overall programing difficult for us. For example, the logic behind the Ace being equal to 11 or 1. The logic system of busting, winning, or tying as the player or dealer. We had to find ways to organize our code better so that it would become easier to call certain variables, functions, and classes a lot easier. Not to mention we actually had to learn about what classes were. We decided to use resources online such as video explanations on how to implement the logic in a coding environment, and how to simply run the game in a terminal. Eventually, we figured out how to create the game just in the terminal, next we were tasked with the monumental task of creating a GUI. We thought creating a GUI would be super intuitive... We were met with surprise again. We head to learn about a python module called TKinter, which was expected since we knew we needed some toolkit to actually build the GUI. What we didn't expect was the overwhelming challenge of using images with TKinter. We had to install Pillow with pip in our command prompt to actually utilize PNG files. After that, we were met with the change of obscure instructions on how to call images, resize images, and place an image and keep it on the canvas of the GUI. We spent many nights fighting through trial and error before we finally got what we wanted. We found that once we found the answer to one obstacle we had to go onto the next and repeat the trial-and-error process many times before we finally got it.

# List Problems Faced and Solved:
1.	Creating a deck without writing each and every card out
2.	Learning to use classes, and certain elements of classes such as self, and init.
3.	Installing Pillow with pip in the command prompt to enable the use of images.
4.	Looping the entire game so it wouldn’t keep re-looping when it ended.
5.	Logic behind winning, loosing, tying, automating the dealer.
6.	Keeping track of different variables.
7.	Learning how to use dictionaries to enable the ability to create new variable names inside loops
8.	Wanting to drop out of college but understanding we cannot ☹.
9.	 Using TKinter and using the different parts of its toolkit.

# New Things Learned and Incorporated with Links to Credit those Resources
1.	Classes and Having Functions within Them
a.	https://www.youtube.com/watch?v=wfcWRAxRVBA
2.	TKinter
a.	https://www.youtube.com/watch?v=jE-SpRI3K5g
b.	https://pillow.readthedocs.io/en/stable/installation.html
c.	https://realpython.com/python-gui-tkinter/
d.	https://stackoverflow.com/questions/36767496/creating-multiple-variables-during-each-iteration-of-for-loop-and-executing-tk-c
e.	https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python
3.	Guide to Blackjack Logic in a Program
a.	https://www.youtube.com/watch?v=8QTsK1aVMI0&t=1133s
4.	Global Keyword
a.	https://www.geeksforgeeks.org/global-keyword-in-python/
5.	“Break” Loop
a.	https://www.tutorialspoint.com/python/python_loop_control.htm
6.	Creating 52 Card Deck
a.	https://stackoverflow.com/questions/41970795/what-is-the-best-way-to-create-a-deck-of-cards/41970851
7.	Pillow install with pip in Command Prompt
a.	https://pillow.readthedocs.io/en/stable/installation.html
8.	ValueError in Loop
a.	https://www.journaldev.com/33500/python-valueerror-exception-handling-examples#:~:text=Python%20ValueError%20is%20raised%20when,precise%20exception%20such%20as%20IndexError.
9.	Using Dictionaries to Create New Variable Names within Loops
a.	https://stackoverflow.com/questions/36767496/creating-multiple-variables-during-each-iteration-of-for-loop-and-executing-tk-c
10.	Finding a filed with images of Same-Sized 52 Cards
a.	https://boardgames.stackexchange.com/questions/51426/where-can-i-download-high-quality-images-of-poker-cards

# Final Thoughts:
The coding world is massive, and it is quite naive to think that an introductory python class could prepare us to blast through a final project as we had originally thought. We learned a lot from this project. For one, there are so many resources out there that enable programmers to be better than they can be just by themselves. We found so many how-to guides for individual parts of the project, and without the internet it would be literally impossible to randomly figure out how to resize an image or use dictionaries to create new variable names within a loop. We found that we love Stack Overflow, and all those that contribute. We learned that coding is not a over night process. Sometimes you have to walk away, and come back, because you will, and we mean WILL hit a wall. It’s okay to walk away, as long as you are able to come back with a cool head and be ready to tackle the problem again. Most importantly we learned that the coding world is MASSIVE! We could probably have found a better GUI toolkit if we pursued another coding language. We as first-year coding students have barely scratched the surface of the world that is programing. In essence, whenever we are tasked with a project, weather that be a final for an introductory class or for a job when we become real programmers, we will always be students because it might actually be impossible to know and do everything yourself. And the best part is, the programing world is perfect for that. 
