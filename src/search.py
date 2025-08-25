
## 📋 Day 2: Core Search Implementation

### Step 1: Create the Search Module

 
import requests
from typing import List, Dict, Optional
import json
import time

try:
    from duckduckgo_search import DDGS
    DUCKDUCKGO_AVAILABLE = True
except ImportError:
    DUCKDUCKGO_AVAILABLE = False
    print("DuckDuckGo search not available. Install with: pip install duckduckgo-search")

try:
    from serpapi import GoogleSearch
    SERPAPI_AVAILABLE = True
except ImportError:
    SERPAPI_AVAILABLE = False
    print("SerpAPI not available. Install with: pip install serpapi")

class SearchProvider:
    """Abstract base class for search providers."""
    
    def search(self, query: str, num_results: int = 10) -> List[Dict[str, str]]:
        """Search for query and return structured results."""
        raise NotImplementedError
    
    def test_connection(self) -> bool:
        """Test if the search provider is working."""
        try:
            results = self.search("test query", num_results=1)
            return len(results) > 0
        except Exception:
            return False

class DuckDuckGoSearch(SearchProvider):
    """DuckDuckGo search - completely free, no API key needed."""
    
    def __init__(self):
        if not DUCKDUCKGO_AVAILABLE:
            raise ImportError("DuckDuckGo search requires: pip install duckduckgo-search")
    
    def search(self, query: str, num_results: int = 10) -> List[Dict[str, str]]:
        """Perform DuckDuckGo search."""
        try:
            print(f"🔍 Searching DuckDuckGo for: {query}")
            
            with DDGS() as ddgs:
                # Use text search
                results = list(ddgs.text(query, max_results=num_results))
            
            formatted_results = []
            for i, result in enumerate(results):
                formatted_results.append({
                    "title": result.get("title", "No title"),
                    "link": result.get("href", ""),
                    "snippet": result.get("body", "No description available"),
                    "source": "DuckDuckGo",
                    "rank": i + 1
                })
            
            print(f"✅ Found {len(formatted_results)} results")
            return formatted_results
            
        except Exception as e:
            print(f"❌ DuckDuckGo search error: {e}")
            return self._fallback_search(query, num_results)
    
    def _fallback_search(self, query: str, num_results: int) -> List[Dict[str, str]]:
        """Simple fallback when main search fails."""
        print("🔄 Using basic fallback search...")
        
        # This is a very basic fallback - in a real app you might use multiple APIs
        fallback_results = [
            {
                "title": f"Search result for: {query}",
                "link": "https://example.com/search",
                "snippet": f"This is a fallback result for the query '{query}'. In a real implementation, this would connect to alternative search APIs.",
                "source": "Fallback",
                "rank": 1
            }
        ]
        
        return fallback_results[:num_results]

class SerpAPISearch(SearchProvider):
    """Google Search via SerpAPI - requires API key but gives better results."""
    
    def __init__(self, api_key: str):
        if not SERPAPI_AVAILABLE:
            raise ImportError("SerpAPI requires: pip install serpapi")
        
        self.api_key = api_key
        if not api_key:
            raise ValueError("SerpAPI requires an API key")
    
    def search(self, query: str, num_results: int = 10) -> List[Dict[str, str]]:
        """Perform Google search via SerpAPI."""
        try:
            print(f"🔍 Searching Google (SerpAPI) for: {query}")
            
            search = GoogleSearch({
                "q": query,
                "api_key": self.api_key,
                "num": min(num_results, 20),  # SerpAPI limit
                "engine": "google"
            })
            
            results = search.get_dict()
            
            if "error" in results:
                print(f"❌ SerpAPI error: {results['error']}")
                return []
            
            formatted_results = []
            organic_results = results.get("organic_results", [])
            
            for i, result in enumerate(organic_results):
                formatted_results.append({
                    "title": result.get("title", "No title"),
                    "link": result.get("link", ""),
                    "snippet": result.get("snippet", "No description available"),
                    "source": "Google",
                    "rank": i + 1
                })
            
            print(f"✅ Found {len(formatted_results)} results")
            return formatted_results[:num_results]
            
        except Exception as e:
            print(f"❌ SerpAPI search error: {e}")
            return []

def get_search_provider(provider_type: str, api_key: Optional[str] = None) -> SearchProvider:
    """Factory function to get the appropriate search provider."""
    
    provider_type = provider_type.lower()
    
    if provider_type == "duckduckgo":
        return DuckDuckGoSearch()
    
    elif provider_type == "serpapi":
        if not api_key:
            print("⚠️  SerpAPI requires API key, falling back to DuckDuckGo")
            return DuckDuckGoSearch()
        return SerpAPISearch(api_key)
    
    else:
        print(f"⚠️  Unknown search provider '{provider_type}', using DuckDuckGo")
        return DuckDuckGoSearch()

def test_search_functionality():
    """Test function to verify search is working."""
    print("🧪 Testing Search Functionality")
    print("-" * 40)
    
    # Test DuckDuckGo
    try:
        ddg_search = DuckDuckGoSearch()
        results = ddg_search.search("python programming", num_results=3)
        
        print(f"✅ DuckDuckGo: {len(results)} results")
        if results:
            print(f"   First result: {results['title'][:50]}...")
        
    except Exception as e:
        print(f"❌ DuckDuckGo test failed: {e}")
    
    print("\n🎉 Search testing complete!")

if __name__ == "__main__":
    test_search_functionality()
