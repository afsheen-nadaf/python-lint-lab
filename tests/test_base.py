"""Tests for the base module."""

from project_package import base


def test_run():
    """Test that runme returns 1."""
    assert base.runme() == 1