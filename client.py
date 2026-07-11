"""
genpark-coupon-referral-abuse-screening-skill: Client SDK
Flags checkout coupon code redemptions that exceed normal user velocities.
"""
from __future__ import annotations
from typing import Optional

TEMPORARY_EMAIL_DOMAINS = ["tempmail.com", "throwaway.com", "mailinator.com"]


class CouponReferralAbuseClient:
    """
    SDK for promotional verification screening.
    """

    def screen_redemption(
        self,
        ip_address: str,
        email_domain: str,
        daily_redeemed_count: int,
    ) -> dict:
        dom = email_domain.lower()
        score = 0

        # Abuse check rules
        if dom in TEMPORARY_EMAIL_DOMAINS:
            score += 45
            
        if daily_redeemed_count > 5:
            score += 40
        elif daily_redeemed_count > 2:
            score += 15

        flag = score >= 40
        
        if score >= 60:
            risk = "high"
        elif score >= 30:
            risk = "medium"
        else:
            risk = "low"

        return {
            "abuse_flag": flag,
            "risk_classification": risk,
            "abuse_signals_score": score
        }
