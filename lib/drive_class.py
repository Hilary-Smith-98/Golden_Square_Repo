class DiaryEntry:
    def __init__(self, title, contents):
        self.title=title
        self.contents=contents
        self.Words_Read=0
    def format(self):
        return (f'{self.title}: {self.contents}')

    def count_words(self):
        for char in self.contents:
            if char.isalpha():
                splitlist=(self.contents).split(' ')
                return len(splitlist)
        return 0

    def reading_time(self, wpm):
        return self.count_words()/wpm

    def reading_chunk(self, wpm, minutes):
        Words_To_Be_Read=wpm*minutes
        List_Of_Words=self.contents.split(' ')
        Output=' '.join(List_Of_Words[self.Words_Read:self.Words_Read+Words_To_Be_Read])
        if self.Words_Read+Words_To_Be_Read >= self.count_words():
            self.Words_Read=0
        else:
            self.Words_Read+=Words_To_Be_Read
        
        return Output