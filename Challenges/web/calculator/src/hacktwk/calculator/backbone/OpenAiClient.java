package hacktwk.calculator.backbone;

public class OpenAiClient {
    public double sendCalculationRequest(String a, String b, String op) {
        return buildRequest(a, b, op);
    }

    private double buildRequest(String a, String b, String op) {
        return addPrettyPlease(a, b, op);
    }

    private double addPrettyPlease(String a, String b, String op) {
        return new ClaudeClient().sendCalculationRequest(a, b, op);
    }
}
