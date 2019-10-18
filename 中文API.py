# 以下是可供复用的API中文化代码片段. 将其复制到需要运行的代码末尾即可.

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

底盘 = chassis_ctrl
底盘.设置平移速度 = 底盘.set_trans_speed
底盘.设置轮速 = 底盘.set_wheel_speed
底盘.指定速度运动 = 底盘.move_with_speed

云台 = gimbal_ctrl
云台.设置旋转速度 = 云台.set_rotate_speed
云台.平转 = 云台.yaw_ctrl
云台.旋转 = 云台.rotate

装甲 = armor_ctrl
装甲.等待时机 = 装甲.cond_wait

LED灯 = led_ctrl
LED灯.开启枪LED = LED灯.gun_led_on
LED灯.云台 = LED灯.set_top_led
LED灯.底部 = LED灯.set_bottom_led

多媒体 = media_ctrl
多媒体.演奏 = 多媒体.play_sound
多媒体.更新曝光值 = 多媒体.exposure_value_update

视觉 = vision_ctrl
视觉.启用探测 = 视觉.enable_detection
视觉.禁用探测 = 视觉.disable_detection
视觉.设置探测距离 = 视觉.set_marker_detection_distance
视觉.探测标签并瞄准 = 视觉.detect_marker_and_aim

# 常量部分
常量 = rm_define
常量.自由模式 = 常量.robot_mode_free
常量.底盘跟随模式 = 常量.robot_mode_chassis_follow
常量.装甲被袭_后底 = 常量.cond_armor_bottom_back_hit
常量.装甲顶部所有 = 常量.armor_top_all
常量.装甲底部所有 = 常量.armor_bottom_all
常量.效果_走马灯 = 常量.effect_marquee
常量.云台左侧 = 常量.gimbal_left
常量.云台右侧 = 常量.gimbal_right

# 视觉
常量.视觉探测标签 = 常量.vision_detection_marker
常量.红心标签 = 常量.marker_trans_red_heart
常量.小曝光值 = 常量.exposure_value_small

常量.射击音效 = 常量.media_sound_shoot

常量.闪烁灯效 = 常量.effect_flash

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

数学 = math
数学.π = math.pi