 import os
from typing import Dict, Any
from dotenv import load_dotenv

def load_config() -> Dict[str, Any]:
    """Load configuration from environment variables."""
    load_dotenv()
    
    config = {
        # API Keys
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "serpapi_key": os.getenv("SERPAPI_KEY"),
        
        # Model Configuration
        "llm_provider": os.getenv("LLM_PROVIDER", "openai").lower(),
        "model_name": os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
        
        # Storage Configuration
        "storage_type": os.getenv("STORAGE_TYPE", "sqlite").lower(),
        "db_path": os.getenv("DB_PATH", "data/notes.db"),
        
        # Search Configuration
        "search_provider": os.getenv("SEARCH_PROVIDER", "duckduckgo").lower(),
        "max_search_results": int(os.getenv("MAX_SEARCH_RESULTS", "10")),
    }
    
    # Validation
    if config["llm_provider"] == "openai" and not config["openai_api_key"]:
        print("Warning: OpenAI API key not found. Using Ollama as fallback.")
        config["llm_provider"] = "ollama"
        config["model_name"] = "llama3"
    
    if config["search_provider"] == "serpapi" and not config["serpapi_key"]:
        print("Warning: SerpAPI key not found, using DuckDuckGo")
        config["search_provider"] = "duckduckgo"
    
    return config

def validate_setup():
    """Validate that the setup is working correctly."""
    config = load_config()
    
    print("🔧 Configuration Status:")
    print(f"  LLM Provider: {config['llm_provider']}")
    print(f"  Model: {config['model_name']}")
    print(f"  Search Provider: {config['search_provider']}")
    print(f"  Storage Type: {config['storage_type']}")
    
    return True

if __name__ == "__main__":
    validate_setup()
