import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class D2 {

    public static void main(String[] args) {
        List<String> commands = importCommands();
        System.out.println("Part 1: " + part1(commands));
        System.out.println("Part 1: " + part2(commands));
    }

    public static List<String> importCommands() {
        List<String> commands = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("in/input"))) {
            String line;
            while ((line = br.readLine()) != null) {
                commands.add(line);
            }
        }
        catch(Exception e) {
            e.printStackTrace();
        }
        return commands;
    }

    public static Integer part1(List<String> commandList) {
        List<String> commands = commandList;
        Integer horizontal = 0;
        Integer depth = 0;

        for (int i = 0; i < commands.size(); i++) {
            String[] coms = commands.get(i).split(" ");
            if (coms[0].equals("forward")){
                horizontal += Integer.parseInt(coms[1]);
            } else if (coms[0].equals("down")){
                depth += Integer.parseInt(coms[1]);
            } else if (coms[0].equals("up")){
                depth -= Integer.parseInt(coms[1]);
            }
        }
        return horizontal*depth;
    }
    public static Integer part2(List<String> commandList) {
        List<String> commands = commandList;
        Integer horizontal = 0;
        Integer depth = 0;
        Integer aim = 0;

        for (int i = 0; i < commands.size(); i++) {
            String[] coms = commands.get(i).split(" ");
            if (coms[0].equals("forward")){
                horizontal += Integer.parseInt(coms[1]);
                depth += aim * Integer.parseInt(coms[1]);
            } else if (coms[0].equals("down")){
                aim += Integer.parseInt(coms[1]);
            } else if (coms[0].equals("up")){
                aim -= Integer.parseInt(coms[1]);
            }
        }
        return horizontal*depth;
    }

}
