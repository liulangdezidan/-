import pyautogui
import time

# 设置要点击的坐标（x, y）
x = 159  # 替换为你想要点击的x坐标
y = 511  # 替换为你想要点击的y坐标

# 等待几秒钟，以便你有时间切换到目标窗口
time.sleep(5)

# 点击100次
for i in range(1000):
    pyautogui.click(x, y)
    time.sleep(0.1)  # 点击之间的延迟，可以根据需要调整