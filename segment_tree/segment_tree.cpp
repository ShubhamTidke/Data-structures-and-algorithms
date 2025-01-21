/*

Segment tree practice problem using C++:

https://cses.fi/problemset/task/1137


*/

#include <bits/stdc++.h>
using namespace std;

#define pll pair<long long, long long>
#define inf __INT32_MAX__
#define ll long long
#define vll vector<ll>
#define vll2 vector<vector<ll>>

template <typename T>
istream &operator>>(istream &is, vector<T> &v)
{
    for (auto &i : v)
        is >> i;
    return is;
}
template <typename T>
ostream &operator<<(ostream &os, vector<T> v)
{
    for (auto &i : v)
        os << i << ' ';
    return os;
}

// template<typename T>
// istream& operator>> (istream& stream, vector<T> &a) {
//   a.clear(); // remove whatever was in a before

//   string line;
//   do {
//     if (stream.eof())
//       return stream; // if the stream has ended, just let a be empty

//     getline(stream, line);
//   } while (line.empty());

//   istringstream line_stream (line);
//   T x;
//   while(line_stream >> x)
//     a.push_back(x);

//   return stream;
// }

vector<vll> tree;
vll value, visisted;
vll seg_tree, tree_size, node_pos;
int n, q;

void dfs(int u, int &pos)
{
    visisted[u] = 1;
    seg_tree[pos + n] = value[u - 1];
    node_pos[u] = pos + n;

    for (ll &v : tree[u])
    {
        if (!visisted[v])
        {
            dfs(v, ++pos);
        }
    }

    tree_size[u] = pos + n;
}

void update(int u, int val)
{
    u = node_pos[u];
    ll diff = val - seg_tree[u];
    while (u)
    {
        seg_tree[u] += diff;
        u >>= 1;
    }
}

ll query(int u)
{
    int l = node_pos[u];
    int r = tree_size[u];
    ll res = 0;
    while (l <= r and l != 0)
    {
        if (l & 1)
        {
            res += seg_tree[l++];
        }
        if (!(r & 1))
        {
            res += seg_tree[r--];
        }
        l >>= 1;
        r >>= 1;
    }
    return res;
}

void test_case(int t)
{

    cin >> n >> q;

    tree.resize(n + 1);
    value.resize(n);

    cin >> value;

    int u, v;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    u = 0;
    visisted.resize(n + 1, 0);
    seg_tree.resize(2 * n, 0);
    tree_size.resize(n + 1, 0);
    node_pos.resize(n + 1, 0);
    dfs(1, u);

    for (int i = n - 1; i > 0; i--)
    {
        seg_tree[i] = seg_tree[i << 1] + seg_tree[i << 1 | 1];
    }

    int type, cnt = 0;
    while (cnt < q && cin >> type)
    {
        cnt++;
        int s, x;
        if (type == 1)
        {
            cin >> s >> x;
            update(s, x);
        }
        else if (type == 2)
        {
            cin >> s;
            cout << query(s) << "\n";
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    ll t = 1;
    // cin >> t;
    for (int i = 0; i < t; i++)
    {
        test_case(i);
    }
    return 0;
}