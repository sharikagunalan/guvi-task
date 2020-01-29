import hashlib
password = input("enter password")
p=hashlib.new('md4').hexdigest()
print(p)
