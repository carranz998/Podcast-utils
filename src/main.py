from src.Podcast import Podcast

if __name__ == "__main__":
    p = Podcast()
    p.assign_section_durations()
    p.say_every_section()
