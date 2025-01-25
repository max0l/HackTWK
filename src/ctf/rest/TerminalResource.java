package ctf.rest;

import dobby.annotations.Post;
import dobby.io.HttpContext;
import dobby.io.response.ResponseCodes;

public class TerminalResource {
    @Post("/rest/cl-terminal")
    public void execWebTermCommand(HttpContext context) {
        final String command = context.getRequest().getBody().getString("command");

        if (command == null) {
            context.getResponse().setCode(ResponseCodes.BAD_REQUEST);
            return;
        }
        final String response;

        if (command.equalsIgnoreCase("help")) {
            response = "Available commands: help, list, cat <i>filename</i>, download <i>filename</i>";
        } else if (command.equalsIgnoreCase("list")) {
            response = "Files: secret.png, archive.txt";
        } else if (command.startsWith("cat")) {
            final String[] splitted = command.split(" ");
            if (splitted.length != 2) {
                response = "Usage: cat <i>filename</i>";
            } else {
                final String filename = splitted[1];
                if (filename.equalsIgnoreCase("secret.png")) {
                    response = "This is a binary file. Use the download command to get it.";
                } else if (filename.equalsIgnoreCase("archive.txt")) {
                    response = "<h2>Alex's Joke Archive</h2><ul><li>Why do Lisp programmers love parentheses? Because they make them feel enclosed!</li><li>If programming languages were superheroes, Lisp would be Doctor Strange. Weird syntax, but powerful magic!</li></ul>";
                } else {
                    response = "File not found: " + filename;
                }
            }
        } else if (command.startsWith("download")) {
            final String[] splitted = command.split(" ");
            if (splitted.length != 2) {
                response = "Usage: download <i>filename</i>";
            } else {
                final String filename = splitted[1];
                if (filename.equalsIgnoreCase("secret.png")) {
                    response = "/ctf/secret_space/egarots/secret.png";
                } else if (filename.equalsIgnoreCase("archive.txt")) {
                    response = "/ctf/secret_space/storage/archive.txt";
                } else {
                    response = "File not found: " + filename;
                }
            }
        } else {
            response = "Unknown command: " + command;
        }

        context.getResponse().setCode(ResponseCodes.OK);
        context.getResponse().setBody(response);
    }
}
