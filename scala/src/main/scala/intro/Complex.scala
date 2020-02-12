package intro

class Complex(real: Double, imaginary: Double) {
  def re = real
  def im = imaginary

  override def toString: String = re.toString + (if (im > 0) s" + $im" + "i" else "")
}

object ComplexTest {
  def main(args: Array[String]): Unit = {
    val c = new Complex(4,0.5)

    println(c.toString)
  }
}


