import machine
import time

led_red = [machine.Pin(3, machine.Pin.OUT), machine.Pin(7, machine.Pin.OUT), machine.Pin(12, machine.Pin.OUT), machine.Pin(6, machine.Pin.OUT)]
led_yellow = [machine.Pin(1, machine.Pin.OUT), machine.Pin(15, machine.Pin.OUT), machine.Pin(11, machine.Pin.OUT), machine.Pin(5, machine.Pin.OUT)]
led_green = [machine.Pin(0, machine.Pin.OUT), machine.Pin(14, machine.Pin.OUT), machine.Pin(10, machine.Pin.OUT), machine.Pin(26, machine.Pin.OUT)]


i = 0
while True:
    if i % 2 == 0:
        led_red[2].value(1)
        led_red[0].value(1)
        led_yellow[1].value(1)
        led_yellow[3].value(1)
        time.sleep(0.5)
        led_yellow[1].value(0)
        led_yellow[3].value(0)
        time.sleep(0.5)
        led_green[1].value(1)
        led_green[3].value(1)
        time.sleep(0.5)
    else:
        led_red[1].value(1)
        led_red[3].value(1)
        led_yellow[2].value(1)
        led_yellow[0].value(1)
        time.sleep(0.5)
        led_yellow[2].value(0)
        led_yellow[0].value(0)
        time.sleep(0.5)
        led_green[2].value(1)
        led_green[0].value(1)
        time.sleep(0.5)

    time.sleep(1)

    if i % 2 == 0:
        led_red[2].value(0)
        led_red[0].value(0)
        led_green[1].value(0)
        led_green[3].value(0)
        time.sleep(0.2)
    else:
        led_red[1].value(0)
        led_red[3].value(0)
        led_green[2].value(0)
        led_green[0].value(0)
        time.sleep(0.2)

    i = (i + 1) % 2