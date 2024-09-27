
num_0_10: int = int(input('enter a word: '))
count: int = int(input('enter a character: '))
stat_counter: int = 0
SENTINEL = -999

for _ in range(10):
    if num_0_10 == SENTINEL:
        break
    if 0 <= num_0_10 <= 10:
        stat_counter += 1
    print(f"numbers have been taken'{num_0_10}'")



