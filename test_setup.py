#!/usr/bin/env python3
"""
Test script to verify that all dependencies are installed correctly
"""

def test_imports():
    try:
        print("Testing imports...")
        
        # Test Flask
        import flask
        print(f"✓ Flask {flask.__version__} imported successfully")
        
        # Test Transformers
        import transformers
        print(f"✓ Transformers {transformers.__version__} imported successfully")
        
        # Test PyTorch
        import torch
        print(f"✓ PyTorch {torch.__version__} imported successfully")
        
        # Test SQLite (built-in)
        import sqlite3
        print("✓ SQLite3 imported successfully")
        
        # Test datetime (built-in)
        from datetime import datetime
        print("✓ Datetime imported successfully")
        
        print("\n✅ All dependencies are installed correctly!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_ai_generator():
    try:
        print("\nTesting AI generator...")
        from ai_generator import generate_horoscope
        print("✓ AI generator imported successfully")
        
        # Test with a sample horoscope generation
        horoscope = generate_horoscope("Aries")
        print(f"✓ Generated horoscope for Aries: {horoscope[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ AI generator error: {e}")
        return False

def test_database():
    try:
        print("\nTesting database...")
        from database import init_db, save_prediction, get_predictions
        
        # Initialize database
        init_db()
        print("✓ Database initialized successfully")
        
        # Test saving a prediction
        save_prediction(1, "Test horoscope prediction")
        print("✓ Prediction saved successfully")
        
        # Test getting predictions
        predictions = get_predictions(1)
        print(f"✓ Retrieved {len(predictions)} predictions")
        
        return True
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

if __name__ == "__main__":
    print("🔮 AI-Horoscope Dependency Test\n")
    
    success = True
    success &= test_imports()
    success &= test_ai_generator()
    success &= test_database()
    
    if success:
        print("\n🎉 All tests passed! Your environment is ready.")
        print("You can now run 'python app.py' to start the application.")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
