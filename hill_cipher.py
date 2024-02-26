import streamlit as st
import random
import string

import hill_cipher_functions as hcf

st.title("Hill Cipher")

plain_text = st.text_area("Enter plain text for encryption")

n = st.text_input("Enter the dimensions of the matrix")

st.markdown("Here is a random inveritible matrix key: ")

A = ncf.random_invertible_matrix(n)
A