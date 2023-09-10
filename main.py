# --- ENCRYPTING --- #
import jwt

# --- ENCRYPT 1 --- #
# encoded = jwt.encode({
#                     "name":"Vera", 
#                     "amount":15000, 
#                     "commodity":"fuel"
#                      },
#                     "secret", 
#                     algorithm="HS256")
# print(encoded)

# --- ENCRYPT 2 --- #
# payload_data = {
#                 "id": 4,
#                 "name":"NNA", 
#                 "amount":30000,
#                 "commodity":"fuel"
#                 }

# secret = "awesome"
# token = jwt.encode(
#                     payload=payload_data,
#                     key=secret
#                   )
# print(token)

# --- ENCRYPT 3 --- #
# payload_info = {}
# secret = ""

# info_name = input("Enter first name: ")
# payload_info.update({"name": info_name})

# commodity = input("What Commodity are you paying for? ")
# payload_info.update({"commodity": commodity})

# amount = int(input(f"How much {commodity} are you purchasing? "))
# payload_info.update({"amount": amount})

# secret = input("Enter secret password? ")

# token = jwt.encode(
#                    payload=payload_info,
#                    key=secret
#                    )

# print(token)
# print()