package hacktwk.calculator.ui;

import common.html.Button;
import common.html.Div;

public class ButtonLine extends Div {
    public ButtonLine(String a, String b, String c) {
        super();
        addStyle("button-line");
        addChild(new Button(a, ""));
        addChild(new Button(b, ""));
        addChild(new Button(c, ""));
    }
}
