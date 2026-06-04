class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        int L = nums.length;
  
            int num1=-1,num2=-1,cnt1=0,cnt2=0;
            for(int ii : nums) {
                if(ii==num1) {
                    cnt1++;
                } else if(ii==num2) {
                    cnt2++;
                }else if(cnt1 == 0) {
                    num1=ii;
                    cnt1=1;
                }else if(cnt2==0) {
                    num2=ii;
                    cnt2=1;
                }else {
                    cnt1--;
                    cnt2--;
                }
            }
            cnt1=0;cnt2=0;
            for(int ii:nums) {
                if (ii==num1) {
                    cnt1++;
                } else if(ii==num2) {
                    cnt2++;
                }
            }
            if (cnt1 > L / 3) {
                res.add(num1);
            }
            if (cnt2 > L / 3) {
                res.add(num2);
            }
        return res;
    }
}