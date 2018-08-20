def merge_the_tools(string, k):
    print(len(string))
    n = int(len(string)/k)
    numb = len(string)
    start = 0
    end = int(numb/n)
    for i in range(n):
        emp = ''
        sub = string[start:end]
        print(sub)
        for j in range(len(sub)):
            if sub[j] not in emp:
                emp += sub[j]
        print(emp)
        emp = ''
        start += k
        end += k



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)