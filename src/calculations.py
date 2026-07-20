"""Pure calculation functions used by the Materials Calculator interface."""

import math
from typing import Literal

PressureUnit = Literal["MPa", "GPa"]


def _require_finite_positive(value: float, name: str) -> None:
    """Raise ``ValueError`` when a value is not finite and strictly positive."""
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a positive, finite number.")


def calculate_density(mass_g: float, volume_cm3: float) -> float:
    """Return density in g/cm³ from mass in g and volume in cm³."""
    _require_finite_positive(mass_g, "Mass")
    _require_finite_positive(volume_cm3, "Volume")
    return mass_g / volume_cm3


def calculate_porosity(measured_density: float, theoretical_density: float) -> float:
    """Return theoretical porosity as a percentage.

    Measured density must not be greater than theoretical density because that
    would produce a negative porosity for this simplified model.
    """
    _require_finite_positive(measured_density, "Measured density")
    _require_finite_positive(theoretical_density, "Theoretical density")
    if measured_density > theoretical_density:
        raise ValueError("Measured density cannot be greater than theoretical density.")
    return (1 - measured_density / theoretical_density) * 100


def convert_pressure(
    value: float, from_unit: PressureUnit, to_unit: PressureUnit
) -> float:
    """Convert a non-negative pressure value between MPa and GPa."""
    if not math.isfinite(value) or value < 0:
        raise ValueError("Pressure must be a non-negative, finite number.")
    if from_unit == to_unit:
        return value
    if from_unit == "MPa" and to_unit == "GPa":
        return value / 1000
    if from_unit == "GPa" and to_unit == "MPa":
        return value * 1000
    raise ValueError("Units must be 'MPa' or 'GPa'.")
