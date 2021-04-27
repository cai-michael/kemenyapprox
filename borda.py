"""
Implements the Borda Count
"""

import time
import datetime
from collections import defaultdict

def borda_count(profile):
    """
    Implements the Borda count by calculating all Borda scores
    """

    print('\nApplying Borda Count to the Profile...')
    # Start timer
    time_start = time.perf_counter()

    num_candidates = len(profile[0])
    borda_scores = defaultdict(int)

    for vote in profile:
        for rank, candidate in enumerate(vote):
            borda_scores[candidate] += (num_candidates - rank - 1)

    sorted_scores = sorted(borda_scores.items(), key=lambda item: item[1], reverse=True)
    final_ranking = [pair[0] for pair in sorted_scores]

    print("The winning ranking is as follows: ")
    winning_ranking_stringified = [str(i) for i in final_ranking]
    print(", ".join(winning_ranking_stringified))

    # Calculate time required to finish
    time_finish = time.perf_counter()
    time_elapsed = datetime.timedelta(seconds = (time_finish - time_start))
    print(f"Applying the Borda Count took {time_elapsed}")
