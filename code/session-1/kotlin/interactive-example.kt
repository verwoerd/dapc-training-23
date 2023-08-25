fun main() {
  val output = System.out.bufferedWriter()
  var low = 0
  var high = readln().toInt()
  var state: String
  do {
    val mid = (low + high) shr 1
    output.write("$mid\n")
    output.flush()
    state = readln()
    when (state) {
      "higher" -> low = mid + 1
      "lower" -> high = mid - 1
    }
  } while (state != "correct")
}
