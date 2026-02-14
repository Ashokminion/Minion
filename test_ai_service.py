"""
AI Recommendation Service - Standalone Demo
This script tests the Flask AI service directly without needing the full Spring Boot backend
"""

import requests
import json

AI_SERVICE_URL = "http://localhost:5000"

def test_health():
    """Check if AI service is running"""
    print("=" * 60)
    print("Testing AI Service Health...")
    print("=" * 60)
    try:
        response = requests.get(f"{AI_SERVICE_URL}/health")
        if response.status_code == 200:
            print("✅ AI Service is RUNNING!")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"❌ Service returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to AI service: {e}")
        print("Make sure Flask is running on http://localhost:5000")
        return False

def test_recommendations():
    """Test the recommendation endpoint with sample data"""
    print("\n" + "=" * 60)
    print("Testing AI Recommendations...")
    print("=" * 60)
    
    # Sample user profile
    user_profile = {
        "user_id": 1,
        "categories": ["action", "sci-fi"]
    }
    
    # Sample items (movies, books, tech)
    items = [
        {"id": 1, "title": "Avengers Endgame", "category": "action", "tags": "superhero,marvel,adventure"},
        {"id": 2, "title": "The Matrix", "category": "sci-fi", "tags": "cyberpunk,action,ai"},
        {"id": 3, "title": "Inception", "category": "sci-fi", "tags": "dream,thriller,mystery"},
        {"id": 4, "title": "The Shawshank Redemption", "category": "drama", "tags": "prison,hope,friendship"},
        {"id": 5, "title": "Interstellar", "category": "sci-fi", "tags": "space,exploration,science"},
        {"id": 6, "title": "Clean Code", "category": "books", "tags": "programming,software,tech"},
        {"id": 7, "title": "The Lean Startup", "category": "books", "tags": "business,startup,tech"},
        {"id": 8, "title": "iPhone 15 Pro", "category": "tech", "tags": "smartphone,apple,gadget"},
        {"id": 9, "title": "MacBook Pro M3", "category": "tech", "tags": "laptop,apple,performance"},
        {"id": 10, "title": "The Dark Knight", "category": "action", "tags": "superhero,dc,batman"}
    ]
    
    payload = {
        "user_profile": user_profile,
        "items": items
    }
    
    print(f"\n📊 User Preferences: {user_profile['categories']}")
    print(f"📦 Testing with {len(items)} items")
    
    try:
        response = requests.post(
            f"{AI_SERVICE_URL}/recommend",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            recommended_ids = result.get('recommended_items', [])
            scores = result.get('scores', [])
            
            print("\n✅ AI Recommendations Generated!")
            print(f"\n🎯 Top {len(recommended_ids)} Recommendations:")
            print("-" * 60)
            
            for i, (item_id, score) in enumerate(zip(recommended_ids, scores), 1):
                # Find the item details
                item = next((item for item in items if item['id'] == item_id), None)
                if item:
                    print(f"\n{i}. {item['title']}")
                    print(f"   Category: {item['category']}")
                    print(f"   Tags: {item['tags']}")
                    print(f"   📈 Similarity Score: {score:.4f}")
            
            print("\n" + "=" * 60)
            print("🧠 AI Analysis:")
            print("The content-based filtering algorithm analyzed:")
            print("  • TF-IDF vectorization of item tags and categories")
            print("  • Cosine similarity between user preferences and items")
            print("  • Category matching boost (1.5x for matching categories)")
            print(f"  • Result: Items matching '{user_profile['categories']}' ranked highest")
            
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Error calling AI service: {e}")

def test_custom_preferences():
    """Test with custom user preferences"""
    print("\n" + "=" * 60)
    print("Custom Recommendation Test")
    print("=" * 60)
    
    # User who likes tech and books
    user_profile = {
        "user_id": 2,
        "categories": ["tech", "books"]
    }
    
    items = [
        {"id": 1, "title": "iPhone 15 Pro", "category": "tech", "tags": "smartphone,apple,5g"},
        {"id": 2, "title": "Deep Work", "category": "books", "tags": "productivity,focus,self-improvement"},
        {"id": 3, "title": "The Matrix", "category": "movies", "tags": "sci-fi,action"},
        {"id": 4, "title": "MacBook Pro", "category": "tech", "tags": "laptop,apple,m3"},
        {"id": 5, "title": "Atomic Habits", "category": "books", "tags": "habits,self-improvement,productivity"}
    ]
    
    payload = {
        "user_profile": user_profile,
        "items": items
    }
    
    print(f"\n📊 User Preferences: {user_profile['categories']}")
    
    try:
        response = requests.post(
            f"{AI_SERVICE_URL}/recommend",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            recommended_ids = result.get('recommended_items', [])
            scores = result.get('scores', [])
            
            print("\n✅ Custom Recommendations:")
            for i, (item_id, score) in enumerate(zip(recommended_ids[:3], scores[:3]), 1):
                item = next((item for item in items if item['id'] == item_id), None)
                if item:
                    print(f"{i}. {item['title']} (Score: {score:.4f})")
                    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n🚀 AI RECOMMENDATION SERVICE - DEMO SCRIPT")
    print("=" * 60)
    
    # Test 1: Health check
    if not test_health():
        print("\n⚠️  Please start the Flask AI service first:")
        print("   cd python-ai-service")
        print("   python app.py")
        exit(1)
    
    # Test 2: Main recommendation test
    test_recommendations()
    
    # Test 3: Custom preferences
    test_custom_preferences()
    
    print("\n" + "=" * 60)
    print("✅ Demo Complete!")
    print("=" * 60)
    print("\n💡 Next Steps:")
    print("   1. Install Maven to run Spring Boot backend")
    print("   2. Start MySQL service")
    print("   3. Run: mvn spring-boot:run (in java/ folder)")
    print("   4. Access full UI at http://localhost:3000")
    print("=" * 60)
