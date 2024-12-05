from furhat_remote_api import FurhatRemoteAPI
import json
import time

furhat = FurhatRemoteAPI("localhost")

# Load the JSON file content
with open('dialogues.json', 'r') as file:
    conversation_data = json.load(file)

blinking_gesture = {
    "frames": [
        {
            "time": [0.33],
            "params": {
                "BLINK_LEFT": 1.0
            }
        },
        {
            "time": [0.67],
            "params": {
                "reset": True
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
}

current_index = 0
conversation = conversation_data["conversation"]
linetext=""
while current_index < len(conversation):
    print(current_index)
    # Get the current response
    response = conversation[current_index]["response"]
    
    # Handle the response based on its type
    if response["type"] == "line":
        linetext=response["content"]
        furhat.say(text=linetext)
        print(f"Robot said: {linetext}") 
       # For debugging
    elif response["type"] == "combo":
        # Iterate through contents and their respective types
        contents = response["content"]["contents"]
        types = response["content"]["types"]
        for content, content_type in zip(contents, types):
            if content_type == "line":
                linetext=content
                furhat.say(text=linetext)
                print(f"Robot said: {linetext}")  
                # For debugging
            elif content_type == "gesture":
                if content == "blink":
                    furhat.gesture(body=blinking_gesture)
                else:
                    furhat.gesture(name=content)
    
    
    # Wait for the robot to finish speaking
     # Adjust this sleep time if needed for robot's speech duration
    
    # Infinite loop to listen until word count > 0
    while True:
        time.sleep(0.533 * len(linetext.split(' '))) 
        result = furhat.listen()
        print(len(linetext.split(' ')))
        
        result_statement = result.__dict__['_message']
        word_count = len(result_statement.split())  # Calculate word count
        
        print(f"User said: {result_statement}")  # For debugging
        print(f"Word count: {word_count}")  # Print word count
        
        if word_count > 0:  # Exit loop when valid input is detected
            break
    
    current_index += 1

furhat.gesture(body=blinking_gesture)
furhat.say(text="That's all I have for now. Goodbye!")
