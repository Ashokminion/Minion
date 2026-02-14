from flask import Flask, request, jsonify
from flask_cors import CORS
from model.similarity_engine import ContentBasedRecommender

app = Flask(__name__)
CORS(app)

recommender = ContentBasedRecommender()

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Endpoint to get personalized recommendations
    Request body:
    {
        "user_profile": {
            "user_id": 1,
            "categories": ["action", "sci-fi"]
        },
        "items": [
            {"id": 1, "title": "Movie 1", "category": "action", "tags": "superhero,adventure"},
            {"id": 2, "title": "Movie 2", "category": "drama", "tags": "emotional,family"}
        ]
    }
    Response:
    {
        "recommended_items": [1, 3, 5],
        "scores": [0.95, 0.87, 0.82]
    }
    """
    try:
        data = request.get_json()
        user_profile = data.get('user_profile', {})
        items = data.get('items', [])
        
        if not items:
            return jsonify({'error': 'No items provided'}), 400
        
        # Get recommendations
        recommended_ids, scores = recommender.get_recommendations(user_profile, items)
        
        return jsonify({
            'recommended_items': recommended_ids,
            'scores': scores,
            'count': len(recommended_ids)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'AI Recommendation Engine'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
