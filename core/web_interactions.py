from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_platform():
    driver = webdriver.Chrome()  # Asegúrate de tener el driver configurado
    try:
        driver.get("https://platform.bluemessaging.net/login.html")

        # Esperar hasta que el iframe esté disponible y cambiar al contexto
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe')))
        iframe = driver.find_element(By.XPATH, '//iframe')
        driver.switch_to.frame(iframe)

        # Interactuar con elementos dentro del iframe
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '__BVID__12')))
        element = driver.find_element(By.ID, '__BVID__12')
        element.send_keys("infonavit-rtsct")

        user = driver.find_element(By.ID, 'form-user')
        user.send_keys("act02_jct14")

        password = driver.find_element(By.ID, 'form-password')
        password.send_keys("Ux6jPoz26")
        
        button = driver.find_element(By.ID, 'button-login')
        driver.execute_script("arguments[0].click();", button)

        # Regresar al contenido principal
        driver.switch_to.default_content()

        print("Inicio de sesión exitoso.")

    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")

    # finally:
    #     # driver.quit()
