# genpark-coupon-referral-abuse-screening-skill

> **GenPark AI Agent Skill** -- Checkout coupon referral abuse auditor.

## Quick Start

```python
from client import CouponReferralAbuseClient
client = CouponReferralAbuseClient()
res = client.screen_redemption("1.1.1.1", "gmail.com", 1)
print(res["abuse_flag"])
```
