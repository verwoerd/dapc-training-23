fun main() {
  val t = readln().toInt();
  System.`in`.bufferedReader().lineSequence().take(t).forEach { line ->
    println(line.split(" ").map { it.toLong() }.let { (a, b) -> a * b })
  }
}
