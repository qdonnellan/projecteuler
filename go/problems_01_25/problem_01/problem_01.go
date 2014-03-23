package problem_01


// find all numbers that are multiples of 3 or 5 less than the limit
// return the sum of these numbers
func SumThreeFive(limit int) int{
    sum := 0
    for i := 0; i < limit; i++ {
        if (i%3 == 0) || (i%5 == 0) {
            sum += i
        }
    }
    return sum
}
