from app.services.intent_classifier import IntentClassifier
from app.services.response_builder import ResponseBuilder
from app.services.fallback import FallbackService

classifier = IntentClassifier()
builder = ResponseBuilder()
fallback = FallbackService()

def process_message(message):
    intent = classifier.classify(message)
    response = builder.build(intent)

    if response:
        return response

    return fallback.handle(message)

