# test_pixelvault.py
"""
Tests for PixelVault module.
"""

import unittest
from pixelvault import PixelVault

class TestPixelVault(unittest.TestCase):
    """Test cases for PixelVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelVault()
        self.assertIsInstance(instance, PixelVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
