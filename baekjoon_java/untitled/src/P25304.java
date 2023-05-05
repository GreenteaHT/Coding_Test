// https://www.acmicpc.net/problem/25304

import java.util.Scanner;

public class P25304 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int N = sc.nextInt();
        int cnt = 0;
        for(int i = 0; i < N; i++){
            int price = sc.nextInt();
            int m = sc.nextInt();
            cnt += price * m;
        }
        if (cnt == X){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
