class Solution {
  public void rotate(int[] nums, int k) {
    k = k % nums.length;
    int rest[] = new int[k];
    for (int i = 0; i < k; i++) {
      rest[i] = nums[nums.length-k+i];
    }
    for (int i = nums.length-k-1; i >= 0; i--) {
      nums[k+i] = nums[i];
    }
    for (int i = 0; i < k; i++) {
      nums[i] = rest[i];
    }
  }
}
