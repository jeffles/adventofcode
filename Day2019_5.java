package com.jefsumne;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day2019_5 {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> startingMemory=new ArrayList<>();

        File inputFile = new File("input.txt");
        Scanner myReader = new Scanner(inputFile);
        myReader.useDelimiter(",");

        while (myReader.hasNext()) {
            int data = myReader.nextInt();
            startingMemory.add(data);
        }
        myReader.close();

        int answer = runProgram(startingMemory);
//        System.out.println("Part 1 " + answer);


    }


    private static int runProgram(ArrayList<Integer>startingMemory) {
        Scanner myInput = new Scanner(System.in);
        List<Integer> memory = new ArrayList<>(startingMemory);
//        int i4=0;
//        for(int s : memory){
//            System.out.println(String.valueOf(i4++)+": "+s);
//        }

        int index = 0;
        while (memory.get(index) != 99) {
            int instruction = memory.get(index);
            int opcode = instruction % 100;
            int parameters = instruction / 100;
//            System.out.println(parameters);

            int param1 = memory.get(index+1);
            int param2 = 0;
            int param3 = 0;

            if (parameters % 10 == 0 && (opcode != 3)){
                param1 = memory.get(param1);
            }
            parameters = parameters / 10;

            if  (opcode != 3 && opcode != 4) {
                param2 = memory.get(index + 2);
                if (parameters % 10 == 0) {
                    param2 = memory.get(param2);
                }

                if (opcode == 1 || opcode == 2 || opcode == 7 || opcode == 8) {
                    param3 = memory.get(index + 3);
                }
            }

            if (opcode == 1){
                memory.set(param3, param1 + param2);
                if (index != param3) {
                    index += 4;
                }
            }

            else if (opcode == 2){
                memory.set(param3, param1 * param2);
                if (index != param3) {
                    index += 4;
                }
            }
            else if (opcode == 3){
                System.out.printf("Input>");
                int input = myInput.nextInt();
                memory.set(param1, input);
                if (index != param1) {
                    index += 2;
                }
            }
            else if (opcode == 4){
                System.out.printf("Output>");
                System.out.println(param1);
                index += 2;
            }
            else if (opcode == 5){
                if (param1 != 0){
                    index = param2;
                } else {
                    index += 3;
                }
            }
            else if (opcode == 6){
                if (param1 == 0){
                    index = param2;
                } else {
                    index += 3;
                }
            }
            else if (opcode == 7){
                if (param1 < param2){
                    memory.set(param3, 1);
                } else {
                    memory.set(param3, 0);
                }
                if (param3 != index) {
                    index += 4;
                }
            }
            else if (opcode == 8){
                if (param1 == param2){
                    memory.set(param3, 1);
                } else {
                    memory.set(param3, 0);
                }
                if (index != param3) {
                    index += 4;
                }
            }
            else {
                System.out.println("ERR" + opcode + "-" + index);
                System.out.println(memory);
                return(0);
            }

        }
        return (memory.get(0));
    }

}
