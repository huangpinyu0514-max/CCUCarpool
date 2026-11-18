import bcrypt

def generate_hash(passwd: str):
    passwd = passwd.encode("utf-8")
    return bcrypt.hashpw(passwd, bcrypt.gensalt())