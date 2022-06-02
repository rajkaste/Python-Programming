n = int(input("Enter an integer:"))
prime_list = []

for i in range(n + 1):
    prime_list.append(i)

prime_list[1] = 0
p = 2

while p * p <= n:
    if p != 0:
        for i in range(p * 2, n + 1, p):
            prime_list[i] = 0
    p += 1

print("All the prime nos. up to", n, "are:")
for i in range(len(prime_list)):
    if prime_list[i] != 0:
        print(prime_list[i], end=" ")
