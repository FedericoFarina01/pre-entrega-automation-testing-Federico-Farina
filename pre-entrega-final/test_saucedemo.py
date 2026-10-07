import pytest
from selenium import webdriver
from utils.funciones_auxiliares import (
    realizar_login,
    esperar_url,
    obtener_titulo,
    obtener_productos,
    obtener_primer_producto,
    elementos_interfaz_visibles,
)


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


def test_02_verificacion_catalogo(driver):
    "Valida título, presencia de productos, datos del primero y elementos de interfaz"
    realizar_login(driver)

    titulo = obtener_titulo(driver)
    assert titulo == "Products", f"Esperaba título 'Products', pero se obtuvo: {titulo}"

    productos = obtener_productos(driver)
    assert len(productos) > 0, "No se encontraron productos visibles"

    nombre, precio = obtener_primer_producto(driver)
    print(f"Primer producto: {nombre} | Precio: {precio}")
    assert nombre != "", "El nombre del primer producto está vacío"
    assert precio != "", "El precio del primer producto está vacío"

    assert elementos_interfaz_visibles(driver), "El menú o el filtro no están visibles"
