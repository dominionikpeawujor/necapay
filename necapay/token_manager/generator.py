import jwt

# Secret key for JWT encoding and decoding
secret_key = "your_secret_key_here"


def generate(data):
    # Encode the JWT with the payment data
    data['confirmation'] = "confirmed"
    
    encoded_token = jwt.encode(data, secret_key, algorithm="HS256")
    return encoded_token

def verify(token):
    try:
        # Decode and verify the received token
        decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])

        # Check if the payment is confirmed
        if decoded_payload.get("confirmation") == "confirmed":
            payment_id = decoded_payload.get("payment_id")
            amount = decoded_payload.get("amount")

            return amount
            
        else:
            print("Payment not confirmed. Do not proceed with payment.")

    except jwt.ExpiredSignatureError:
        print("JWT has expired")
    except jwt.DecodeError:
        print("JWT is invalid")


