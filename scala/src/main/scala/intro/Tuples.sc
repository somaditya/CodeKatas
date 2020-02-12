class Person(var name: String)

val t1 = (11, "Eleven", new Person("som"))

println(t1._2)

val (num, string, person) = t1

println(num)
println(string)
println(person)
