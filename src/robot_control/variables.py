from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(279)
print(laser1)

laser2 = rc.get_laser(359)
print(laser2)

laser2 = rc.get_laser(125)
print(laser2)
