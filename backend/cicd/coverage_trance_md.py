import sys


def main():
    with open(sys.argv[1], "r") as f:
        t = f.read()
    lines = t.split("\n")
    mkdown = "|Name|Stmts|Miss|Cover|\n|---|---|---|---|\n"
    for line in lines[2:-1]:
        cells = line.split(" ")
        elms = []
        for cell in cells:
            if cell == "":
                continue
            else:
                elms.append(cell)
        s = "|" + "|".join(elms) + "|\n"
        mkdown += s
    with open(sys.argv[1], "w") as f:
        f.write(mkdown)


if __name__ == "__main__":
    main()
