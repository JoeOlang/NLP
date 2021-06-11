"""
A chatbot created using AIML, an XML based markup language meant to create artificial intelligent applications.

"""

import os
import aiml

brain_file = "brain.dump"

k = aiml.Kernel()

if os.path.exists(brain_file):
    print("Loading from brain file: " + brain_file)
    k.loadBrain(brain_file)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + brain_file)
    k.saveBrain(brain_file)


while True:
    input_text = input(" Human > ")
    response = k.respond(input_text)
    print(" Bot > " + response)
