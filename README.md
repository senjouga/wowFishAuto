refer to https://github.com/kioltk/wow-fishipy/blob/master/fishing.py#L115

<h1>原理</h1>
使用虚拟声卡捕获钓鱼提示音 触发交互按键
实验时虚拟声卡软件为 VBCABLE_Driver


<h1>windows 设置</h1>
windows 设置 - 系统 - 声音 - 输入设备 输出设备设为虚拟声卡
windows 设置 - 隐私 - 麦克风 - 开启设备麦克风权限 开启 允许应用访问你的麦克风

打开声音合成器可查看声音变化


<h1>游戏设置</h1>
wow 10.0
选择 窗口模式
仅开启 主音量 和 效果音 调高这两项音量
开启自动拾取
交互键的设置：ESC-选项-控制-开启交互按键-设置与目标互动的键位

默认开始钓鱼按键 F
默认交互键按键 G

<h1>原理</h1>
中鱼提示音高于设置阈值即可触发交互按键钓鱼

volume-test 用于测试 安静环境下的声音值 和  钩住鱼时声音值
 
auto.py 中 silentVolume  gotVolume
低于 silentVolume 视为安静状态
高于 gotVolume 视为钩中鱼 触发交互按键
maxCatch 钩中鱼次数超过次数停止

devicelist.py 可查看当前音频输入输出设备

<h1>启动</h1>
python auto.py
切换到wow 窗口 开始钓鱼