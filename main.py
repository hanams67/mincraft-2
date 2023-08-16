def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        # # # # .
        . # # # #
        # # # # #
        . # . # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_leds("""
    . . . . .
    # # # # #
    . . . . .
    # # # # #
    . . . . .
    """)
led.plot(0, 0)
led.unplot(0, 0)
basic.show_leds("""
    . . . . .
    # # . # #
    . . # . .
    . # # # .
    . . . . .
    """)
    