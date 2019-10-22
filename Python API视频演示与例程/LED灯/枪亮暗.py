def start():
    次数 = 0
    while 次数 < 3:
        LED灯.枪亮()
        time.sleep(1)
        LED灯.枪暗()
        time.sleep(1)
        次数 += 1

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.
LED灯 = led_ctrl
LED灯.枪亮 = LED灯.gun_led_on
LED灯.枪暗 = LED灯.gun_led_off