# Diffie-Hellman
ALGORITHM:
A prime number q
An integer α that is a primitive root of q.
(Note: Premitive root of a prime number P is one, whose powers module P generate all the images from 1 to P-1)
Suppose users A and B wish to exchange the key.
User A selects a random integer XA<q and computes
YA=α^XAmod q
User B independently selects a random integer XB<q and compute
YB=α^XBmod q
Each side keeps X value private and makes Y value available publicly to the other side user A computes the key as:
k=(YB)^XAmod q
User B computes the key as :
k=(YA)^XBmod q
The calculations produce identical results 
Diffie Hellman key Exchange Algorithm
k=(YA)^XBmodq -> same as calculated by B
Global Public Elements
q ; prime number
α ; α < q and it is primitive root of q
USER A KEY GENERATION
Select Private key XA<q
Calculation of Public key YA=α^XAmod q
USER B KEY GENERATION
Select Private key XB<q
Calculation of Public key YB=α^XBmod q
Calculation of Secret Key by A
k=(YB)XAmod q
Calculation of Secret Key by B
k=(YA)XBmod q
The result is that two sides have exchanged a secret value.
