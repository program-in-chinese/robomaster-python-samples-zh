# 以下是可供复用的API中文化代码片段. 将其复制到需要运行的代码末尾即可.

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

云台 = gimbal_ctrl
云台.设置旋转速度 = 云台.set_rotate_speed
云台.平转 = 云台.yaw_ctrl

装甲 = armor_ctrl
装甲.等待时机 = 装甲.cond_wait

LED灯 = led_ctrl
LED灯.云台 = LED灯.set_top_led

多媒体 = media_ctrl
多媒体.演奏 = 多媒体.play_sound

# 常量部分
常量 = rm_define
常量.自由模式 = 常量.robot_mode_free
常量.装甲被袭_后底 = 常量.cond_armor_bottom_back_hit
常量.云台_所有 = 常量.armor_top_all
常量.效果_走马灯 = 常量.effect_marquee

# 多媒体
常量.哆 = 常量.media_sound_solmization_1C
常量.来 = 常量.media_sound_solmization_1D
常量.咪 = 常量.media_sound_solmization_1E
常量.发 = 常量.media_sound_solmization_1F
常量.嗦 = 常量.media_sound_solmization_1G
常量.啦 = 常量.media_sound_solmization_1A
常量.西 = 常量.media_sound_solmization_1B

# Python通用库

时间 = time
时间.睡眠 = 时间.sleep
