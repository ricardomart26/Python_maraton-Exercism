def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    total = 0
    size = len(student_scores)
    i = 0
    for i in student_scores:
        total = total + i
    return round(total/size)


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    count = 0
    for i in student_scores:
        if i <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    count = 0
    student_scores.sort()
    for index, i in student_scores:
        if i > threshold:
            count = index
            break
    return student_scores[index:]

def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    arr = list()
    diff = highest - 40
    ret = round(diff / 4)
    start = 41
    for i in range(4):
        arr.append(start+(ret * i))
    return arr


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    pass


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    pass


print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
print(letter_grades(100))
print(letter_grades(88))
