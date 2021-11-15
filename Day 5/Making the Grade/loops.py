def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """ 
    return [round(num) for num in student_scores]


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    return sum(i <= 40 for i in student_scores)


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    if not student_scores:
        return []
    if max(student_scores) < threshold:
        return []
    return [i for i in student_scores if i >= threshold]


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    ret = round(highest - 40 / 4)
    return [41 +(ret * i) for i in range(4)]

def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    return [
        str(index + 1) + ". " + i + ": " + str(student_scores[index])
        for index, i in enumerate(student_names)
    ]


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for i in student_info:
        if i[1] == 100:
            return i
    return "No perfect score."

print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
print(letter_grades(100))
print(letter_grades(88))
