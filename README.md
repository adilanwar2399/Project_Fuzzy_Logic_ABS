# Project_Fuzzy_Logic_ABS

This is a Fuzzy Logic Automatic Braking System:

The main aim of this project is to devise a Fuzzy System that enables the Automatic Breaking System (ABS) of cars to operate more efficiently, depending on the speed, distance and the braking force of the car – to maintain an appropriate distance between the cars. 

Measurement units plus constraints and assumptions:

• Speed -> km/h (kilometres per hour) - (Maximum Input (Antecedent) Speed: 100km).

• Velocity -> m/s (metres per second) - (Normally considered but not utilised in this implementation as the other two antecedents were used).

• Distance -> m (metres) (Maximum Input (Antecedent) distance: 60m).

• Brake Force -> the force is measured in N (Newtons) - but the value (intensity) is represented as a % (Percentage) - (0-100% (It can't go lower than 0% and it can't go higher than 100%)).

This System focuses on these:

There are 2 approaches:

1. The Approach that uses the Control API.
2. The Alternative approach (not using the control API/ Contol Primer).

Functionality of the implementation(s):

Firstly, the User inputs the values via prompts showing in the console for the antecedents – speed and distance values – then these processes occur:

•	The inputted values get fuzzified – all the universe variables will be displayed – with their relationships with their respective membership functions – graphically.

•	Then the antecedent values (Speed and Distance values) are merged together (using the Fuzzy Operator).

•	Then the implications are generated from the speed and distance values through to the consequent (braking force). As the values go through 16 fuzzy rules – here user can graphically see the activity of the output membership.

•	Then the fuzzified sets get merged into one set via aggregation – this is essentially the where the execution of brakes data gets stored as it is controlled – leading to the final stage.

•	Finally, the aggregated value gets defuzzified using the most popular centroid method of defuzzification in order to obtain the optimum braking force needed to be displayed as a percentage value.

Now, after the value has defuzzified – the user will see a graphical representation of the potential overlaps and a single line will also be drawn on the graph’s highlighted region that is indicating the braking force’s percentage value – showing that if very heavy, heavy, very light or light intensity of braking is needed – based on the values the user inputted.

Note of Importance: The Inference System used is the Mamdani Inference System.

Another important point to remember is that the Python Code files can be copy and pasted into separate Jupyter Notebook documents and ran like that - also ensure before simulating that the Kernel is reset and fresh to ensure that it starts and simulates each implementation correctly and accurately. 

The Jupyter Notebooks of the respective 2 implementations are displayed for you to see worked example(s) of how this Automatic Braking System works.

Link to my Github: https://github.com/adilanwar2399/Project_Fuzzy_Logic_ABS.git

------------------------------------------------------------------------------------------------------

Pre-requisites for the execution of the implementation(s):

For the execution of these implementations a couple of pre-requisites need to be on the machine:

1. Python (Preferably the Latest Version) needs to be installed on the Machine, this can be done via going to this website and following the steps correctly choosing the correct version for the correct operating system (OS) of the machine:  

• -> https://www.python.org/downloads/            

Additionally, if the machine already has python installed - you can check by typing a specific command in the terminal to see what version of python is installed: 

• -> python --version

• -> python -V 

• -> python -VV

2. SkFuzzy - Scikit Fuzzy Toolkit needs to be installed on to the machine using the terminal - follow the steps on this website:

• -> https://pythonhosted.org/scikit-fuzzy/install.html

3. Install Jupyter Notebook - follow the steps in the command line terminal from this website:

• -> https://jupyter.org/install

------------------------------------------------------------------------------------------------------

Project Inspirations:

This Project's implementation was inspired mainly by these respective works: 

1. Scikit-fuzzy development team. (2022), Tipping Problem [Online] [Accessed: 20th December 2021] https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html

2. Scikit-fuzzy development team. (2022), Tipping Problem: The Hard Way [Online] [Accessed: 20th December 2021] https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html

3. Bilal, E. (2020) Automatic Braking System Using Fuzzy Logic [Online] [Accessed: 21st November 2021] https://github.com/emrebilal/Automatic-Brake-System-using-Fuzzy-Logic

4. Rizianiza, I. Shoodiqin, D,M. (2005) Automatic braking system using fuzzy logic method [Online] [Accessed: 2nd September 2021] https://iopscience.iop.org/article/10.1088/1742-6596/1833/1/012005/pdf

5. Griffiths, A, J. (2019) Jupyter-Fuzzy-Logic System [Online] [Accessed: 21st November 2021] https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter

6. Bassey, E,F. Udofia, K,M. (2019) Modelling of Automatic Braking System Using Fuzzy Logic Controller [Online] [Accessed: 4th September 2021]
https://www.ajol.info/index.php/njt/article/view/191781

7. A. N. D. Dewa, O. Wahyunggoro and P. Nugroho, "Prototype of Automatic Braking System on Car Model Using Fuzzy Logic," 2019 International Conference on Sustainable Engineering and Creative Computing (ICSECC), 2019, pp. 369-374, doi: 10.1109/ICSECC.2019.8907011.
[Accessed: 4th September 2021]

8. Ding, X. (2018) Auto-Brake-System [Online] [Accessed: 21st November 2021] https://github.com/XiangyuDing/Auto-Brake-System

9. Jarrah, M,A. Shaout, A. (1999) Automatic Braking System Using Fuzzy Logic (Abstract) [Online] [Accessed: 2nd September 2021]
https://dl.acm.org/doi/10.5555/1314668.1314672

10.	The MathWorks. (2022) Fuzzy Inference Process [Online] [Accessed: 22nd December 2021] https://uk.mathworks.com/help/fuzzy/fuzzy-inference-process.html#FP347

11.	The MathWorks. (2022) Mamdani and Sugeno Inference Systems [Online] [Accessed: 23rd December 2021] https://uk.mathworks.com/help/fuzzy/types-of-fuzzy-inference-systems.html






