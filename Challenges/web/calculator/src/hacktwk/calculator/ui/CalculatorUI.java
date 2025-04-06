package hacktwk.calculator.ui;

import common.html.Comment;
import common.html.Div;
import common.html.Document;
import common.html.Paragraph;
import dobby.files.StaticFile;

import java.nio.charset.StandardCharsets;

public class CalculatorUI {
    private final String result;

    public CalculatorUI(String result) {
        this.result = result;
    }

    public StaticFile build() {
        final StaticFile file = new StaticFile();
        file.setContentType("text/html");

        final Document doc = new Document();
        doc.addStyle("/index.css");
        doc.setTitle("Calculator");

        doc.addChild(new Comment("TODO: fix verbose errors"));

        final Div app = new Div();
        app.addStyle("app");

        final Paragraph p = new Paragraph(result);
        p.addStyle("result");
        app.addChild(p);

        app.addChild(new KeyPad());
        doc.addChild(app);

        file.setContent(doc.toHtml().getBytes(StandardCharsets.UTF_8));
        return file;
    }
}
