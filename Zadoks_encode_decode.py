import jwt

# Secret key for JWT encoding and decoding
secret_key = "your_secret_key_here"

# Payment data to be included in the JWT payload
payment_data = {
    "payment_id": 12345,
    "amount": 100.0,
    "confirmation": "confirmed"
}

# Encode the JWT with the payment data
encoded_token = jwt.encode(payment_data, secret_key, algorithm="HS256")

# Simulate sending the encoded token to the payment processing endpoint
# In a real scenario, this would be an HTTP request to a payment service
print("Sending token to payment processing:", encoded_token)

# Simulate receiving the token on the payment processing side
received_token = input("Enter the received token: ")

try:
    # Decode and verify the received token
    decoded_payload = jwt.decode(received_token, secret_key, algorithms=["HS256"])

    # Check if the payment is confirmed
    if decoded_payload.get("confirmation") == "confirmed":
        payment_id = decoded_payload.get("payment_id")
        amount = decoded_payload.get("amount")
        print(f"Payment confirmed for payment ID {payment_id} and amount {amount}. Proceed with payment processing.")
    else:
        print("Payment not confirmed. Do not proceed with payment.")

except jwt.ExpiredSignatureError:
    print("JWT has expired")
except jwt.DecodeError:
    print("JWT is invalid")