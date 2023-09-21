from django.apps import AppConfig
from AI_models.emotion_analysis import KcBERT
from AI_models.SentenceTransformers import SBERT

class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'
    KcBERT = KcBERT()
    SBERT = SBERT()