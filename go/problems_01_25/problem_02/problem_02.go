package problem_02

// return the sum of all even terms of the Fibonnaci sequence (which
// contains no term larger than the limit passed)
func SumEvenFibTerms(limit int) int{
    // the running sum
    sum := 0

    // first term of Fibonnaci sequence
    a := 1

    // second term of Fibonnaci sequence
    b := 2

    for b < limit {
        if b%2 == 0 {
            sum += b
        }
        a, b = b, a+b // b is the new a! (fib style!)
    }

    return sum
}
