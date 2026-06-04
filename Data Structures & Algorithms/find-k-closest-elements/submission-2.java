class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        //first find the element x or an element closes to x
        //then set the locations of left = loc of le - 1, and right = loc of le + 1
        //continue expanding the window until you find elements closer to x
        int le=0, ri = arr.length - 1;
        while(le < ri) {
            int mid = (le + ri) / 2;
            if (arr[mid] < x) {
               le=mid + 1;
            } else {
                ri=mid;
            }
        }
        le = le - 1;
        ri = le + 1;
        while(ri - le - 1 < k) {
            //if le goes out of bounds or below 0
            if (le < 0) {
                ri++;
            } else if(ri >= arr.length) {
                //else if ri goes out of bounds or beyond the len of the input arr
                le--;
            } else if(Math.abs(arr[le] - x) <= Math.abs(arr[ri] - x)) {
                //else if you find a element closer to x i.e. arr[le] - x <= arr[ri] - x, go left
                le--;
            } else {
                //else continue going right
                ri++;
            }
        }
        System.out.println("le="+le+" and ri="+ri);
        //capture all the elements within the window of le and ri
        List<Integer> res = new ArrayList<>();
        for(int i=le+1; i < ri; i++) {
            res.add(arr[i]);
        }
        return res;
    }
}