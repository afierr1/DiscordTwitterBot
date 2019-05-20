
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

interpreter = RasaNLUInterpreter('models/current/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('models/dialogue', interpreter=interpreter)

responses = agent.handle_message("Hello")
for r in responses:
    print(r)