class Solution {
    public void reverseString(char[] s) {
        int n=s.length;
        int i=0;
        while (i<n/2){
            char temp=s[i];
            s[i]=s[n-i-1];
            s[n-i-1]=temp;
            i++;
        }
    }
}