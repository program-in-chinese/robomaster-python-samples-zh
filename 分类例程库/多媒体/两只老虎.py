# 介绍： https://zhuanlan.zhihu.com/p/87072890
def start():
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

常量 = rm_define
常量.哆 = 常量.media_sound_solmization_1C
常量.来 = 常量.media_sound_solmization_1D
常量.咪 = 常量.media_sound_solmization_1E
常量.发 = 常量.media_sound_solmization_1F
常量.嗦 = 常量.media_sound_solmization_1G
常量.啦 = 常量.media_sound_solmization_1A
常量.西 = 常量.media_sound_solmization_1B

多媒体 = media_ctrl
多媒体.演奏 = 多媒体.play_sound

时间 = time
时间.睡眠 = 时间.sleep