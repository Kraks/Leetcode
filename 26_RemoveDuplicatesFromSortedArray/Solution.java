class Solution {
  public int removeDuplicates(int[] nums) {
    int size = nums.length;
    for (int i = 0; i < size; i++) {
      for (int j = i+1; j < size; j++) {
        if (nums[i] == nums[j]) {
          //move nums[j+1, ...] one cell left
          for (int k = j+1; k < size; k++) {
            nums[k-1] = nums[k];
          }
          size = size - 1;
          j = j - 1;
        }
      }
    }
    return size;
  }
}
