# AI Recommendation Service (Python Flask)

This service provides content-based recommendations using TF-IDF and cosine similarity.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the service:
```bash
python app.py
```

The service will run on `http://localhost:5000`

## API Endpoints

### POST /recommend
Get personalized recommendations

**Request:**
```json
{
  "user_profile": {
    "user_id": 1,
    "categories": ["action", "sci-fi"]
  },
  "items": [
    {"id": 1, "title": "Avengers", "category": "action", "tags": "superhero,marvel"},
    {"id": 2, "title": "Inception", "category": "sci-fi", "tags": "dream,mystery"}
  ]
}
```

**Response:**
```json
{
  "recommended_items": [2, 1],
  "scores": [0.98, 0.85],
  "count": 2
}
```

### GET /health
Check service health

**Response:**
```json
{
  "status": "healthy",
  "service": "AI Recommendation Engine"
}
```
