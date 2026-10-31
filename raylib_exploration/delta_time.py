
import pyray as rl


def main():
    # Initialization
    screen_width = 800
    screen_height = 450

    rl.init_window(
        screen_width,
        screen_height,
        "raylib [core] example - delta time"
    )

    current_fps = 60

    # Store the position for both circles
    delta_circle = rl.Vector2(0, screen_height / 3.0)
    frame_circle = rl.Vector2(0, screen_height * (2.0 / 3.0))

    # Speed applied to both circles
    speed = 10.0
    circle_radius = 32.0

    rl.set_target_fps(current_fps)

    # Main game loop
    while not rl.window_should_close():

        # Update
        # --------------------------------------------

        # Adjust FPS target using mouse wheel
        mouse_wheel = rl.get_mouse_wheel_move()

        if mouse_wheel != 0:
            current_fps += int(mouse_wheel)

            if current_fps < 0:
                current_fps = 0

            rl.set_target_fps(current_fps)

        # Move circles
        delta_circle.x += rl.get_frame_time() * 6.0 * speed
        frame_circle.x += 0.1 * speed

        # Reset circles when they leave the screen
        if delta_circle.x > screen_width:
            delta_circle.x = 0

        if frame_circle.x > screen_width:
            frame_circle.x = 0

        # Reset both circles
        if rl.is_key_pressed(rl.KeyboardKey.KEY_R):
            delta_circle.x = 0
            frame_circle.x = 0

        # Draw
        # --------------------------------------------

        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)

        # Draw circles
        rl.draw_circle_v(
            delta_circle,
            circle_radius,
            rl.RED
        )

        rl.draw_circle_v(
            frame_circle,
            circle_radius,
            rl.BLUE
        )

        # FPS information
        if current_fps <= 0:
            fps_text = f"FPS: unlimited ({rl.get_fps()})"
        else:
            fps_text = f"FPS: {rl.get_fps()} (target: {current_fps})"

        rl.draw_text(fps_text, 10, 10, 20, rl.DARKGRAY)

        rl.draw_text(
            f"Frame time: {rl.get_frame_time() * 1000:.2f} ms",
            10, 30, 20, rl.DARKGRAY
        )

        rl.draw_text(
            "Use the scroll wheel to change the fps limit, r to reset",
            10, 50, 20, rl.DARKGRAY
        )

        # Text above circles
        rl.draw_text(
            "FUNC: x += GetFrameTime() * speed",
            10, 90, 20, rl.RED
        )

        rl.draw_text(
            "FUNC: x += speed",
            10, 240, 20, rl.BLUE
        )

        rl.end_drawing()

    # De-initialization
    rl.close_window()


if __name__ == "__main__":
    main()
