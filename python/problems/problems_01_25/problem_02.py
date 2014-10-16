class Problem02:
    """
    find the sum of all even terms in the Fibonacci series where
    the largest term is less than some limit
    """

    limit = 3
    fibonacci_series = []
    even_terms = []
    solution = None

    def solve_problem(self):
        self.construct_fibonacci_series_less_than_limit()
        self.construct_series_of_even_terms()
        self.solution = sum(self.even_terms)

    def construct_fibonacci_series_less_than_limit(self):
        seed_terms = [1, 2]
        self.fibonacci_series.extend(seed_terms)
        while not self.next_term_exceeds_limit():
            self.fibonacci_series.append(self.next_term_in_series())

    def construct_series_of_even_terms(self):
        self.even_terms = [x for x in self.fibonacci_series if x % 2 == 0]

    def next_term_exceeds_limit(self):
        if self.next_term_in_series() > self.limit:
            return True
        else:
            return False

    def next_term_in_series(self):
        last_term = self.fibonacci_series[-1]
        next_to_last_term = self.fibonacci_series[-2]
        return last_term + next_to_last_term
