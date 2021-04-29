"""
Compares the Kemeny-Rule with a heuristic method
"""

import sys
from kemeny import kemeny_rule, markov_heuristic
from borda import borda_count

def load_voting_profile(filename):
    """
    Loads a voting profile of the form:
    x,a,b,...,n
    Where x is the number of that particular kind of ballot
    and a-n are numerics corresponding with candidates
    """
    profile = []

    input_file = open(filename, 'r')

    for line in input_file:
        string_array = line.split(',')
        ranking = [int(num_str) for num_str in string_array]
        for _ in range(ranking[0]):
            profile.append(ranking[1:])

    return profile

def simplify_profile(profile, num_candidates):
    """
    Simplifies a profile to only contain a certain number of candidates
    """
    simplified_profile = []
    current_candidates = len(profile[0])
    for vote in profile:
        modified_vote = vote.copy()
        # Remove candidates
        for i in range(num_candidates + 1, current_candidates + 1):
            modified_vote.remove(i)
        simplified_profile.append(modified_vote)
    return simplified_profile


def main():
    """
    This program implements Kemeny-Young as well as an approximation algorithm.
    """

    file_name = "sushi_data.txt"
    simplified_num_candidates = int(sys.argv[1])

    # Load voting profile P for the data
    profile = load_voting_profile(file_name)

    # Create a smalller profile for the brute-force approach
    short_profile = simplify_profile(profile, simplified_num_candidates)

    # Perform the original Kemeny Rule using Kendall-Tau Distances
    kemeny_rule(short_profile)

    # Perform the Borda Count, a 5-Approximation of the Kemeny Rule
    borda_count(short_profile)

    # Perform Markov chain based approximations of the Kemeny Rule
    markov_heuristic(short_profile, 1)
    markov_heuristic(short_profile, 2)
    markov_heuristic(short_profile, 3)

if __name__ == "__main__":
    main()
