from simulator import robot,FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
# Robot travels at speed of 6cm/s 
def forwardwithsonar(howlong):
	"This function does forward"
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

def square():
	for i in range(4):
		forwardwithsonar(3)
		robot.motors(FORWARD, STOP, 3.05)
def spinright(spinrighttime):
	robot.motors(FORWARD, BACKWARD, spinrighttime)
def spinleft(spinlefttime):
	robot.motors(BACKWARD, FORWARD, spinlefttime)
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
userInput = input("Select one: \n square\nspinright\nspinleft\nscreensaver\nforward\nanything else to exit\n")
if userInput=='square':
	square()
elif userInput=='spinright':
	spintime = int(input("How many seconds should it spin for?"))
	spinright(spintime)
elif userInput=='spinleft':
	spintime = int(input("How many seconds should it spin for?"))
	spinleft(spintime)
elif userInput=='screensaver':
	screenSaver()
else:
	print("Breaking")
	robot.exit()