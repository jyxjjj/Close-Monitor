# Close Monitor

### 使用
此应用将使用Pythonw.exe来启动
这意味着它将不会显示命令行窗口

将此py文件放在桌面并将打开方式设置为Pythonw.exe以双击启动该应用

双击后显示器将被关闭

### ReEnv
ReEnv.py 将Windows环境变量刷新到应用程序，实现实时生效。

### 注意
移动鼠标或其他操作将重新打开显示器

### 授权
此应用使用Unlicense进行许可，这意味着作者将放弃此应用版权

原因是此应用过于简单基础

源码来自网络，调用C语言Windows API来关闭显示器

### Issue
我不知道 ctypes 和 pywin32 在py2.7和py3.7都能正常使用的原因和为什么我分别用了两个不同的包
别问，因为我抄的！
