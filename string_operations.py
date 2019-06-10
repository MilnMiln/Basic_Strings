#! /usr/bin/python3

astring = "Hello world!"

print(astring)
print("012345678901 len(%s)                -> %d" % (astring, len(astring))) 
print("    4        %s.index('o')          -> %d" % (astring,astring.index("o")))
print("      6789   %s[6:9]                -> '%s' (NOT [6:8])." % (astring, astring[6:9]))
print("  12     3   %s.count('l')          ->" % astring, astring.count('l'))
print("         901 %s[-3:len(astring)]    -> '%s'" % (astring, astring[-3:len(astring)]))
print("0 2 4 6 8 0  %s[0:len():2]          -> '%s'" % (astring, astring[0:len(astring):2]))
print("012345678901 %s[::-1]               -> '%s'" % (astring, astring[::-1]))
print("012345678901 %s.upper()             -> '%s' (.lower() -> '%s')" % (astring, astring.upper(), astring.lower()))
print("012345678901 %s.startswith('Hello') -> '%s'" % (astring, astring.startswith("Hello")))
print("012345678901 %s.endswith('Hello')   -> '%s'" % (astring, astring.endswith("Hello")))
print("  ll     l   %s.split('l')          -> '%s'" % (astring, astring.split("l")))



print(astring)
