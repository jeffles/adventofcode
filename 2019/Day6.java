package com.jefsumne;

import java.io.*;
import java.util.*;

public class Day2019_6 {
    public static void main(String[] args) throws IOException {

        File inputFile = new File("input.txt");
        Scanner myReader = new Scanner(inputFile);
        HashMap<String, String> orbits = new HashMap<String, String>();

        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String[] parts = data.split("\\)", 2);
            String orbitee = parts[0];
            String orbiter = parts[1];
//            System.out.println(orbitee + "-" + orbiter);
            orbits.put(orbiter, orbitee);
        }
        myReader.close();
        System.out.println(orbits);

        int distance = 0;
        for (String i : orbits.keySet()) {
//            System.out.println(i);
            while (orbits.get(i) != null) {
                distance += 1;
                i = orbits.get(i);
            }
        }
        System.out.println(distance);
        distance = 0;
        String i = "YOU";
        while (orbits.get(i) != null && !"124".equals(i)) {
            distance += 1;
            System.out.println(i);
            i = orbits.get(i);
        }
        System.out.println("-------------------");
        i = "SAN";
        while (orbits.get(i) != null && !"124".equals(i)) {
            distance += 1;
            System.out.println(i);
            i = orbits.get(i);
        }
        System.out.print(distance-2);






    }

}
