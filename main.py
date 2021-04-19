from kemeny import kemeny_rule

def load_voting_profile(filename):
    profile = []

    input_file = open(filename, 'r')

    for line in input_file:
        string_array = line.split(',')
        ranking = [int(num_str) for num_str in string_array]
        profile.append(ranking)

    return profile

def main():
    """
    This program implements Kemeny-Young as well as a few approximation algorithms.
    """

    file_name = "sushi_data.txt"

    # Load voting profile P for the data
    profile = load_voting_profile(file_name)

    # Perform the original Kemeny Rule using Kendall-Tau Distances
    kemeny_rule(profile)

    # Perform a Markov chain based 

if __name__ == "__main__":
    main()
