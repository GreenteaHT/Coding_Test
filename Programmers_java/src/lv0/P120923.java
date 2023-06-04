package lv0;

import java.util.Arrays;
import java.util.stream.IntStream;

public class P120923 {
    public int[] solution(int num, int total) {
        // 연속된 수열의 합 공식을 이용한 첫번째 값 추적
        // num * nStart + (num-1) * num / 2 = total
        int nStart = (total - ((num-1) * num / 2)) / num;

        // 선언과 루프문을 이용한 어레이 초기화
        int[] answer = new int[num];
        for (int i=0; i < num; i++){
            answer[i] = i + nStart;
        }

        // 위의 풀이 대신에 IntStream의 range를 이용하여 연속된 수열을 생성 가능
        // int [] answer = IntStream.range(a, a+num).toArray();
        return answer;
    }

    public static void main(String[] args){
        P120923 a = new P120923();
        System.out.println(Arrays.toString(a.solution(3, 12)));
    }

}
