from furhat_remote_api import FurhatRemoteAPI
furhat = FurhatRemoteAPI("localhost")
voices = furhat.get_voices()

# Select a character for the virtual Furhat
furhat.set_face(character="Isabel", mask="adult")

# Set the voice of the robot
furhat.set_voice(name='Joanna')

# Have Furhat greet the user
furhat.say(text="Hi, my name is Furhat, how are you", blocking=True)

# Instruct Furhat to smile and nod.
furhat.gesture(name="Nod")
furhat.gesture(name="Smile")

# Ask a question to the user through Furhat
furhat.say(text="What is the weather like today?", blocking=True)

# Listen to the user's response
response = furhat.listen()

# Check if listening was successful
if response.success and response.message:
    print("User said:", response.message)
else:
    print("Listening failed or no speech detected.")
