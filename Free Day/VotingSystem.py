from collections import defaultdict

class VotingSystem:
    def __init__(self):
        # trump -> 40k votes (total)
        self.candidate_to_total_votes = defaultdict(int)
        # state -> state object
        self.state_to_state_info = {}
        # clinton -> 270 votes (electoral)
        self.candidate_to_electoral_votes = defaultdict(int)

    def add_state(self, state, electoral_votes):
        self.state_to_state_info[state] = State(electoral_votes)

    def add_votes(self, state, candidate, votes):
        self.state_to_state_info[state].add_votes(candidate, votes)

    def pick_winner(self):
        max_candidate_electoral = ""
        max_candidate_electoral_votes = 0
        max_candidate_total = ""
        max_candidate_total_votes = 0
        for state, state_object in self.state_to_state_info:
            max_candidate = ""
            max_candidate_votes = 0
            for candidate, candidate_votes in state_object.candidate_to_votes:
                if candidate_votes > max_candidate_votes:
                    max_candidate = candidate
                    max_candidate_votes = candidate_votes
                self.candidate_to_total_votes[candidate] += candidate_votes
                if self.candidate_to_total_votes[candidate] > max_candidate_total_votes:
                    max_candidate_total_votes = self.candidate_to_total_votes
                    max_candidate_total = candidate
            self.candidate_to_electoral_votes[max_candidate] += state_object.electoral
            if self.candidate_to_electoral_votes[max_candidate] > max_candidate_electoral_votes:
                max_candidate_electoral_votes = self.candidate_to_electoral_votes
                max_candidate_electoral = max_candidate
        if max_candidate_electoral_votes >= 270:
            return max_candidate_electoral
        else:
            return max_candidate_total

class State:
    def __init__(self, electoral_votes):
        self.electoral = electoral_votes
        self.candidate_to_votes = defaultdict(int)

    def add_votes(self, candidate, votes):
        self.candidate_to_votes[candidate] += votes
