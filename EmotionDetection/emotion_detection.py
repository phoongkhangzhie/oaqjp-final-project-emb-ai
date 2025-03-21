import json
import requests


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=json_obj, headers=headers)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    json_response = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    dominant_emotion = max([(v,k) for k,v in json_response.items()])[1]
    json_response["dominant_emotion"] = dominant_emotion
    return json_response
