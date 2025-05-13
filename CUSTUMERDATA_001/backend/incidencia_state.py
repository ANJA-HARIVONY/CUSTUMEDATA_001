import csv
from pathlib import Path
from typing import List
import reflex as rx
from ..models.incidencias_model import Incidencia


class IncidenciasState(rx.State):
    """The Incidencias state class."""

    incidencias: List[Incidencia] = []

    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    total_incidencias: int = 0
    offset: int = 0
    limit: int = 12  # Number of rows per page

    @rx.var(cache=True)
    def filtered_sorted_incidencias(self) -> List[Incidencia]:
        incidencias = self.incidencias

        # Filter incidencias based on selected item
        if self.sort_value:
            incidencias = sorted(
                incidencias,
                key=lambda incidencia: str(getattr(incidencia, self.sort_value)).lower(),
                reverse=self.sort_reverse,
            )

        # Filter incidencias based on search value
        if self.search_value:
            search_value = self.search_value.lower()
            incidencias = [
                incidencia
                for incidencia in incidencias
                if any(
                    search_value in str(getattr(incidencia, attr)).lower()
                    for attr in [
                        "nombre",
                        "telefono",
                        "direccion",
                        "motivo",
                        "usuario",
                        "fecha",
                        "status",
                        "bitrix",
                    ]
                )
            ]
        return incidencias

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return (self.total_incidencias // self.limit) + (
            1 if self.total_incidencias % self.limit else 0
        )

    @rx.var(cache=True, initial_value=[])
    def get_current_page(self) -> list[Incidencia]:
        start_index = self.offset
        end_index = start_index + self.limit
        return self.filtered_sorted_incidencias[start_index:end_index]

    def prev_page(self):
        if self.page_number > 1:
            self.offset -= self.limit

    def next_page(self):
        if self.page_number < self.total_pages:
            self.offset += self.limit

    def first_page(self):
        self.offset = 0

    def last_page(self):
        self.offset = (self.total_pages - 1) * self.limit

    def load_entries(self):
        with Path("data_001.csv").open(encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.incidencias = [Incidencia(**row) for row in reader]
            self.total_incidencias = len(self.incidencias)

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()
