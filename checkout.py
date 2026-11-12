def apply_student_discount(total, is_student):
    """Apply 10% student discount if the customer is a student."""
    if is_student:
        return total * 0.90
    return total


def checkout(total, is_student=False):
    """Main checkout function with student discount support."""
    if total <= 0:
        raise ValueError("Total must be greater than zero")
    
    final_total = apply_student_discount(total, is_student)
    
    print(f"Original total: £{total:.2f}")
    if is_student:
        discount = total - final_total
        print(f"Student discount (10%): -£{discount:.2f}")
    print(f"Final total: £{final_total:.2f}")
    
    return final_total


# Test cases
if __name__ == "__main__":
    print("=== Test 1: Non-student, £100 ===")
    checkout(100, is_student=False)
    
    print("\n=== Test 2: Student, £100 ===")
    checkout(100, is_student=True)
    
    print("\n=== Test 3: Student, £55.50 ===")
    checkout(55.50, is_student=True)
