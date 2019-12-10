import java.io.File;
import java.util.Scanner;
public class ReadFromFile {
  public static void read(name) throws Exception {
    File file = new File(name);
    Scanner sc = new Scanner sc = new Scanner(file);

    while (sc.hasNextLine())
      System.out.println(sc.nextLine());
  }
}

public static void main() {
  read("text.txt");
}
