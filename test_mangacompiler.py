# test_mangacompiler.py
"""
Tests for MangaCompiler module.
"""

import unittest
from mangacompiler import MangaCompiler

class TestMangaCompiler(unittest.TestCase):
    """Test cases for MangaCompiler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaCompiler()
        self.assertIsInstance(instance, MangaCompiler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaCompiler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
