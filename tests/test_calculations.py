"""Unit tests for the pure calculation functions."""

import pytest

from src.calculations import (
    calculate_density,
    calculate_porosity,
    convert_pressure,
)


def test_density_calculation() -> None:
    """Density is mass divided by volume."""
    assert calculate_density(20.0, 4.0) == pytest.approx(5.0)


def test_density_rejects_zero_volume() -> None:
    """A zero volume cannot be used as a divisor."""
    with pytest.raises(ValueError, match="Volume"):
        calculate_density(20.0, 0.0)


def test_porosity_calculation() -> None:
    """A sample at 80% of theoretical density has 20% porosity."""
    assert calculate_porosity(4.0, 5.0) == pytest.approx(20.0)


def test_porosity_rejects_invalid_theoretical_density() -> None:
    """Theoretical density must be positive."""
    with pytest.raises(ValueError, match="Theoretical density"):
        calculate_porosity(4.0, 0.0)


@pytest.mark.parametrize("measured,theoretical", [(6.0, 5.0), (-1.0, 5.0)])
def test_porosity_rejects_invalid_density_combinations(
    measured: float, theoretical: float
) -> None:
    """Porosity must remain within the simplified model's physical limits."""
    with pytest.raises(ValueError):
        calculate_porosity(measured, theoretical)


def test_mpa_to_gpa_conversion() -> None:
    """One thousand MPa equals one GPa."""
    assert convert_pressure(1000.0, "MPa", "GPa") == pytest.approx(1.0)


def test_gpa_to_mpa_conversion() -> None:
    """One GPa equals one thousand MPa."""
    assert convert_pressure(1.0, "GPa", "MPa") == pytest.approx(1000.0)
