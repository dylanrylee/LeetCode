class Solution {
    public int[] productExceptSelf(int[] nums) {

        int n = nums.length;

        int[] res = new int[n];
        int[] prefix = new int[n];
        int[] postfix = new int[n];

        for (int i = 0; i <= n - 1; i++) {
            int prefProd = 0;
            if (i != 0) {
                prefProd = nums[i] * prefix[i - 1];             
            } 
            else if (i == 0) {
                prefProd = nums[i];
            }
            prefix[i] = prefProd;
        }

        for (int i = n - 1; i >= 0; i--) {
            int postProd = 0;
            if (i != n - 1) {
                postProd = nums[i] * postfix[i + 1];
            } 
            else if (i == n - 1) {
                postProd = nums[i];
            }
            postfix[i] = postProd;
        }

        for (int i = 0; i <= n - 1; i++) {
            int result = 0;

            if (i == 0) {
                result = postfix[i + 1];
            }
            else if (i == n - 1) {
                result = prefix[i - 1];
            }
            else {
                result = prefix[i - 1] * postfix[i + 1];
            }

            res[i] = result;
        }

        return res;

        
    }
}  
