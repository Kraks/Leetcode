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

// another solution

var swap = function(arr, i, j) {
  var t = arr[j];
  arr[j] = arr[i];
  arr[i] = t;
};

var sortColors = function(nums) {
  var r = 0, w = 0, b = nums.length;
  while (w < b) {
    if (nums[w] == 0) swap(nums, r++, w++);
    else if (nums[w] == 2) swap(nums, --b, w);
    else w++;
  }
};

var nums = [2, 0];
sortColors(nums);
console.log(nums);
