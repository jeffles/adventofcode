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

        List<Integer> memory = new ArrayList<>(startingMemory);
        memory.set(1, 12);
        memory.set(2, 2);
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
        System.out.println("Part 1 " + memory.get(0));
        part2(startingMemory);

    }
    private static int part2(ArrayList<Integer> startingMemory) {
        for (int noun = 0; noun <= 99; noun++){
            for (int verb = 0; verb <= 99; verb++){
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
                if (memory.get(0) == 19690720) {
                    System.out.printf("Part 2 %s%s\n", noun, verb);
                    return 1;
                }

            }
        }
        return 1;
    }

}
