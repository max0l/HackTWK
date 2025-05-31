# The Calculator - Walkthrough

The `EXE` button redirects to `/operation/a/b` to return the result rendered in the normal calculator UI. Producing any error while calculating the result will send the stacktrace to the client.

Sending an invalid operation (`^(add|subtract|multiply|divide)`) or a value for `a` or `b` that can't be parsed to a number, an exception will trigger revealing the stacktrace.

For example for `/divide/42/0` results in this stacktrace:
```
500 - Internal Server Error
java.lang.reflect.InvocationTargetException
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:119)
	at java.base/java.lang.reflect.Method.invoke(Method.java:565)
	at dobby.routes.RouteDiscoverer.lambda$analyzeClassAndMethods$0(RouteDiscoverer.java:47)
	at dobby.filter.FilterManager.runFilterChain(FilterManager.java:94)
	at dobby.Dobby.handleConnection(Dobby.java:275)
	at dobby.Dobby.lambda$acceptConnections$0(Dobby.java:222)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1095)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:619)
	at java.base/java.lang.Thread.run(Thread.java:1447)
Caused by: java.lang.IllegalArgumentException: Division by zero is not allowed
	at hacktwk.calculator.backbone.ResultComparitor.runInternalCalculation(ResultComparitor.java:13)
	at hacktwk.calculator.backbone.ResultComparitor.compare(ResultComparitor.java:5)
	at hacktwk.calculator.backbone.ClaudeClient.threatenViolence(ClaudeClient.java:13)
	at hacktwk.calculator.backbone.ClaudeClient.buildRequest(ClaudeClient.java:9)
	at hacktwk.calculator.backbone.ClaudeClient.sendCalculationRequest(ClaudeClient.java:5)
	at hacktwk.calculator.backbone.OpenAiClient.addPrettyPlease(OpenAiClient.java:13)
	at hacktwk.calculator.backbone.OpenAiClient.buildRequest(OpenAiClient.java:9)
	at hacktwk.calculator.backbone.OpenAiClient.sendCalculationRequest(OpenAiClient.java:5)
	at hacktwk.calculator.flag.D3t41ls.calc(D3t41ls.java:7)
	at hacktwk.calculator.flag.ImP1.calc(ImP1.java:5)
	at hacktwk.calculator.flag.Le4k.calc(Le4k.java:5)
	at hacktwk.calculator.flag.D0nt.calc(D0nt.java:5)
	at hacktwk.calculator.flag.HackTWK.calc(HackTWK.java:5)
	at hacktwk.calculator.Validator.validate(Validator.java:7)
	at hacktwk.calculator.CalculatorResource.preprocessParameters(CalculatorResource.java:20)
	at hacktwk.calculator.CalculatorResource.doCalc(CalculatorResource.java:16)
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104)
	... 8 more
```

The flag is "hidden" in the stacktrace. Looking only at the `hacktwk.calculator.flag` classes, the flag ist `HackTWKD0ntLe4kImP1D3t41ls`
