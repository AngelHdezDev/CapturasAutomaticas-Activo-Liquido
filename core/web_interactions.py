from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_to_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://platform.bluemessaging.net/login.html")
        time.sleep(2)  # Espera para cargar la página

        # Selección del input de dominio usando el placeholder
        # Usando By.CLASS_NAME
        element = driver.find_element(By.CLASS_NAME, "form-section__inputs")

     
        print("Campo de dominio llenado correctamente.", element)





    except Exception as e:
        print(f"Error: {e}")
