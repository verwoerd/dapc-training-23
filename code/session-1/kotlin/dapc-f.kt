fun main() {
  val (x, y) = readln().split(" ").take(2).map { it.toDouble() / 100.0 }
  println((x * (1 - y)) / (y * (1 - x)))
}
