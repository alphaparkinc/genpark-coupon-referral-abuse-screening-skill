class CouponReferralAbuseClient:
    def screen_redemption(self, ip_address: str, email_domain: str, daily_redeemed_count: int) -> dict:
        return {"abuse_flag": daily_redeemed_count > 5}