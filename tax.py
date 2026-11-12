UK_VAT_RATE = 0.20


def calculate_tax(total, is_exempt=False):
    """Calculate VAT (Value Added Tax) for the order."""
    if is_exempt:
        return 0.0
    return total * UK_VAT_RATE


def get_tax_breakdown(total, is_exempt=False):
    """Return a tax breakdown dictionary."""
    tax = calculate_tax(total, is_exempt)
    return {
        "subtotal": total,
        "tax_rate": "0%" if is_exempt else f"{UK_VAT_RATE * 100:.0f}%",
        "tax_amount": tax,
        "total_with_tax": total + tax
    }


def print_tax_breakdown(total, is_exempt=False):
    """Print a formatted tax breakdown."""
    breakdown = get_tax_breakdown(total, is_exempt)
    print(f"Subtotal: £{breakdown['subtotal']:.2f}")
    print(f"VAT rate: {breakdown['tax_rate']}")
    print(f"VAT amount: £{breakdown['tax_amount']:.2f}")
    print(f"Total (incl. VAT): £{breakdown['total_with_tax']:.2f}")


# Test cases
if __name__ == "__main__":
    print("=== Test 1: £100 standard purchase ===")
    print_tax_breakdown(100, is_exempt=False)
    
    print("\n=== Test 2: £50 tax-exempt (books) ===")
    print_tax_breakdown(50, is_exempt=True)
