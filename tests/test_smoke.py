"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import docusync


def test_version_is_set() -> None:
    assert docusync.__version__
