def start():
    大师.设置模式(常量.自由模式)
    红 = 1
    绿 = 0
    蓝 = 0
    for times in range(1, 4):
        红,绿,蓝 = 蓝,红,绿
        LED灯.云台(常量.云台_所有, 255*红, 255*绿, 255*蓝, 常量.效果_走马灯)
        time.sleep(1)

常量 = rm_define
常量.自由模式 = 常量.robot_mode_free
常量.云台_所有 = 常量.armor_top_all
常量.效果_走马灯 = 常量.effect_marquee

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

LED灯 = led_ctrl
LED灯.云台 = LED灯.set_top_led