import pandas as pd
from src.Speaker import Speaker


class Section:

    def __init__(self):
        self.duration = 0
        self.circumstances = {}
        self.get_circumstances()
        self.speaker = Speaker()

    @staticmethod
    def random_item(elements):
        return elements.dropna().sample().item()

    def get_circumstances(self):
        df = pd.read_csv("resources/section_circumstances.csv")

        for (title, elements) in df.iteritems():
            self.circumstances[title] = self.random_item(elements)

    def speak_circumstances(self):
        for (category, circumstance) in self.circumstances.items():
            self.speaker.speak(category)
            self.speaker.speak(circumstance)
