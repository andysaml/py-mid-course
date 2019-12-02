from django.test import TestCase
from django.conf import settings # correct way
import os

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))