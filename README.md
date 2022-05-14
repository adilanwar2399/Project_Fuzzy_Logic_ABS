# Project_Fuzzy_Logic_ABS

This is a Fuzzy Logic Automatic Braking System, that has the main aim of this project is to devise a Fuzzy System that enables the Automatic Breaking System (ABS) of cars to operate more efficiently, depending on the speed, distance and the braking force of the car – to maintain an appropriate distance between the cars. 

This System focuses on these:

There are 2 approaches:

1. The Approach that uses the Control API
2. The Alternative approach (not using the control API/ Contol Primer).

Firstly, the User inputs the values via prompts showing in the console for the antecedents – speed and distance values – then these processes occur:

•	The inputted values get fuzzified – all the universe variables will be displayed – with their relationships with their respective membership functions – graphically.
•	Then the antecedent values (Speed and Distance values) are merged together (using the Fuzzy Operator).
•	Then the implications are generated from the speed and distance values through to the consequent (braking force). As the values go through 16 fuzzy rules – here user can graphically see the activity of the output membership.
•	Then the fuzzified sets get merged into one set via aggregation – this is essentially the where the execution of brakes data gets stored as it is controlled – leading to the final stage.
•	Finally, the aggregated value gets defuzzified using the most popular centroid method of defuzzification in order to obtain the optimum braking force needed to be displayed as a percentage value.

Now, after the value has defuzzified – the user will see a graphical representation of the potential overlaps and a single line will also be drawn on the graph’s highlighted region indication the braking force’s percentage value – showing that if very heavy, heavy, very light or light intensity of braking is needed – based on the values the user inputted.

Note of Importance: The Inference System used is the Mamdani Inference System.


