#!/usr/bin/env python

"""
Adapted from django-constance, which itself was adapted from django-adminfiles.
"""

import os
import sys
import django

here = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(here)
sys.path[0:0] = [here, parent]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

from django.test.runner import DiscoverRunner

def main():
    if django.VERSION >= (1, 7):
        django.setup()
    runner = DiscoverRunner(pattern='tests*', failfast=True, verbosity=1)
    failures = runner.run_tests(['testapp'], interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    main()
