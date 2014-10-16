from common_methods import number_is_multiple_of_3_or_5

class Problem01:
    """
    find the sum of all multiples of 3 or 5 less than some limit
    """

    limit = 0
    known_multiples = []
    solution = None

    def solve_problem(self):
        self.find_multiples_of_3_or_5_less_than_limit()
        self.solution = self.sum_multiples()

    def find_multiples_of_3_or_5_less_than_limit(self):
        for candidate in range(1, self.limit):
            if number_is_multiple_of_3_or_5(candidate):
                self.known_multiples.append(candidate)

    def sum_multiples(self):
        return sum(self.known_multiples)