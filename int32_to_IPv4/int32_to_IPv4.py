from cgi import test


def int32_to_ip(int32):
    strng = bin(int32)
    strng = strng[2:len(strng)].zfill(32)
    l = [str(int(strng[i: i+8],2)) for i in range(0, len(strng), 8)]
    strng = '.'.join(l)
    return strng

print(int32_to_ip(2154959208) == "128.114.17.104") 
print(int32_to_ip(0) == "0.0.0.0")
print(int32_to_ip(2149583361) == "128.32.10.1")