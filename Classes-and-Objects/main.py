class Student():
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print('new name is ' + change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print('your age is', change_age)

    def add_track(self, add_track):
        self.add_track = add_track
        print('your track is ', self.tracks, 'and', add_track)

    def get_score(self):
        print('your score is ', self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
Bob.change_name('peter')
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()