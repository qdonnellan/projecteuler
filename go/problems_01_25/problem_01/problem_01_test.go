package problem_01

import "testing"

// test the implementation of Project Euler problem 1
func TestProblem01(t *testing.T) {

    var result int

    // there are 4 multiples of 3 or 5 less than 10,
    // their sum is 3+5+6+9 = 23
    result = SumThreeFive(10)
    if result != 23 {
        t.Error("Expecting 23, instead received: ", result)
    }

    // there are 8 multiples of 3 or 5 less than 20,
    // their sum is 3+5+6+9+10+12+15+18 = 78
    result = SumThreeFive(20)
    if result != 78 {
        t.Error("Expected 78, instead recieved: ", result)
    }
}
