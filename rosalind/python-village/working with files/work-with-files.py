def main(file):
    for i, line in enumerate(open(file).readlines()):
        if i % 2 == 1:
            print(line, end="")

main(r'python-village\working with files\rosalind_ini5.txt')