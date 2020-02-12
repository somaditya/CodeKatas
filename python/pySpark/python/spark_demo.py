from pyspark import SparkContext


def main():
    sc = SparkContext.getOrCreate()
    emp = SparkContext.textFile(sc, "emp.txt")
    dept = SparkContext.textFile(sc, "dept.txt")

    emp_data = emp.filter(lambda x: x != "emp_id,emp_name,emp_dept" and int(x.split(",")[0]) % 2 == 0).collect()

    dept_head_rem = dept.filter(lambda x: x != "dept_id,dept_name")
    dept_data = dept_head_rem.collect()

    for row in emp_data:
        print(row)

    print()

    for row in dept_data:
        print(row)


if __name__ == "__main__":
    main()
