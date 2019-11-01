def start():
    单位间隔 = 53/160
    乐谱 = [
        常量.嗦1, 3, 常量.啦1, 1, 常量.哆2, 1, 常量.来2, 1, 常量.咪2, 1, 常量.嗦2, 1, 常量.啦2, 8,
        常量.啦2, 1, 常量.哆3, 2, 常量.啦2, 1, 常量.嗦2, 1, 常量.咪2, 1, 常量.嗦2, 2,
        常量.啦2, 1, 常量.哆3, 2, 常量.啦2, 1, 常量.嗦2, 1, 常量.咪2, 1, 常量.嗦2, 2,
        常量.啦2, 1, 常量.哆3, 2, 常量.啦2, 1, 常量.嗦2, 1, 常量.咪2, 1, 常量.嗦2, 1, 常量.啦2, 1, 常量.咪2, 8,
        常量.咪2, 1, 常量.嗦2, 2, 常量.咪2, 1, 常量.来2, 1, 常量.哆2, 1, 常量.来2, 2,
        常量.咪2, 1, 常量.嗦2, 2, 常量.咪2, 1, 常量.来2, 1, 常量.哆2, 1, 常量.来2, 2,
        常量.咪2, 1, 常量.嗦2, 2, 常量.咪2, 1, 常量.来2, 1, 常量.哆2, 1, 常量.嗦1, 1, 常量.啦1, 1, 常量.哆2, 8,
        常量.发2, 3, 常量.啦2, 1, 常量.啦2, 2, 常量.啦2, 2,
        常量.哆2, 3, 常量.嗦2, 1, 常量.嗦2, 2, 常量.嗦2, 2,
        常量.哆2, 1, 常量.来2, 2, 常量.咪2, 1, 常量.啦2, 1, 常量.嗦2, 1, 常量.咪2, 2,
        常量.哆3, 3, 常量.嗦2, 1, 常量.啦2, 4,
        常量.哆3, 1, 常量.嗦2, 2, 常量.西2, 1, 常量.啦2, 1, 常量.西2, 1, 常量.啦2, 1, 常量.嗦2, 1, 常量.咪2, 8,
        常量.来2, 1, 常量.咪2, 1, 常量.嗦2, 1, 常量.来2, 1, 常量.咪2, 3,
        常量.嗦2, 1, 常量.咪2, 3, 常量.来2, 1, 常量.啦1, 4,
        常量.嗦2, 1, 常量.啦2, 1, 常量.嗦2, 1, 常量.发2, 1, 常量.咪2, 1, 常量.嗦2, 1, 常量.来2, 2, 常量.哆2, 8
    ]
    for 序号 in range(0, len(乐谱)):
        if 序号 % 2 == 0:
            多媒体.演奏(乐谱[序号])
        else:
            时间.睡眠(乐谱[序号])

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

常量 = rm_define
常量.哆1 = 常量.media_sound_solmization_1C
常量.来1 = 常量.media_sound_solmization_1D
常量.咪1 = 常量.media_sound_solmization_1E
常量.发1 = 常量.media_sound_solmization_1F
常量.嗦1 = 常量.media_sound_solmization_1G
常量.啦1 = 常量.media_sound_solmization_1A
常量.西1 = 常量.media_sound_solmization_1B

常量.哆2 = 常量.media_sound_solmization_2C
常量.来2 = 常量.media_sound_solmization_2D
常量.咪2 = 常量.media_sound_solmization_2E
常量.发2 = 常量.media_sound_solmization_2F
常量.嗦2 = 常量.media_sound_solmization_2G
常量.啦2 = 常量.media_sound_solmization_2A
常量.西2 = 常量.media_sound_solmization_2B

常量.哆3 = 常量.media_sound_solmization_3C
常量.来3 = 常量.media_sound_solmization_3D
常量.咪3 = 常量.media_sound_solmization_3E
常量.发3 = 常量.media_sound_solmization_3F
常量.嗦3 = 常量.media_sound_solmization_3G
常量.啦3 = 常量.media_sound_solmization_3A
常量.西3 = 常量.media_sound_solmization_3B

多媒体 = media_ctrl
多媒体.演奏 = 多媒体.play_sound

时间 = time
时间.睡眠 = 时间.sleep