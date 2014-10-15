// return the largest prime factor of a number
function LargestPrimeFactor(n) {
    // i is the current factor
    for (i=2; i*i < n; i++) {
        while (n%i == 0) {
            n = n/i;
        }
    };
    return n;
};

module.exports.LargestPrimeFactor = LargestPrimeFactor;
