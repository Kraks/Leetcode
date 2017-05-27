public class Solution {
    public int reverse(int x) {
        if (x == 0) return 0;
        byte[] t = String.format("%d", x).getBytes();
        byte[] src;
        if (x < 0) {
            src = new byte[t.length-1];
            System.arraycopy(t, 1, src, 0, t.length-1);
        }
        else {
            src = t;
        }

        int i = src.length - 1;
        for (; src[i] == '0'; i--);
        byte[] res = new byte[i + 1];
        for (int k = 0; k < src.length && i >= 0 && src[i] != '-'; k++) {
            res[k] = src[i--];
        }

        if (x < 0)
            return -Integer.parseInt(new String(res));
        return Integer.parseInt(new String(res));
    }
}
