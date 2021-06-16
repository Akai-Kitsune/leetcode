class Solution {
public:
    int maxSumMinProduct(vector<int>& a) {
        #define mod 1000000007
        
        long res = 0; int s = a.size();
        vector<long> tmp(s + 1);
        vector<long> st;

        for (int i = 0; i < s; ++i){
            tmp[i + 1] = tmp[i] + a[i];
        }

        for (int i = 0; i <= s; ++i) {
            while ((a[st.back()] > a[i]) || (!st.empty() && (i == s))) {
                int j = st.back();
                st.pop_back();
                res = max(res, a[j] * (tmp[i] - tmp[st.empty() ? 0 : st.back() + 1]));
            }
            st.push_back(i);
        }   
    return res % mod;
}
};
