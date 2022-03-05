import random
from tkinter import messagebox


def rabinMiller(num):
    """
    This function gets a number and checks if he may be
    a prime number. if the number may be a prime number
    the function returns True else she will return False

    :param num: int

    :return: True\False
    """

    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
        return True


def isPrime(num):
    """
      This function gets a number from type int. the
      function check if the number is a prime number by check
      if the number is biger then 2 check if the number exists
      in the list of prime numbers from 2 to 997

    :param num: int

    :return: True\False
    """

    if (num < 2):
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
                 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
                 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    return rabinMiller(num)


def gcd(a, b):
    """
    This function takes two nonzero integers and finds the
    greatest positive integer d

    :param a: int
    :param b: int

    :return: int
    """

    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    """
    This function gets to parameters a and m

    :param a: int
    :param m: int

    :return: int
    """

    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m


def generateKey(p, q):
    keySize = 2048
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    p = p
    q = q
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e.
    d = findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)

    return publicKey, privateKey


def encrypt(pk, plaintext):
    """ The function gets a public key and a message(plain text) and return encoded
    message(ciphertext)"""
    # Unpack the key into it's components

    key, n = separate_pk(pk)

    # Convert each letter in the plaintext to numbers based on the character using a ^ bmodm
    cipher = [(ord(char) ** int(key)) % int(n) for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    """ The function gets a private key and a ciphertext and return a plaintext"""
    # Unpacking the key into its components

    key, n = separate_pk(pk)

    # Generating the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((int(char) ** key) % n) for char in ciphertext]
    # Returning the array of bytes as a string
    return ''.join(plain)


def separate_pk(pk):
    key = ""
    n = ""

    count = 1
    l = pk[count]

    while (l != ","):
        key = key + str(l)
        count = count + 1
        l = pk[count]

    count = count + 2
    r = pk[count]

    while (r != ")"):
        n = n + str(r)
        count = count + 1
        r = pk[count]

    return int(key), int(n)


def show_about():
    SHOW_ABOUT = "Name: Amit Dorman\nSchool: Eitan Sitria\n"
    messagebox.showinfo("About", SHOW_ABOUT)


def show_help():
    SHOW_HELP = "This is my help windows\nHere you will find instructions about ....."
    messagebox.showinfo("Help", SHOW_HELP)


def show_rsa_algorithm():
    SHOW_RSA_Algorithm = "RSA Algorithm: \n"
    messagebox.showinfo("Help", SHOW_RSA_Algorithm)
