import logging
import os
import pytest

_logger = logging.getLogger()
if not any(getattr(h, "baseFilename", None) == os.path.abspath("ejecucion.log") for h in _logger.handlers):
    _handler = logging.FileHandler("ejecucion.log")
    _handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    _logger.addHandler(_handler)
_logger.setLevel(logging.INFO)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    if reporte.when == "call":
        logging.info(f"{item.name}: {reporte.outcome}")
        if reporte.failed:
            driver = item.funcargs.get("driver")
            if driver:
                driver.save_screenshot(f"screenshot_{item.name}.png")
                logging.info(f"{item.name}: captura guardada en screenshot_{item.name}.png")