from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")

def hash(password):
    return pwd_context.hash(password)