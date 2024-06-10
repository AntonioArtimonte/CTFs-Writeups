import jwt

PUBLIC_KEY = u'''-----BEGIN PUBLIC KEY-----
MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQBGOtycGkAMpTEDsjFykEywLecIdCX
1QIShxmJB0qJj9K2yFNwJj/eRR6yzIZcHJPZWzQU6Mad62y1MsJ8uOgdZ2sBmkS0
HJtT4FZq/EQbtkHeahsDnSLbFpPfoN/t8hmKrVmDzDRGe3PNl7OQVuzoY2TVSxVK
IKmpZ9Pw9/5HOzSmOxs=-----END PUBLIC KEY-----
'''

def encode_jwt(payload, key):
    """
    Encode the given payload into a JSON Web Token (JWT) using the provided key.

    Args:
        payload (dict): The payload to be encoded.
        key (str): The key used for encoding.

    Returns:
        str: The encoded JWT.
    """
    encoded_jwt = jwt.encode(payload, key=key, algorithm='HS256')
    return encoded_jwt

payload = {
    "version": "1.0",
    "docType": "iso.org.18013.5.1.mDL",
    "family_name": "TURNER",
    "given_name": "SUSAN",
    "birth_date": "1998-08-28",
    "issue_date": "2018-01-15T10:00:00.00",
    "expiry_date": "2025-08-27T12:00:00.00",
    "issuing_country": "US",
    "issuing_authority": "CO",
    "document_number": "542426814",
    "driving_privileges": [
        {
            "codes": [{"code": "D"}],
            "vehicle_category_code": "D",
            "issue_date": "2019-01-01",
            "expiry_date": "2027-01-01"
        }
    ],
    "un_distinguishing_sign": "USA"
}

encoded_jwt = encode_jwt(payload, key=PUBLIC_KEY)

print("Encoded JWT with HS256 and public key as secret:", encoded_jwt)