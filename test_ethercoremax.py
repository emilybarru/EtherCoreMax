# test_ethercoremax.py
"""
Tests for EtherCoreMax module.
"""

import unittest
from ethercoremax import EtherCoreMax

class TestEtherCoreMax(unittest.TestCase):
    """Test cases for EtherCoreMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherCoreMax()
        self.assertIsInstance(instance, EtherCoreMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherCoreMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
