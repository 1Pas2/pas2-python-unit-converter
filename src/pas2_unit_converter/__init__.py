import math

_UNITS = {
    "m": ("length", 1.0, 0.0),
    "km": ("length", 1000.0, 0.0),
    "cm": ("length", 0.01, 0.0),
    "in": ("length", 0.0254, 0.0),
    "ft": ("length", 0.3048, 0.0),
    "kg": ("mass", 1.0, 0.0),
    "g": ("mass", 0.001, 0.0),
    "lb": ("mass", 0.45359237, 0.0),
    "K": ("temperature", 1.0, 0.0),
    "C": ("temperature", 1.0, 273.15),
    "F": ("temperature", 5 / 9, 255.3722222222222),
}


def convert(value: float, source: str, target: str) -> float:
    if source not in _UNITS or target not in _UNITS:
        raise ValueError("Unknown unit")
    a, b = _UNITS[source], _UNITS[target]
    if a[0] != b[0] or not math.isfinite(value):
        raise ValueError("Incompatible units or non-finite value")
    base = value * a[1] + a[2]
    if a[0] == "temperature" and base < -1e-10:
        raise ValueError("Below absolute zero")
    result = (base - b[2]) / b[1]
    if not math.isfinite(result):
        raise OverflowError("Conversion overflow")
    return result
