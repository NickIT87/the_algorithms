
import pyray as rl


def main():
    # Инициализация окна
    screen_width = 800
    screen_height = 450

    rl.init_window(
        screen_width,
        screen_height,
        "raylib [core] example - input keys"
    )

    # Начальная позиция мяча
    ball_position = rl.Vector2(
        screen_width / 2,
        screen_height / 2
    )

    # Ограничение FPS
    rl.set_target_fps(60)

    # Главный игровой цикл
    while not rl.window_should_close():

        # Update: обработка нажатий клавиш
        if rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
            ball_position.x += 2.0

        if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
            ball_position.x -= 2.0

        if rl.is_key_down(rl.KeyboardKey.KEY_UP):
            ball_position.y -= 2.0

        if rl.is_key_down(rl.KeyboardKey.KEY_DOWN):
            ball_position.y += 2.0

        # Draw: отрисовка
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)

        rl.draw_text(
            "move the ball with arrow keys",
            10, 10, 20,
            rl.DARKGRAY
        )

        rl.draw_circle_v(
            ball_position,
            50,
            rl.MAROON
        )

        rl.end_drawing()

    # Закрытие окна
    rl.close_window()


if __name__ == "__main__":
    main()
