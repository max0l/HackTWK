package hacktwk.calculator.backbone;

public class ResultComparitor {
    public double compare(String a, String b, String op) {
        return runInternalCalculation(a, b, op);
    }

    private double runInternalCalculation(String a, String b, String op) {
        final int A = Integer.parseInt(a);
        final int B = Integer.parseInt(b);

        if (B == 0 && op.equals("divide")) {
            throw new IllegalArgumentException("Division by zero is not allowed");
        }

        return switch (op.toLowerCase()) {
            case "add" -> A + B;
            case "subtract" -> A - B;
            case "multiply" -> A * B;
            case "divide" -> (double) A / (double) B;
            default -> throw new IllegalArgumentException("Invalid operation: " + op);
        };
    }
}
