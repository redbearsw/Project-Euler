
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Day1 {

  public static int part1(String name) {
    int sum = 0;
    int num;
    String line;
    

    try {
      File file = new File(name);
      Scanner sc = new Scanner(file);

      while (sc.hasNextLine()) {
        line = sc.nextLine();
        num = Integer.parseInt(line);
        num = num / 3;
        num = num - 2;
        sum += num;
      }
    }
    catch (FileNotFoundException e) {
      e.printStackTrace();
    }
    
    return sum;
  }

  public static int findFuel(int mass) {
    int fuel = (mass / 3) - 2;
    if (fuel <= 0) {
      return 0;
    }
    else {
      return fuel + findFuel(fuel);
    }
    
  }

  public static int part2(String name) {
    int sum = 0;
    int num;
    int newFuel;
    String line;
    try {
      File file = new File(name);
      Scanner sc = new Scanner(file);

      while (sc.hasNextLine()) {
        line = sc.nextLine();
        num = Integer.parseInt(line);
        newFuel = findFuel(num);
        sum += newFuel;
      }
    }
    catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    return sum;
  }
    
  public static void main(String args[]) {
    System.out.println("Part 1: " + part1("input.txt"));
    System.out.println("Part 2: " + part2("input.txt"));

  }
}
