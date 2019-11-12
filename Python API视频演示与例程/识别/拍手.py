def 开始():
    多媒体.开启声音识别(常量.识别拍手)
    
    视觉.直到识别到(常量.两次拍手)
    告知('twice')
    亮灯(绿色)

    视觉.直到识别到(常量.三次拍手)
    print('thrice')
    亮灯(红色)
        
def 亮灯(颜色):
    云台灯(常量.云台所有, 颜色, 常量.效果常亮)
    时间.睡眠(1)
    云台灯(常量.云台所有, 黑色, 常量.效果熄灭)

def 云台灯(位置, 颜色, 灯效):
    LED灯.云台(位置, 颜色['红'], 颜色['绿'], 颜色['蓝'], 灯效)

黑色 = {'红': 0, '绿': 0, '蓝': 0}
红色 = {'红': 255, '绿': 0, '蓝': 0}
绿色 = {'红': 0, '绿': 255, '蓝': 0}

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

start = 开始

多媒体 = media_ctrl
多媒体.开启声音识别 = 多媒体.enable_sound_recognition

视觉 = vision_ctrl
视觉.直到识别到 = 视觉.cond_wait
视觉.取行人信息 = 视觉.get_people_detection_info

LED灯 = led_ctrl
LED灯.云台 = LED灯.set_top_led

# 常量部分
常量 = rm_define
常量.识别拍手 = 常量.sound_detection_applause
常量.两次拍手 = 常量.cond_sound_recognized_applause_twice
常量.三次拍手 = 常量.cond_sound_recognized_applause_thrice

常量.云台所有 = 常量.armor_top_all
常量.云台左 = 常量.armor_top_left
常量.云台右 = 常量.armor_top_right

常量.效果常亮 = 常量.effect_always_on
常量.效果熄灭 = 常量.effect_always_off
常量.效果呼吸 = 常量.effect_breath
常量.效果闪烁 = 常量.effect_flash
常量.效果走马灯 = 常量.effect_marquee

时间 = time
时间.睡眠 = 时间.sleep

告知 = print