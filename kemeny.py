"""
Implements the Kemeny Rule and various heuristics
"""

import time
import datetime
from itertools import combinations, permutations
from multiprocessing import Pool
import functools
from collections import defaultdict
from matrix import generate_zeros_matrix, matrix_multiplication

NUM_WORKERS = 2
STATIONARY_DISTRIBUTION_ITERATIONS = 1000

def kendall_tau_distance(ranking_a, ranking_b):
    """
    Determines the Kendell Tau Distance between two orderings
    """
    distance = 0
    num_candidates = len(ranking_a)
    pairs = combinations(range(1, num_candidates + 1), 2)
    for alt_x, alt_y in pairs:
        a_order = ranking_a.index(alt_x) - ranking_a.index(alt_y)
        b_order = ranking_b.index(alt_x) - ranking_b.index(alt_y)
        if a_order * b_order < 0:
            distance += 1
    return distance

def calculate_ranking_score(ranking, profile):
    """
    Calculates the ranking score for a particular strict ordering
    """
    ranking_score = 0

    for profile_ranking in profile:
        ranking_score += kendall_tau_distance(ranking, profile_ranking)

    return ranking_score

def kemeny_rule(profile, num_workers=1):
    """
    Implements the kemeny rule by calculating all Kendell-Tau distances
    """
    print('\nApplying the Kemeny Rule to the Profile...')

    # Start timer
    time_start = time.perf_counter()

    num_candidates = len(profile[0])

    ranking_scores = []

    rank_permutations = list(permutations(range(1, num_candidates + 1)))

    calculate_scores = functools.partial(calculate_ranking_score, profile=profile)
    with Pool(num_workers) as worker_pool:
        ranking_scores = worker_pool.map(calculate_scores, rank_permutations)

    min_ranking_score = min(ranking_scores)
    win_idx = [index for index, score in enumerate(ranking_scores) if score == min_ranking_score]

    print("The winning ranking(s) are as follows: ")
    for index in win_idx:
        winning_ranking = rank_permutations[index]
        winning_ranking_stringified = [str(i) for i in winning_ranking]
        print(", ".join(winning_ranking_stringified))

    # Calculate time required to finish
    time_finish = time.perf_counter()
    time_elapsed = datetime.timedelta(seconds = (time_finish - time_start))
    print(f"Applying the Kemeny Rule took {time_elapsed}")

def determine_pairwise_victories(profile):
    """
    Determines the pairwise victories for candidates
    Returns a dictionary indexed by tuples of candidates
    """
    pairwise_victories = defaultdict(int)
    num_candidates = len(profile[0])
    candidiate_pairs = list(permutations(range(1, num_candidates + 1), 2))
    for pair in candidiate_pairs:
        for vote in profile:
            if vote.index(pair[0]) < vote.index(pair[1]):
                pairwise_victories[pair] += 1
    return pairwise_victories

def create_transition_matrix(pairwise_victories, num_candidates, num_votes, mc_type):
    """
    Generates a transition matrix based on the MC heuristic type

    Type 1:
    The transition probability of a to b is:
    1 / # Candidates if b is preferred to a at some point
    0 otherwise
    The transition probability from a to a is 1 - Sum of all other transitions

    Type 2:
    The transition probability of a to b is:
    1 / # Candidates if the majority of ballots prefer b to a
    0 otherwise
    The transition probability from a to a is 1 - Sum of all other transitions

    Type 3:
    The transition probability of a to b is:
    Summation of all orderings where
    sum(orderings where b is preferred to a) / Orderings * candidates
    The transition probability from a to a is 1 - Sum of all other transitions
    """

    # Put 0's on transition matrix
    transition_matrix = generate_zeros_matrix(num_candidates, num_candidates)

    # Populate transition probabilities in the matrix
    candidiate_pairs = list(permutations(range(1, num_candidates + 1), 2))

    # Based on preferences of a and b assign probability of a -> b
    if mc_type == 1:
        for first, second in candidiate_pairs:
            if pairwise_victories[(second, first)] > 0:
                probability = 1 / num_candidates
            else:
                probability = 0
            transition_matrix[first - 1][second - 1] = probability

    elif mc_type == 2:
        for first, second in candidiate_pairs:
            if pairwise_victories[(second, first)] > (num_votes // 2):
                probability = 1 / num_candidates
            else:
                probability = 0
            transition_matrix[first - 1][second - 1] = probability

    elif mc_type == 3:
        for first, second in candidiate_pairs:
            probability = pairwise_victories[(second, first)] / (num_votes * num_candidates)
            transition_matrix[first - 1][second - 1] = probability

    # Determine the probability of a self-transition
    for candidate in range(1, num_candidates + 1):
        self_transition_probability = 1 - sum(transition_matrix[candidate - 1])
        transition_matrix[candidate - 1][candidate - 1] = self_transition_probability

    return transition_matrix

def markov_heuristic(profile, mc_type):
    """
    Applies the Markov Chain Heuristic to a Profile using a transition function of mc_type
    """

    print(f'\nApplying the MC{mc_type} Markov Heuristic to the Profile...')

    # Start timer
    time_start = time.perf_counter()

    num_candidates = len(profile[0])
    num_votes = len(profile)

    # Determine pairwise victories for each pair of candidates
    pairwise_wins = determine_pairwise_victories(profile)

    transition_matrix = create_transition_matrix(pairwise_wins, num_candidates, num_votes, mc_type)

    # Put the probability matrix to a high power to find the stationary distribution
    stationary_distribution = transition_matrix.copy()
    for _ in range(STATIONARY_DISTRIBUTION_ITERATIONS):
        stationary_distribution = matrix_multiplication(stationary_distribution, transition_matrix)

    final_probabilities = stationary_distribution[0]
    prob_tuples = [(idx + 1, prob) for idx, prob in enumerate(final_probabilities)]
    prob_tuples.sort(key=lambda x: x[1], reverse=True)
    final_ranking = [pair[0] for pair in prob_tuples]

    print("The winning ranking is as follows: ")
    winning_ranking_stringified = [str(i) for i in final_ranking]
    print(", ".join(winning_ranking_stringified))

    # Calculate time required to finish
    time_finish = time.perf_counter()
    time_elapsed = datetime.timedelta(seconds = (time_finish - time_start))
    print(f"Applying the MC{mc_type} Markov Model took {time_elapsed}")
