from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep,sleep_ms

# ---------- LED 配置 ----------
led = Pin(25, Pin.OUT)

# ---------- 按键配置 ----------
button = Pin(15, Pin.IN, Pin.PULL_UP)   # 内部上拉，按下为低电平
press_count = 0                         # 按键计数
update_display = False                  # 标记是否需要更新 OLED

# 按键中断服务程序
def button_irq(pin):
    global press_count, update_display
    # 简单防抖：先禁用中断，待会再启用（或使用软件延时）
    button.irq(handler=None)            # 临时关闭中断
    # 等待10ms后再检测是否确实按下（防抖动）
    sleep_ms(10)
    if button.value() == 0:             # 确认按下
        press_count += 1
        update_display = True
    button.irq(handler=button_irq)      # 重新启用中断

# 配置中断：下降沿触发
button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq)

# ---------- OLED 配置 ----------
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

print("扫描 I2C 总线...")
devices = i2c.scan()
if devices:
    for d in devices:
        print("找到设备，地址:", hex(d))
else:
    print("未找到 I2C 设备，请检查接线！")
    # 如果没有设备，可以停止执行或继续（但会报错）
    # 这里我们直接退出
    raise RuntimeError("I2C设备未找到")

oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)  # 如果地址是0x3D请修改

# 清屏并显示初始内容
oled.fill(0)
oled.text("Hello, World!", 0, 0)
oled.text("Count: 0", 0, 20)
oled.show()

print("LED 开始闪烁，按键计数开始...")
# ---------- 主循环 ----------
while True:
    try:
        led.toggle()
        print("Hello, World!")      # 控制台输出

        # 如果按键中断触发了更新标记，则刷新OLED第二行
        if update_display:
            # 重新绘制第二行（注意先清除旧数字，这里用填充整个区域再重绘所有内容更简单）
            # 更好的做法是只刷新第二行，但为了简洁，我们重建整个屏幕
            oled.fill(0)
            oled.text("Hello, World!", 0, 0)
            oled.text("Count: {}".format(press_count), 0, 20)
            oled.show()
            update_display = False

        sleep(1)   # 1秒闪烁一次
    except KeyboardInterrupt:
        break

# 退出时关闭 LED
led.off()
oled.fill(0)
oled.show()
print("程序结束。")