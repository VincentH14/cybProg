#!/usr/bin/python3

import hashlib

hashvalue = input("[*]Enter String to Hash: ")

hashObj1 = hashlib.md5()
hashObj1.update(hashvalue.encode())

print(hashObj1.hexdigest())

hashObj2 = hashlib.sha1()
hashObj2.update(hashvalue.encode())

print(hashObj2.hexdigest())

hashObj3 = hashlib.sha224()
hashObj3.update(hashvalue.encode())

print(hashObj3.hexdigest())

hashObj4 = hashlib.sha256()
hashObj4.update(hashvalue.encode())

print(hashObj4.hexdigest())

hashObj5 = hashlib.sha512()
hashObj5.update(hashvalue.encode())

print(hashObj5.hexdigest())

