package hacktwk.calculator;

import hacktwk.calculator.flag.HackTWK;

public class Validator {
    public double validate(String a, String b, String op) {
        return new HackTWK().calc(a, b, op);
    }
}
