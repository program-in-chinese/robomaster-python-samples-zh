def 开始():
    视觉.开启识别(行人)
    
    while True:
        if 视觉.当识别到(常量.有行人时):
            信息 = 视觉.取行人信息()
            告知(信息)
        时间.睡眠(1)
        

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

start = 开始

视觉 = vision_ctrl
视觉.开启识别 = 视觉.enable_detection
视觉.当识别到 = 视觉.check_condition
视觉.取行人信息 = 视觉.get_people_detection_info

# 常量部分
常量 = rm_define
常量.有行人时 = 常量.cond_recognized_people
常量.行人 = 常量.vision_detection_people

时间 = time
时间.睡眠 = 时间.sleep

告知 = print