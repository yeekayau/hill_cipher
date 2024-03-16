import random
import string
import numpy as np
from numpy.linalg import inv

def generate_invertible_matrix_mod26(n):
    while True:
        # Generate a random matrix of size nxn with elements modulo 26
        matrix = np.random.randint(0, 26, size=(n, n))

        # Check if the determinant of the matrix is invertible modulo 26
        det = int(round(np.linalg.det(matrix))) % 26
        if det != 0 and np.gcd(det, 26) == 1:
            return matrix


def plain_text_prep(text):
    """
    This function takes a string as input, converts to uppercase and removes all punctuation marks and spaces from it.

    Args:
    - text (str): The input string to remove punctuation from.

    Returns:
    - str: The input string without any punctuation marks.
    """
    text = text.upper()

    # Only include letters
    text_no_punct = ''.join(char for char in text if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    text_no_punct.replace('“', "") # remove double quotation marks

    return text_no_punct.upper().replace(" ", "")

def partition_and_numberfy(cleaned_text, n):
  """
    Partition a cleaned piece of text into blocks of size n, and return the set of vectors of encoded text. 
    If n does not divide the length of the text, a few random letters are added, so that the length of the text is a multiple of n.

    Args:
      cleaned_text: uppercase string of letters with no spacing.
      n: dimensions of square matrix

    Returns:
      set of vectors encoding the text.
  """

  uppercase_alphabet = string.ascii_uppercase
  mappings = list(zip(uppercase_alphabet, [i for i in range(0,26)]))

  # returns list of letters in the text as their number counterparts
  numberfied = [letter[1] for i in cleaned_text for letter in mappings if i == letter[0] ]

  # Case when n (dimensions of the matrix) does not divide the length of the text
  if len(numberfied)%n != 0:
    num_randoms_needed = (len(cleaned_text)//n + 1)*n - len(numberfied)

    for i in range(num_randoms_needed):
      numberfied.append(random.randint(0,26)) # add some random letters

  return [ numberfied[i:i+n] for i in [k*n for k in range(0, len(cleaned_text)//n + 1)] if i != len(numberfied) ]



def encrypt_blocks(input_text, A):
  """
    Encrypts the input text using the Hill cipher with square invertible matrix A.
    Returns the encrypted text as an np array of blocks modulo 25 (i.e. the encrypted text)

    Args:
      input_text:  a string.
      A: A square invertible matrix

    Returns:
      Hill cipher encrypted text
  """

  clean_text = plain_text_prep(input_text)

  encoded_blocks = partition_and_numberfy(clean_text, A.shape[0])

  # encrypted matrix - not modded.
  encrypted = [np.dot(A,np.array(r)) for r in encoded_blocks]
  
  # Reduce entries mod 25
  encrypted_mod26 = [r%26 for r in encrypted]

  return encrypted_mod26


def encrypt_hill(input_text, A):
  '''
  Encrypt hill cipher
  '''
  encrypted_blocks = encrypt_blocks(input_text, A)
  
  uppercase_alphabet = string.ascii_uppercase
  mappings = list(zip(uppercase_alphabet, [i for i in range(0,26)]))

  cipher_text_list = [k[0] for r in encrypted_blocks for l in r for k in mappings if l == k[1]]

  cipher_text = ''.join([i for i in cipher_text_list])

  return cipher_text

