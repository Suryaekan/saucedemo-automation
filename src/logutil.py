"""Small helpers for test logging: one-time root setup and named loggers.

The unified report format (timestamp, level, logger, file:line, message) is used
for file logs and should stay in sync with ``log_format`` / ``log_date_format``
in ``pytest.ini`` so pytest-html "Captured log" matches ``artifacts/logs/*.log``.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Final

_CONFIGURED: bool = False

# Single line layout for reports, files, and pytest captured logs (keep pytest.ini in sync).
REPORT_LOG_FORMAT: Final[str] = (
    "%(asctime)s | %(levelname)-5s | %(name)s:%(filename)s:%(lineno)d | %(message)s"
)
REPORT_LOG_DATEFMT: Final[str] = "%Y-%m-%d %H:%M:%S"

# Console-only when not running under pytest (short time, no file:line to reduce noise).
_CONSOLE_FORMAT: Final[str] = "%(asctime)s | %(levelname)-5s | %(name)s | %(message)s"
_CONSOLE_DATEFMT: Final[str] = "%H:%M:%S"
_DEFAULT_LOG_FILE: Final[str] = "artifacts/logs/tests.log"
_DEFAULT_LEVEL_NAME: Final[str] = "DEBUG"
_CONSOLE_HANDLER_LEVEL: Final[int] = logging.DEBUG

# Set by ``conftest.py`` before importing this module; name duplicated there on purpose.
_ENV_UNDER_PYTEST: Final[str] = "SAUCE_DEMO_UNDER_PYTEST"


def _running_under_pytest() -> bool:
    """Detect pytest runs (``SAUCE_DEMO_UNDER_PYTEST`` set by ``conftest``).

    Returns:
        ``True`` when the environment flag is set so logging skips duplicate stdout.
    """
    return os.environ.get(_ENV_UNDER_PYTEST) == "1"


def configure_logging(level: int | None = None, log_file: str | None = None) -> None:
    """Configure the root logger once (idempotent).

    Normal runs attach a compact stdout handler (DEBUG) plus an optional UTF-8 file
    using the report line format. Under pytest, the stdout handler is omitted so
    pytest-html does not duplicate the same lines under "Captured stdout" and
    "Captured log"; pytest formats output via ``pytest.ini``.

    Environment variables:

    * ``LOG_LEVEL`` — root level name (default ``DEBUG``).
    * ``LOG_FILE`` — file path (default ``artifacts/logs/tests.log``); empty string
      disables the file handler.

    Args:
        level: Root log level; if ``None``, taken from ``LOG_LEVEL`` or default DEBUG.
        log_file: If not ``None``, overrides the log file path from the environment;
            pass ``""`` to force-disable the file handler for this call.

    Returns:
        None
    """
    global _CONFIGURED
    if _CONFIGURED:
        return
    if level is None:
        name = os.environ.get("LOG_LEVEL", _DEFAULT_LEVEL_NAME).upper()
        level = getattr(logging, name, logging.DEBUG)

    if log_file is not None:
        path: str | None = log_file or None
    else:
        raw = os.environ.get("LOG_FILE", _DEFAULT_LOG_FILE)
        path = None if raw.strip() == "" else raw

    root = logging.getLogger()
    root.setLevel(level)

    under_pytest = _running_under_pytest()

    if not under_pytest:
        console_formatter = logging.Formatter(_CONSOLE_FORMAT, datefmt=_CONSOLE_DATEFMT)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(_CONSOLE_HANDLER_LEVEL)
        stream_handler.setFormatter(console_formatter)
        root.addHandler(stream_handler)

    if path:
        log_path = Path(path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_formatter = logging.Formatter(REPORT_LOG_FORMAT, datefmt=REPORT_LOG_DATEFMT)
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(file_formatter)
        root.addHandler(file_handler)
    elif under_pytest:
        # Pytest + no file: still emit somewhere for local debugging without duplicating HTML.
        fallback = logging.StreamHandler(sys.stdout)
        fallback.setLevel(_CONSOLE_HANDLER_LEVEL)
        fallback.setFormatter(
            logging.Formatter(REPORT_LOG_FORMAT, datefmt=REPORT_LOG_DATEFMT)
        )
        root.addHandler(fallback)

    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """Return a named logger after ensuring ``configure_logging`` has run.

    Args:
        name: Logger name, usually ``__name__`` of the calling module.

    Returns:
        The ``logging.Logger`` for ``name`` (child of the configured root).
    """
    configure_logging()
    return logging.getLogger(name)
