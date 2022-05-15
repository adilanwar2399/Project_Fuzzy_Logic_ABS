import numpy as np
import skfuzzy as fuzz

# Matplotlib: Only needed for plotting the graphs by hand;
# Not needed if the Control Primer (Control API) is used, 
# as the in built .view() Method allows the graphical representation to be generated.
import matplotlib.pyplot as plt 
# Magic Function.
%matplotlib inline

# Form and declare the universe variables:

#1. Speed
speed = np.arange(0, 101, 1)

#2. Distance
distance = np.arange (0,61,1)

#3. Brake Force
brake_Force = np.arange (0,101,1)

# Fuzzy Membership Functions are created and initialised over here:

# These functions are determined on linguistic scenarios that are based upon: 
# 1. How fast the vehicle is going? 
# 2. What is the distance e.g. between the vehicles (useful for braking)?
# 3. What is the amount of force required for a safe and successful brake?

# NB: Here the function trapf is implemented for every membership function; 
# this is useful as this allows computational fuzzy membership function values to be 
# returned via the usage of this trapezoidal function. (Used in MATLAB also.)

# Speed - Fuzzy Membership Function:

# <-------Evaluation Experimentation 1: Triangular Membership function ---------->
# speed_very_fast = fuzz.trimf(speed, [67, 100, 100])
# speed_fast = fuzz.trimf(speed, [34, 67, 100])
# speed_very_slow= fuzz.trimf(speed, [0, 0, 34])
# speed_slow = fuzz.trimf(speed, [0, 34, 67 ])

# <-------Evaluation Experimentation 2: Speed Membership Function values modified ---------->
# speed_very_fast = fuzz.trapmf(speed, [85, 100, 100, 100])
# speed_fast = fuzz.trapmf(speed, [55, 70, 85, 100])
# speed_very_slow= fuzz.trapmf(speed, [0, 0, 25, 40])
# speed_slow = fuzz.trapmf(speed, [25, 40, 55, 70])

speed_very_fast = fuzz.trapmf(speed, [70, 85, 100, 100])
speed_fast = fuzz.trapmf(speed, [45, 55, 70, 80])
speed_very_slow= fuzz.trapmf(speed, [0, 0, 15, 30])
speed_slow = fuzz.trapmf(speed, [20, 30, 45, 55])

# NB: For the next two membership functions - the function trimf is implemented; 
# this is useful as this allows computational fuzzy membership function values to be 
# returned via the usage of this triangular function. (Used in MATLAB also.)

# Distance - Fuzzy Membership Function:

# <-------Evaluation Experimentation 2: Distance Membership Function values modified ---------->
# distance_very_far = fuzz.trimf(distance, [45, 60, 60])
# distance_far = fuzz.trimf(distance, [30, 45, 60])
# distance_very_close = fuzz.trimf(distance, [0, 0, 15])
# distance_close = fuzz.trimf(distance, [0, 15, 30])

distance_very_far = fuzz.trimf(distance, [35, 45, 55])
distance_far = fuzz.trimf(distance, [20, 30, 40])
distance_very_close = fuzz.trimf(distance, [0, 0, 10])
distance_close = fuzz.trimf(distance, [5, 15, 25])

# Brake Force - Fuzzy Membership Function:
brake_force_very_heavy = fuzz.trimf(brake_Force, [60, 80, 100])
brake_force_heavy = fuzz.trimf(brake_Force, [40, 60, 80])
brake_force_very_light = fuzz.trimf(brake_Force, [0, 20, 40])
brake_force_light= fuzz.trimf(brake_Force, [20, 40, 60])

# Graphical Representation of the Fuzzy Membership Functions and the Universe Variables.
# - Speed graph plot 
# - Distance graph plot
# - Brakes graph plot

fig, (Distance_Axis_Plot) = plt.subplots(figsize=(30, 10), nrows =1)

Distance_Axis_Plot.set_title('Distance:', fontsize='25') 
Distance_Axis_Plot.plot(distance, distance_very_close, 'r', linewidth=2.5, label='Very Close')
Distance_Axis_Plot.plot(distance, distance_close, 'g', linewidth=2.5, label='Close')
Distance_Axis_Plot.plot(distance, distance_very_far, 'b', linewidth=2.5, label='Very Far')
Distance_Axis_Plot.plot(distance, distance_far, 'm', linewidth=2.5, label='Far')
Distance_Axis_Plot.legend()

