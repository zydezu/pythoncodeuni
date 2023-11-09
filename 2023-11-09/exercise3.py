def save_to_log(entry, logfile):
    f = open(f"2023-11-09\\{logfile}",'a') # GIT !
    f.write(entry+"\n")

save_to_log(input("whaddyyaa logg:3") ,"ex3.txt")