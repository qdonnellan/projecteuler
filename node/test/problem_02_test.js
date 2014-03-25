var prb = require("../problems_01_25/problem_02.js");
var assert = require("assert");

describe("Problem_02", function() {
    describe("#EvenFibSum()", function() {
        // There are 2 terms (2,8) in the Fib. Seq. 
        //less than 20; their sum is 10
        it("should return 10 when the input is 20", function() {
            assert.equal(10, prb.EvenFibSum(20));
        });
    });
});
