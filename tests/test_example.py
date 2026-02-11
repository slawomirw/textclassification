"""Example test to verify the test runner."""

from textclassification import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"
