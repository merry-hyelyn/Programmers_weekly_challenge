def check_turn_size(w, h, card_w, card_h):
    if card_w <= w and card_h <= h:
        return True
    return False


def solution(sizes):
    answer = 0
    width, height = zip(* sizes)
    max_card = max([k * v for k, v in sizes])
    wallets = [(w, h) for w in width for h in height if w * h >= max_card]
    for w, h in sorted(wallets, reverse=True):
        count = 0
        for size in sizes:
            card_w, card_h = size
            if card_w > w or card_h > h:
                if not check_turn_size(h, w, card_w, card_h):
                    count += 1
        if count == 0:
            answer = w * h
    return answer
# size 케이스가 모두 통과해야함!


print("answer : ", solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print("answer : ", solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print("answer : ", solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
