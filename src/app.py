"""Streamlit user interface for the Materials Calculator."""

from typing import cast

import streamlit as st

from src.calculations import (
    PressureUnit,
    calculate_density,
    calculate_porosity,
    convert_pressure,
)


def _show_density_calculator() -> None:
    """Render the density calculator tab."""
    st.header("Density calculator")
    st.write("Calculate density from a sample's mass and volume.")
    st.latex(r"\rho = \frac{m}{V}")
    mass = st.number_input("Mass (g)", min_value=0.0, format="%.4f")
    volume = st.number_input("Volume (cm³)", min_value=0.0, format="%.4f")

    if st.button("Calculate density", type="primary"):
        try:
            density = calculate_density(mass, volume)
        except ValueError as error:
            st.error(str(error))
        else:
            st.success(f"Density: {density:.4f} g/cm³")


def _show_porosity_calculator() -> None:
    """Render the theoretical porosity calculator tab."""
    st.header("Theoretical porosity calculator")
    st.write(
        "Estimate porosity by comparing measured density with the fully dense material."
    )
    st.latex(
        r"P = \left(1 - \frac{\rho_{measured}}{\rho_{theoretical}}\right)\times100\%"
    )
    measured = st.number_input("Measured density (g/cm³)", min_value=0.0, format="%.4f")
    theoretical = st.number_input(
        "Theoretical density (g/cm³)", min_value=0.0, format="%.4f"
    )

    if st.button("Calculate porosity", type="primary"):
        try:
            porosity = calculate_porosity(measured, theoretical)
        except ValueError as error:
            st.error(str(error))
        else:
            st.success(f"Theoretical porosity: {porosity:.2f}%")


def _show_converter() -> None:
    """Render the MPa/GPa unit converter tab."""
    st.header("Pressure unit converter")
    st.write("Convert pressure values between megapascals and gigapascals.")
    st.latex(r"1\ \mathrm{GPa} = 1000\ \mathrm{MPa}")
    value = st.number_input("Pressure value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", ("MPa", "GPa"))
    to_unit = st.selectbox("To", ("GPa", "MPa"))

    if st.button("Convert pressure", type="primary"):
        try:
            result = convert_pressure(
                value, cast(PressureUnit, from_unit), cast(PressureUnit, to_unit)
            )
        except ValueError as error:
            st.error(str(error))
        else:
            st.success(f"Converted pressure: {result:.4f} {to_unit}")


def main() -> None:
    """Configure and render the Streamlit application."""
    st.set_page_config(page_title="Materials Calculator", page_icon="🧪")
    st.title("Materials Calculator")
    st.caption("Small, testable calculations for common materials quantities.")

    density_tab, porosity_tab, converter_tab = st.tabs(
        ["Density", "Theoretical porosity", "Unit converter"]
    )
    with density_tab:
        _show_density_calculator()
    with porosity_tab:
        _show_porosity_calculator()
    with converter_tab:
        _show_converter()


if __name__ == "__main__":
    main()
