def verify_certificate(certificate_data):
    """
    Simulated verification function.
    Replace this logic with real validation (e.g., signature check).
    """
    # Example: assume original certificates contain a valid signature
    if certificate_data.get("signature") == "VALID_SIGNATURE":
        return True
    return False


def process_certificate(certificate_data):
    if verify_certificate(certificate_data):
        return "Accepted"
    else:
        return "Declined"


# Example usage
uploaded_certificate_1 = {
    "name": "John Doe",
    "course": "Cyber Security",
    "signature": "VALID_SIGNATURE"  # Original
}

uploaded_certificate_2 = {
    "name": "Jane Doe",
    "course": "Cyber Security",
    "signature": "FAKE_SIGNATURE"  # Fake
}

print(process_certificate(uploaded_certificate_1))  # Output: Accepted
print(process_certificate(uploaded_certificate_2))  # Output: Declined
