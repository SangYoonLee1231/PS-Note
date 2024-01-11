n, m = tuple(map(int, input().split()))

not_heard = [
    input()
    for _ in range(n)
]

not_seen = [
    input()
    for _ in range(m)
]

not_heard = set(not_heard)
not_seen = set(not_seen)

answer = not_heard.intersection(not_seen)

# for elem in not_seen:
#     if elem in not_heard:
#         answer.append(elem)

answer = list(answer)
answer.sort()

print(len(answer))
for elem in answer:
    print(elem)
