package lv1;

import lv0.P12949;

import java.util.Arrays;

public class P72410 {
    public String solution(String new_id) {
        // 1단계
        new_id = new_id.toLowerCase();
        // 2단계
        new_id = new_id.replaceAll("[^a-z\\d\\-_.]", "");
        // 3단계
        new_id = new_id.replaceAll(("[.]+"), ".");
        // 4단계
        new_id = new_id.replaceAll("^[.]|[.]$", "");
        // 5단계
        if (new_id.isBlank()){new_id = "a";}
        // 6단계
        if (new_id.length() >= 16){new_id = new_id.substring(0, 15);}
        new_id = new_id.replaceAll("[.]$", "");
        // 7단계
        while (new_id.length() < 3){new_id += new_id.charAt(new_id.length()-1);}

        return new_id;
    }

    public static void main(String[] args){
        P72410 a = new P72410();
        String input1 = "...!@BaT#*..y.abcdefghijklm";
        String input2 = "z-+.^.";
        String input3 = "=.=";
        String input4 = "123_.def";
        String input5 = "abcdefghijklmn.p";
        System.out.println((a.solution(input1)));
        System.out.println((a.solution(input2)));
        System.out.println((a.solution(input3)));
        System.out.println((a.solution(input4)));
        System.out.println((a.solution(input5)));

    }
}
