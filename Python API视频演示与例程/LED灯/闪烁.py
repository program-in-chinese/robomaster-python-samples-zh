def start():
    LED灯.闪烁(常量.装甲所有, 2)
    时间.睡眠(2)
    LED灯.闪烁(常量.装甲前底, 2)
    时间.睡眠(2)
    LED灯.闪烁(常量.装甲左底, 2)
    时间.睡眠(2)
    LED灯.闪烁(常量.装甲右底, 2)
    时间.睡眠(2)
    LED灯.闪烁(常量.装甲左顶, 2)
    时间.睡眠(2)
    LED灯.闪烁(常量.装甲右顶, 2)
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