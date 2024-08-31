"""
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
	1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
	686974207468652062756c6c277320657965
... should produce:
	746865206b696420646f6e277420706c6179
"""

hex_str_1 = "1c0111001f010100061a024b53535009181c"
hex_str_2 = "686974207468652062756c6c277320657965"

bytes_from_hex_1 = bytes.fromhex(hex_str_1)
bytes_from_hex_2 = bytes.fromhex(hex_str_2)

xor_str = bytes.hex(bytes(a ^ b for a, b in zip(bytes_from_hex_1, bytes_from_hex_2)))
print(xor_str)
print(xor_str == "746865206b696420646f6e277420706c6179")