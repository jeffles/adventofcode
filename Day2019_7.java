package com.jefsumne;

import java.io.File;
import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;



public class Day2019_7 {
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

//        int[] numbers = {4, 3, 2, 1, 0};
//        Permute<Integer> perm = new Permute<Integer>(new Integer[]{4, 3, 2, 1, 0});
//        int maxVal = 0;
//        while(perm.hasNext()){
//            Integer[] nextVal = perm.next();
//            String retVal = " 0";
//            int intRetVal = 0;
//            for (int i : nextVal) {
//                intRetVal = runProgram(startingMemory, String.valueOf(i) + retVal);
//                retVal = " "+ String.valueOf(intRetVal);
//            }
//            if (intRetVal > maxVal){
//                maxVal = intRetVal;
//                System.out.println("total: " + retVal + "-" + Arrays.toString(nextVal));
//            }
//
//        }

        Permute<Integer> perm = new Permute<Integer>(new Integer[]{5, 6, 7, 8, 9});
        int maxVal = 0;
        while(perm.hasNext()){
            Integer[] nextVal = perm.next();
            String retVal = " 0";
            int intRetVal = 0;
            for (int i : nextVal) {
                intRetVal = runProgram(startingMemory, String.valueOf(i) + retVal);
                retVal = " "+ String.valueOf(intRetVal);
            }
            if (intRetVal > maxVal){
                maxVal = intRetVal;
                System.out.println("total: " + retVal + "-" + Arrays.toString(nextVal));
            }

        }
//        int answer = runProgram(startingMemory, numbers);
//        System.out.println("Part 1 " + answer);


    }

    private static int runProgram(ArrayList<Integer>startingMemory) {
        Scanner myInput = new Scanner(System.in);
        return runProgram(startingMemory, myInput);
    }

    private static int runProgram(ArrayList<Integer>startingMemory, String input) {
        StringReader reader = new StringReader(input);
        Scanner myInput = new Scanner(reader);
        return runProgram(startingMemory, myInput);
    }

    private static int runProgram(ArrayList<Integer>startingMemory, Integer[] input) {
        String myString = Arrays.toString(input).replace("[", "").replace("]", "").replace(",", "");

        return runProgram(startingMemory, myString);
    }

    private static int runProgram(ArrayList<Integer>startingMemory, Scanner myInput) {
        List<Integer> memory = new ArrayList<>(startingMemory);

        int index = 0;
        while (memory.get(index) != 99) {
            int instruction = memory.get(index);
            int opcode = instruction % 100;
            int parameters = instruction / 100;

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
                // System.out.printf("Input>");
                int input = myInput.nextInt();
                // System.out.println(input);
                memory.set(param1, input);
                if (index != param1) {
                    index += 2;
                }
            }
            else if (opcode == 4){
                // System.out.printf("Output>");
                // System.out.println(param1);
                return(param1);
                // index += 2;
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
