"""The dashboard page."""

import reflex as rx

from ..backend.incidencia_state import IncidenciasState
from ..templates import template
from ..views.incidencias_table_view import main_table


@template(route="/incidencias", title="Incidencias", on_load=IncidenciasState.load_entries)
def incidencias() -> rx.Component:
    """The incidencias page.

    Returns:
        The UI for the Incidencias page.

    """
    return rx.vstack(
        rx.heading("Incidencias", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
