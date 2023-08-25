import java.io.*;

class ProblemCorrect {
  public static void main(String[] args) throws IOException {
    var input = new BufferedReader(new InputStreamReader(System.in));
    var cases = Integer.parseInt(input.readLine());
    for (int i = 0; i < cases; i++) {
      var line = input.readLine().split(" ");
      System.out.println(
        Long.parseLong(line[0]) * Long.parseLong(line[1])
      );
    }
  }
}
