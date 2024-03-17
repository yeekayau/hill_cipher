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

	key = hcf.generate_invertible_matrix_mod26(int(n))
	st.write(key)

	plain_text = plain_text_prep(plain_text)

	blocks = partition_and_numberfy(plain_text, int(n))

	encrypted_blocks = encrypt_blocks(plain_text, key)

	cipher_text = encrypt_hill(plain_text, key)

	everything = zip([i for i in plain_text], [i for k in blocks for i in k], [i for k in encrypted_blocks for i in k], [i for i in cipher_text])

	# Convert zip object to a list of lists
	table_data = list(everything)

	# Transpose the table_data to have each tuple element as a separate row
	transposed_data = list(map(list, zip(*table_data)))

	# Display table in Streamlit
	st.write("Table Display:")
	st.table(transposed_data)


