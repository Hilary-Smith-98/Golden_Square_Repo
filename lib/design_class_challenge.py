class Tracklist:
    def __init__(self):
        self.tracklist = []

    def add(self, track):
        if not isinstance(track, str):
            raise Exception('That\'s not a song!')
        self.tracklist.append(track)

    def see_list(self):
        return self.tracklist
