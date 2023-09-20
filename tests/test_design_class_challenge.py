import pytest
from lib.design_class_challenge import Tracklist

"""
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
"""

def test_empty_list():
    playlist = Tracklist()
    assert playlist.see_list() == []

def test_add_song():
    playlist = Tracklist()
    playlist.add('Gold')
    assert playlist.see_list() == ['Gold']

def test_add_multiple_songs():
    playlist = Tracklist()
    playlist.add('Gold')
    playlist.add('Here Comes The Rain Again')
    playlist.add('Edge of Seventeen')
    playlist.add('The Chain')
    assert playlist.see_list() == ['Gold', 'Here Comes The Rain Again', 'Edge of Seventeen', 'The Chain']

def test_error():
    playlist = Tracklist()
    with pytest.raises(Exception) as e:
        playlist.add(37)
    error_message = str(e.value)
    assert error_message == 'That\'s not a song!'