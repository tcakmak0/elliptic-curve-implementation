from ellipticCurve import EllipticCurve

curve = EllipticCurve(2, 3, 17)
base_point = (5, 1)

privateKeyAlice = int(input("Random private key for Alice: "))
publicKeyAlice = curve.scalarMultiplication(privateKeyAlice, base_point)

privateKeyBob = int(input("Random private key for Bob: "))
publicKeyBob = curve.scalarMultiplication(privateKeyBob, base_point)

sharedSecretAlice = curve.scalarMultiplication(privateKeyAlice, publicKeyBob)
sharedSecretBob = curve.scalarMultiplication(privateKeyBob, publicKeyAlice)

print("Alice's shared secret:", sharedSecretAlice)
print("Bob's shared secret:", sharedSecretBob)
