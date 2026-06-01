**Bug Description**

Message creation currently builds the record as `{ id: generatedId, ...payload, sentAt }`, so a caller can include `id` in the payload and overwrite the generated message id. Message ids should remain server-owned so clients cannot spoof or collide with records created by the service.

This issue is limited only to the creator of this issue. This means that only the issue author can attempt to solve this issue. If you would like to work on it, please create another issue with the same contents and refer to issue #743 for more information.

**Steps to Reproduce**
1. POST /api/messages with body: `{ "id": "fake_id_123", "text": "Hello" }`
2. The returned message has id `fake_id_123` instead of server-generated id

**Expected Behavior**
- Server should always generate and own the message id
- Client-provided id should be ignored or rejected
- Returns should be snapshots to prevent external mutation

**Actual Behavior**
- Client can overwrite server-owned id by including it in payload
- Returned object is a reference to the internal store (mutation affects stored data)

**Impact**
- ID spoofing/collision
- Potential data integrity issues
- External mutation of internal state
