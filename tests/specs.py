import os, sys
modulePath = os.path.abspath("../RepositoryChecker")
if modulePath not in sys.path:
    sys.path.insert(0, modulePath)

import unittest
from RepositoryChecker import RepositoryChecker

class TestRepositoryChecker(unittest.TestCase):

    def test___init__(self):
        rep = RepositoryChecker()
