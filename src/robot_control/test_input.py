from robot_control_class import RobotControl

rc = RobotControl()

x = int(input("Type a number between 0 and 719"))
a = rc.get_laser(x)
print(a)
