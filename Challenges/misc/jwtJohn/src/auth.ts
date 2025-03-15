import { NextFunction, Request, Response } from "express";
import { sign, verify } from "jsonwebtoken";

// TODO read key from .env
const JWT_KEY: string = "super_secret_key";
const JWT_COOKIE_NAME: string = "jwt";

const isAdmin = (req: Request): boolean => {
  const token: string | undefined = req.cookies[JWT_COOKIE_NAME];
  if (token === undefined) {
    return false;
  }

  try {
    const decoded = verify(token, JWT_KEY);
    // @ts-ignore
    return decoded["user"] === "admin";
  } catch (err) {
    return false;
  }
};

const setJwtMiddleware = (req: Request, res: Response, next: NextFunction) => {
  if (req.cookies[JWT_COOKIE_NAME] === undefined) {
    res.cookie(JWT_COOKIE_NAME, initNewToken());
  }
  next();
};

const initNewToken = (): string => {
  return sign({ user: "public" }, JWT_KEY);
};

export { isAdmin, setJwtMiddleware };
