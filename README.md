# 🛡️ Shelby Firewall

> 🚀 Project 6 of the Sutra AI Cybersecurity Suite  
> Created by [@sangeeth00712](https://github.com/sangeeth00712)

---

## 🔥 Overview

**Shelby Firewall** is a custom-built, Python-powered GUI firewall system designed for Linux environments.  
It’s part of the `Sutra AI` Cybersecurity Suite, focused on giving users a clear visual interface to manage system defenses like IP blocking, resource monitoring, and firewall control — all in real-time.

---

## ✨ Features

✅ Real-time display of:
- CPU usage (%)
- RAM usage (%)
- Network IP address (auto-refreshes every 10 seconds)

✅ Firewall GUI Controls:
- Add/Remove IPs to blocklist or allowlist  
- Apply or reset firewall rules  
- Uses native Linux `iptables` backend  

✅ System Friendly:
- Lightweight Python-based architecture  
- Auto-detects environment and adapts  
- Includes a `.desktop` launcher file for easy access on Linux

---

## 🖼️ GUI Preview

![Shelby Firewall GUI](assets/gui_screenshot.png)

---

## 📁 Project Structure
ShelbyFirewall/
├── assets/ # GUI icons/images
├── shelbyfirewall_gui.py # Main Python GUI
├── run_shelbyfirewall.sh # Shell script to launch
├── ShelbyFirewall.desktop # Linux desktop shortcut
├── requirements.txt # Dependencies
└── README.md  


---

## 🛠️ Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/sangeeth00712/ShelbyFirewall.git
cd ShelbyFirewall

 2. Set up the Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. How to Run

Option 1 — Using Run Script:
bash run_shelbyfirewall.sh

Option 2 — Directly with Python:
python3 shelbyfirewall

4.🧪 Tested On
✅ Ubuntu 22.04 LTS

✅ Python 3.10+

✅ GNOME Desktop

✅ Requires root privileges for iptables

5.Technologies Used
Python 3

Tkinter – for GUI

psutil – system resource stats

socket, os, subprocess

Linux iptables

6. License
This project is released under the MIT License.

7.🤝 Credits
Built by Mr. Shelby (sangeeth thumuganti)


