常量 = rm_define
大师 = robot_ctrl
云台 = gimbal_ctrl
装甲 = armor_ctrl

def start():
    大师.set_mode(常量.robot_mode_free)
    云台.set_rotate_speed(260)
    装甲.cond_wait(常量.cond_armor_bottom_back_hit)
    云台.yaw_ctrl(10)
