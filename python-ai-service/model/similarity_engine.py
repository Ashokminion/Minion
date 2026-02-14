import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    """
    Content-based recommendation engine using TF-IDF and cosine similarity
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
    
    def get_recommendations(self, user_profile, items, top_n=10):
        """
        Generate recommendations based on user preferences and item features
        
        Args:
            user_profile: dict with 'categories' list
            items: list of dicts with 'id', 'category', 'tags'
            top_n: number of recommendations to return
        
        Returns:
            tuple: (list of item ids, list of scores)
        """
        if not items:
            return [], []
        
        # Extract user preferences
        user_categories = set(user_profile.get('categories', []))
        
        # Build content strings for each item
        item_contents = []
        item_ids = []
        
        for item in items:
            item_id = item.get('id')
            category = item.get('category', '')
            tags = item.get('tags', '').replace(',', ' ')
            title = item.get('title', '')
            
            # Combine all text features
            content = f"{title} {category} {tags}"
            item_contents.append(content)
            item_ids.append(item_id)
        
        # Build user profile string from preferences
        user_content = ' '.join(user_categories)
        
        if not user_content:
            # If no user preferences, return top items by category match
            return self._fallback_recommendations(items, top_n)
        
        # Compute TF-IDF vectors
        all_contents = [user_content] + item_contents
        tfidf_matrix = self.vectorizer.fit_transform(all_contents)
        
        # User vector is the first row
        user_vector = tfidf_matrix[0:1]
        item_vectors = tfidf_matrix[1:]
        
        # Compute cosine similarity
        similarities = cosine_similarity(user_vector, item_vectors).flatten()
        
        # Apply category boost: if item category matches user preference, boost score
        boosted_similarities = []
        for idx, item in enumerate(items):
            score = similarities[idx]
            
            # Boost if category matches
            if item.get('category') in user_categories:
                score *= 1.5  # 50% boost for category match
            
            boosted_similarities.append(score)
        
        # Sort by score (descending)
        sorted_indices = np.argsort(boosted_similarities)[::-1]
        
        # Get top N
        top_indices = sorted_indices[:top_n]
        recommended_ids = [item_ids[i] for i in top_indices]
        scores = [float(boosted_similarities[i]) for i in top_indices]
        
        return recommended_ids, scores
    
    def _fallback_recommendations(self, items, top_n):
        """
        Fallback: return random items if no user profile
        """
        import random
        sample_size = min(top_n, len(items))
        sampled_items = random.sample(items, sample_size)
        
        recommended_ids = [item.get('id') for item in sampled_items]
        scores = [0.5] * len(recommended_ids)  # Neutral score
        
        return recommended_ids, scores
