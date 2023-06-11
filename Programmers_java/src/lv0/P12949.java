package lv0;

import java.util.Arrays;

public class P12949 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        for (int i = 0; i < arr1.length; i++){
            for (int j = 0; j < arr2[0].length; j++){
                for (int k = 0; k < arr1[0].length; k++){
                    answer[i][j] += arr1[i][k] * arr2[k][j];
                }
            }
        }

        return answer;
    }

    public static void main(String[] args){
        P12949 a = new P12949();
        int [][] input1 = {{1, 4}, {3, 2}, {4, 1}};
        int [][] input2 = {{3, 3}, {3, 3}};
        System.out.println(Arrays.toString(a.solution(input1, input2)));
    }
}
