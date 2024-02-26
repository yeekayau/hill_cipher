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

	st.markdown("Here is a random inveritible matrix key: ")

	A = hcf.random_invertible_matrix(int(n))
	A

	st.markdown("Here is the encrypted text in blocks: ")

	blocks = hcf.encrypt_blocks(hcf.plain_text_prep(plain_text), A)
	blocks
