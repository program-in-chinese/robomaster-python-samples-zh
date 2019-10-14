def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(260)
    armor_ctrl.cond_wait(rm_define.cond_armor_bottom_back_hit)
    gimbal_ctrl.yaw_ctrl(180)
    gun_ctrl.fire_once()
