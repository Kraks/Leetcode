import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 *  * Created by kraks on 3/29/14.
 *   */
public class Solution {
  public int singleNumber(int[] nums) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    for (int i = 0; i < nums.length; i++) {
      if (map.containsKey(nums[i])) { map.put(nums[i], 2); }
      else { map.put(nums[i], 1); }
    }
    for(Integer key : map.keySet()) {
      if (map.get(key) == 1) return key;
    }
    return -1;
  }

  public static void main(String[] args) {
    int[] a = {1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 6};
    Solution solution = new Solution();
    System.out.println(solution.singleNumber(a));
  }
}
