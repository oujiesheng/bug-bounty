import { signAccessToken, verifyAccessToken } from "../utils/jwt.js";

const users = new Map();

export async function registerUser(payload) {
  const id = `usr_${Date.now()}`;
  const user = { id, email: payload.email, role: payload.role ?? "client" };
  users.set(id, user);
  return {
    ...user,
    token: signAccessToken({ sub: id, role: user.role })
  };
}

export async function loginUser(payload) {
  // Find user by email
  let foundUser = null;
  for (const user of users.values()) {
    if (user.email === payload.email) {
      foundUser = user;
      break;
    }
  }

  if (!foundUser) {
    throw new Error("Invalid credentials");
  }

  return {
    email: foundUser.email,
    token: signAccessToken({ sub: foundUser.id, role: foundUser.role })
  };
}

export async function refreshToken(authHeader) {
  if (!authHeader?.startsWith("Bearer ")) {
    throw new Error("Missing authorization header");
  }

  try {
    const decoded = verifyAccessToken(authHeader.slice(7));
    return {
      token: signAccessToken({ sub: decoded.sub, role: decoded.role })
    };
  } catch {
    throw new Error("Invalid token");
  }
}
