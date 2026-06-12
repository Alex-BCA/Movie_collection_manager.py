movies=[]
while True:
    print("****Movie collection manager")
    print("1.Add movie")
    print("2.View movie")
    print("3.Search movie")
    print("4.Delete movie")
    print("5.Count movie")
    print("6.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        print("Add movie:")
        movie=input("Enter movie name:")
        movies.append(movie)
    elif choice=="2":
        print("View movie:")
        for i in range(len(movies)):
            print(i+1,".",movies[i])
    elif choice=="3":
        print("Search movies:")
        movie=input("Enter searching movie name")
        if movie in movies:
            print("movie identified!")
        else:
            print("Do not fouunt!")
    elif choice=="4":
        print("Delete movie:")
        movie=input("Enter deleting movie name:")
        if movie in movies:
            movies.remove(movie)
            print("Delete successfully!")
        else:
            print("Do not found!")
    elif choice=="5":
        print("Count movies:")
        print("Total movies =",len(movies))
    elif choice=="6":
        print("Thank you!")
        break
    else:
        print("In-valid syntax")
        
        

