def start():
    闹钟时刻 = {'时': 10, '分': 35}
    # 省电
    LED灯.熄灭(常量.装甲所有)
    while True:
        当前时间 = 取当前时间()
        # 仅作演示, 并不严谨
        if 当前时间['时'] == 闹钟时刻['时'] and 当前时间['分'] == 闹钟时刻['分']:
            放歌()
            break
        时间.睡眠(20)

def 取当前时间():
    年 = 工具.取本地时间(常量.本地年)
    月 = 工具.取本地时间(常量.本地月)
    日 = 工具.取本地时间(常量.本地日)
    时 = 工具.取本地时间(常量.本地时)
    分 = 工具.取本地时间(常量.本地分)
    秒 = 工具.取本地时间(常量.本地秒)
    print(str(年) + '/' + str(月) + '/' + str(日) + ' '
        + str(时) + ':' + str(分) + ':' + str(秒))
    return {
        '年': 年,
        '月': 月,
        '日': 日,
        '时': 时,
        '分': 分,
        '秒': 秒
    }

def 放歌():
    短=0.3
    中=0.5
    长=0.6
    乐谱 = [常量.哆, 短, 常量.来, 短, 常量.咪, 短, 常量.哆, 中,
            常量.哆, 短, 常量.来, 短, 常量.咪, 短, 常量.哆, 中,
            常量.咪, 短, 常量.发, 短, 常量.嗦, 中,
            常量.咪, 短, 常量.发, 短, 常量.嗦, 中,
            常量.嗦, 短, 常量.啦, 短, 常量.嗦, 短, 常量.发, 中, 常量.咪, 短, 常量.哆, 中,
            常量.嗦, 短, 常量.啦, 短, 常量.嗦, 短, 常量.发, 中, 常量.咪, 短, 常量.哆, 中,
            常量.来, 短, 常量.嗦, 短, 常量.哆, 长,
            常量.来, 短, 常量.嗦, 短, 常量.哆, 长]
    while True:
        for 序号 in range(0, len(乐谱)):
            if 序号 % 2 == 0:
                多媒体.演奏(乐谱[序号])
            else:
                时间.睡眠(乐谱[序号])

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

工具 = tools
工具.取本地时间 = 工具.get_localtime

LED灯 = led_ctrl
LED灯.云台 = LED灯.set_top_led
LED灯.云台单灯 = LED灯.set_single_led
LED灯.熄灭 = LED灯.turn_off

多媒体 = media_ctrl
多媒体.演奏 = 多媒体.play_sound

# 常量部分
常量 = rm_define
常量.装甲所有 = 常量.armor_all
常量.底盘前 = 常量.armor_bottom_front
常量.底盘后 = 常量.armor_bottom_back
常量.底盘左 = 常量.armor_bottom_left
常量.底盘右 = 常量.armor_bottom_right
常量.云台左 = 常量.armor_top_left
常量.云台右 = 常量.armor_top_right

常量.效果常亮 = 常量.effect_always_on
常量.效果熄灭 = 常量.effect_always_off
常量.效果呼吸 = 常量.effect_breath
常量.效果闪烁 = 常量.effect_flash
常量.效果走马灯 = 常量.effect_marquee

常量.本地年 = 常量.localtime_year
常量.本地月 = 常量.localtime_month
常量.本地日 = 常量.localtime_day
常量.本地时 = 常量.localtime_hour
常量.本地分 = 常量.localtime_minute
常量.本地秒 = 常量.localtime_second

常量.哆 = 常量.media_sound_solmization_1C
常量.来 = 常量.media_sound_solmization_1D
常量.咪 = 常量.media_sound_solmization_1E
常量.发 = 常量.media_sound_solmization_1F
常量.嗦 = 常量.media_sound_solmization_1G
常量.啦 = 常量.media_sound_solmization_1A
常量.西 = 常量.media_sound_solmization_1B

时间 = time
时间.睡眠 = 时间.sleep