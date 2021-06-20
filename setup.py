#setup.py cannot be run. please call via terminal or autorun.inf
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'speechrecognition', 'playsound', 'gtts', 'pillow', 'pyautogui', 'pyttsx3', 'bs4', 'pyaudio', 'pyjokes', 'playsound'])