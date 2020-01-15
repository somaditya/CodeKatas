val names = List("Som", "Sia", "Somaditya", "Sharmila")

val shortNames = for {
  n <- names
  if n.length < 4
} yield n