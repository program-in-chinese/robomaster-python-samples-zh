# 介绍： https://zhuanlan.zhihu.com/p/86692696
def start():
    大师.设置模式(常量.自由模式)
    云台.设置旋转速度(60)
    装甲.等待时机(常量.装甲被袭_后底)
    云台.平转(20)

常量 = rm_define
常量.自由模式 = 常量.robot_mode_free
常量.装甲被袭_后底 = 常量.cond_armor_bottom_back_hit

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

云台 = gimbal_ctrl
云台.设置旋转速度 = 云台.set_rotate_speed
云台.平转 = 云台.yaw_ctrl

装甲 = armor_ctrl
装甲.等待时机 = 装甲.cond_wait
