from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(359)

if(a > 1):
    rc.move_straight()
else:
    rc.stop_robot()

print(a)
