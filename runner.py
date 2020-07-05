import sys
from unittest import TextTestRunner, defaultTestLoader

suite = defaultTestLoader.discover(".")
runner = TextTestRunner()

if not runner.run(suite).wasSuccessful():
    sys.exit(1)
