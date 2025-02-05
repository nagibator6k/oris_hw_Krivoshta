import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QTimer, Qt

from ui_main import Ui_MainWindow

# ДЗ
#
# №1 - реализовать столкновение игрока с врагом (-> останавливаем игру, и пишем на весь экран "Loser")
# №2 - постановка а паузу (пр нажатии на escape ига ставится на паузу, то есть скорость игрок, врагв и
# бэкграунда равна 0, а также пишем на весь экран "Pause", при повторном нажатии на escape игра продолжается)

class AnimationHandler:
    def __init__(self, bg1: QLabel, bg2: QLabel, player: QLabel, rocket: QLabel):
        self.bg1 = bg1
        self.bg2 = bg2
        self.player = player
        self.rocket = rocket
        self.bg1_animation = None
        self.bg2_animation = None
        self.rocket_animation = None
        self.jump_direction = 1 # 1 - вверх, -1 - вниз
        self.is_jumping = False
        self.jump_height = 100
        self.speed = 5
        self.timer = QTimer()
        self.paused = False

    def start_bg_animation(self):
        self.bg1_animation = QPropertyAnimation(self.bg1, b"pos")
        self.bg1_animation.setStartValue(QPoint(0,0))
        self.bg1_animation.setEndValue(QPoint(-463, 0))
        self.bg1_animation.setDuration(5000)
        self.bg1_animation.setEasingCurve(QEasingCurve.Linear)
        self.bg1_animation.setLoopCount(-1)

        self.bg2_animation = QPropertyAnimation(self.bg2, b"pos")
        self.bg2_animation.setStartValue(QPoint(463, 0))
        self.bg2_animation.setEndValue(QPoint(0, 0))
        self.bg2_animation.setDuration(5000)
        self.bg2_animation.setEasingCurve(QEasingCurve.Linear)
        self.bg2_animation.setLoopCount(-1)

        self.bg1_animation.start()
        self.bg2_animation.start()

    def start_rocket_animation(self):
        self.rocket_animation = QPropertyAnimation(self.rocket, b"pos")
        self.rocket_animation.setStartValue(QPoint(500, 200))
        self.rocket_animation.setEndValue(QPoint(-50, 200))
        self.rocket_animation.setDuration(3500)
        self.rocket_animation.setEasingCurve(QEasingCurve.Linear)
        self.rocket_animation.setLoopCount(-1)

        self.rocket_animation.start()

    def move_player(self, direction):
        if self.paused:
            return
        current_pos = self.player.pos()
        if direction == 'left' and current_pos.x() > 0:
            self.player.move(current_pos.x() - self.speed, current_pos.y())
        elif direction == 'right' and current_pos.x() < 200:
            self.player.move(current_pos.x() + self.speed, current_pos.y())

    def jump_player(self):
        if self.paused:
            return
        elif not self.is_jumping:
            self.is_jumping = True
            self.timer.timeout.connect(self.handle_jump)
            self.timer.start(30)

    def handle_jump(self):
        current_pos = self.player.pos()

        if self.jump_direction == 1 and current_pos.y() <= 200 - self.jump_height:
            self.jump_direction = -1
        elif self.jump_direction == -1 and current_pos.y() > 160:
            self.jump_direction = 1
            self.is_jumping = False
            self.timer.stop()
            self.timer.timeout.disconnect(self.handle_jump)

        self.player.move(current_pos.x(), current_pos.y() - (self.speed * self.jump_direction))

    def pause(self):
        self.paused = not self.paused
        if self.paused:
            self.bg1_animation.pause()
            self.bg2_animation.pause()
            self.rocket_animation.pause()
        else:
            self.bg1_animation.resume()
            self.bg2_animation.resume()
            self.rocket_animation.resume()

    def collision(self):
        if self.player.geometry().intersects(self.rocket.geometry()):
            return True
        return False


class OurApplication(QMainWindow):
    def __init__(self):
        super(OurApplication, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("OUR GAME")
        self.animation_handler = AnimationHandler(self.ui.bg1, self.ui.bg2, self.ui.player, self.ui.rocket)
        self.is_game_over = False
        self.pause_label = QLabel(self)
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_game)
        self.update_timer.start(16)

    def start_animations(self):
        self.animation_handler.start_bg_animation()
        self.animation_handler.start_rocket_animation()

    def update_game(self):
        if self.animation_handler == False or self.is_game_over:
            return

        if self.animation_handler.collision():
            self.is_game_over = True
            self.animation_handler = False
            self.show_message("Loser")

    def show_message(self, text):
        self.pause_label.setText(text)
        self.pause_label.setStyleSheet("font-size: 300px; color: black;")# на весь экран, при желании
        self.pause_label.setStyleSheet("font-size: 52px; color: black;")
        self.pause_label.setAlignment(Qt.AlignCenter)
        self.pause_label.setGeometry(self.rect())
        self.pause_label.show()

    def hide_message(self):  # скрывает текст
        self.pause_label.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.animation_handler.move_player('left')
        elif event.key() == Qt.Key_Right:
            self.animation_handler.move_player('right')
        elif event.key() == Qt.Key_Space:
            self.animation_handler.jump_player()
        elif event.key() == Qt.Key_Escape:
            self.animation_handler.pause()
            if self.animation_handler.paused:
                self.show_message("Pause")
            else:
                self.hide_message()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OurApplication()
    window.show()

    window.start_animations()

    sys.exit(app.exec())