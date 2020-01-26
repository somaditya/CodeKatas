val nums = (1 to 10).toList
val names = List("som", "sia", "joe", "scott")

names.foreach(println)

nums.filter(_ > 5).foreach(println)

val squares = nums.map(Math.pow(_, 2))

val capNames = names.map(_.capitalize)

val gtFive = nums.filter(_ > 5)

nums.foldLeft(0)(_ + _)

nums.foldLeft(1)(_ * _)