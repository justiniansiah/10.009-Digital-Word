a) 2 sonars are the minimum required. The front sonar and at least one of the side sonars. This is so that the bot can measure the distance from the front as well as from the sides. The angular heading of the robot can be calulated by the 2 readings from the sonars.

If the follower is to follow a right wall, a right sonar is required, and left if the left wall is to be followed.


b) The states I used in my controller is 1: follow the wall. ie no obstruction in front and minimum distance from wall is kept so the robot moves forward without rotation.
state 2 is activated when the distance exceeeds the minimum or maximum threshold distance from a wall to which the bot will rotate accordingly to correct the error.