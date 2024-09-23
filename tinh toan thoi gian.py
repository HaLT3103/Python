from datetime import datetime
class gamer:
    def __init__(self, id, name, start, end):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
    def calculate_time(self):
        start_hours, start_minutes = map(int, self.start.split(':'))
        end_hours, end_minutes = map(int, self.end.split(':'))

        total_start_minutes = start_hours * 60 + start_minutes
        total_end_minutes = end_hours * 60 + end_minutes

        difference_in_minutes = total_end_minutes - total_start_minutes

        hours = difference_in_minutes // 60
        minutes = difference_in_minutes % 60

        return f"{hours} giờ {minutes} phút"
    def __lt__(self, other):
        return self.calculate_time() > other.calculate_time()

n = int(input())
a = []
for i in range(n):
    id = input()
    name = input()
    stat = input()
    end = input()
    a.append(gamer(id, name, stat, end))
a.sort()
for x in a:
    print(f"{x.id} {x.name} {x.calculate_time()}")