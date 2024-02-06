Chord Intersection Counter!


This specific algorithm is designed to calculate the number of intersections between chords in a circle, given their radian measure and identifiers.
  The identifiers are used in order to label if the point that is being entered is a starting or end point.




How to run:
With python properly installed on your system, copy and paste the algorithm into VSCODE, a Juypter notebook, or a Python Script.
Replace points with your own data.
Run the script.


** It is important to note that s_1 and e_1 are corresponding to each other. This is a way of labeling one starting point, and ending point without the use of multiple variables. The algorithm takes this into consideration, HOWEVER you do not need to list the identifiers in a specific order.
FOR EXAMPLE:
points = [0.78, 1.47, 1.77, 3.92]
identifiers = ["s_1", "s_2", "e_1", "e_2"]


0.78 corresponds to identifier s_1, while 1.77 corresponds to e_1.


Input your points properly is important in order to ensure that the counter works properly.


BIG O RUNTIME:


The particular approach I took when creating this algorithm uses a sorting step and because of that I estimate the time complexity to be of O(n log n). However the subsequent iteration through the points input has an estimated time complexity of O(n). Overall the script has an estimated total time complexity of O(n log n).


NOTES:
The algorithm ALWAYS assumes valid input, this means constraints are satisfied.
The chord identifiers are not required to be in any specific order.
The algorithm considers intersections that ONLY OCCUR INSIDE THE CIRCLE, therefore anything outside the circle won't be accounted for.
The algorithm assumes that there are no intersections at the same point.
Radian measures are sorted in ascending order!




I am hoping to learn from you all on the best way to create this algorithm, and want to see the different approaches that can be taken!


Feel free to modify the algorithm to fit your needs and have a great day!





