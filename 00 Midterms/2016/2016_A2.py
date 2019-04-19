a) The student connects to the ebot and assigns a variable called power as 0.1
he makes a fucntion called increasepower which takes in an argument (power) and increases it by 0.1

he makes a while loop which will loop while power is less than or equal to 1.
in the loop, he makes the ebot moves with power 0.1 in each wheel
after 2s,
it will call the increasePower function which increases the power by 0.1 to 0.2
the loop will continue to increase the power till it reaches 1.0 till which it will disconnect from the ebot

The student is trying to slowly increase the speed of the ebot


b) 10 
1st 0.1
2nd 0.2
...
9th 0.9
10th 1.0
when it reaches 1.1, the while loop will not be activated

c) if sleep is removed, the code will reach 1.0 very quickly and the robot will move for a veryveryv3ery shory time (so short it will seem that nothing happened)