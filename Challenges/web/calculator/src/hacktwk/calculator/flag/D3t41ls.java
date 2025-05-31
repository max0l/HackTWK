package hacktwk.calculator.flag;

import hacktwk.calculator.backbone.OpenAiClient;

public class D3t41ls {
    public double calc(String a, String b, String op) {
        return new OpenAiClient().sendCalculationRequest(a, b, op);
    }
}
