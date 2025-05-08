"""
Content recommendation system for AllWorks Company website
This module provides content recommendations based on the current page and user interactions.
"""

from collections import defaultdict

class ContentRecommender:
    """Recommends related content based on the current page and user preferences"""
    
    def __init__(self):
        """Initialize the recommender system with content relationships"""
        # Define relationships between different types of content
        self.content_relationships = {
            # Project relationships
            'projects': {
                'data_analytics': ['courses:data_science', 'courses:big_data', 'training:data_analytics_bootcamp', 'publications:data_trends'],
                'web_development': ['courses:web_design', 'courses:javascript', 'training:web_dev_fundamentals', 'publications:web_dev_guide'],
                'mobile_app': ['courses:mobile_dev', 'courses:ui_design', 'training:app_development', 'publications:mobile_trends'],
                'cloud_solutions': ['courses:cloud_computing', 'courses:devops', 'training:cloud_architecture', 'publications:cloud_security'],
                'ai_machine_learning': ['courses:machine_learning', 'courses:python', 'training:ai_workshop', 'publications:ai_ethics'],
                'cybersecurity': ['courses:security_fundamentals', 'courses:network_security', 'training:security_certification', 'publications:security_report']
            },
            
            # Course relationships
            'courses': {
                'data_science': ['projects:data_analytics', 'training:data_science_certification', 'publications:data_trends'],
                'web_design': ['projects:web_development', 'courses:javascript', 'publications:design_trends'],
                'javascript': ['courses:web_design', 'projects:web_development', 'training:web_dev_fundamentals'],
                'python': ['courses:machine_learning', 'projects:ai_machine_learning', 'training:python_bootcamp'],
                'cloud_computing': ['projects:cloud_solutions', 'courses:devops', 'publications:cloud_security'],
                'big_data': ['projects:data_analytics', 'courses:data_science', 'publications:data_trends'],
                'mobile_dev': ['projects:mobile_app', 'courses:ui_design', 'training:app_development'],
                'ui_design': ['courses:mobile_dev', 'courses:web_design', 'publications:design_trends'],
                'devops': ['courses:cloud_computing', 'projects:cloud_solutions', 'training:devops_pipeline'],
                'machine_learning': ['projects:ai_machine_learning', 'courses:python', 'publications:ai_research'],
                'security_fundamentals': ['projects:cybersecurity', 'courses:network_security', 'publications:security_report']
            },
            
            # Training relationships
            'training': {
                'data_analytics_bootcamp': ['projects:data_analytics', 'courses:data_science', 'publications:data_trends'],
                'web_dev_fundamentals': ['projects:web_development', 'courses:javascript', 'publications:web_dev_guide'],
                'cloud_architecture': ['projects:cloud_solutions', 'courses:cloud_computing', 'publications:cloud_security'],
                'security_certification': ['projects:cybersecurity', 'courses:security_fundamentals', 'publications:security_report'],
                'ai_workshop': ['projects:ai_machine_learning', 'courses:machine_learning', 'publications:ai_ethics'],
                'app_development': ['projects:mobile_app', 'courses:mobile_dev', 'publications:mobile_trends'],
                'data_science_certification': ['courses:data_science', 'projects:data_analytics', 'publications:data_trends'],
                'python_bootcamp': ['courses:python', 'projects:ai_machine_learning', 'courses:machine_learning'],
                'devops_pipeline': ['courses:devops', 'projects:cloud_solutions', 'courses:cloud_computing']
            },
            
            # Publication relationships
            'publications': {
                'data_trends': ['projects:data_analytics', 'courses:data_science', 'training:data_analytics_bootcamp'],
                'web_dev_guide': ['projects:web_development', 'courses:web_design', 'training:web_dev_fundamentals'],
                'mobile_trends': ['projects:mobile_app', 'courses:mobile_dev', 'training:app_development'],
                'cloud_security': ['projects:cloud_solutions', 'courses:cloud_computing', 'training:cloud_architecture'],
                'ai_ethics': ['projects:ai_machine_learning', 'courses:machine_learning', 'publications:ai_research'],
                'security_report': ['projects:cybersecurity', 'courses:security_fundamentals', 'training:security_certification'],
                'design_trends': ['courses:ui_design', 'courses:web_design', 'projects:mobile_app'],
                'ai_research': ['publications:ai_ethics', 'projects:ai_machine_learning', 'courses:machine_learning']
            }
        }
        
        # Track user interactions 
        self.user_interactions = defaultdict(int)
        
    def get_recommendations(self, current_page, current_item=None, limit=3):
        """
        Get content recommendations based on the current page and item
        
        Args:
            current_page: The current page type ('projects', 'courses', 'training', 'publications')
            current_item: The specific item being viewed
            limit: Maximum number of recommendations to return
            
        Returns:
            List of recommendation dictionaries with type, id, and relevance score
        """
        recommendations = []
        
        # If we have a specific item, get related content
        if current_item and current_page in self.content_relationships and current_item in self.content_relationships[current_page]:
            for related in self.content_relationships[current_page][current_item]:
                content_type, content_id = related.split(':')
                relevance = 1.0
                
                # Boost relevance for items the user has interacted with
                interaction_key = f"{content_type}:{content_id}"
                if self.user_interactions[interaction_key] > 0:
                    relevance += min(0.5, self.user_interactions[interaction_key] * 0.1)
                
                recommendations.append({
                    'type': content_type,
                    'id': content_id,
                    'relevance': relevance
                })
        
        # If no specific item or not enough recommendations, add popular items from each category
        popular_items = {
            'projects': ['web_development', 'ai_machine_learning', 'data_analytics'],
            'courses': ['python', 'javascript', 'data_science'],
            'training': ['data_analytics_bootcamp', 'web_dev_fundamentals', 'ai_workshop'],
            'publications': ['data_trends', 'ai_ethics', 'web_dev_guide']
        }
        
        if len(recommendations) < limit:
            needed = limit - len(recommendations)
            for page_type, items in popular_items.items():
                # Skip current page type to avoid showing same content type
                if page_type == current_page:
                    continue
                
                for item in items:
                    # Skip items already in recommendations
                    if any(r['type'] == page_type and r['id'] == item for r in recommendations):
                        continue
                    
                    # Add with lower relevance since it's a general recommendation
                    recommendations.append({
                        'type': page_type,
                        'id': item,
                        'relevance': 0.5
                    })
                    
                    needed -= 1
                    if needed <= 0:
                        break
                
                if needed <= 0:
                    break
        
        # Sort by relevance and limit
        recommendations.sort(key=lambda x: x['relevance'], reverse=True)
        return recommendations[:limit]
    
    def record_interaction(self, content_type, content_id):
        """
        Record a user interaction with content to improve future recommendations
        
        Args:
            content_type: The type of content ('projects', 'courses', etc.)
            content_id: The specific content id
        """
        interaction_key = f"{content_type}:{content_id}"
        self.user_interactions[interaction_key] += 1
        
    def get_popular_content(self, limit=5):
        """
        Get the most popular content based on user interactions
        
        Args:
            limit: Maximum number of items to return
            
        Returns:
            List of popular content items
        """
        # Sort user interactions by count
        sorted_interactions = sorted(
            self.user_interactions.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        popular = []
        for interaction, count in sorted_interactions[:limit]:
            content_type, content_id = interaction.split(':')
            popular.append({
                'type': content_type,
                'id': content_id,
                'interaction_count': count
            })
        
        return popular


# Create global instance
recommender = ContentRecommender()