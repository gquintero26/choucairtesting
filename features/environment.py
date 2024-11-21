from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import pyautogui
from pathlib import Path

def before_all(context):
    # Configure PyAutoGUI settings
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1
    
    # Setup Firefox driver
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)
    context.driver.maximize_window()
    
    # Ensure file directory exists
    Path('file').mkdir(exist_ok=True)

def after_all(context):
    context.driver.quit()