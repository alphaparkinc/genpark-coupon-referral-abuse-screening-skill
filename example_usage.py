"""
example_usage.py -- Demonstrates CouponReferralAbuseClient
"""
from client import CouponReferralAbuseClient

def main():
    client = CouponReferralAbuseClient()
    result = client.screen_redemption(
        ip_address="192.168.1.50",
        email_domain="tempmail.com",
        daily_redeemed_count=6
    )
    print("[Coupon Referral Abuse Result]")
    print(f"Abuse Detected: {result['abuse_flag']}")
    print(f"Risk classification: {result['risk_classification'].upper()} (Score: {result['abuse_signals_score']})")

if __name__ == "__main__":
    main()
