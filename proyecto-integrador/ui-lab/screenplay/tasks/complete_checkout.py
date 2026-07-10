"""Task: CompleteCheckout — completa los datos iniciales del checkout."""

from __future__ import annotations

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from screenplay.abilities.browse_web import BrowseTheWeb


class CompleteCheckout:
    """Tarea de negocio para iniciar y completar los datos del checkout."""

    def __init__(
        self,
        first: str,
        last: str,
        zip_code: str,
    ) -> None:
        self._first = first
        self._last = last
        self._zip_code = zip_code

    @classmethod
    def with_info(
        cls,
        first: str,
        last: str,
        zip_code: str,
    ) -> "CompleteCheckout":
        """Constructor expresivo para usar desde el Actor."""
        return cls(first, last, zip_code)

    def perform_as(self, actor) -> None:
        """Ejecuta el flujo de checkout usando la Ability del Actor."""
        page = actor.ability_to(BrowseTheWeb).page

        InventoryPage(page).go_to_cart()
        CartPage(page).proceed_to_checkout()

        CheckoutPage(page) \
            .fill_shipping(
                self._first,
                self._last,
                self._zip_code,
            ) \
            .continue_to_overview()