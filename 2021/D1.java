import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class D1 {

    public static void main(String[] args) {
        List<String> depths = importDepths();
        System.out.println("Part 1: " + checkEntries(depths));
        System.out.println("Part 1: " + checkEntries2(depths));
    }

    public static List<String> importDepths() {
        List<String> depths = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("in/D1.in"))) {
            String line;
            while ((line = br.readLine()) != null) {
                depths.add(line);
            }
        }
        catch(Exception e) {
            e.printStackTrace();
        }
        return depths;
    }

    public static Integer checkEntries(List<String> depthList) {
        List<String> depth = depthList;Integer previous = Integer.parseInt(depthList.get(0));Integer count = 0;

        for (int i = 1; i < depth.size(); i++) {
            int x = Integer.parseInt(depth.get(i));
            if (x > previous) {
                count++;
            }
            previous = x;
        }
        return count;
    }
    public static Integer checkEntries2(List<String> expenseList) {
        List<String> expenses = expenseList;
        Integer sum = Integer.parseInt(expenseList.get(0))+ Integer.parseInt(expenseList.get(1)) + Integer.parseInt(expenseList.get(2));
        Integer count = 0;

        for (int i = 3; i < expenses.size(); i++) {
            int new_sum = sum + Integer.parseInt(expenses.get(i)) - Integer.parseInt(expenses.get(i-3));

            if (new_sum > sum) {
                count++;
            }
            sum = new_sum;
        }
        return count;
    }

}
