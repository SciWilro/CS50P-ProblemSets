# Maths interpreter
# # https://cs50.harvard.edu/python/2022/psets/1/interpreter/
__author__ = "Wilro - https://github.com/SciWilro"


def main():
    expression = input("Gimme maths: ")
    x, y, z = expression.split(" ")
    answer = do_maths(float(x), y, float(z))
    print(answer)


def do_maths(x, y, z) -> float:
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "/":
            return x / z
        case "*":
            return x * z


main()
