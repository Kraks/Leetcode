public class Solution {
    public String reverseString(String s) {
        byte[] bytes = s.getBytes();
        int length = bytes.length;
        byte[] newStr = new byte[length];
        for (int i = length; i > 0; i--) {
            newStr[length-i] = bytes[i-1];
        }
        return new String(newStr);
    }

    public static void main(String[] args) {
        String s1 = "hello";
        System.out.println(new Solution().reverseString(s1));
    }
}