# Turn off top/right axes
for everyAxis in (Distance_Axis_Plot,):
    everyAxis.spines['top'].set_visible(False)
    everyAxis.spines['right'].set_visible(False)
    everyAxis.get_xaxis().tick_bottom()
    everyAxis.get_yaxis().tick_left()

plt.tight_layout()

fig, (Brake_Axis_Plot) = plt.subplots(figsize=(30, 10), nrows =1)

Brake_Axis_Plot.set_title('Brake Force:', fontsize='25')
Brake_Axis_Plot.plot(brake_Force, brake_force_very_heavy, 'r', linewidth=2.5, label='Very Heavy')
Brake_Axis_Plot.plot(brake_Force, brake_force_heavy, 'g', linewidth=2.5, label='Heavy')
Brake_Axis_Plot.plot(brake_Force, brake_force_very_light, 'b', linewidth=2.5, label='Very Light')
Brake_Axis_Plot.plot(brake_Force, brake_force_light, 'm', linewidth=2.5, label='Light')
Brake_Axis_Plot.legend()

# Turn off top/right axes
for everyAxis in (Brake_Axis_Plot,):
    everyAxis.spines['top'].set_visible(False)
    everyAxis.spines['right'].set_visible(False)
    everyAxis.get_xaxis().tick_bottom()
    everyAxis.get_yaxis().tick_left()

plt.tight_layout()

# Graphical Representation of the Fuzzy Membership Functions and the Universe Variables.
# - Speed graph plot 
# - Distance graph plot
# - Brakes graph plot

fig, (Distance_Axis_Plot, Speed_Axis_Plot, Brake_Axis_Plot) = plt.subplots(figsize=(20, 18), nrows =3)

Distance_Axis_Plot.set_title('Distance:', fontsize='25') 
Distance_Axis_Plot.plot(distance, distance_very_close, 'r', linewidth=2.5, label='Very Close')
Distance_Axis_Plot.plot(distance, distance_close, 'g', linewidth=2.5, label='Close')
Distance_Axis_Plot.plot(distance, distance_very_far, 'b', linewidth=2.5, label='Very Far')
Distance_Axis_Plot.plot(distance, distance_far, 'm', linewidth=2.5, label='Far')
Distance_Axis_Plot.legend()

Speed_Axis_Plot.set_title('Speed: ', fontsize='25')
Speed_Axis_Plot.plot(speed, speed_very_fast, 'r', linewidth=2.5, label='Very Fast')
Speed_Axis_Plot.plot(speed, speed_fast, 'g', linewidth=2.5, label='Fast')
Speed_Axis_Plot.plot(speed, speed_very_slow, 'b', linewidth=2.5, label='Very Slow')
Speed_Axis_Plot.plot(speed, speed_slow, 'm', linewidth=2.5, label='Slow')
Speed_Axis_Plot.legend()

Brake_Axis_Plot.set_title('Brake Force:', fontsize='25')
Brake_Axis_Plot.plot(brake_Force, brake_force_very_heavy, 'r', linewidth=2.5, label='Very Heavy')
Brake_Axis_Plot.plot(brake_Force, brake_force_heavy, 'g', linewidth=2.5, label='Heavy')
Brake_Axis_Plot.plot(brake_Force, brake_force_very_light, 'b', linewidth=2.5, label='Very Light')
Brake_Axis_Plot.plot(brake_Force, brake_force_light, 'm', linewidth=2.5, label='Light')
Brake_Axis_Plot.legend()

# Turn off top/right axes
for everyAxis in (Distance_Axis_Plot, Speed_Axis_Plot, Brake_Axis_Plot):
    everyAxis.spines['top'].set_visible(False)
    everyAxis.spines['right'].set_visible(False)
    everyAxis.get_xaxis().tick_bottom()
    everyAxis.get_yaxis().tick_left()

plt.tight_layout()

# Activation of the Fuzzy Membership functions occurs here:
inputDriving_Distance = float(input("Distance to drive: "))
inputDriving_Speed = float(input("Speed of driving: "))    

