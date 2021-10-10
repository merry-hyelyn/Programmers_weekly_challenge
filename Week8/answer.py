def solution(sizes):
    cards = [(max(size), min(size)) for size in sizes]
    width, height = zip(*cards)
    return max(width) * max(height)


print("answer : ", solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print("answer : ", solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print("answer : ", solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
