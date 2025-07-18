# test_cognitiveledger.py
"""
Tests for CognitiveLedger module.
"""

import unittest
from cognitiveledger import CognitiveLedger

class TestCognitiveLedger(unittest.TestCase):
    """Test cases for CognitiveLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CognitiveLedger()
        self.assertIsInstance(instance, CognitiveLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CognitiveLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
