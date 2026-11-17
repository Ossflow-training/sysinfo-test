import unittest

from .. import mysystem


class TestLabFailure(unittest.TestCase):
    def test_memory_lab_failure(self):
        # Intentionally fails to demonstrate a CI test failure.
        self.assertFalse(mysystem.is_enough_memory(63))