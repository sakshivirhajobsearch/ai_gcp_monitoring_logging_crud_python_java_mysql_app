from cryptography.hazmat.primitives import serialization

pem_string = ""

try:
    private_key = serialization.load_pem_private_key(
        pem_string.encode(),
        password=None,
    )
    print("✅ Valid PEM private key")
except Exception as e:
    print("❌ Invalid PEM key:", e)
