# "角度" 未定义，但控制台未报错. 仅在中文命名变量时复现.
def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(30)
    turn()

def turn():
    gimbal_ctrl.yaw_ctrl(角度)