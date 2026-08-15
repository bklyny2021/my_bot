# my_bot — HiWonder TurboPi AI Vision Robot (Raspberry Pi 5)

**Custom code for Boo's TurboPi** — the 4-wheel mecanum AI vision rover with pan-tilt camera, line-follower IR array, ultrasonic sensor, RGB LEDs, and buzzer, running on a Raspberry Pi 5.

## What's inside

| Path | Description |
|------|-------------|
| `description/turbopi.urdf.xacro` | **Custom URDF** matching the real hardware: chassis, Pi 5, pan-tilt camera, 4 mecanum wheels, IR array, ultrasonic |
| `description/robot.urdf.xacro` | Stock ROS 2 starter (kept for reference) |
| `scripts/turbopi_driver.py` | **Custom driver** — serial protocol (FF 55 + device + cmd + data + checksum) for motors, servos, sensors, RGB, buzzer |
| `scripts/turbopi_control.py` | **Custom console** — WASD drive, pan/tilt camera, sensor reads |
| `docs/FLASHING.md` | **Custom guide** — which image to flash on the Pi 5 + first-boot setup |
| `images/` | Official HiWonder TurboPi product photos |
| `launch/rsp.launch.py` | ROS 2 launch (robot_state_publisher) |
| `worlds/empty.world` | Empty Gazebo world |

## Quick start (on the robot)

```bash
cd ~/my_bot
pip3 install pyserial
python3 scripts/turbopi_control.py
```

Controls: `w/a/s/d` drive · `q/e` spin · `i/k` pan · `j/l` tilt · `u` ultrasonic · `r` IR · `space` stop · `x` exit

## Flashing the Pi 5

See **`docs/FLASHING.md`** — use the **official HiWonder TurboPi system image for Raspberry Pi 5** (stock Raspberry Pi OS won't drive the robot).

## ROS 2 (optional)

```bash
cd ~/ros2_ws/src && git clone https://github.com/bklyny2021/my_bot.git
cd ~/ros2_ws && colcon build --packages-select my_bot
source install/setup.bash
ros2 launch my_bot rsp.launch.py
```

## Hardware

- **Brain:** Raspberry Pi 5
- **Drive:** 4× DC motors, mecanum wheels (omnidirectional)
- **Vision:** 120° wide-angle camera on 2-servo pan-tilt head
- **Sensors:** 5-channel IR line follower, ultrasonic
- **Effects:** RGB LEDs, buzzer
- **Interface:** UART serial (115200 baud, HiWonder protocol)

## License

Apache-2.0 — see `LICENSE.md`.
