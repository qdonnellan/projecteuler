from common_methods import check_if_multiple_of_3_or_5

class Problem01:
    limit = 0
    known_multiples = []

    def find_multiples_of_3_or_5_less_than_limit(self):
        for candidate in range(1, self.limit):
            if check_if_multiple_of_3_or_5(candidate):
                self.known_multiples.append(candidate)

    def sum_multiples(self):
        return sum(self.known_multiples)