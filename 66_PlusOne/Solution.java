class Solution {
  public int[] plusOne(int[] digits) {
    boolean carry = true;
    for (int i = digits.length-1; i >= 0; i--) {
      if (carry) digits[i] = digits[i] + 1;
      if (digits[i] > 9) {
        digits[i] = 0;
        carry = true;
      }
      else {
        carry = false;
      }
    }
    if (carry) {
      int[] newdigits = new int[digits.length+1];
      newdigits[0] = 1;
      for (int i = 1; i < digits.length; i++) {
        newdigits[i] = digits[i-1];
      }
      return newdigits;
    }
    return digits;
  }
}
