// return the sume of all numbers less than the limit which are
// multiples of three or five
function SumThreeFive(limit) {
    var sum = 0;
    for (i=1; i < limit; i++) {
        if (i % 3 == 0 || i % 5 ==0 ){
            sum += i;
        }
    };
    return sum;
};

module.exports.SumThreeFive = SumThreeFive;
