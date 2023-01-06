/*

Change character

Problem Description
You are given a string A of size N consisting of lowercase alphabets.

You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.

Find the minimum number of distinct characters in the resulting string.



Problem Constraints
1 <= N <= 100000

0 <= B < N



Input Format
The first argument is a string A.

The second argument is an integer B.



Output Format
Return an integer denoting the minimum number of distinct characters in the string.



Example Input
A = "abcabbccd"
B = 3



Example Output
2



Example Explanation
We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
So the minimum number of distinct character will be 2.

Solution Approach
Since there are 26 characters we can find frequency of each character.
Sort them in ascending order. Since we have to minimize the number of distinct characters, we will change characters whose frequency is less into the character which has the highest frequency.
We will check the maximum number of distinct characters we can successfully change.

# Java ####
public class Solution {
    public int solve(String A, int B) {
        int cnt[] = new int[26];
        for(int i = 0; i < A.length(); ++i){
            ++cnt[A.charAt(i)-'a'];
        }
        ArrayList<Integer> C = new ArrayList<Integer>();
        for(int i = 0; i < 26; ++i){
            if(cnt[i] > 0){
                C.add(cnt[i]);
            }
        }
        Collections.sort(C);
        for(int i = 0; i < C.size(); ++i){
            B -= C.get(i);
            if(B < 0){
                return C.size() - i;
            }
        }
        return 1;
    }
}

time  :- O(nlogn + n) = O(nlogn) n = length of A
space :- O(1) arr = [0]*26 since space of 26 chars is very small

*/

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        arr = [0]*26
        ans = 0
        for i in A:
            arr[ord(i)-97] += 1
            if(arr[ord(i)-97] == 1):
                ans += 1
        arr.sort()
        for i in range(26):
            if(B-arr[i] >= 0 and arr[i] != 0):
                ans -= 1
                B -= arr[i]
        ans = max(ans, 1)
        return ans   