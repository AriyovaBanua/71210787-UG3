input_kalimat = str(input("Masukkan kalimat: "))

input_kalimat = ''.join(e for e in input_kalimat if e.isalnum() or e.isspace())

kata = input_kalimat.split()

fr = {}
for iterasi in kata:
    if iterasi in fr:
        fr[iterasi] = fr[iterasi] + 1
    else:
        fr[iterasi] = 1

print("Output:")
sum_kata = sum(fr.values())

for k, v in fr.items():
    print(k, "=", v)

print("Total kata =", sum_kata)
print("Kata unik =", len(fr))