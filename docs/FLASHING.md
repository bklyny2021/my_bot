# 🖥️ Flashing the Raspberry Pi 5 for TurboPi

**Custom setup guide for Boo's HiWonder TurboPi (Raspberry Pi 5).**

## What you need

- Raspberry Pi 5 (8GB recommended)
- MicroSD card (32GB+ recommended, Class 10 / A2)
- Card reader
- **Raspberry Pi Imager** — free, from https://www.raspberrypi.com/software/

## The image to use

> ⚠️ **Use the official HiWonder TurboPi system image** — it comes pre-loaded with the HiWonder software stack (motor/servo/sensor drivers, camera tools, and their demos). A stock Raspberry Pi OS image will NOT drive the robot out of the box.

**Where to get it:**
1. Go to **https://www.hiwonder.com** → find the **TurboPi** product page
2. Look for the **"Download" / "Wiki" / "System Image"** section (the wiki is at `wiki.hiwonder.com` — if it's down, check the product page or contact HiWonder support for the image link)
3. Download the **TurboPi system image for Raspberry Pi 5** (NOT the Pi 4B image — the Pi 5 image is the one you need)

> If you can't find the image link, email HiWonder support (support@hiwonder.com) and ask for the **TurboPi Raspberry Pi 5 system image download link** — they'll send it.

## Flash it (Raspberry Pi Imager)

1. Open **Raspberry Pi Imager**
2. Click **Choose OS** → **Use custom** → select the downloaded TurboPi `.img` / `.img.xz` file
3. Click **Choose Storage** → select your SD card
4. Click **Next** — when asked, choose **"Edit settings"** and set:
   - **Username:** `pi` (or whatever HiWonder's image expects — check their docs)
   - **Password:** something you'll remember
   - **Wi-Fi:** your network name + password (so the robot can connect)
   - **Enable SSH:** tick it (you'll need SSH to control the robot)
5. Click **Save** → **Yes** to write
6. Wait for the write + verify to finish, then put the SD card in the Pi 5

## First boot

1. Power the robot on (battery switch on the chassis)
2. Wait ~1-2 minutes for first boot
3. Find its IP: check your router's DHCP list, or scan with `nmap -sn 192.168.1.0/24`
4. SSH in:
   ```bash
   ssh pi@<robot-ip>
   ```
5. Test the robot:
   ```bash
   cd ~/TurboPi   # or wherever HiWonder's code lives
   python3 demo/motor_demo.py   # wheels should spin
   ```

## After flashing — install this repo's custom code

```bash
cd ~
git clone https://github.com/bklyny2021/my_bot.git
cd my_bot
pip3 install pyserial
# Test the driver:
python3 scripts/turbopi_control.py
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| SSH refused | Enable SSH in Imager settings, or `sudo raspi-config` → Interface Options → SSH |
| Motors don't respond | Check the battery switch + charge; check the serial port is `ttyAMA0` (run `ls /dev/ttyAMA*`) |
| Camera not working | `sudo raspi-config` → Interface Options → Camera → Enable, then reboot |
| Serial permission denied | `sudo usermod -aG dialout pi` then log out/in |
