def on_pin_pressed_p0():
    global total
    total = num1 - num2
    basic.show_number(total)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global num1
    num1 += 1
    basic.show_number(num1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global total
    total = num1 / num2
    basic.show_number(total)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    global total
    total = num1 + num2
    basic.show_number(total)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global num2
    num2 += 1
    basic.show_number(num2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global total
    total = num1 * num2
    basic.show_number(total)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    global num1, num2, total
    num1 = 0
    num2 = 0
    total = 0
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

total = 0
num2 = 0
num1 = 0
num1 = 0
num2 = 0
total = 0