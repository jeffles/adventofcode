package com.jefsumne;

import java.io.*;
import java.util.*;

public class Day2019_2 {
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

        int answer = runProgram(startingMemory, 12, 2);
        System.out.println("Part 1 " + answer);
        part2(startingMemory);

    }
    private static int part2(ArrayList<Integer> startingMemory) {
        for (int noun = 0; noun <= 99; noun++){
            for (int verb = 0; verb <= 99; verb++){
                int answer = runProgram(startingMemory, noun, verb);

                if (answer == 19690720) {
                    System.out.printf("Part 2 %s%s\n", noun, verb);
                    return 1;
                }

            }
        }
        return 1;
    }

    private static int runProgram(ArrayList<Integer>startingMemory, int noun, int verb) {
        List<Integer> memory = new ArrayList<>(startingMemory);
        memory.set(1, noun);
        memory.set(2, verb);
        int index = 0;
        while (memory.get(index) != 99) {
            int instruction = memory.get(index);
            if (instruction == 1){
                memory.set(memory.get(index+3), memory.get(memory.get(index+1)) + memory.get(memory.get(index+2)));
            }
            else if (instruction == 2){
                memory.set(memory.get(index+3), memory.get(memory.get(index+1)) * memory.get(memory.get(index+2)));
            }
            else {
                System.out.println("ERR");
            }
            index += 4;
        }
        return (memory.get(0));
    }

}
