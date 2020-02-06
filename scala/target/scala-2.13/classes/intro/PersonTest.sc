class Person(var firstName: String, var lastName: String) {
  def printFullName(): Unit = println(s"$firstName $lastName")
}

val p = new Person("Som", "Basak")
println(p.firstName)
p.lastName = "Sia"
p.printFullName()