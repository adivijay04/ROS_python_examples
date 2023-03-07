from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(359)
while(a > 1):
    rc.move_straight()
    a = rc.get_laser(359)
    print("current distance to wall is %f" % a)

rc.stop_robot()
print("Wall is at %f meters! Stop the robot!" % a)
