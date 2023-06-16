# Elliptic Curve Cryptography (ECC) Encryption

This code provides an implementation of Elliptic Curve Cryptography (ECC) encryption using the `hmac`, `hashlib`, `secrets`, `pyrcryptodom` libraries.

## Usage

The `EllipticCurve` class provides methods for ECC encryption and decryption. Here's an overview of the available methods:

- `__init__(self, c1, c2, p)`: Initializes an elliptic curve with the provided coefficients `c1`, `c2`, and modulus `p`.

- `pointAddition(self, point1, point2)`: Performs point addition on the elliptic curve given two points `point1` and `point2`.

- `scalarMultiplication(self, k, point)`: Performs scalar multiplication on the elliptic curve given a scalar `k` and a point `point`. Basically adds point to itself for k times.

- `keyDerivator(self, point, salt=b'')`: Derives a key from a point on the elliptic curve using HMAC-SHA256 with an optional salt.

- `encrypt_ECC(self, basePoint, msg, pubKey)`: Encrypts a message `msg` using ECC encryption with a base point `basePoint` and a public key `pubKey`. 

- `decrypt_ECC(self, encryptedMsg, privKey)`: Decrypts an encrypted message `encryptedMsg` using ECC decryption with a private key `privKey`.

## Dependencies

This code relies on the following dependencies:

- `hmac`: Used for HMAC-SHA256 key derivation.
- `hashlib`: Used for SHA256 hashing.
- `secrets`: Used for generating random private keys.
- `pycryptodom`: Used for AES encryption and decryption.

Please make sure to install these dependencies using the provided `requirements.txt` file.
All the libraries except pycryptodom are included by default

## Examples

Here are some examples of how to use the `EllipticCurve` class for ECC encryption and decryption:

```python
# Create an instance of the EllipticCurve class
ecc = EllipticCurve(2, 3, 17)
base_point = (5, 1)
# Generate a key pair
private_key = secrets.randbelow(ecc.p)
public_key = ecc.scalarMultiplication(private_key, ecc.basePoint)

# Encrypt a message
message = b'This is a secret message'
encrypted_msg = ecc.encrypt_ECC(basePoint, message, public_key)

# Decrypt the encrypted message
decrypted_msg = ecc.decrypt_ECC(encrypted_msg, private_key)
