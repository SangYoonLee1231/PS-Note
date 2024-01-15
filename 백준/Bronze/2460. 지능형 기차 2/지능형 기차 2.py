minus_people = []
plus_people = []
max_people = 0
people = 0

for _ in range(10):
    m, p = tuple(map(int, input().split()))
    minus_people.append(m)
    plus_people.append(p)

for i in range(10):
    people -= minus_people[i]
    people += plus_people[i]
    max_people = max(max_people, people)

print(max_people)
