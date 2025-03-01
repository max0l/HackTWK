package ctf.filter;

import dobby.filter.Filter;
import dobby.filter.FilterType;
import dobby.io.HttpContext;
import dobby.io.response.ResponseCodes;
import dobby.session.Session;

public class LoginFilter implements Filter {
    @Override
    public String getName() {
        return "LoginFilter";
    }

    @Override
    public FilterType getType() {
        return FilterType.PRE;
    }

    @Override
    public int getOrder() {
        return 20;
    }

    @Override
    public boolean run(HttpContext httpContext) {
        final String path = httpContext.getRequest().getPath().toLowerCase();

        if (path.startsWith("/rest/cl-login") || path.equalsIgnoreCase("/") || path.equalsIgnoreCase("/index.html") || path.startsWith("/login")) {
            return true;
        }

        final Session session = httpContext.getSession();

        if (!session.contains("logged-in")) {
            httpContext.getResponse().setCode(ResponseCodes.FOUND);
            httpContext.getResponse().setHeader("Location", "/login");
            return false;
        }

        return true;
    }
}
