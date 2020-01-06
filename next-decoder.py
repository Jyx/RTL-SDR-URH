#!/usr/bin/env python3
import sys

def convert(r):
    start = r[0]
    buf = r[1:53]
    end = r[53:]
    tmp = ""
    for i in range(0, len(buf), 2):
        #print(i)
        if (buf[i] == "1" and buf[i+1] == "0"):
            tmp += "1"
        elif (buf[i] == "0" and buf[i+1] == "1"):
            tmp += "0"
        else:
            print("Error in convert")
    return start + tmp + end

def is_sync(d, sz):
    if sz < 10:
        return False

    for i in range(0, 10):
        if d[i] != "0":
            return False
    #print("Found sync msg")
    return True

def is_zero_bit(d, sz):
    if sz < 5:
        return False

    for i in range(0, 5):
        if d[i] != "0":
            return False
    #print("Found zero bit")
    return True

def is_one_bit(d, sz):
    if sz <= 1:
        if d != "0":
            return False
    #print("Found one bit")
    return True

def main(d):
    #print("{}".format(d))
    i = 0
    r = ""

    while i < len(d):
        if d[i] == "1":
            i += 1
            if len(d[i:]) == 0:
                break

            if is_sync(d[i:], len(d[i:])):
                r += "1"
                i += 10
            elif is_zero_bit(d[i:], len(d[i:])):
                r += "0"
                i += 5
            elif is_one_bit(d[i], 1):
                r += "1"
                i += 1
        else:
            i += 1
            print("error")
    #print("r[{}]: {}".format(len(r), r))
    r = convert(r)
    print("r[{}]: {}".format(len(r), r))
    return r

if __name__ == "__main__":
    main(sys.argv[1])
