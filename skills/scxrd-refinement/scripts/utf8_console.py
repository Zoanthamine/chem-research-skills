"""Use UTF-8 for CLI logs on Windows and redirected host streams."""
import sys

def configure_utf8():
    for stream in (sys.stdout, sys.stderr):
        configure = getattr(stream, "reconfigure", None)
        if callable(configure):
            try:
                configure(encoding="utf-8", errors="backslashreplace")
            except (OSError, ValueError):
                pass
