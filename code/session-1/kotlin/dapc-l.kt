import kotlin.math.pow

fun main() = println(
  System.`in`.bufferedReader().lineSequence().drop(1).first()
    .split(" ").sumOf { it.toDouble().pow(3) }.pow(1.0 / 3)
)
