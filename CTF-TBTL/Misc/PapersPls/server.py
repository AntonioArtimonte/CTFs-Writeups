#!/usr/bin/python3

import base64
import datetime
import json
import os
import signal

import humanize
import jwt


# openssl ecparam -name secp521r1 -genkey -noout -out private.key
# openssl ec -in private.key -pubout -out public.pem
PUBLIC_KEY = u'''-----BEGIN PUBLIC KEY-----
MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQBGOtycGkAMpTEDsjFykEywLecIdCX
1QIShxmJB0qJj9K2yFNwJj/eRR6yzIZcHJPZWzQU6Mad62y1MsJ8uOgdZ2sBmkS0
HJtT4FZq/EQbtkHeahsDnSLbFpPfoN/t8hmKrVmDzDRGe3PNl7OQVuzoY2TVSxVK
IKmpZ9Pw9/5HOzSmOxs=-----END PUBLIC KEY-----
'''


def myprint(s):
    print(s, flush=True)


def handler(_signum, _frame):
    myprint("Time out!")
    exit(0)


def decode(token):
    signing_input, crypto_segment = token.rsplit(".", 1)
    header_segment, payload_segment = signing_input.split(".", 1)
    header_data = base64.urlsafe_b64decode(header_segment)
    header = json.loads(header_data)
    alg = header["alg"]
    return jwt.decode(token, algorithms=[alg], key=PUBLIC_KEY)


def main():
    #signal.signal(signal.SIGALRM, handler)
    #signal.alarm(300)

    myprint("Your papers, please.")
    token = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0=.eyJ2ZXJzaW9uIjoiMS4wIiwiZG9jVHlwZSI6Imlzby5vcmcuMTgwMTMuNS4xLm1ETCIsImZhbWlseV9uYW1lIjoiVFVSTkVSIiwiZ2l2ZW5fbmFtZSI6IlNVU0FOIiwiYmlydGhfZGF0ZSI6IjE5OTgtMDgtMjgiLCJpc3N1ZV9kYXRlIjoiMjAxOC0wMS0xNVQxMDowMDowMC4wMCIsImV4cGlyeV9kYXRlIjoiMjAyMi0wOC0yN1QxMjowMDowMC4wMCIsImlzc3VpbmdfY291bnRyeSI6IlVTIiwiaXNzdWluZ19hdXRob3JpdHkiOiJDTyIsImRvY3VtZW50X251bWJlciI6IjU0MjQyNjgxNCIsImRyaXZpbmdfcHJpdmlsZWdlcyI6W3siY29kZXMiOlt7ImNvZGUiOiJEIn1dLCJ2ZWhpY2xlX2NhdGVnb3J5X2NvZGUiOiJEIiwiaXNzdWVfZGF0ZSI6IjIwMTktMDEtMDEiLCJleHBpcnlfZGF0ZSI6IjIwMjctMDEtMDEifV0sInVuX2Rpc3Rpbmd1aXNoaW5nX3NpZ24iOiJVU0EifQ.ATOuXnzmtdiOPhuu1ksgF6FqKjHNHJoyMLHF28xsRgVNUANFlUv9l_xM9TGg_s9ZbFy6gimaH80MSHl6wHOxg8yxAFS22jy1GEPX3Kc4ZPUKEjd7q6vbo1zLXEfNjpkwBbU6M9pbqS6CmBxM1MY93WDjNY8p5mGYdBtbD3XccmOivGDH'
    try:
        mdl = decode(token)
        assert mdl["docType"] == "iso.org.18013.5.1.mDL"
        family_name = mdl["family_name"] 
        given_name = mdl["given_name"] 
        expiry_date = datetime.datetime.strptime(mdl["expiry_date"], "%Y-%m-%dT%H:%M:%S.%f")
    except Exception as e:
        print(decode(token))
        myprint("Your papers are not in order!")
        exit(0)
    myprint("Hello {} {}!".format(given_name, family_name))
    delta = expiry_date - datetime.datetime.now()
    if delta <= datetime.timedelta(0):
        myprint("Your papers expired {} ago!".format(humanize.naturaldelta(delta)))
        exit(0)

    flag = open("flag.txt", "r").read().strip()
    myprint("Your papers are in order, here is your flag: {}".format(flag))
    exit(0)


if __name__ == '__main__':
    main()
