# %%
k1 = 5764801
k2 = 17807724
k1 = 15113849
k2 = 4206373

loopsize = 8
num = 1

def find_loopsize(public_key, subject_num):
    n = 1
    loopsize = 0
    while n != public_key:
        n = (n * subject_num) % 20201227
        loopsize += 1
    return loopsize

def calculate_key(subject_num, loopsize):
    n = 1
    for _ in range(loopsize):
        n = (n * subject_num) % 20201227
    return n

loopsize1 = find_loopsize(k1, 7)
loopsize2 = find_loopsize(k2, 7)

# print(loopsize1, loopsize2)
key1 = calculate_key(k2, loopsize1)
key2 = calculate_key(k1, loopsize2)

print(key1, key2)

