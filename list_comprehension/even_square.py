
if __name__=="__main__":
    list1=[i for i in range(1,11)]
    print("total number",list1)
    print("even",list([i for i in list1 if i%2==0]))
    print("even square",list([i*i for i in list1 if i%2==0]))
    print("odd",list([i for i in list1 if i%2!=0]))
    print("odd",list([i*i for i in list1 if i%2!=0]))