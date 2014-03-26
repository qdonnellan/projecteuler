var prb = require("../problems_01_25/problem_01.js");
var assert = require("assert");

describe("Problem_01", function() {
    describe("#SumThreeFive()", function() {
        // The multiples of 3 or 5 less than 10 are:
        // 3, 5, 6, and 9. Their sum is 23
        it("should return 23 when the input is 10", function() {
            assert.equal(23, prb.SumThreeFive(10));
        });
    });
});
