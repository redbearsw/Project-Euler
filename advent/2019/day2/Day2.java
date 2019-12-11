import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.ArrayList;

class Day2 {

  public static ArrayList<Integer> readInput(String name) {
    String line;
    ArrayList<Integer> inputs = new ArrayList<Integer>();
    
    // Read in file to integer array
    try {
      File file = new File(name);
      Scanner sc = new Scanner(file);

      while (sc.hasNextLine()) {
        line = sc.nextLine();
        StringTokenizer tok = new StringTokenizer(line, ",");

        while (tok.hasMoreTokens())
          inputs.add(Integer.parseInt(tok.nextToken()));
      }
    }
    catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    return inputs;
  }

  public static ArrayList<Integer> copy(ArrayList<Integer> oldArr) {
    int i;
    int len = oldArr.size();
    ArrayList<Integer> newArr = new ArrayList<Integer>();
    for (i = 0; i < len; i++)
      newArr.add(oldArr.get(i));
    return newArr;
  }


  public static int part1(ArrayList<Integer> inputs, int noun, int verb) {
    // overwrite positions 1 and 2
    inputs.set(1, noun);
    inputs.set(2, verb);

    // Run the program
    int i;
    int opcode = 0;
    int num1;
    int num2;
    int pos;
    for (i = 0; i < inputs.size(); i += 4) {
      opcode = inputs.get(i);
      if (opcode == 1) {
        num1 = inputs.get(i + 1);
        num2 = inputs.get(i + 2);
        pos = inputs.get(i + 3);
        inputs.set(pos, inputs.get(num1) + inputs.get(num2));
      }
      else if (opcode == 2) {
        num1 = inputs.get(i + 1);
        num2 = inputs.get(i + 2);
        pos = inputs.get(i + 3);
        inputs.set(pos, inputs.get(num1) * inputs.get(num2));
      }
      else if (opcode == 99) {
        return inputs.get(0);
      }
      else {
        // error
        return -1;
      }
    }

    // error  
    return -1;
  }

  public static int part2(ArrayList<Integer> inputs) {
    int noun;
    int verb;
    int res;
    for (noun = 0; noun < 100; noun++) {
      for (verb = 0; verb < 100; verb++) {
        ArrayList<Integer> test_state = copy(inputs);
        res = part1(test_state, noun, verb);
        if (res == 19690720)
          return 100 * noun + verb;
        
      }
    }
    return -1;

  }

  public static void main(String args[]) {
    ArrayList<Integer> inputs = readInput("input.txt");
    System.out.println("Part 1: " + part1(inputs, 12, 2));

    inputs = readInput("input.txt");
    System.out.println("Part 2: " + part2(inputs));
  }
}

