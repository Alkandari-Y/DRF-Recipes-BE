#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import dotenv


def main():
    # dotenv.read_dotenv()

    """Run administrative tasks."""
    if str(os.environ.get('DEVELOPMENT_MODE')) == "1":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodiez.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodiez.settings.prod")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
