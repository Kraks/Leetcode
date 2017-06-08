import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 *  * Created by kraks on 3/29/14.
 *   */
public class Solution {
    public int singleNumber(int[] A) {
        Integer key = null;
        HashMap<Integer, Integer> freq1 = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> freq2 = new HashMap<Integer, Integer>();
        for (int i = 0; i < A.length; i++) {
            if (!freq1.containsKey(A[i])) {
                freq1.put(A[i], 1);
            }
            else {
                freq2.put(A[i], 2);
                freq1.remove(A[i]);
            }
        }

        Iterator iter = freq1.entrySet().iterator();
        while (iter.hasNext()) {
            Map.Entry entry = (Map.Entry) iter.next();
            Object k = entry.getKey();
            key = (Integer)k;
        }
        return key;
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 6};
        Solution solution = new Solution();
        System.out.println(solution.singleNumber(a));
    }
}
