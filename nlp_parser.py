import spacy

nlp = spacy.load("en_core_web_sm")

def parse_command(command):
    doc = nlp(command.lower())
    action = None
    device = None
    location = None

    if "turn on" in command.lower():
        action = "ON"
    elif "turn off" in command.lower():
        action = "OFF"

    for token in doc:
        if token.text in ["light", "fan", "ac"]:
            device = token.text
        elif token.text in ["bedroom", "kitchen", "hall", "living"]:
            location = token.text

    return {
        "action": action,
        "device": device,
        "location": location
    }