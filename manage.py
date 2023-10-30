#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks.

    Raises:
        ImportError: Raised  when django is not installed or
            the path is incorrectly specified
            or the virtual environment is not activated.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WalkerShop.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        error_message = """
            Couldn't import Django. Are you sure it's installed and
            available on your PYTHONPATH environment variable? Did you
            forget to activate a virtual environment?
        """
        raise ImportError(error_message) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
