from simulator import robot,FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
yes = True
robot.motors(FORWARD, STOP, 1.7)
for i in range(100):
	robot.motors(FORWARD, FORWARD, 1)
	if robot.left_sonar()<15:
		robot.motors(FORWARD, STOP, 4.5)
		robot.motors(FORWARD, FORWARD, 1)
	elif robot.right_sonar()<15:
            robot.motors(STOP, FORWARD, 4.5)
            robot.motors(FORWARD, FORWARD, 1)

robot.exit()


