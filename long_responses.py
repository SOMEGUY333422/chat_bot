import random

coconuts = "I was coded with python!"
longest = " i am a basic chat bot :)"

def unknown():
    response = ['Could you please re-phrase that?',
    "....",
    "sounds about right",
    "What does that mean?"][random.randrange(4)]
    
    return response