level_of_driving_distance_very_close = fuzz.interp_membership(distance, distance_very_close, inputDriving_Distance )
level_of_driving_distance_close = fuzz.interp_membership(distance, distance_close, inputDriving_Distance)
level_of_driving_distance_very_far = fuzz.interp_membership(distance, distance_very_far, inputDriving_Distance)
level_of_driving_distance_far = fuzz.interp_membership(distance, distance_far, inputDriving_Distance)
                                                            
level_of_driving_speed_very_slow = fuzz.interp_membership(speed, speed_very_slow, inputDriving_Speed)
level_of_driving_speed_slow = fuzz.interp_membership(speed, speed_slow, inputDriving_Speed)
level_of_driving_speed_very_fast = fuzz.interp_membership(speed, speed_very_fast, inputDriving_Speed)
level_of_driving_speed_fast = fuzz.interp_membership(speed, speed_fast, inputDriving_Speed)

controlling_brakes_for_execution = []

# Rule activation:
rule_one_activating = np.fmin(level_of_driving_distance_close, level_of_driving_speed_very_fast)
rule_two_activating = np.fmin(level_of_driving_distance_far, level_of_driving_speed_very_fast)
rule_three_activating = np.fmin(level_of_driving_distance_very_far, level_of_driving_speed_very_fast)
rule_four_activating = np.fmin(level_of_driving_distance_very_close, level_of_driving_speed_very_fast)
rule_five_activating = np.fmin(level_of_driving_distance_close, level_of_driving_speed_fast)
rule_six_activating = np.fmin(level_of_driving_distance_far, level_of_driving_speed_fast)
rule_seven_activating = np.fmin(level_of_driving_distance_very_far, level_of_driving_speed_fast)
rule_eight_activating = np.fmin(level_of_driving_distance_very_close, level_of_driving_speed_fast)
rule_nine_activating = np.fmin(level_of_driving_distance_close, level_of_driving_speed_very_slow)
rule_ten_activating = np.fmin(level_of_driving_distance_far, level_of_driving_speed_very_slow)
rule_eleven_activating = np.fmin(level_of_driving_distance_very_far, level_of_driving_speed_very_slow)
rule_twelve_activating = np.fmax(level_of_driving_distance_very_close, level_of_driving_speed_very_slow)
rule_thirteen_activating = np.fmin(level_of_driving_distance_close, level_of_driving_speed_slow)
rule_fourteen_activating = np.fmin(level_of_driving_distance_far, level_of_driving_speed_slow)
rule_fifteen_activating = np.fmin(level_of_driving_distance_very_far, level_of_driving_speed_slow)
rule_sixteen_activating = np.fmin(level_of_driving_distance_very_close, level_of_driving_speed_slow)

# Incorporate braking force with the rule activations:
force_of_braking_very_heavy_one = np.fmin(rule_one_activating, brake_force_very_heavy)
force_of_braking_very_heavy_two = np.fmin(rule_two_activating, brake_force_very_heavy)
force_of_braking_very_heavy_three = np.fmin(rule_three_activating, brake_force_very_heavy)
force_of_braking_very_heavy_four = np.fmin(rule_four_activating, brake_force_very_heavy)
force_of_braking_heavy_five= np.fmin(rule_five_activating, brake_force_heavy)
force_of_braking_heavy_six= np.fmin(rule_six_activating, brake_force_heavy)
force_of_braking_heavy_seven= np.fmin(rule_seven_activating, brake_force_heavy)
force_of_braking_heavy_eight= np.fmin(rule_eight_activating, brake_force_heavy)
force_of_braking_very_light_nine = np.fmin(rule_nine_activating, brake_force_very_light)
force_of_braking_very_light_ten = np.fmin(rule_ten_activating, brake_force_very_light)
force_of_braking_very_light_eleven = np.fmin(rule_eleven_activating, brake_force_very_light)
force_of_braking_very_light_twelve = np.fmin(rule_twelve_activating, brake_force_very_light)
force_of_braking_light_thirteen = np.fmin(rule_thirteen_activating, brake_force_light)
force_of_braking_light_fourteen = np.fmin(rule_fourteen_activating, brake_force_light)
force_of_braking_light_fifteen = np.fmin(rule_fifteen_activating, brake_force_light)
force_of_braking_light_sixteen = np.fmin(rule_sixteen_activating, brake_force_light)

