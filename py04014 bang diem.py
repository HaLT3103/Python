class Student:
    def __init__(self,id, name, scores):
        self.id = id
        self.name = name
        self.scores = scores
        self.avg = self.calculate_average()

    def calculate_average(self):
        total = sum(self.scores[0:2])*2 + sum(self.scores[2:])
        return round(total / 12, 1)

    def get_grade(self):
        if self.avg >= 9:
            return 'XUAT SAC'
        elif 8 <= self.avg <= 8.9:
            return 'GIOI'
        elif 7 <= self.avg <= 7.9:
            return 'KHA'
        elif 5 <= self.avg <= 6.9:
            return 'TB'
        else:
            return 'YEU'

students = []
n = int(input())
for i in range(n):
    id = f'HS{i + 1:02d}'
    name = input()
    scores = list(map(float, input().split()))
    students.append(Student(id, name, scores))

students.sort(key=lambda x: (-x.avg, x.name))

for i, student in enumerate(students, start=1):
    print(f'{student.id} {student.name} {student.avg} {student.get_grade()}')
'''
12
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
Luu Thuy Nhi 1
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam 1
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh 1
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
Luu Thuy Nhi 2
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam 2
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh 2
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
Luu Thuy Nhi 3
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam 3
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh 3
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
'''