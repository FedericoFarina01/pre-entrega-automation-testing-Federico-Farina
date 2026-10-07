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


def obtener_productos(driver):
    """Lista las tarjetas de productos del inventario."""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    return driver.find_elements(By.CLASS_NAME, "inventory_item")


def obtener_primer_producto(driver):
    """Nombre y precio del primer producto del inventario."""
    producto = obtener_productos(driver)[0]
    nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    return nombre, precio


def elementos_interfaz_visibles(driver):
    """True si el menú hamburguesa y el filtro de ordenamiento están visibles."""
    menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "react-burger-menu-btn"))
    )
    filtro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )
    return menu.is_displayed() and filtro.is_displayed()


def agregar_producto_al_carrito(driver):
    """Agrega el primer producto al carrito."""
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(@id,'add-to-cart')])[1]")
        )
    )
    boton.click()


def obtener_contador_carrito(driver):
    """Espera el badge del carrito y devuelve su valor."""
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    return badge.text


def ir_al_carrito(driver):
    """Abre el carrito de compras."""
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))


def obtener_producto_en_carrito(driver):
    """Nombre y precio del primer producto en el carrito."""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    return nombre, precio
