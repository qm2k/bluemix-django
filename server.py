#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    # Read port selected by the cloud for our application
    PORT = int(os.getenv('VCAP_APP_PORT', 8000))
    ARGS = sys.argv
    ARGS[1:1] = ['runserver', '--noreload', '0.0.0.0:' + str(PORT)]

    from django.core.management import execute_from_command_line

    execute_from_command_line(ARGS)

