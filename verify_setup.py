import sys
print(f"Python: {sys.version}")

packages = ["crewai", "langchain", "yfinance", "pandas", "fastapi", "dotenv"]
for pkg in packages:
    try:
        __import__(pkg)
        print(f"  ✓ {pkg}")
    except ImportError:
        print(f"  ✗ {pkg} — NOT FOUND")

from dotenv import load_dotenv
import os
load_dotenv()
print("\nAPI Keys loaded:")
for key in ["ANTHROPIC_API_KEY", "OPENAI_API_KEY", "ALPACA_API_KEY"]:
    val = os.getenv(key)
    print(f"  {'✓' if val else '✗'} {key}: {'SET' if val else 'MISSING'}")