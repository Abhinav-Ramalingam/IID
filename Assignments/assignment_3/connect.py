from furhat_remote_api import FurhatRemoteAPI
import json
import time

furhat = FurhatRemoteAPI("localhost")

# Load the JSON file content
with open('dialogues.json', 'r') as file:
    conversation_data = json.load(file)

blinking_gesture = body={
    "frames": [
        {
            "time": [
                0.33
            ],
            "params": {
                "BLINK_LEFT": 1.0
            }
        },
        {
            "time": [
                0.67
            ],
            "params": {
                "reset": True
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    }

# Get the voices on the robot
#voices = furhat.get_voices()

current_index = 0
conversation = conversation_data["conversation"]

while current_index < len(conversation):
    print(current_index)
    # Get the current response
    response = conversation[current_index]["response"]

    # Handle the response based on its type
    if response["type"] == "line":
        furhat.say(text=response["content"])
    elif response["type"] == "combo":
        # Iterate through contents and their respective types
        contents = response["content"]["contents"]
        types = response["content"]["types"]
        for content, content_type in zip(contents, types):
            if content_type == "line":
                furhat.say(text=content)
                print(f"Robot said: {content}")  # For debugging
            elif content_type == "gesture":
                if content == "blink":
                    furhat.gesture(body=blinking_gesture)
                else:
                    furhat.gesture(name=content)
  
    result = furhat.listen()
    time.sleep(5)
    result_statement = result.__dict__['_message']
    print(f"User said: {result_statement}")  # For debugging
    
    current_index += 1

furhat.gesture(body=blinking_gesture)
furhat.say(text="That's all I have for now. Goodbye!")

