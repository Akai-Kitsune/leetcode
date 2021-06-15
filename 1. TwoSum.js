/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function(nums, target) {
    let map = new Map();
    for(let i = 0; i < nums.length; ++i) {
        let t = target - nums[i];
        if(map.has(t) == true) {
            return [map.get(t), i];
        }
        map.set(nums[i], i);
    }
};