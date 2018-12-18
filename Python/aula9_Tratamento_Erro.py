import sys
import ipaddress

try:

    i6 = ipaddress.IPv6Address('::1')
    print(i6.compressed)

except ZeroDivisionError or ArithmeticError:
    print(ZeroDivisionError.mro())

