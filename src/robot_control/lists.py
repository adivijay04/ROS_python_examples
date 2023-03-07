from robot_control_class import RobotControl

rc = RobotControl()

a = list(rc.get_laser_full())
print(a[0], a[361], a[719])
