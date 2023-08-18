import kotlin.math.sqrt
fun main() {
  val input = System.`in`.bufferedReader()
  val (n, x) = input.readLine().split(" ").take(2).map { it.toInt() }
  val frequencies = input.readLine().split(" ").take(n).map { it.toDouble() }
  val average = frequencies.sumOf { it * it } / n
  val factor = if (average == 0.0) 0.0 else sqrt(x / average)
  println(frequencies.joinToString(" ") { "${it * factor}" })
}
