class student:
    def __init__(self, name, correct, submit):
        self.name = name
        self.correct = correct
        self.submit = submit
    def __lt__(self, other):
        if self.correct != other.correct:
            return self.correct > other.correct
        if self.submit != other.submit:
            return self.submit < other.submit
        return self.name < other.name

n = int(input())
a = []
for i in range(n):
    name = input().strip()
    correct, submit = map(int, input().split())
    a.append(student(name, correct, submit))
a.sort()
for i in a:
    print(str(i.name) + " " + str(i.correct) + " " + str(i.submit))