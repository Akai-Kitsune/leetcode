/*
You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements

Input: nums = [6,2,0,9,7]
Output: [9,7,6,2,0]
Explanation:
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
*/

#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>

using namespace std;

class Solution {
public:
	void swamp(int& a, int& b){
		int tmp = a;
		a = b;
		b = tmp;
	}
    vector<int> rearrangeArray(vector<int>& nums) {
    	bool fullTest = true;
    	int eq = 0;
    	int tmp;
        for(int i = 1; i < nums.size() - 1; i += 2){
        	if(nums[i] == (nums[i-1] + nums[i+1])/2){
        		swamp(nums[i], nums[i-1]);
        	}
        }
        return nums;
    }
};

void printV(std::vector<int> &v)
{
	for (unsigned i = 0; i < v.size(); i++)
	{
		std::cout << v[i] << " ";
	}
	std::cout << std::endl;
}


