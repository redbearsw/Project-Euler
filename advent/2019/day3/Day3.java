import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;

class Day3 {

  public static ArrayList<ArrayList<String>> readInput(String name) {
    String line;
    ArrayList<ArrayList<String>> inputs = new ArrayList<ArrayList<String>>();
    ArrayList<String> path;
    
    // Read in file to integer array
    try {
      File file = new File(name);
      Scanner sc = new Scanner(file);
      
      while (sc.hasNextLine()) {
        
        path = new ArrayList<String>();
        line = sc.nextLine();
        StringTokenizer tok = new StringTokenizer(line, ",");

        while (tok.hasMoreTokens())
          path.add(tok.nextToken());
        
        inputs.add(path);
      }
    }
    catch (FileNotFoundException e) {
      e.printStackTrace();
    }
    
    return inputs;
  }

  public static ArrayList<ArrayList<String>> buildGrid(ArrayList<String> inputs) {
    // grid starting point
    ArrayList<ArrayList<String>> grid = new ArrayList<ArrayList<String>>();
    grid.add(new ArrayList<String>());
    grid.get(0).add("o");

    // add wires
    int i;
    int j;
    int k;
    int currX = 0;
    int currY = 0;
    int len = inputs.size();
    for (i = 0; i < len; i++) {
      String instr = inputs.get(i);
      char firstChar = instr.charAt(0);
      int num = Integer.parseInt(instr.substring(1));

      if (firstChar == 'U') {
        for (j = currY + 1; j <= currY + num; j++) {
          try {
            grid.get(j);
          } catch (IndexOutOfBoundsException e) {
            grid.add(new ArrayList<String>());
          }
          for (k = 0; k <= currX; k++) {
            try {
              grid.get(j).get(k);
            } catch (IndexOutOfBoundsException e) {
              grid.get(j).add(".");
            }
          }
          grid.get(j).set(currX, "-");
        }

        currY = currY + num;
      }
      else if (firstChar == 'R') {
        for (j = currX + 1; j <= currX + num; j++) {
          try {
            grid.get(currY).get(j);
          } catch (IndexOutOfBoundsException e) {
            grid.get(currY).add(".");
          }
          grid.get(currY).set(j, "-");
        }
        currX = currX + num;
      }
      else if (firstChar == 'L') {
        for (j = currX - 1; j >= currX - num; j--) {
          try {
            grid.get(currY).get(j);
          } catch (IndexOutOfBoundsException e) {
            grid.get(currY).add(".");
          }
          grid.get(currY).set(j, "-");
        }
        currX = currX - num;
      }
      else if (firstChar == 'D') {
        for (j = currY - 1; j >= currY - num; j--)
          try {
            grid.get(j);
          } catch (IndexOutOfBoundsException e) {
            grid.add(new ArrayList<String>());
          }
          for (k = 0; k <= currX; k++) {
            try {
              grid.get(j).get(k);
            } catch (IndexOutOfBoundsException e) {
              grid.get(j).add(".");
            }
          }
          grid.get(j).set(currX, "-");

        currY = currY - num;
      }
      else {
        throw new IllegalArgumentException("Instruction given improperly");
      }
    }
    return grid;
  }

  public static int min(int a, int b) {
    if (a < b)
      return a;
    else
      return b;
  }

  public static ArrayList<Tuple> intersect(ArrayList<ArrayList<String>> firstGrid, ArrayList<ArrayList<String>> secondGrid) {
    ArrayList<Tuple> isects = new ArrayList<Tuple>();
    int i;
    int j;

    // len1 is set to the minimum of the two grids bc they can't intersect past that
    int len1;
    int len2;
    int lenFirst = firstGrid.size();
    int lenSec = secondGrid.size();

    len1 = min(lenFirst, lenSec);
    
    for (i = 0; i < len1; i++) {

      lenFirst = firstGrid.get(i).size();
      lenSec = secondGrid.get(i).size();
      len2 = min(lenFirst, lenSec);

      for (j = 0; j < len2; j++)
        if (firstGrid.get(i).get(j) == "-" && secondGrid.get(i).get(j) == "-")
          isects.add(new Tuple<Integer, Integer>(i, j));
    }

    return isects;
  }

  public static int part1(String name) {
    // read inputs
    ArrayList<ArrayList<String>> inputs = readInput(name);

    // create grids from inputs
    ArrayList<ArrayList<String>> firstGrid = buildGrid(inputs.get(0));
    ArrayList<ArrayList<String>> secondGrid = buildGrid(inputs.get(1));

    // search grids and list intersections
    ArrayList<Tuple> isects = intersect(firstGrid, secondGrid);

    // find manhattan distance from port to each intersection
    int i;
    int len = isects.size();
    int dist;
    Tuple<Integer, Integer> coord = isects.get(0);
    int currMin = coord.getX() + coord.getY();
    for (i = 1; i < len; i++) {
      coord = isects.get(i);
      dist = coord.getX() + coord.getY();
      currMin = min (dist, currMin);
    }

    return currMin;
  }

  public static void main(String[] args) {
    System.out.println("Part 1: " + part1("input.txt"));
  }
}

