import dialogflow

project_id = "chatbot-b03e9"

#client = dialogflow.AgentsClient()
#parent = client.project_path(project_id)
#response = client.import_agent(parent)

session_client = dialogflow.SessionsClient()


session_id = "3530"
session = session_client.session_path(project_id, session_id)
print('Session path: {}\n'.format(session))
language_code = "EN"
texts = ["Hi!", "Hei!", "Tere päevast!", "Hola!"]



for text in texts:
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
