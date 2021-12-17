en=input("\033[38;5;22;48;5;227m python payload or virus file name enter ->> ")
import binascii

with open(en,'r') as f:
    print(eval(f'binascii.hexlify(b"{f.read()}")'))
