from naoqi import ALProxy
robot_ip = "192.168.137.95"
puerto = 9559

motion = ALProxy("ALMotion", robot_ip, puerto)

motion.post.openHand("RHand")
motion.setStiffnesses("RArm", 1.0)

motion.move.rightArm( 0, 0.5, 0)
