import streamlit as st
import random
import string
import numpy as np
from numpy.linalg import inv

import hill_cipher_functions as hcf

st.title("Hill Cipher")

plain_text = st.text_area("Enter plain text for encryption")

n = st.text_input("Enter the dimensions of the matrix")

if plain_text and n:

	st.markdown("Here is a random inveritible matrix key: (ignore the first row for now)")

	A = hcf.random_invertible_matrix(int(n))
	st.write(A)

	st.markdown("Here is the plain text encrypted as numbers (mod 25): ")

	cleaned_text = hcf.plain_text_prep(plain_text)
	encoded_text = hcf.partition_and_numberfy(cleaned_text, int(n))
	encoded_text

	st.markdown("Here is the encrypted text in blocks: ")

	blocks = hcf.encrypt_blocks(cleaned_text, A)
	blocks

	st.markdown("Here is the encrypted text: ")

	cipher_text = hcf.encrypt_hill(cleaned_text, A)
	cipher_text
