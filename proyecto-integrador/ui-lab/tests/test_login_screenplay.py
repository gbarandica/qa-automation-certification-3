"""Tests de login usando el patrón Screenplay.

Qué demuestra este archivo
--------------------------
1. Screenplay vs POM: el mismo flujo, pero narrado desde la perspectiva
   del usuario (Actor), no de la herramienta.
2. Composición de Tasks: attempts_to() acepta múltiples tareas en cadena.
3. Legibilidad de intención: "carlos intenta iniciar sesión como standard_user"
   es más expresivo que una secuencia de fill/click.

Cuándo usar Screenplay sobre POM
---------------------------------
- Tests con múltiples roles (admin + usuario regular en el mismo test).
- Flujos complejos donde nombrar al Actor clarifica el escenario.
- Equipos que trabajan con Gherkin / BDD y quieren alineación lenguaje↔código.
"""

from screenplay.actor import Actor
from screenplay.abilities.browse_web import BrowseTheWeb
from screenplay.tasks.login import Login
from screenplay.tasks.add_to_cart import AddToCart
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from screenplay.tasks.complete_checkout import CompleteCheckout
from pages.checkout_page import CheckoutPage


def test_actor_inicia_sesion_exitosamente(page):
    """Un Actor con BrowseTheWeb puede iniciar sesión en la aplicación."""
    carlos = Actor("Carlos").can(BrowseTheWeb.using(page))

    carlos.attempts_to(
        Login.as_user("standard_user", "secret_sauce"),
    )

    assert InventoryPage(page).is_loaded(), (
        "Carlos debería estar en el inventario tras el login."
    )


def test_actor_agrega_producto_al_carrito(page):
    """Un Actor puede iniciar sesión y agregar un producto al carrito."""
    ana = Actor("Ana").can(BrowseTheWeb.using(page))

    ana.attempts_to(
        Login.as_user("standard_user", "secret_sauce"),
        AddToCart.the_item("Sauce Labs Backpack"),
    )

    assert InventoryPage(page).cart_count() == 1, (
        "Ana debería tener 1 producto en el carrito."
    )


def test_actor_agrega_multiples_productos(page):
    """Un Actor puede agregar varios productos en una sola secuencia."""
    diego = Actor("Diego").can(BrowseTheWeb.using(page))

    diego.attempts_to(
        Login.as_user("standard_user", "secret_sauce"),
        AddToCart.the_item("Sauce Labs Backpack"),
        AddToCart.the_item("Sauce Labs Bike Light"),
    )

    assert InventoryPage(page).cart_count() == 2


def test_actor_verifica_carrito(page):
    """Un Actor puede navegar al carrito y verificar los productos agregados."""
    sofia = Actor("Sofía").can(BrowseTheWeb.using(page))

    sofia.attempts_to(
        Login.as_user("standard_user", "secret_sauce"),
        AddToCart.the_item("Sauce Labs Fleece Jacket"),
    )

    InventoryPage(page).go_to_cart()
    cart = CartPage(page)

    assert cart.is_loaded()
    assert cart.contains("Sauce Labs Fleece Jacket")

def test_actor_completa_checkout_sin_datos_y_obtiene_error(page):
    """Un Actor intenta continuar el checkout sin información de envío."""
    laura = Actor("Laura").can(BrowseTheWeb.using(page))

    laura.attempts_to(
        Login.as_user("standard_user", "secret_sauce"),
        AddToCart.the_item("Sauce Labs Backpack"),
        CompleteCheckout.with_info("", "", ""),
    )

    assert CheckoutPage(page).has_error(), (
        "Laura debería ver un error al continuar "
        "sin completar los datos de envío."
    )
