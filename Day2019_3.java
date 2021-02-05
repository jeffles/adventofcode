package com.jefsumne;

import java.io.*;
import java.util.*;

public class Day2019_3 {
    public static void main(String[] args) throws IOException {

        File inputFile = new File("input.txt");
        Scanner myReader = new Scanner(inputFile);
        String[] wire1 = myReader.nextLine().split(",");
        String[] wire2 = myReader.nextLine().split(",");
        myReader.close();


//        int answer = runProgram(startingMemory, 12, 2);
        int x = 0;
        int y = 0;
        int d = 0;
        Map<String, Integer> grid = new HashMap<String, Integer>();

        for (String instr : wire1) {

            char direction = instr.substring(0,1).charAt(0);
            int distance = Integer.parseInt(instr.substring(1));
            for (int i=0; i< distance; i++){
                d += 1;
                switch(direction) {
                    case 'U':
                        y += 1;
                        break;
                    case 'D':
                        y -= 1;
                        break;
                    case 'L':
                        x -= 1;
                        break;
                    case 'R':
                        x += 1;
                }
                if (!grid.containsKey(x +"-" + y)) {
                    grid.put(x + "-" + y, d);
                }

            }
//            System.out.printf("%s %s\n", direction, distance);
//            System.out.println(grid);
        }
        x = 0;
        y = 0;
        d = 0;
        int closest = Integer.MAX_VALUE;
        for (String instr : wire2) {

            char direction = instr.substring(0,1).charAt(0);
            int distance = Integer.parseInt(instr.substring(1));
            for (int i=0; i< distance; i++){
                d += 1;
                switch(direction) {
                    case 'U':
                        y += 1;
                        break;
                    case 'D':
                        y -= 1;
                        break;
                    case 'L':
                        x -= 1;
                        break;
                    case 'R':
                        x += 1;
                }
                if (grid.containsKey(x +"-" + y)) {
                    int manhattan = grid.get(x +"-" + y) + d;
                    if (manhattan < closest){
                        closest = manhattan;
                    }
                    System.out.println("Match!" +x +"-" + y);
                }


            }
        }
        System.out.println("Part 2-" + closest);
//        part2(startingMemory);

    }

}
