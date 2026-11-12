VALID_COUPONS = {
    "STUDENT10": {"type": "discount", "value": 0.10, "description": "10% off for students"},
    "WELCOME20": {"type": "discount", "value": 0.05, "description": "5% off for new users"},
    "FREESHIP": {"type": "free_shipping", "value": 1.0, "description": "Free shipping"},
}


def validate_coupon(code):
    """Check if a coupon code is valid."""
    return code in VALID_COUPONS


def apply_coupon(total, coupon_code):
    """Apply a coupon code to the order total."""
    if not validate_coupon(coupon_code):
        return total, "Invalid coupon code"
    
    coupon = VALID_COUPONS[coupon_code]
    
    if coupon["type"] == "discount":
        discount = total * coupon["value"]
        new_total = total - discount
        return new_total, f"Applied {coupon_code}: -{discount:.2f}"
    
    if coupon["type"] == "free_shipping":
        return total, f"Applied {coupon_code}: Free shipping"
    
    return total, "Unknown coupon type"


# Test cases
if __name__ == "__main__":
    print("=== Test 1: Valid coupon STUDENT10 ===")
    final, msg = apply_coupon(100, "STUDENT10")
    print(msg)
    print(f"Final total: £{final:.2f}")
    
    print("\n=== Test 2: Invalid coupon ===")
    final, msg = apply_coupon(100, "FAKECODE")
    print(msg)
    print(f"Final total: £{final:.2f}")
    
    print("\n=== Test 3: WELCOME20 coupon ===")
    final, msg = apply_coupon(80, "WELCOME20")
    print(msg)
    print(f"Final total: £{final:.2f}")
