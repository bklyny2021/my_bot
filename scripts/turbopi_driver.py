"""
turbopi_driver.py — Custom driver for the HiWonder TurboPi AI Vision Robot (Raspberry Pi 5).

Custom code written for Boo's TurboPi. Talks to the HiWonder serial board
(UART) using the standard HiWonder protocol:

    FF 55 [device] [command] [data...] [checksum]

Checksum = low byte of the sum of all bytes after 0xFF 0x55.
"""

import serial
import time

# Device IDs (HiWonder standard)
DEV_SERVO = 0x01
DEV_MOTOR = 0x02
DEV_RGB = 0x04
DEV_BUZZER = 0x06
DEV_ULTRASONIC = 0x07
DEV_IR = 0x08

# Commands
CMD_GET = 0x01
CMD_SET = 0x02
CMD_RUN = 0x03
CMD_STOP = 0x04

# Motor indices (mecanum layout)
MOTOR_FL = 1
MOTOR_FR = 2
MOTOR_RL = 3
MOTOR_RR = 4


class TurboPi:
    def __init__(self, port="/dev/ttyAMA0", baud=115200, timeout=0.1):
        self.ser = serial.Serial(port, baud, timeout=timeout)

    def _send(self, device, command, data):
        frame = bytes([0xFF, 0x55, device, command]) + bytes(data)
        checksum = sum(frame[2:]) & 0xFF
        self.ser.write(frame + bytes([checksum]))

    def _read(self, n=8):
        return self.ser.read(n)

    # ---- Motors (mecanum drive) ----
    def set_motor(self, index, speed):
        """speed: -100..100"""
        speed = max(-100, min(100, int(speed)))
        self._send(DEV_MOTOR, CMD_SET, [index, speed & 0xFF])

    def drive(self, fl, fr, rl, rr):
        """Set all four wheels at once."""
        for idx, s in ((MOTOR_FL, fl), (MOTOR_FR, fr), (MOTOR_RL, rl), (MOTOR_RR, rr)):
            self.set_motor(idx, s)

    def stop(self):
        self.drive(0, 0, 0, 0)

    # ---- Pan-tilt camera head ----
    def set_servo(self, index, angle):
        """angle: 0..180 (servo 1 = pan, servo 2 = tilt)"""
        angle = max(0, min(180, int(angle)))
        self._send(DEV_SERVO, CMD_SET, [index, angle])

    def look(self, pan, tilt):
        self.set_servo(1, pan)
        self.set_servo(2, tilt)

    # ---- Sensors ----
    def read_ultrasonic(self):
        self._send(DEV_ULTRASONIC, CMD_GET, [])
        time.sleep(0.05)
        data = self._read(4)
        if len(data) >= 4:
            return (data[2] << 8) | data[3]
        return -1

    def read_ir(self):
        """Line-follower IR array: list of 5 booleans (True = line detected)."""
        self._send(DEV_IR, CMD_GET, [])
        time.sleep(0.05)
        data = self._read(8)
        if len(data) >= 8:
            return [bool(data[2 + i]) for i in range(5)]
        return [False] * 5

    # ---- Effects ----
    def set_rgb(self, r, g, b):
        self._send(DEV_RGB, CMD_SET, [r, g, b])

    def beep(self, freq=1000, duration=0.1):
        self._send(DEV_BUZZER, CMD_RUN, [freq & 0xFF, (freq >> 8) & 0xFF, int(duration * 1000) & 0xFF])
        time.sleep(duration)
        self._send(DEV_BUZZER, CMD_STOP, [])

    def close(self):
        self.stop()
        self.ser.close()
