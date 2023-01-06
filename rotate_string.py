/*
 Rotate string
 Problem Description

Given a string A, rotate the string B times in clockwise direction and return the string.



Problem Constraints

1 <= |A| <= 105

1 <= B <= 109

String A consist only of lowercase characters.



Input Format

First and only argument is a string A.



Output Format

Return a string denoting the rotated string.



Example Input

Input 1:

 A = "scaler"
 B = 2
Input 2:

 A = "academy"
 B = 7


Example Output

Output 1:

 "erscal"
Output 2:

 "academy"


Example Explanation

Explanation 1:

 Rotate the given string twice so the string becomes "erscal".
 */

 class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def check_B(self, A, B):
        if B == len(A) or B==0:
                return A
        return False
    def solve(self, A, B):
        #output  =
        n = len(A)
        if self.check_B(A, B):
            return self.check_B(A, B)
        elif B>len(A):
            B = B%len(A)
            #print(B)
            if self.check_B(A, B):
                return self.check_B(A, B)
            return A[-B:] + A[0:(n -(B))]
        else:
            return A[-B:] + A[0:(n -(B))]