# Populate the controlling brakes array by appending to the list for the execution of these rules:
controlling_brakes_for_execution.append(force_of_braking_very_heavy_one)
controlling_brakes_for_execution.append(force_of_braking_very_heavy_two)
controlling_brakes_for_execution.append(force_of_braking_very_heavy_three)
controlling_brakes_for_execution.append(force_of_braking_very_heavy_four)
controlling_brakes_for_execution.append(force_of_braking_heavy_five)
controlling_brakes_for_execution.append(force_of_braking_heavy_six)
controlling_brakes_for_execution.append(force_of_braking_heavy_seven)
controlling_brakes_for_execution.append(force_of_braking_heavy_eight)
controlling_brakes_for_execution.append(force_of_braking_very_light_nine)
controlling_brakes_for_execution.append(force_of_braking_very_light_ten)
controlling_brakes_for_execution.append(force_of_braking_very_light_eleven)
controlling_brakes_for_execution.append(force_of_braking_very_light_twelve)
controlling_brakes_for_execution.append(force_of_braking_light_thirteen)
controlling_brakes_for_execution.append(force_of_braking_light_fourteen)
controlling_brakes_for_execution.append(force_of_braking_light_fifteen)
controlling_brakes_for_execution.append(force_of_braking_light_sixteen)

# Visualise membership output activity:
initial_brake_force = np.zeros_like(brake_Force)

fig, brakingForce_Membership_Plot = plt.subplots(figsize=(30, 10))

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_heavy_one, facecolor= 'm', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_heavy, 'm', linewidth=3.0, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_heavy_two, facecolor= 'm', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_heavy, 'm', linewidth=3.0, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_heavy_three, facecolor= 'm', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_heavy, 'm', linewidth=3.0, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_heavy_four, facecolor= 'm', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_heavy, 'm', linewidth=3.0, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_heavy_five, facecolor= 'r', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_heavy, 'r', linewidth=2.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_heavy_six, facecolor= 'r', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_heavy, 'r', linewidth=2.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_heavy_seven, facecolor= 'r', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_heavy, 'r', linewidth=2.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_heavy_eight, facecolor= 'r', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_heavy, 'r', linewidth=2.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_light_nine, facecolor= 'b', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_light, 'b', linewidth=0.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_light_ten, facecolor= 'b', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_light, 'b', linewidth=0.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_light_eleven, facecolor= 'b', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_light, 'b', linewidth=0.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_very_light_twelve, facecolor= 'b', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_very_light, 'b', linewidth=0.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_light_thirteen, facecolor= 'g', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_light, 'g', linewidth=1.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_light_fourteen, facecolor= 'g', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_light, 'g', linewidth=1.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_light_fifteen, facecolor= 'g', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_light, 'g', linewidth=1.5, linestyle='--', )

brakingForce_Membership_Plot.fill_between(brake_Force, initial_brake_force, force_of_braking_light_sixteen, facecolor= 'none', alpha=0.7)
brakingForce_Membership_Plot.plot(brake_Force, brake_force_light, 'g', linewidth=1.5, linestyle='--', )

brakingForce_Membership_Plot.set_title('Activity of the Output Membership:')

# Turn off top/right axes
for everyAxis in (brakingForce_Membership_Plot,):
    everyAxis.spines['top'].set_visible(False)
    everyAxis.spines['right'].set_visible(False)
    everyAxis.get_xaxis().tick_bottom()
    everyAxis.get_yaxis().tick_left()

plt.tight_layout()

#########################
# METHOD OF AGGREGATION #
#########################

# NB: ALL IN ONE CAUSES MEMORY ERROR!

#aggregated = np.fmax(force_of_braking_very_heavy_one, (np.fmax(force_of_braking_very_heavy_two, ((np.fmax(force_of_braking_very_heavy_three,
                   # (((np.fmax(force_of_braking_very_heavy_four, ((((np.fmax(force_of_braking_heavy_five, (((((np.fmax(force_of_braking_heavy_six,
                   # ((((((np.fmax(force_of_braking_heavy_seven, (((((((np.fmax(force_of_braking_heavy_eight, ((((((((np.fmax(force_of_braking_very_light_nine,
                   # (((((((((np.fmax(force_of_braking_very_light_ten, ((((((((((np.fmax(force_of_braking_very_light_eleven, (((((((((((np.fmax(force_of_braking_very_light_twelve
                   # ((((((((((((np.fmax(force_of_braking_light_thirteen, (((((((((((((np.fmax(force_of_braking_light_fourteen, ((((((((((((((np.fmax(force_of_braking_light_fifteen, 
                   # (((((((((((((((np.fmax(force_of_braking_light_sixteen))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
                                      
