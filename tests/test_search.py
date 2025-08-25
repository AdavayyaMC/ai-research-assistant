import unittest
import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from search import DuckDuckGoSearch, get_search_provider

class TestSearchFunctionality(unittest.TestCase):
    """Test search providers."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_query = "python programming"
        self.max_results = 5
    
    def test_duckduckgo_search_creation(self):
        """Test that we can create a DuckDuckGo search instance."""
        try:
            search = DuckDuckGoSearch()
            self.assertIsNotNone(search)
            print("✅ DuckDuckGo search instance created successfully")
        except ImportError as e:
            self.skipTest(f"DuckDuckGo not available: {e}")
    
    def test_search_provider_factory(self):
        """Test the search provider factory function."""
        
        # Test DuckDuckGo provider
        provider = get_search_provider("duckduckgo")
        self.assertIsInstance(provider, DuckDuckGoSearch)
        
        # Test unknown provider fallback
        provider = get_search_provider("unknown_provider")
        self.assertIsInstance(provider, DuckDuckGoSearch)
        
        print("✅ Search provider factory working correctly")
    
    def test_search_results_structure(self):
        """Test that search results have the correct structure."""
        try:
            search = DuckDuckGoSearch()
            results = search.search(self.test_query, self.max_results)
            
            # Check that we got some results
            self.assertGreater(len(results), 0, "Should return at least one result")
            
            # Check result structure
            required_fields = ["title", "link", "snippet", "source", "rank"]
            for field in required_fields:
                self.assertIn(field, results, f"Result should contain '{field}' field")
            
            # Check data types
            self.assertIsInstance(results["title"], str)
            self.assertIsInstance(results["link"], str)
            self.assertIsInstance(results["snippet"], str)
            self.assertIsInstance(results["rank"], int)
            
            print(f"✅ Search returned {len(results)} properly structured results")
            
        except ImportError:
            self.skipTest("DuckDuckGo search not available")
        except Exception as e:
            self.fail(f"Search test failed: {e}")

def run_manual_search_test():
    """Manual test function that can be run independently."""
    print("\n🔍 Manual Search Test")
    print("=" * 50)
    
    try:
        from search import test_search_functionality
        test_search_functionality()
        
    except Exception as e:
        print(f"❌ Manual test failed: {e}")

if __name__ == "__main__":
    # Run both unit tests and manual tests
    print("🧪 Running Search Tests")
    print("=" * 50)
    
    # Run unit tests
    unittest.main(verbosity=2, exit=False)
    
    # Run manual test
    run_manual_search_test()

