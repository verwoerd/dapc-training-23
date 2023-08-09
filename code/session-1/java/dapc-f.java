import java.util.*;
import java.io.*;

public class DAPCF {
  public static void main(String[] args) throws IOException {
    Scanner scanner = new Scanner(System.in);
    int x = scanner.nextInt();
    int y = scanner.nextInt();
    double ans = x / (((1.0 * (100 - x) / (100 - y)) * 100.0) - (100 - x));
    System.out.println(ans);
  }
}
