import json
import requests  # Import the requests library to handle HTTP requests


def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    data = json.loads(response.text) # Load the JSON response into a Python dictionary
    emotion_predictions = data["emotionPredictions"] # Extract the emotion predictions
    emotion_scores = emotion_predictions[0]["emotion"] # Extract the emotion scores
    dominant_emotion = max(emotion_scores, key=emotion_scores.get) # Determine the dominant emotion
    # Create the output dictionary
    output = {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "dominant_emotion": dominant_emotion
    }

    return output  