import time

import numpy as np

from src.Section import Section


class Podcast:

    def __init__(self):
        self.duration = np.random.randint(30, 51) * 60
        self.number_of_sections = np.random.randint(10, 21)
        self.sections = [Section() for i in range(self.number_of_sections)]

    def random_proportions(self):
        return np.random.dirichlet(np.ones(self.number_of_sections), 1)[0]

    def assign_section_durations(self):
        time_proportions = self.random_proportions()

        for i in range(self.number_of_sections):
            self.sections[i].duration = time_proportions[i] * self.duration

    def say_every_section(self):
        for i in range(self.number_of_sections):

            self.sections[i].speak_circumstances()
            time.sleep(self.sections[i].duration)
