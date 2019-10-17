def start():
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    chassis_ctrl.set_trans_speed(0.5)
    
    media_ctrl.exposure_value_update(rm_define.exposure_value_small)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(3)
    
    vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)
    led_ctrl.gun_led_on()
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_complete_flag=True)
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    
    v = 0.5
    t0 = math.pi/20
    changliang = math.pi/180
    
    for j in range(1,3):
        chassis_ctrl.set_wheel_speed(170, -30, -30, 170)
        gimbal_ctrl.set_rotate_speed(10/0.9)
        gimbal_ctrl.rotate(rm_define.gimbal_left)
        time.sleep(0.9)
        
        for i in range(3, 22):
            xita = i*15*changliang
            vx = v*math.cos(xita)
            vy = v*math.sin(xita)
            chassis_ctrl.move_with_speed(vx+0.015, vy, 0)
            gimbal_ctrl.set_rotate_speed(0)
            if i < 9:
                gimbal_ctrl.set_rotate_speed(10/6/t0)
                gimbal_ctrl.rotate(rm_define.gimbal_left)
            elif i > 15:
                gimbal_ctrl.set_rotate_speed(11/6/t0)
                gimbal_ctrl.rotate(rm_define.gimbal_right)
            time.sleep(t0)
            
        chassis_ctrl.set_wheel_speed(-20, 180, 180, -20)
        gimbal_ctrl.set_rotate_speed(11/0.9)
        gimbal_ctrl.rotate(rm_define.gimbal_right)
        time.sleep(0.9)
        
        for i in range(3, 22):
            xita = i*15*changliang
            vx = v*math.cos(xita)
            vy = -v*math.sin(xita)
            chassis_ctrl.move_with_speed(vx+0.015, vy, 0)
            gimbal_ctrl.set_rotate_speed(0)
            if i < 9:
                gimbal_ctrl.set_rotate_speed(10/6/t0)
                gimbal_ctrl.rotate(rm_define.gimbal_right)
            elif i > 15:
                gimbal_ctrl.set_rotate_speed(12/6/t0)
                gimbal_ctrl.rotate(rm_define.gimbal_left)
            time.sleep(t0)