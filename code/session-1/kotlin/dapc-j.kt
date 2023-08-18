import java.math.RoundingMode
import kotlin.math.*
const val CIRCLE = 2* PI
fun main() {
  val input = System.`in`.bufferedReader()
  val (circles, e) = input.readLine().split(" ").take(2).map { it.toDouble() }
  val radii = input.readLine().split(" ").take(circles.toInt()).map { it.toDouble() }
  println(radii.sumOf {
    val alpha = asin(e/(2*it))*2
    when {
      alpha.isNaN() -> 1
      else -> (CIRCLE / alpha).toBigDecimal().setScale(6, RoundingMode.HALF_UP).toLong()
    }
  })
}
