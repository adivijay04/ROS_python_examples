from robot_control_class import RobotControl

rc = RobotControl()

d = rc.get_laser_full()
l = {"Position 0": d[0], "Position 100": d[100], "Position 200": d[200], "Position 300": d[300], "Position 400": d[400], "Position 500": d[500], "Position 600": d[600], "Position 719": d[719]}
print(l)