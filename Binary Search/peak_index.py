class Solution {
    public int peakIndexInMountainArray(int[] a) {
        int l = a.length;
		int res = 0;
		for (int i = 0; i < l-2; i++) {
			if(a[i] < a[i+1] && a[i+1] > a[i+2]){
				res = i+1;
				break;
			}
		}
		return res;
    }
}
