from furhat_remote_api import FurhatRemoteAPI

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
furhat = FurhatRemoteAPI("localhost")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')

# Listen to user speech and return ASR result
result = furhat.listen()
result_statement = result.__dict__['_message']

print(result_statement)
furhat.say(text = result_statement)

# Perform a named gesture
furhat.gesture(name="BigSmile")
