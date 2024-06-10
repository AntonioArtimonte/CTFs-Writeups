from Crypto.Util.number import bytes_to_long, inverse
from Crypto.PublicKey import RSA

def main():

    TARGET = b'I challenge you to sign this message!'
    target_long = bytes_to_long(TARGET)
    N = 109177336050364626862921891505207455225305084818778522716275701265280698048102984142525366766388383050433791631145423358256325260826961799402189103542656655718436729986078791569167167034743520389261225031998498739363914101000592083358214920407429637984872628195722344516961722620606414591752418955256648858489
    
    # Step 1: Pick m1 and calculate m2
    m1 = 2  # Starting with a simple value that is sure to be allowed
    m1_inv = inverse(m1, N)
    m2 = (target_long * m1_inv) % N

    print(m1)
    print(m2)

if __name__ == '__main__':
    main()

