package hacktwk.calculator;

import dobby.annotations.Get;
import dobby.files.StaticFile;
import dobby.io.HttpContext;
import hacktwk.calculator.ui.CalculatorUI;

public class CalculatorResource {
    @Get("/")
    public void doIndex(HttpContext context) {
        sendResult(context, "");
    }

    @Get("/{operation}/{a}/{b}")
    public void doCalc(HttpContext context) {
        sendResult(context, preprocessParameters(context.getRequest().getParam("a"), context.getRequest().getParam("b"), context.getRequest().getParam("operation")));
    }

    private double preprocessParameters(String a, String b, String op) {
        return new Validator().validate(a, b, op);
    }

    private void sendResult(HttpContext context, Object result) {
        final StaticFile file = new CalculatorUI(result.toString()).build();

        context.getResponse().setHeader("Content-Type", file.getContentType());
        context.getResponse().setBody(file.getContent());
    }
}
