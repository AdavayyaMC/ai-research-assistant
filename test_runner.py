#!/usr/bin/env python3
"""
Simple test runner for the AI Research Assistant project.
Run this to test your setup after Day 2.
"""

import sys
import os

def test_imports():
    """Test that we can import all our modules."""
    print("📦 Testing Imports...")
    
    try:
        # Test config import
        sys.path.insert(0, 'src')
        from config import load_config, validate_setup
        print("  ✅ Config module imported successfully")
        
        # Test search import
        from search import DuckDuckGoSearch, get_search_provider
        print("  ✅ Search module imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return False

def test_configuration():
    """Test configuration loading."""
    print("\n⚙️  Testing Configuration...")
    
    try:
        from config import validate_setup
        validate_setup()
        return True
        
    except Exception as e:
        print(f"  ❌ Configuration error: {e}")
        return False

def test_search():
    """Test search functionality."""
    print("\n🔍 Testing Search...")
    
    try:
        from search import test_search_functionality
        test_search_functionality()
        return True
        
    except Exception as e:
        print(f"  ❌ Search error: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 AI Research Assistant - Day 2 Test Suite")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Configuration", test_configuration),
        ("Search", test_search)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🧪 Running {test_name} tests...")
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"  {test_name}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! Ready for Day 3!")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
        print("💡 Try: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
