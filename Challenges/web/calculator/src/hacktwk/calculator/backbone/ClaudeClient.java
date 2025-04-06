package hacktwk.calculator.backbone;

public class ClaudeClient {
    public double sendCalculationRequest(String a, String b, String op) {
        return buildRequest(a, b, op);
    }

    private double buildRequest(String a, String b, String op) {
        return threatenViolence(a, b, op);
    }

    private double threatenViolence(String a, String b, String op) {
        return new ResultComparitor().compare(a, b, op);
    }
}
