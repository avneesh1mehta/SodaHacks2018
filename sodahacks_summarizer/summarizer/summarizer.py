from Algorithmia import client
class Summarizer:

    def __init__(self):
        self.summarization_algorithm = client("simFaH42Oe6xcB+ny9tjF+TiYdk1").algo("nlp/Summarizer/0.1.6")

    def summary(self, contents, num_sentences):
        VALID = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM:;_-,.!?()']%$@ \n"
        contents = ''.join(char for char in contents if char in VALID)
        contents.replace('\n', ' ')
        contents = ' '.join(contents.split())
        summary = self.summarization_algorithm.pipe([contents, num_sentences]).result
        return summary
