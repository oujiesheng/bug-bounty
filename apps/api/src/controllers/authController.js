import { registerSchema, loginSchema } from "../validators/auth.js";
import { loginUser, refreshToken, registerUser } from "../services/authService.js";
import { ok, fail } from "../utils/response.js";

export async function register(req, res) {
  try {
    const payload = registerSchema.parse(req.body);
    const result = await registerUser(payload);
    return ok(res, result, 201);
  } catch (error) {
    return fail(res, error.message, 400);
  }
}

export async function login(req, res) {
  try {
    const payload = loginSchema.parse(req.body);
    const result = await loginUser(payload);
    return ok(res, result);
  } catch (error) {
    const status = error.message === "Invalid credentials" ? 401 : 400;
    return fail(res, error.message, status);
  }
}

export async function oauthCallback(req, res) {
  return ok(res, {
    provider: req.params.provider,
    status: "callback-received"
  });
}

export async function refresh(req, res) {
  try {
    const result = await refreshToken(req.headers.authorization);
    return ok(res, result);
  } catch (error) {
    const status = error.message.includes("Invalid") ? 401 : 400;
    return fail(res, error.message, status);
  }
}
