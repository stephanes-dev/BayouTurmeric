# test_bayouturmeric.py
"""
Tests for BayouTurmeric module.
"""

import unittest
from bayouturmeric import BayouTurmeric

class TestBayouTurmeric(unittest.TestCase):
    """Test cases for BayouTurmeric class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BayouTurmeric()
        self.assertIsInstance(instance, BayouTurmeric)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BayouTurmeric()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
