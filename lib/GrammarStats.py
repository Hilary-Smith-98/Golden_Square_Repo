class GrammarStats:
    def __init__(self):
        self.Tests_Run=0
        self.Passed_Tests=0
        
    def check(self, text):
        Result=False
        self.Tests_Run+=1
        if text[0].isupper() and text[-1] in '.!?':
            Result=True
            self.Passed_Tests+=1
        return  Result
            
    def percentage_good(self):
        return (self.Passed_Tests/self.Tests_Run)*100
