
import pyray as rl


def main():
    # Initialization
    screen_width = 800
    screen_height = 450

    rl.init_window(
        screen_width,
        screen_height,
        "raylib [core] example - input mouse wheel"
    )

    # Initial box position
    box_position_y = screen_height // 2 - 40

    # Scrolling speed in pixels
    scroll_speed = 4

    rl.set_target_fps(60)

    # Main game loop
    while not rl.window_should_close():

        # Update
        mouse_wheel = rl.get_mouse_wheel_move()

        box_position_y -= int(mouse_wheel * scroll_speed)

        # Draw
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)

        rl.draw_rectangle(
            screen_width // 2 - 40,
            box_position_y,
            80,
            80,
            rl.MAROON
        )

        rl.draw_text(
            "Use mouse wheel to move the cube up and down!",
            10, 10, 20, rl.GRAY
        )

        rl.draw_text(
            f"Box position Y: {box_position_y:03d}",
            10, 40, 20, rl.LIGHTGRAY
        )

        rl.end_drawing()

    # De-initialization
    rl.close_window()


if __name__ == "__main__":
    main()
