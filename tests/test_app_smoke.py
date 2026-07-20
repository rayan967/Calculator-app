"""Browser-free smoke tests for the Streamlit application."""

import importlib


def test_application_imports() -> None:
    """The UI module can be imported without starting a browser or server."""
    module = importlib.import_module("src.app")
    assert callable(module.main)
