from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def realizar_login(driver, username="standard_user", password="secret_sauce"):
    """Ingresar con credenciales válidas."""
    driver.get("https://www.saucedemo.com/")
    usuario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    usuario.send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def esperar_url(driver, fragmento):
    WebDriverWait(driver, 10).until(EC.url_contains(fragmento))
    return driver.current_url


def obtener_titulo(driver):
    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.header_secondary_container .title")
        )
    )
    return titulo.text
