#include <iostream>
#include <vector>
#include <map>
int main() {
    int n;
    std::cin >> n;
    std::vector<int> l(n);
    std::map<int, int> mp;
    for (int i = 0; i < n; ++i) {
        std::cin >> l[i];
        if (mp.find(l[i]) == mp.end()) {
            mp[l[i]] = 1;
        } else {
            mp[l[i]] += 1;
        }
    }

    std::cout << mp.size() << std::endl;

    return 0;
}