agg_arr1 = np.fmax(force_of_braking_very_heavy_one, (np.fmax(force_of_braking_very_heavy_two, ((np.fmax(force_of_braking_very_heavy_three, force_of_braking_very_heavy_four))))))
agg_arr2 = np.fmax(force_of_braking_heavy_five, (np.fmax(force_of_braking_heavy_six, ((np.fmax(force_of_braking_heavy_seven, force_of_braking_heavy_eight))))))
agg_arr3 = np.fmax(force_of_braking_very_light_nine, (np.fmax(force_of_braking_very_light_ten, ((np.fmax(force_of_braking_very_light_eleven, force_of_braking_very_light_twelve))))))
agg_arr4 = np.fmax(force_of_braking_light_thirteen, (np.fmax(force_of_braking_light_fourteen, ((np.fmax(force_of_braking_light_fifteen, force_of_braking_light_sixteen))))))

aggregated_arr1_arr2 = np.fmax(agg_arr1, agg_arr2)
aggregated_arr3_arr4 = np.fmax(agg_arr3, agg_arr4)

aggregated = np.fmax(aggregated_arr1_arr2, aggregated_arr3_arr4 )

########################################
# CENTROID - METHOD OF DEFUZZIFICATION #
########################################

# Calculate Defuzzified result:
execution_of_brakes = fuzz.defuzz(brake_Force, aggregated, 'centroid')
print(execution_of_brakes, "%: is the Essential Braking Force Required. ")

if (inputDriving_Distance < inputDriving_Speed):
    print (execution_of_brakes, "%: is the Essential Braking Force Required. ")
    if(inputDriving_Distance < inputDriving_Speed/2):
        print ("As the driving distance is less than half of the driving speed then,", execution_of_brakes, "%: is the Essential Braking Force Required. ")
elif (inputDriving_Distance > inputDriving_Speed):
    print ("0% is the required braking force; braking is not necessary; you may continue to travel.")
    if(inputDriving_Distance > inputDriving_Speed/2):
        print ("As the driving distance is greater than half of the driving speed then 0%: is the Essential Braking Force Required. ")
elif (inputDriving_Distance == inputDriving_Speed):
    print ("0% is the required braking force; braking is not necessary; you may continue to travel.")
else: 
    print ("0% is the required braking force; braking is not necessary; you may continue to travel.")    

# This is essential for the plotting of the Defuzzified result:    
activation_of_braking_force = fuzz.interp_membership(brake_Force, aggregated, execution_of_brakes)  

# Visualize this Defuzzification Plot:
fig, brakingDefuzz_Plot = plt.subplots(figsize=(30, 10))

brakingDefuzz_Plot.plot(brake_Force, brake_force_very_heavy, 'm', linewidth=2, linestyle='--')
brakingDefuzz_Plot.plot(brake_Force, brake_force_heavy, 'r', linewidth=1.5, linestyle='--')
brakingDefuzz_Plot.plot(brake_Force, brake_force_very_light, 'b', linewidth=1, linestyle='--', )
brakingDefuzz_Plot.plot(brake_Force, brake_force_light, 'g', linewidth=0.5, linestyle='--')

brakingDefuzz_Plot.fill_between(brake_Force, initial_brake_force, aggregated, facecolor='Orange', alpha=0.7)
brakingDefuzz_Plot.plot([execution_of_brakes, execution_of_brakes], [0, activation_of_braking_force], 'k', linewidth=1.5, alpha=0.9)
brakingDefuzz_Plot.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for everyAxis in (brakingDefuzz_Plot,):
    everyAxis.spines['top'].set_visible(False)
    everyAxis.spines['right'].set_visible(False)
    everyAxis.get_xaxis().tick_bottom()
    everyAxis.get_yaxis().tick_left()

plt.tight_layout()