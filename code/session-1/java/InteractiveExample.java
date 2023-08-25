import java.io.*;

public class InteractiveExample {
  public static void main(String... args) throws IOException {
    var output = new BufferedWriter(new OutputStreamWriter(System.out));
    var input = new BufferedReader(new InputStreamReader(System.in));
    var low = 0;
    var high = Integer.parseInt(input.readLine());
    String state;
    do {
      var mid = (low + high) >> 1;
      output.write(mid + "\n");
      output.flush();
      state = input.readLine();
      if (state.equals("higher")) {
        low = mid + 1;
      } else if (state.equals("lower")) {
        high = mid - 1;
      }
    } while (!state.equals("correct"));
  }
}
