import pytest
from selenium import webdriver
from utils.funciones_auxiliares import realizar_login, esperar_url, obtener_titulo


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_01_login_exitoso(driver):
    "Login con credenciales válidas y validación de /inventory.html y 'Products'"
    realizar_login(driver)

    url = esperar_url(driver, "/inventory.html")
    assert "/inventory.html" in url, f"Esperaba /inventory.html, pero la URL es: {url}"

    titulo = obtener_titulo(driver)
    assert titulo == "Products", f"Esperaba título 'Products', pero se obtuvo: {titulo}"
