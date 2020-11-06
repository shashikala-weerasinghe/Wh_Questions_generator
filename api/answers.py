import spacy
import Levenshtein


nlp = spacy.load('en')


class AnswerScoring:
    def __init__(self, marking_answer, student_answer):
        self._score = 0
        self._marking_answer = nlp(marking_answer)
        self._student_answer = nlp(student_answer)

    @property
    def score(self):
        self._marking_answer = nlp(' '.join([str(t) for t in self._marking_answer if not t.is_stop]))
        self._student_answer = nlp(' '.join([str(t) for t in self._student_answer if not t.is_stop]))
        return round(self._marking_answer.similarity(self._student_answer),2)
