<div style='text-align: justify;'>

# Computational Tools: the art of programming

This is the document of the evidence of the subject Computational Tools
: the art of programming. During this week we learned, explored, and put
into practice knowledge about the use of the fundamental tool for 
code development called Git; likewise, we put into practice our
knowledge of the Python programming language, incorporating the 
PEP-8 code documentation and style guide, which establishes specific 
rules or recommendations for the documentation and code development 
style, to generate code that can be understandable and reused in 
posterity. In the case of how we put our skills in the Python 
programming language to work, it was by downloading a python module 
called FreeGames, which contains a collection of retro or fairly basic 
mini-games, programmed with a library called Turtle, which allows 
generating certain types of 2D graphics in a primary and easy way; the 
activities tried to complete or add specific functionalities to five 
video games, the following: Paint, Snake, Pacman, Cannon, Memory. 
In this way, when making changes and adding functionality to the 
games, it was possible to practice the concepts of Git and code 
documentation, following the PEP-8 standards. Below we will present 
the video games we work on, along with the individual commits and 
changes made, according to the instructions of each activity.

## Collaborators

Luis Angel Gonzales Tapia <br>
Héctor Miranda García

## Games 
As said, we worked in some freegames module mini-games. For this
subject, we worked on five games, the following ones, with what 
was done.


## Cannon

The Cannon video game is a video game that consists of two types of 
important objects, on the one hand, you have the objectives and on 
the other hand you have the projectile. The game is about the 
projectile being fired parabolically towards the targets, which are 
blue dots that move from right to left. Likewise, the user can only 
fire a projectile until the previous projectile is off the screen or 
off the map. The user has to destroy the targets at will. The control 
of this game is the mouse; the projectile is fired from the lower-left 
corner and the farther away the mouse is and clicked, the projectile 
is fired with much more force. The requirements for carrying out 
this activity were to modify the speed of the movement of the 
projectile and of the objectives and make the game infinite or 
never end; To achieve this, the following steps are followed.

For the question of increasing the speed of both objectives, 
the following was applied to the code shown in image XI, where, 
as the comment indicates, the frequency in which the speed was 
divided was changed, which allows increasing the velocity.

