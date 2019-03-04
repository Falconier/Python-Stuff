from Student import Student

def main():
    s1 = Student("A", 3)
    s2 = Student("B", 3)

    print("s1 greather than s2:", s1>s2)
    print("s1 less than s2:", s1<s2)
    print(s1==s2)
    print(s1!=s2)

main()