import hashlib


def hash_password(password: str):
    # Har doim Salt .env fileda saqlanadi
    salt = "random_private_password".encode("utf-8")
    hashed = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=salt,
        iterations=100_000
    )
    return hashed


def verify_hash(password: str, hash_hex: str) -> bool:
    salt = "random_private_password".encode("utf-8")
    hashed = hashlib.pbkdf2_hmac(hash_name="sha256", password=password.encode(
        "utf-8"), salt=salt, iterations=100_000)

    return hashed.hex() == hash_hex
