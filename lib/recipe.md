1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


2. Design the Class Interface
class Tracklist:

def __init__(self):
    pass
    #side effect: creates an empty list

def add(self, track):
    pass
    #parameter:
        #track: string, adds string to list
    #if not string, raises error

def see_list(self):
    pass
    #returns: list of songs added


3. Create Examples as Tests

Initially, an empty list is created:

playlist = Tracklist()
playlist.see_list = []

If we add a song, it is reflected in the list:

playlist = Tracklist()
playlist.add('Gold')
playlist.see_list() => ['Gold']

If we add multiple songs, they should all be reflected in the list:

playlist = Tracklist()
playlist.add('Gold')
playlist.add('Here Comes The Rain Again')
playlist.add('Edge of Seventeen')
playlist.add('The Chain')
playlist.see_list() => ['Gold', 'Here Comes The Rain Again', 'Edge of Seventeen', 'The Chain']

If we add something that's not a song title, it raises an error

playlist = Tracklist()
playlist.add(37) => 'That's not a song!'


4. Implement the Behaviour