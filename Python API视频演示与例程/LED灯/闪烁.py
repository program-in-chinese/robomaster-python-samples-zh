def start():
    慢 = 1
    快 = 2
    闪两秒(常量.装甲所有, 慢)
    闪两秒(常量.装甲前底, 快)
    闪两秒(常量.装甲左底, 快)
    闪两秒(常量.装甲后底, 快)
    闪两秒(常量.装甲右底, 快)
    闪两秒(常量.装甲左顶, 快)
    闪两秒(常量.装甲右顶, 快)

def 闪两秒(位置, 频率):
    LED灯.闪烁(位置, 频率)
    时间.睡眠(2)

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

LED灯 = led_ctrl
LED灯.闪烁 = LED灯.set_flash

# 常量部分
常量 = rm_define
常量.装甲所有 = 常量.armor_all
常量.装甲前底 = 常量.armor_bottom_front
常量.装甲后底 = 常量.armor_bottom_back
常量.装甲左底 = 常量.armor_bottom_left
常量.装甲右底 = 常量.armor_bottom_right
常量.装甲左顶 = 常量.armor_top_left
常量.装甲右顶 = 常量.armor_top_right

时间 = time
时间.睡眠 = 时间.sleep