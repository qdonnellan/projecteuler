package problem_02

import (
    "fmt"
    "testing"
    )

// test the problem 2 case where the largest term in the sequence is 20
func TestProblem02CaseWhereLimitIs20(t *testing.T) {
    result := SumEvenFibTerms(20)
    if result != 10 {
        t.Error(fmt.Sprintf(
            "The sum should be 10; received %d instead",
            result,
            ))
    }
}

// test the problem 2 case where the largest term in the sequence is 100
func TestProblem02CaseWhereLimitIs100(t *testing.T) {
    result := SumEvenFibTerms(100)
    if result != 44 {
        t.Error(fmt.Sprintf(
            "The sum should be 44, recieved %d instead",
            result,
            ))
    }
}
