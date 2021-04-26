"""
Compares the Kemeny-Rule with a heuristic method
"""

from kemeny import kemeny_rule

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

def main():
    """
    This program implements Kemeny-Young as well as a few approximation algorithms.
    """

    file_name = "sushi_data.txt"
    short_file_name = "sushi_data.txt"

    # Load voting profile P for the data
    profile = load_voting_profile(file_name)

    # Perform the original Kemeny Rule using Kendall-Tau Distances
    kemeny_rule(profile)

    # Perform a Markov chain based 

if __name__ == "__main__":
    main()
