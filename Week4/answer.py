def make_language_preference_table(languages, preference):
    table = {}
    for i in range(len(languages)):
        table[languages[i]] = preference[i]
    return table

def make_grade_by_job_table(table):
    grade_by_job_lang = {}
    for t in table:
        t_list = t.split(' ')
        grade_by_lang = {}
        for i, lang in enumerate(t_list[1:]):
            grade_by_lang[lang] = 5 - i
        grade_by_job_lang[t_list[0]] = grade_by_lang
    return grade_by_job_lang


def solution(table, languages, preference):
    answer = ''
    grade_by_job_lang = make_language_preference_table(table)
    languages_preference = make_language_preference_table(languages, preference)
    preference_by_job = {}
    
    for key, value in grade_by_job_lang.items():
        score = 0
        for lang, grade in languages_preference.items():
            score += value[lang] * grade
        preference_by_job[key] = score
    return answer

solution(
    [
        "SI JAVA JAVASCRIPT SQL PYTHON C#", 
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"
    ],
        ["PYTHON", "C++", "SQL"],
        [7, 5, 5]
    )