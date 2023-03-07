from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")

rc.move_straight_time("forward", 0.3, 5)
rc.turn("counter-clockwise", 0.3, 7)
rc.move_straight_time("forward", 0.3, 7)
rc.turn("counter-clockwise", 0.3, 7)
rc.move_straight_time("forward", 0.3, 5)
