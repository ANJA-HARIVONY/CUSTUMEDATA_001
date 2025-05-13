import reflex as rx

class Item(rx.Model, Table=True):
    """The item class."""

    pipeline: str
    status: str
    workflow: str
    timestamp: str
    duration: str
