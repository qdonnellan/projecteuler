var prb = require("../problems_01_25/problem_01.js");
var assert = require("assert");

describe("Problem_01", function() {
    describe("#SumThreeFive()", function() {
        it("should return 23 when the input is 10", function() {
            assert.equal(23, prb.SumThreeFive(10));
        });
    });
});
