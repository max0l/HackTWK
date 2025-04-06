package hacktwk.calculator;

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
        doc.setTitle("Calculator");

        doc.addChild(new Paragraph(result != null ? result : ""));

        file.setContent(doc.toHtml().getBytes(StandardCharsets.UTF_8));
        return file;
    }
}
