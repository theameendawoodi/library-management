books={
    'theory of philosophy':{
        'author':'ameen',
        'pages':"342",
        'genre':'philosophy',
        'instock':True,
    },
    'ursule':{
        'author':'muty',
        'pages':"2345",
        'genre':'novel',
        'instock':True
    },
    'programming in c':{
        'author':'yashwant kanetkar',
        'pages':'2345',
        'genre':'programming',
        'instock':True,
        }
}
members={
    'ameen':{
        'address':'201 safa residency nri colony nizamabad',
        'phone number':"7993534416",
        'lent books':'theory of philosophy'
        },
    'muti':{
        'address':'201 safa residency nri colony nizamabad',
        'phone number':"8096730314",
        'lent books':'programming in c,ursule'
        }
    }
def printdata(dict1,dict2=None):
    print(dict1)
    if dict2!=None:
        print(dict2)
def finddata(name,dict1,dict2=None):
    for i in dict1.keys():
        for j in dict1[i]:
            if dict1[i][j]==name:
                print(i,"\n",dict1[i])
    if dict2!=None:
        for i in dict2.keys():
            for j in dict2[i]:
                if dict2[i][j]==name:
                    print(i,"\n",dict2[j])
def finddataindata(name,dict1,dict2=None):
    for i in dict1.keys():
        if i==name:
            print(dict1[i])
    if dict2!=None:
        for i in dict2.keys():
            if i==name:
                print(dict2[i])
                
        
print()
print("your options are \n1.printing all the data avialable")
print()
print("2.finding a specific data in all the given data")
print()
choice=int(input("enter your choice"))
print()
if choice==1:
    print("in this you will have three options")
    print()
    print("data of\n1.books\n2.members\n3.all the data about books and members")
    print()
    choicedata=int(input("enter your choice"))
    print()
    if choicedata==1:
        printdata(books)
    elif choicedata==2:
        printdata(members)
    elif choicedata==3:
        printdata(books,members)
    else:
        print("the options entered option is invalid")
        print()
elif choice==2:
    print("your choices in the finding options is")
    print()
    print("1.find a data through specification")
    print()
    print("2.find the data through a name")
    print()
    choicefind=int(input("enter your choice"))
    print()
    if choicefind==1:
        print("finding the data with specification in\n1.books\n2.members\n3.both")
        print()
        choicefindspec=int(input("enter your choice"))
        print()
        if choicefindspec==1:
            name=input("enter the specification")
            finddata(name,books)
        elif choicefindspec==2:
            name=input("enter the specification")
            finddata(name,members)
        elif choicefindspec==3:
            name=input("enter the specification")
            print()
            finddata(name,books,members)
        else:
            print("the option given is not valid")
    elif choicefind==2:
        print("find the data of\n1.books\n2.members\n3.both")
        print()
        choicefinddata=int(input("enter your choice"))
        print()
        if choicefinddata==1:
            name=input("enter the name of the book")
            print()
            finddataindata(name,books)
        elif choicefinddata==2:
            name=input("enter the name of the member")
            print()
            finddataindata(name,members)
        elif choicefinddata==3:
            name=input("enter the name of the book or the member")
            print()
            finddataindata(name,books,members)
        else:
            print("the option given is not valid")
            print()
else:
    print("the option entered is not valid")
    print()
