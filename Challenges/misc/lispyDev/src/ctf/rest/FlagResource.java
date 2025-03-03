package ctf.rest;

import dobby.annotations.Post;
import dobby.io.HttpContext;
import dobby.io.response.ResponseCodes;

public class FlagResource {
    @Post("/rest/validate-flag")
    public void validateFlag(HttpContext context) {
        final String flag = context.getRequest().getBody().getString("flag");

        if (flag == null) {
            context.getResponse().setCode(ResponseCodes.BAD_REQUEST);
            return;
        }

        if (flag.equals("CTFlisp{L4mbd4_C41cu1u5_15_Fun!}")) {
            context.getResponse().setCode(ResponseCodes.OK);
            context.getResponse().setBody("Correct flag!");
        } else {
            context.getResponse().setCode(ResponseCodes.PAYMENT_REQUIRED);
            context.getResponse().setBody("Incorrect flag!");
        }
    }
}
