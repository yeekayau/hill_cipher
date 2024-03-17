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

	st.markdown("Here is a random inveritible matrix modulo 26: (ignore the first row for now)")

	A = hcf.generate_invertible_matrix_mod26(int(n))
	st.write(A)


	st.markdown("Here is the plain text encrypted as numbers (mod 26) - ignore the first row and column: ")

	cleaned_text = hcf.plain_text_prep(plain_text)
	encoded_blocks = hcf.partition_and_numberfy(cleaned_text, int(n))
	
	letters_and_numbers = zip([i for i in cleaned_text], [i for k in encoded_blocks for i in k])

	st.write("Plain text and encoded text (mod 26:")
	
	# Convert zipped object to a list of lists
	grid_data = list(map(list, zip(*letters_and_numbers)))

	# Display grid in Streamlit
	st.write("Grid Display:")
	st.write(grid_data)

