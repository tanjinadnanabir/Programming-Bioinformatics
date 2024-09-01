def main(file):
    a, b = map(int, open(file).read().split())
    print(sum([x for x in range(a, b) if x % 2 == 1]))

main(r'C:\Users\tanji\Desktop\bioinfo-rosalind\python-village\conditions and loops\rosalind_ini4.txt')