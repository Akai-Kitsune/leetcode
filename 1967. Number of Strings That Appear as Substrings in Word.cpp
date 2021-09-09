/*Given an array of strings patterns and a string word, 
return the number of strings in patterns that exist as a substring in word.
A substring is a contiguous sequence of characters within a string.

Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

82 / 82 test cases passed.
	Status: Accepted
Runtime: 16 ms
Memory Usage: 14.5 MB
*/

#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>

using namespace std;

#include <limits.h>
class Solution {
public:
    int rabin(string s, string t){
        const int p = 31;
        int r = 0;
        vector<long long> p_pow (max (s.length(), t.length()));
        p_pow[0] = 1;
        for (size_t i=1; i<p_pow.size(); ++i)
            p_pow[i] = ((p_pow[i-1] % (INT32_MAX))* (p % (INT32_MAX)) % (INT32_MAX));

        vector<long long> h (t.length());
        for (size_t i=0; i<t.length(); ++i)
        {
            h[i] = (t[i] - 'a' + 1) * (p_pow[i] % (INT32_MAX));
            if (i)  h[i] += h[i-1];
        }

        long long h_s = 0;
        for (size_t i=0; i<s.length(); ++i)
            h_s += ((s[i] - 'a' + 1) * (p_pow[i]) % (INT32_MAX)) ;

        for (size_t i = 0; i + s.length() - 1 < t.length(); ++i)
        {
            long long cur_h = h[i+s.length()-1];
            if (i) {
                cur_h -= h[i-1];
            }
            if (cur_h % (INT32_MAX)== ((h_s% (INT32_MAX)) * (p_pow[i])% (INT32_MAX)) % (INT32_MAX)){
                return 1;
            }
        }
        return 0;
    }

    int numOfStrings(vector<string>& patterns, string word) {
        int r = 0;
        for(int i = 0; i < patterns.size(); ++i){
            if(rabin(patterns[i], word) != 0){
                r += 1;
            }
        }
        return r;
    }
};
