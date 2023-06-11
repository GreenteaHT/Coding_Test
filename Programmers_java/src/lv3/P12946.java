package lv3;

import lv0.P12949;

import java.util.Arrays;
import java.lang.Math;

public class P12946 {
    public int[][] solution(int n) {
        int[][] answer = new int[0][2];


        return answer;
    }

    public void process(int n, int start, int destination){
        if (n == 1){
            answer.add(new int[] {start, destination});
        }
    }

    public static void main(String[] args){
        P12946 a = new P12946();
        System.out.println(Arrays.toString(a.solution(input1, input2)));
    }
}
