import pytest
from selenium import webdriver
from utils.funciones_auxiliares import (
    realizar_login,
    esperar_url,
    obtener_titulo,
    obtener_productos,
    obtener_primer_producto,
    elementos_interfaz_visibles,
    agregar_producto_al_carrito,
    obtener_contador_carrito,
    ir_al_carrito,
    obtener_producto_en_carrito,
)


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
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


def test_03_producto_en_carrito(driver):
    "Agrega el primer producto, verifica el contador y que aparezca en el carrito"
    realizar_login(driver)

    nombre, precio = obtener_primer_producto(driver)

    agregar_producto_al_carrito(driver)

    contador = obtener_contador_carrito(driver)
    assert contador == "1", f"Esperaba contador '1', pero muestra: {contador}"

    ir_al_carrito(driver)

    nombre_carrito, precio_carrito = obtener_producto_en_carrito(driver)
    assert nombre_carrito == nombre, f"Esperaba '{nombre}', pero el carrito muestra: {nombre_carrito}"
    assert precio_carrito == precio, f"Esperaba '{precio}', pero el carrito muestra: {precio_carrito}"
