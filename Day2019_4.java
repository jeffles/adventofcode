package com.jefsumne;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Day2019_4 {
    public static void main(String[] args) throws IOException {
        int start = 264793;
        int end = 803935;
        int total = 0;
        for (int i=start; i<=end; i++){
            String numStr = String.valueOf(i);
            if (numStr.charAt(0)>numStr.charAt(1)){
                 continue;
            }
            if (numStr.charAt(1)>numStr.charAt(2)){
                continue;
            }
            if (numStr.charAt(2)>numStr.charAt(3)){
                continue;
            }
            if (numStr.charAt(3)>numStr.charAt(4)){
                continue;
            }
            if (numStr.charAt(4)>numStr.charAt(5)){
                continue;
            }
            if (numStr.charAt(0)!=numStr.charAt(1) &&  numStr.charAt(1)!=numStr.charAt(2)
                    &&  numStr.charAt(2)!=numStr.charAt(3) &&  numStr.charAt(3)!=numStr.charAt(4)
                    &&  numStr.charAt(4)!=numStr.charAt(5)){
                continue;
            }
            int series = 1;
            boolean exactly_two = false;
            for (int j=1; j<=5; j++){
                if (numStr.charAt(j) == numStr.charAt(j-1)){
                    series +=1;
                } else if (series == 2){
                    exactly_two = true;
                } else {
                    series = 1;
                }
            }
            if (!(series == 2) && !exactly_two){
                continue;
            }


            System.out.println(i);
            total += 1;
        }
        System.out.println(total);

    }

}
