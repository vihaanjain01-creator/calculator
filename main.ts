input.onPinPressed(TouchPin.P0, function () {
    total = num1 - num2
    basic.showNumber(total)
})
input.onButtonPressed(Button.A, function () {
    num1 += 1
    basic.showNumber(num1)
})
input.onGesture(Gesture.TiltLeft, function () {
    total += num1 ** num2
    basic.showNumber(total)
})
input.onPinPressed(TouchPin.P2, function () {
    total = num1 / num2
    basic.showNumber(total)
})
input.onButtonPressed(Button.AB, function () {
    total = num1 + num2
    basic.showNumber(total)
})
input.onButtonPressed(Button.B, function () {
    num2 += 1
    basic.showNumber(num2)
})
input.onPinPressed(TouchPin.P1, function () {
    total = num1 * num2
    basic.showNumber(total)
})
input.onGesture(Gesture.Shake, function () {
    num1 = 0
    num2 = 0
    total = 0
    basic.clearScreen()
})
let total = 0
let num2 = 0
let num1 = 0
num1 = 0
num2 = 0
total = 0
