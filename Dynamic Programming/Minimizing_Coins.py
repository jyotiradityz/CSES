#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int n, k;
vector<int> l;
vector<vector<int>> dp;

int solve(int i, int cnt, int sm) {
    if (i == n) {
        if (sm == 0) {
            return cnt;
        } else {
            return INT_MAX;
        }
    }
    if (dp[i][sm] != -1) {
        return dp[i][sm];
    }
    int notpick = solve(i + 1, cnt, sm);
    int pick = INT_MAX;
    if (l[i] <= sm) {
        pick = solve(i, cnt + 1, sm - l[i]);
    }
    dp[i][sm] = min(pick, notpick);
    return dp[i][sm];
}

int main() {
    cin >> n >> k;
    l.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }
    
    dp.assign(n + 1, vector<int>(k + 1, -1));

    int result = solve(0, 0, k);
    if (result == INT_MAX) {
        cout << -1 << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}