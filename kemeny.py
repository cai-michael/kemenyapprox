import time
import datetime
import itertools
from multiprocessing import Pool
import functools

i = 0

def kendall_tau_distance(a, b, num_candidates):
    distance = 0
    pairs = itertools.combinations(range(1, num_candidates), 2)
    for x, y in pairs:
        a_order = a.index(x) - a.index(y)
        b_order = b.index(x) - b.index(y)
        if a_order * b_order < 0:
            distance += 1
    return distance

def calculate_ranking_score(ranking, profile, num_candidates):
    ranking_score = 0

    for profile_ranking in profile:
        ranking_score += kendall_tau_distance(ranking, profile_ranking, num_candidates)

    return ranking_score

def kemeny_rule(profile):
    """
    Implements the kemeny rule by calculating all Kendell-Tau distances
    """
    # Start timser
    time_start = time.perf_counter()

    num_candidates = len(profile[0])

    ranking_scores = []

    permutations = list(itertools.permutations(range(1, num_candidates + 1)))

    calculate_scores = functools.partial(calculate_ranking_score, profile=profile, num_candidates=num_candidates)
    with Pool() as worker_pool:
        ranking_scores = worker_pool.map(calculate_scores, permutations)

    """
    i = 0
    for ranking in permutations:
        ranking_scores.append(calculate_ranking_score(ranking, profile, num_candidates))
        i += 1
        if i % 10000 == 0:
            print(i)
    """

    min_ranking_score = min(ranking_scores, key = lambda t: t[1])
    win_indices = [index for index, score in enumerate(ranking_scores) if score == min_ranking_score]

    print("The winning ranking(s) are as follows: ")
    for index in win_indices:
        winning_ranking = permutations[index]
        print(", ".join(winning_ranking))

    # Calculate time required to finish
    time_finish = time.perf_counter()
    time_elapsed = datetime.timedelta(seconds = (time_finish - time_start))
    print(f"Applying the Kemeny Rule took {time_elapsed}")