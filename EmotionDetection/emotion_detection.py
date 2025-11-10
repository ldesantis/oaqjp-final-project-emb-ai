import json
import requests

def get_dominant_emotion(emotions):
    dominant_emotion = max(emotions, key=emotions.get)
    return dominant_emotion

def emotion_detector(text_to_analyze):
    # Endpoint URL for the Watson Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers including the model ID for emotion detection
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Input JSON payload with the text to analyze
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Make the POST request to the Emotion Detection API
    response = requests.post(url, headers=headers, json=input_json)

    # Convert response text to dictionary using json.loads
    response_dict = json.loads(response.text)
    
    # Extract emotions dictionary from nested response
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract individual emotion scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find the dominant emotion (emotion with highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Format the output dictionary
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output