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

	plain_text = hcf.plain_text_prep(plain_text)

	blocks = hcf.partition_and_numberfy(plain_text, int(n))

	encrypted_blocks = hcf.encrypt_blocks(plain_text, key)

	cipher_text = hcf.encrypt_hill(plain_text, key)

	everything = zip([i for i in plain_text], [i for k in blocks for i in k], [i for k in encrypted_blocks for i in k], [i for i in cipher_text])

	
	# Display table in Streamlit
	st.write("Data:")
	st.write("This table displays the following information:")
	# List of items
	items = ["Row 1: Your plain text.", "Row 2: Your plain text modulo 26", "Row 3: The cipher text encoded with integers mod 26", "Row 4: Your cipher text in letters."]

	# Display bullet point list
	for item in items:
    	st.write(f"- {item}")
	
	# Convert zip object to a list of lists
	table_data = list(everything)

	# Transpose the table_data to have each tuple element as a separate row
	transposed_data = list(map(list, zip(*table_data)))

	st.table(transposed_data)	


