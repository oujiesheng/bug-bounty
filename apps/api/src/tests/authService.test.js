import test from "node:test";
import assert from "node:assert/strict";
import { registerUser, loginUser, refreshToken } from "../services/authService.js";

test("registerUser creates user with id and token", async () => {
  const result = await registerUser({ email: "test@example.com", role: "client" });
  assert.ok(result.id.startsWith("usr_"));
  assert.equal(result.email, "test@example.com");
  assert.equal(result.role, "client");
  assert.ok(result.token);
});

test("loginUser succeeds with registered email", async () => {
  await registerUser({ email: "login@example.com", role: "freelancer" });
  const result = await loginUser({ email: "login@example.com" });
  assert.equal(result.email, "login@example.com");
  assert.ok(result.token);
});

test("loginUser rejects unregistered email", async () => {
  await assert.rejects(
    () => loginUser({ email: "nonexistent@example.com" }),
    { message: "Invalid credentials" }
  );
});

test("refreshToken verifies existing token and returns new one", async () => {
  const user = await registerUser({ email: "refresh@example.com", role: "client" });
  const result = await refreshToken(`Bearer ${user.token}`);
  assert.ok(result.token);
  assert.notEqual(result.token, user.token);
});

test("refreshToken rejects missing auth header", async () => {
  await assert.rejects(
    () => refreshToken(undefined),
    { message: "Missing authorization header" }
  );
});

test("refreshToken rejects invalid token", async () => {
  await assert.rejects(
    () => refreshToken("Bearer invalid_token_here"),
    { message: "Invalid token" }
  );
});

test("refreshToken rejects malformed auth header", async () => {
  await assert.rejects(
    () => refreshToken("Basic sometoken"),
    { message: "Missing authorization header" }
  );
});

console.log("All auth service tests passed!");
