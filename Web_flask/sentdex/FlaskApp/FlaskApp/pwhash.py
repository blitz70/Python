from passlib.hash import sha256_crypt as en

password_str = 'pa$$w0rd'
password_hash1 = en.encrypt(password_str)
password_hash2 = en.encrypt(password_str)

print(password_str)
print(password_hash1)
print(password_hash2)

print(password_hash1 is password_hash2)
print(en.verify(password_str, password_hash1))
print(en.verify(password_str, password_hash2))

