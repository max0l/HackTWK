package ctf.rest;

import dobby.annotations.Post;
import dobby.io.HttpContext;
import dobby.io.response.ResponseCodes;
import dobby.session.Session;
import dobby.session.service.SessionService;
import dobby.util.json.NewJson;

public class AuthResource {
    @Post("/rest/cl-login")
    public void doLogin(HttpContext context) {
        final NewJson json = context.getRequest().getBody();

        if(!json.hasKey("cl-password")) {
            context.getResponse().setCode(ResponseCodes.BAD_REQUEST);
            return;
        }

        final String password = json.getString("cl-password");

        if (password.equalsIgnoreCase("lisp")) {
            context.getResponse().setCode(ResponseCodes.OK);
            final Session newSession = SessionService.getInstance().newSession();
            newSession.set("logged-in", "true");
            context.setSession(newSession);
        } else {
            context.getResponse().setCode(ResponseCodes.UNAUTHORIZED);
        }
    }
}
