var prb = require("../problems_01_25/problem_03.js");
var assert = require("assert");

describe("Problem_03", function() {
    describe("#LargestPrimeFactor()", function() {
        // the largest prime factor of 10 is 5
        it("should return 5 when the input is 10", function() {
            assert.equal(5, prb.LargestPrimeFactor(10));
        });

        // the largest prime factor of 13195 is 29
        it("should return 5 when the input is 10", function() {
            assert.equal(29, prb.LargestPrimeFactor(13195));
        });
    });
});
