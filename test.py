
import hashlib
import uuid


pwd = "secret"

x = hashlib.sha256(pwd.encode()).hexdigest()
print(x)
print(str(uuid.uuid4()))