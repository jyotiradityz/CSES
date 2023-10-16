MOD = 1000000007

def count_ways_to_construct_sum(n, memo, dice_faces=6):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n] != -1:
        return memo[n] % MOD

    ways = 0
    for i in range(1, dice_faces + 1):
        ways += count_ways_to_construct_sum(n - i, memo, dice_faces) % MOD

    memo[n] = ways
    return ways % MOD

def main():
    n = int(input())
    memo = [-1] * (n + 1)
    ways = count_ways_to_construct_sum(n, memo) % MOD
    print(ways)

if __name__ == "__main__":
    main()