# Pre-Entrega de Projecto: Federico Farina

Automatización de flujos básicos de navegación web sobre [SauceDemo](https://www.saucedemo.com/) (Swag Labs) usando Selenium WebDriver y Pytest.

## Propósito

Aplicar los conocimientos de las clases 6 a 8 del curso de Automation Testing automatizando:

- **Login**: acceso con credenciales válidas y validación de la redirección al inventario.
- **Catálogo**: verificación del título, presencia de productos y elementos clave de la interfaz.
- **Carrito**: agregar un producto, validar el contador y confirmar el ítem en el carrito.

## Tecnologías

- Python 3
- Selenium WebDriver
- Pytest
- pytest-html (reporte HTML)
- Git y GitHub

## Estructura

```
├── pre-entrega-final/
│   ├── test_saucedemo.py              # Casos de prueba
│   └── utils/
│       └── funciones_auxiliares.py    # Funciones auxiliares de Selenium
├── requirements.txt
└── README.md
```

## Instalación

Clonar el repositorio y entrar a la carpeta:

```bash
git clone https://github.com/FedericoFarina01/pre-entrega-automation-testing-Federico-Farina.git
cd pre-entrega-automation-testing-Federico-Farina
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

```bash
pytest pre-entrega-final/test_saucedemo.py -v
```

## Generar el reporte HTML

```bash
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html
```

El reporte se genera en el archivo `reporte.html` en la raíz del proyecto.

## Evidencias

Ante un fallo, se guardan automáticamente una captura de pantalla y el log de ejecución en la raíz del proyecto.
