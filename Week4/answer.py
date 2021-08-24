def make_language_preference_table(languages, preference):
    table = {}
    for i in range(len(languages)):
        table[languages[i]] = preference[i]
    return table

def solution(table, languages, preference):
    answer = ''
    languages_preference = make_language_preference_table(languages, preference)
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

print(solution(
    [
        "SI JAVA JAVASCRIPT SQL PYTHON C#", 
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"
    ],
        ["PYTHON", "C++", "SQL"],
        [7, 5, 5]
    ))

print(solution(
    [
        "SI JAVA JAVASCRIPT SQL PYTHON C#", 
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"
    ],
    ["JAVA", "JAVASCRIPT"],
    [7, 5],
))