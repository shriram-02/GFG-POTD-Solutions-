class Solution {
    using ll = long long;
    const ll MOD = 1000000007;

    ll normalTime(ll x, ll a, ll b) {
        if (x <= a) return x;

        ll k = (x - a + (a - b) - 1) / (a - b);
        return x + 2 * b * k;
    }

    ll floorSum(ll n, ll m, ll a, ll b) {
        ll ans = 0;

        while (true) {
            if (a >= m) {
                ans += (n - 1) * n * (a / m) / 2;
                a %= m;
            }

            if (b >= m) {
                ans += n * (b / m);
                b %= m;
            }

            ll y = a * n + b;

            if (y < m) break;

            n = y / m;
            b = y % m;
            swap(m, a);
        }

        return ans;
    }

    ll sumTime(ll lo, ll hi, ll a, ll b) {
        if (lo > hi) return 0;

        ll ans = 0;

        if (lo <= a) {
            ll end = min(hi, a);
            ans += (end * (end + 1) - lo * (lo - 1)) / 2;
            lo = end + 1;
        }

        if (lo <= hi) {
            ll n = hi - lo + 1;
            ll c = a - b;

            ll sumK = floorSum(n, c, 1, lo - a + c - 1);

            ans += (lo + hi) * n / 2;
            ans += 2 * b * sumK;
        }

        return ans;
    }

public:
    int minTime(int a, int b, int d, int l, int r) {
        ll normal = normalTime(d, a, b);

        ll low = l, high = r + 1;

        while (low < high) {
            ll mid = low + (high - low) / 2;

            if (normalTime(d - mid, a, b) + 1 < normal)
                high = mid;
            else
                low = mid + 1;
        }

        ll k = low;
        ll ans = 0;

        ans += (k - l) * normal;

        if (k <= r) {
            ll lo = d - r;
            ll hi = d - k;

            ans += sumTime(lo, hi, a, b) + (r - k + 1);
        }

        return ans % MOD;
    }
};