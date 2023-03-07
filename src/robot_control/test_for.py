from robot_control_class import RobotControl

rc = RobotControl()
a = rc.get_laser_full()
maxim = 0
for i in a:
    if i > maxim:
        maxim = i

print(maxim)
