input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        . . . . .
        # # # # .
        . # # # #
        # # # # #
        . # . # .
        `)
})
basic.showLeds(`
    . . . . .
    # # # # #
    . . . . .
    # # # # #
    . . . . .
    `)
led.plot(0, 0)
led.unplot(0, 0)
basic.showLeds(`
    . . . . .
    # # . # #
    . . # . .
    . # # # .
    . . . . .
    `)
