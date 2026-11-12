def calculate_shipping(total, is_international=False):
    """Calculate shipping cost based on order total and destination."""
    FREE_SHIPPING_THRESHOLD = 50.0
    STANDARD_SHIPPING = 5.99
    INTERNATIONAL_SHIPPING = 12.99
    
    if total >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    
    if is_international:
        return INTERNATIONAL_SHIPPING
    
    return STANDARD_SHIPPING


def get_shipping_description(cost, is_international=False):
    """Return a human-readable shipping description."""
    if cost == 0:
        return "Free shipping"
    
    region = "International" if is_international else "Standard"
    return f"{region} shipping: £{cost:.2f}"


# Test cases
if __name__ == "__main__":
    print("=== Test 1: £30 order, UK ===")
    cost = calculate_shipping(30, is_international=False)
    print(get_shipping_description(cost, is_international=False))
    
    print("\n=== Test 2: £60 order, UK (free shipping) ===")
    cost = calculate_shipping(60, is_international=False)
    print(get_shipping_description(cost, is_international=False))
    
    print("\n=== Test 3: £40 order, International ===")
    cost = calculate_shipping(40, is_international=True)
    print(get_shipping_description(cost, is_international=True))
