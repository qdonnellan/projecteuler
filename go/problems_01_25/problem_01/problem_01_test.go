package problem_01

import "testing"

func TestProblem01(t *testing.T) {
    // testing integers less than 10
    // there are 4 multiples of 3 or 5 less than 10,
    // their sum is 23
    var result int
    result = SumThreeFive(10)
    if result != 23 {
        t.Error("Expecting 23, instead received: ", result)
    }
}
