# test_builderchangelog.py
"""
Tests for BuilderChangelog module.
"""

import unittest
from builderchangelog import BuilderChangelog

class TestBuilderChangelog(unittest.TestCase):
    """Test cases for BuilderChangelog class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BuilderChangelog()
        self.assertIsInstance(instance, BuilderChangelog)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BuilderChangelog()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
