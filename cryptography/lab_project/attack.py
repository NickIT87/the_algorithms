from Ciphers import CAESAR


cipher = CAESAR(12, "EN")
enc_msg = cipher.enc("Caesar")


cracked_data = []
for i in range(1, len(cipher.ABC)):
    crack = CAESAR(i, "EN")
    cracked_data.append(crack.dec(enc_msg))


print(cracked_data[11])
assert cracked_data[11] == "caesar"