# angle 未定义，但控制台未报错
def start():
    robot_ctrl.robot_ctrl(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(260)
    turn()

def turn():
    gimbal_ctrl.yaw_ctrl(angle)