![tap function](https://github.com/H3cth0r/artProg/blob/main/resources/cannon_tap_func.png?raw=true)

Likewise, for the speed increase, the speed value of the blue 
targets has been changed, which causes the targets to increase 
their speed, as shown in the following image.

![move function](https://github.com/H3cth0r/artProg/blob/main/resources/cannon_move_funct.png?raw=true)


As far as making the game infinite is concerned, in the part of this 
for where there was only a return that made the game stop, these 
two lines were added to re-accommodate the targets in their 
position on the x-axis and give it a new random point on the y-axis.

![alt text](https://github.com/H3cth0r/artProg/blob/main/resources/cannon_rearange.png?raw=true)


## Memory


## Pacman


## Paint
In the case of the paint video game, basically, the program consists 
of different functionalities and commands activated with the keyboard 
to draw or put figures and lines in the window that appears when the 
program is run, with the possibility of changing the colors of the 
same figures and lines. In the case of this game, we were required to 
complete certain functionalities in code that were not completed, as 
was the case of the functions to draw a circle, draw a rectangle, 
a triangle, and add color to the list of colors, which in our case 
we decided to add the color yellow, which would be activated by 
typing ^Y. In the case of the functions that were completed, the 
following was added for each case:

In the case of the circle function, what was done was first to copy 
certain Turtle functions that were used in previous functions, to 
start and allow the functions to be `drawn' and filled. An important 
aspect of this function is the variable dis_between_points, since this 
variable is the one that will calculate the distance between two 
points, which will allow the distance between the points, which in 
this case are the two clicks made by the user, to be the circle radius 
measure; As you can see, this distance is entered in the cr function, 
which is the abbreviation for the circle function that is part of the 
Turtle library, but its name was changed to avoid confusion between 
the present function and Turtle's. Later the figure will be filled.

![function circle](https://github.com/H3cth0r/artProg/blob/main/resources/paint_circle.png?raw=true)

Consequently, the results obtained with respect to this 
function can be seen as follows when running the program.

*Imagen II. Aplicación de función circle.*
![alt text](http://url/to/img.png)


In the case of the function to display a rectangle, first, the same 
initial procedure that was commented above was carried out, where the 
necessary functions are added to be able to present the figure in the 
application window, which are the up, goto, down functions. , 
begin_fill. Later, the function was used again to measure the 
distance between two points, to know how long the longest side of the 
rectangle should be. Subsequently, a condition is passed, where it is 
evaluated if the distance in the points on the x-axis is longer or if 
the y-axis is longer, in order to know if a rectangle should be made 
with a longer height or at Otherwise, the base is longer. 
Subsequently, within either of the two, any of the if conditions, the 
distance between the points will be used, so that the longest distance 
measures this distance between the points and that the shortest side 
is half the distance between the points. Below is the code for 
that function.

![rectangle function](https://github.com/H3cth0r/artProg/blob/main/resources/paint_rectangle.png?raw=true)

Consequently, when running the program and applying this functionality
, the following can be observed, in case the height or the base of 
the rectangular is longer or not.

*Imagen IV. Aplicación de función rectangle.*
![alt text](http://url/to/img.png)

Finally, in the case of the functionality to be completed called 
triangle, in summary, a for cycle is created that will be repeated 
three times and that, depending on the distance between the values 
of the points on the x axis, will be rotated 120 degrees, 
generating a triangle. equilateral:


![triangle function](https://github.com/H3cth0r/artProg/blob/main/resources/paint_triangle.png?raw=true)

Once the program is run and said functionality is used, the 
following result is obtained to print a triangle:

*Imagen VI. Aplicación de función triangle*
![alt text](http://url/to/img.png)

Finally, the yellow color was added to the color palette that can be 
used to color or add color to the figures that are created on the 
screen. To add this color, the same procedure was followed as for 
the other colors that were already available, as can be seen in the 
following image:

![new color](https://github.com/H3cth0r/artProg/blob/main/resources/paint_yellow.png?raw=true)

## Snake

Clearly the Snake video game is a copy or a version of the classic and 
popular snake video game. As is well known, the video game consists 
of a snake, which is the character that the user controls in the 2D 
plane and whose objective is to eat as much as possible of the food 
that appears randomly on the map; the moment the user consumes the 
food, the snake's tail extends. For the specific case of this 
activity, we must add the functionality so that the food moves 
randomly, but at short and constant distances, throughout the map, 
to make the capture of the food more difficult; likewise, it was 
required to make the color of the snake's head and the food change 
randomly every time the user starts a new game of the game. Below we 
will explain in more detail the procedure we followed to 
accomplish this.

For the first case, in which the food should move on the map, the 
code shown in image VIII was added. The added code is inside the 
if-else. Within the if, where it is entered in case the head has 
captured the food, food will be created within the map randomly; 
later, in case the user has not caught the food yet, the food will 
move 5 units randomly on the x and y-axis; It is important to consider 
that this part is found in the same way inside another if, since as 
can be seen in this if, it is confirmed that the food is inside 
the map, otherwise, the food will be relocated inside the map 
randomly, as if the snake had captured it.

![if code block](https://github.com/H3cth0r/artProg/blob/main/resources/snake_if_code_block.png?raw=true)

For the case of changing the color of the head and food randomly when 
starting a new game, the following code block was added, as can be 
seen in image IX, where a list with different colors was created, and 
later, The ColorFood and ColorSnake variables were created, they 
randomly select some color from the list, as shown in the 
following image.

![random color selection](https://github.com/H3cth0r/artProg/blob/main/resources/snake_color_selection.png?raw=true)

Later, within the move function of the video game, these variables 
are used within the square function that allows the creation of a 
frame, either for the case of the head or the food, as shown in 
the following image:

![color application](https://github.com/H3cth0r/artProg/blob/main/resources/snake_color_selection.png?raw=true)

</div>
