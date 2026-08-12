# Analysis 02 — Phishing

**Sample:** `phishing_02.txt`

## Classification
**PHISHING**

## Red Flags
1. The message creates a payment deadline.
2. It requests a payment through an email link.
3. The sender identity is not independently verified.
4. The payment domain is unrelated to a known delivery organization.
5. The message pressures the user to act quickly.

## Suspicious Keywords
- Action Required
- payment
- within 24 hours
- immediately

## Why It Is Unsafe
The message uses a delivery problem and a payment request to pressure the recipient into following an external link. The destination should be independently verified before any payment is made.

## Recommended Action
Do not use the provided payment link. Verify the delivery through the official delivery provider's normal website or application.
