for i in range(2,21) :
    with open (f"Table/multiplication_table_of_{i}.txt", "w") as f :
        for j in (1,11) :
            print (f"{i}×{j}={i*j}")
            if j !=10:
                print ("\n")
'''with open (f"Table/multiplication_table_of_k.txt", "a") as f :
    for i in range(2,21) :
        for j in range(1,11) :
            f.write(f"\t\t{i}×{j}={i*j} \t\t\n")
        f.write("\t***********************\n")'''