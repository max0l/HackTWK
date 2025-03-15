import express, { Request, Response, Application } from "express";
import { join as pathJoin } from "path";
import cookieParser from "cookie-parser";
import { isAdmin, setJwtMiddleware } from "./auth";

const ROOT_PATH: string = __dirname;
const PORT: number = 3000;
const app: Application = express();
app.use(express.static("src/public"));
app.use(cookieParser());
app.use(setJwtMiddleware);

app.get("/", (req: Request, res: Response) => {
  res.sendFile(`html/${isAdmin(req) ? "admin" : "public"}.html`, {
    root: pathJoin(ROOT_PATH),
  });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`listening on port ${PORT}...`);
});
