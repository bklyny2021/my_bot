"""
turbopi_control.py — Custom control console for the HiWonder TurboPi (Pi 5).

Custom code written for Boo's TurboPi. Interactive console:
  w/a/s/d  — drive (mecanum)
  q/e      — spin left/right
  i/k      — camera pan
  j/l      — camera tilt
  u        — ultrasonic reading
  r        — IR line sensors
  space    — stop
  x        — exit
"""

import time
import sys
import tty
import termios

from turbopi_driver import TurboPi


def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch


def main():
    bot = TurboPi()
    pan, tilt = 90, 90
    bot.look(pan, tilt)
    print("TurboPi control — w/a/s/d drive, q/e spin, i/k pan, j/l tilt, u ultrasonic, r IR, space stop, x exit")

    try:
        while True:
            k = get_key().lower()
            if k == "x":
                break
            elif k == "w":
                bot.drive(100, 100, 100, 100)
            elif k == "s":
                bot.drive(-100, -100, -100, -100)
            elif k == "a":
                bot.drive(-100, 100, -100, 100)   # strafe left (mecanum)
            elif k == "d":
                bot.drive(100, -100, 100, -100)   # strafe right (mecanum)
            elif k == "q":
                bot.drive(-100, 100, 100, -100)   # spin left
            elif k == "e":
                bot.drive(100, -100, -100, 100)   # spin right
            elif k == " ":
                bot.stop()
            elif k == "i":
                pan = min(180, pan + 10); bot.look(pan, tilt)
            elif k == "k":
                pan = max(0, pan - 10); bot.look(pan, tilt)
            elif k == "j":
                tilt = min(180, tilt + 10); bot.look(pan, tilt)
            elif k == "l":
                tilt = max(0, tilt - 10); bot.look(pan, tilt)
            elif k == "u":
                print(f"ultrasonic: {bot.read_ultrasonic()} cm")
            elif k == "r":
                print(f"IR: {bot.read_ir()}")
    except KeyboardInterrupt:
        pass
    finally:
        bot.stop()
        bot.close()
        print("\nbye")


if __name__ == "__main__":
    main()
