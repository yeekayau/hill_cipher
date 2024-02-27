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

	st.markdown("Here is the plain text encrypted as numbers (mod 26) - ignore the first row and column: ")

	cleaned_text = hcf.plain_text_prep(plain_text)
	encoded_text = hcf.partition_and_numberfy(cleaned_text, int(n))
	st.table(encoded_text)

	st.markdown("Here is the encrypted text in blocks (The rows correspond to reading the text from left to right, agian ignore the first row and column for now): ")

	blocks = hcf.encrypt_blocks(cleaned_text, A)
	st.table(blocks)

	st.markdown("Here is the encrypted text: ")

	cipher_text = hcf.encrypt_hill(cleaned_text, A)
	cipher_text
