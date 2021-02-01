package com.jefsumne;

import java.io.*;
import java.util.*;

public class Day1 {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> numbers=new ArrayList<>();

        File inputFile = new File("input.txt");
        Scanner myReader = new Scanner(inputFile);
//
//        while (myReader.hasNextLine()) {
//            String data = myReader.nextLine();
//            int i = Integer.parseInt(data);
//            numbers.add(i);
//        }

        int totalFuel1 = 0;
        int totalFuel2 = 0;
        int fuel;
//        for (int mass : numbers) {
        while (myReader.hasNext()) {
            int mass = myReader.nextInt();
            fuel = (int) Math.floor(mass / 3.0);
            fuel -= 2;
            totalFuel1 += fuel;
            totalFuel2 += fuel;
            while (fuel > 0) {
                fuel = (int) Math.floor(fuel / 3.0);
                fuel -= 2;
                if (fuel > 0) {
                    totalFuel2 += fuel;
                }
            }
//            System.out.printf("Mass: %s Fuel: %s Total: %s\n", mass, fuel, totalFuel1);
        }

        System.out.println("Part 1: " + totalFuel1);
        System.out.println("Part 2: " + totalFuel2);
        myReader.close();
    }

}
