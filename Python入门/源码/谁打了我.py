def start():
    装甲.设置灵敏度(8)
    while True:
        云台.俯仰(30)
        云台.俯仰(-10)

def 装甲被袭(msg):
    print('got hit')
    退出()

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

云台 = gimbal_ctrl
云台.俯仰 = 云台.pitch_ctrl

装甲 = armor_ctrl
装甲.设置灵敏度 = 装甲.set_hit_sensitivity

退出 = rmexit
armor_hit_detection_all = 装甲被袭