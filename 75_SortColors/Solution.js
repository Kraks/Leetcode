/**
 *@param {number[]} nums
 *@return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
  var count = {0:0, 1:0, 2:0};
  nums.forEach(function(item) { count[item]++; });
  for (var i = 0; i < nums.length; i++) {
    if (i < count[0]) nums[i] = 0;
    else if (i < count[0]+count[1]) nums[i] = 1;
    else if (i < count[0]+count[1]+count[2]) nums[i] = 2;
  }
};

var nums = [2, 0];
sortColors(nums);
console.log(nums);
