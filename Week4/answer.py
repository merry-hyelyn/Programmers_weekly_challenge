def make_language_preference_table(languages, preference):
    table = {}
    for i in range(len(languages)):
        table[languages[i]] = preference[i]
    return table

def solution(table, languages, preference):
    answer = ''
    languages_preference = make_language_preference_table(languages, preference)
    '''
    다른 사람의 풀이를 보고 zip을 이용하여 언어 선호도 테이블 생성
    신기방기..
    '''
    use_zip_language_preference = {lang : pref for lang, pref in zip(languages, preference)}
    
    prev_score = 0
    for row in table:
        score = 0
        data = row.split(' ')
        for k, v in languages_preference.items():
            if k in data:
                grade = 6 - data.index(k)
                score += grade * v
        if prev_score < score:
            prev_score = score
            answer = data[0]
        if prev_score == score:
            answer = data[0] if answer > data[0] else answer
    return answer
