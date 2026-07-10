"""Page Object de la pantalla de checkout de SauceDemo."""

from __future__ import annotations

from playwright.sync_api import Page


class CheckoutPage:
    """Representa la pantalla inicial del checkout."""

    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page) -> None:
        self.page = page

        # Locators centralizados del formulario de envío.
        self._first_name = page.locator('[data-test="firstName"]')
        self._last_name = page.locator('[data-test="lastName"]')
        self._postal_code = page.locator('[data-test="postalCode"]')
        self._continue_btn = page.locator('[data-test="continue"]')
        self._error_msg = page.locator('[data-test="error"]')

    def fill_shipping(
        self,
        first: str,
        last: str,
        zip_code: str,
    ) -> "CheckoutPage":
        """Completa los datos de envío y devuelve self para encadenar métodos."""
        self._first_name.fill(first)
        self._last_name.fill(last)
        self._postal_code.fill(zip_code)
        return self

    def continue_to_overview(self) -> "CheckoutPage":
        """Continúa hacia el resumen de la compra."""
        self._continue_btn.click()
        return self

    def has_error(self) -> bool:
        """Devuelve True si el formulario muestra un mensaje de error."""
        return self._error_msg.is_visible()