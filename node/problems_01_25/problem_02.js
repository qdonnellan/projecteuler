// return the sum of all the even terms in the 
// Fibonnaci sequence where the largest term in the seq.
// is less than the limit
function EvenFibSum(limit) {
    var sum = 0;
    var a = 1;
    var b = 2;
    while (b < limit) {
        if (b % 2 == 0) {
            sum += b;
        }
        // this is a cool way of setting (b -> a+b) and (a -> b)
        b = [a + b, a = b][0];
    };
    return sum;
};

module.exports.EvenFibSum = EvenFibSum;
