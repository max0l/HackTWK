package hacktwk.calculator.ui;

import common.html.Div;

public class KeyPad extends Div {
    public KeyPad() {
        super();
        addStyle("keypad");
        addChild(new ButtonLine("7", "8", "9"));
        addChild(new ButtonLine("4", "5", "6"));
        addChild(new ButtonLine("1", "2", "3"));
        addChild(new ButtonLine("C", "0", "EXE"));
    }
}
