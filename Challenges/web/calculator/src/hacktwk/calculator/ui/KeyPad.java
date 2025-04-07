package hacktwk.calculator.ui;

import common.html.Button;
import common.html.Div;

public class KeyPad extends Div {
    public KeyPad() {
        super();
        addStyle("keypad");

        for (String s : new String[]{"7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "C", "0", "EXE", "/"}) {
            addChild(new Button(s, "Calculator.eval('" + s + "');"));
        }

    }
}
