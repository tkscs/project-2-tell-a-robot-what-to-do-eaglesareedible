from simulator import robot,FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
# Robot travels at speed of 6cm/s 
def square():
	for i in range(4):
		forwardwithsonar(3)
		robot.motors(FORWARD, STOP, 3.05)
def spinright(time):
	robot.motors(FORWARD, BACKWARD, time)
def spinleft(time):
	robot.motors(BACKWARD, FORWARD, time)
def screenSaver():
	while True:
		robot.motors(FORWARD, FORWARD, 1)
		if robot.left_sonar()<15:
			robot.motors(FORWARD, BACKWARD, 2)
			robot.motors(FORWARD, FORWARD, 1)
		elif robot.right_sonar()<15:
				robot.motors(BACKWARD, FORWARD, 2)
				robot.motors(FORWARD, FORWARD, 1)
		elif robot.right_sonar()<5:
			break
		elif robot.left_sonar_sonar()<5:
			break
		userInput = input("Press enter in order to end screen saver")
		if not userInput:
			print("Ending screen saver")
			break
def forwardwithsonar(howlong):
	for i in range(howlong):
		robot.motors(FORWARD, FORWARD, 1)
		if robot.left_sonar()<9:
			robot.motors(BACKWARD, BACKWARD, 3)
		elif robot.right_sonar()<9:
				robot.motors(BACKWARD, BACKWARD, 3)
		elif robot.right_sonar()<3:
			break
		elif robot.left_sonar()<3:
			break
screenSaver()

robot.exit()


