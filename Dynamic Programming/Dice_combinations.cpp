#include <iostream>
#include <vector>
#define int long long int
using namespace std;

const int MOD = 1000000007;

int countWaysToConstructSum(int n, vector<int>& memo, int diceFaces = 6) {
    if (n == 0) {
        return 1;
    }
    if (n < 0) {
        return 0;
    }
    if (memo[n] != -1) {
        return memo[n] % MOD;
    }

    int ways = 0;
    for (int i = 1; i <= diceFaces; ++i) {
        ways += countWaysToConstructSum(n - i, memo, diceFaces) % MOD;
    }

    memo[n] = ways;
    return ways % MOD;
}

int32_t main() {
    int n;
    cin >> n;
    vector<int> memo(n + 1, -1);
    int ways = countWaysToConstructSum(n, memo) % MOD;
    cout << ways << endl;

    return 0;
}