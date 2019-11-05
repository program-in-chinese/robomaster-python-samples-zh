def 开始():
    时间戳 = 工具.取上电时间()
    print(时间戳)
    
    时间.睡眠(3)
    print(工具.取上电时间() - 时间戳)

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

start = 开始

工具 = tools
工具.取上电时间 = tools.get_unixtime()

时间 = time
时间.睡眠 = 时间.sleep