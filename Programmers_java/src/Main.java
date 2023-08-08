import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int alu = 0;
        int[][] answer = new int[arr1.length][arr1[0].length];
        for (int i = 0; i < arr1.length; i++){
            for (int j = 0; j < arr1[0].length; j++){
                alu = 0;
                for (int k = 0; k < arr1[0].length; k++){
                    alu += arr1[i][k] * arr2[k][j];
                }
                answer[i][j] = alu;
            }
        }

        return answer;
    }

    public static void main(String[] args){
        Main a = new Main();
        int [][] input1 = {{1, 4}, {3, 2}, {4, 1}};
        int [][] input2 = {{3, 3}, {3, 3}};
        System.out.println(Arrays.toString(a.solution(input1, input2)));
    }

}