import reflex as rx


def _badge(status: str):
    badge_mapping = {
        "solucionada": ("check", "Solucionada", "green"),
        "pendiente": ("loader", "Pendiente", "yellow"),
        "tarea_creada": ("app-window", "Tarea Creada", "blue"),
    }
    icon, text, color_scheme = badge_mapping.get(
        status, ("loader", "Pending", "yellow")
    )
    return rx.badge(
        rx.icon(icon, size=16),
        text,
        color_scheme=color_scheme,
        radius="large",
        variant="surface",
        size="2",
    )


def status_badge(status: str):
    return rx.match(
        status,
        ("Solucionada", _badge("solucionada")),
        ("Pendiente", _badge("pendiente")),
        ("Tarea Creada", _badge("tarea_creada")),
        _badge("pendiente"),
    )
