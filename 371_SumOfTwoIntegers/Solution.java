public class Solution {
  public int getSum(int a, int b) {
    int res = a ^ b;
    int carray = (a & b) << 1;
    if (carray != 0) return getSum(res, carray);
    return res;
  }

  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.print("3 + 4 = ");
    System.out.println(s.getSum(3, 4));

    System.out.print("-4 + -5 = ");
    System.out.println(s.getSum(-4, -5));
  }
}
