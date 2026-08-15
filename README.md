# my_bot — ROS 2 Robot Description Package

A starter **ROS 2** (Humble+) robot package: URDF robot description, launch files, and an empty simulation world. Fork it and rename to start your own robot project.

## What's inside

| Path | Description |
|------|-------------|
| `description/robot.urdf.xacro` | Robot model (URDF via xacro) — edit to define your robot's links, joints, and sensors |
| `launch/rsp.launch.py` | Launch file — starts the robot state publisher (publishes `/robot_description` + TF) |
| `config/empty.yaml` | Empty config placeholder (add your controller/param YAMLs here) |
| `worlds/empty.world` | Empty Gazebo world to start from |
| `CMakeLists.txt` / `package.xml` | Standard `ament_cmake` build files |

## Build & run

```bash
# From your ROS 2 workspace (e.g. ~/ros2_ws/src)
git clone <this-repo> my_bot
cd ~/ros2_ws && colcon build --packages-select my_bot
source install/setup.bash

# Launch the robot description
ros2 launch my_bot rsp.launch.py

# Verify TF is publishing
ros2 run tf2_tools view_frames
```

## Renaming the package

1. Rename the folder: `mv my_bot <your_robot_name>`
2. Update `package.xml` (name, description, maintainer, license)
3. Update `CMakeLists.txt` (project name)
4. Update the URDF and launch file references

## Requirements

- ROS 2 (Humble or newer)
- `colcon` build tools
- `xacro` (usually included with ROS 2 desktop install)
- Gazebo (optional, for the empty world)

## License

See `LICENSE.md`.
