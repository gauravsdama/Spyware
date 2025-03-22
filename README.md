# Spyware Simulation for Educational Purposes

**DISCLAIMER:** This project is provided solely for educational and research purposes. Unauthorized use of these techniques is illegal and unethical. Use responsibly and only in environments where you have explicit permission.

## Overview

This Python project simulates various spyware functionalities by:
- Logging keystrokes using a keylogger.
- Gathering system information (e.g., hostname, IP address, system details).
- Capturing a screenshot of the current display.
- Recording audio from the microphone for a specified duration.

The project demonstrates how these features can be implemented with Python libraries such as `pynput`, `pyautogui`, `sounddevice`, and standard modules like `platform` and `socket`.

## Features

- **Keylogger:**  
  Captures and logs keystrokes to `keylogs.txt`.
  
- **System Information:**  
  Gathers system details (hostname, IP address, OS, version, architecture, processor) and writes them to `sysinfo.txt`.
  
- **Screenshot Capture:**  
  Takes a screenshot of the current screen and saves it as `screenshot.png`.
  
- **Audio Recording:**  
  Records 10 seconds of audio (mono, 16-bit, 44100 Hz) and saves it as `audio_recording.wav`.

## Requirements

- Python 3.x
- [pynput](https://pypi.org/project/pynput/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [sounddevice](https://pypi.org/project/sounddevice/)

*Note: Modules such as `platform`, `socket`, and `wave` are part of Python’s standard library.*

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/spyware-simulation.git
   cd spyware-simulation
