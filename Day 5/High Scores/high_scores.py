def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]

def personal_top_three(scores):
    scores.sort()
    scores.reverse()
    return scores[:3]
