import sys,time,os,re,shutil
Disk="C:"
def JumpBackWD(jump_Nbr) : """This function jump back on the file tree. For exemple, if i got C:\Directory1\Directory2\Directory3,
    and jump_Nbr is equal to 2, at the end of the function, my path gonna be C:\Directory1"""
    new_Cwd=os.getcwd()
    list_Cwd=new_Cwd.split("\\")
    del list_Cwd[len(list_Cwd)-jump_Nbr]
    del list_Cwd[0]
    list_Cwd = '\\'.join(list_Cwd)
    os.chdir(Disk+list_Cwd)
    
print("-help for list commands and quit/exit to exit properly")
while True:
    
    cwd = os.getcwd()
    string_With_Args =input(cwd+">>>")
    list_Args = string_With_Args.split(" ")
    nbr_Args=0
    help="Liste des différentes commandes disponibles :\n   -quit : Quitte le programme proprement" """I need to update this, there's no 
    command yet. I added several command since i wrote this help"""
    while nbr_Args<len(list_Args):
        if list_Args[nbr_Args]=="help":
            print(help)

            
        elif list_Args[nbr_Args]=="quit" or list_Args[nbr_Args]=="exit":
            sys.exit()

              
        elif list_Args[nbr_Args]=="cd": #check if a directory exists, and setup the cwd(current working directory) on this directory if he is a son of the cwd. 
            nbr_Args+=1
            if list_Args[nbr_Args]=="-b": """Call the JumpBackWD function."""
                nbr_Args+=1
                nbr_Jump_Back = list_Args[nbr_Args]
                try:
                    nbr_Jump_Back=int(nbr_Jump_Back)
                    JumpBackWD(nbr_Jump_Back)
                except ValueError:
                    print("Arguments invalides")
            elif os.path.exists(list_Args[nbr_Args]):"""Without arguments, it search the file with the given name, the file need to be a 
            direct son of the last file in the tree """
                os.chdir(cwd+"/"+list_Args[nbr_Args])
            else:
                print("Dossier Inexistant")

                
        elif list_Args[nbr_Args]=="new":
            nbr_Args+=1
            if list_Args[nbr_Args]=="-d" : #create a new directory (-d for directory)
                nbr_Args+=1
                try :
                    os.mkdir(list_Args[nbr_Args])
                except FileExistsError:
                    print("Il existe déjà un fichier/dossier du même nom.")
            elif list_Args[nbr_Args]=="-f": #create a new file. If there's no extension, by default it's txt. 
                nbr_Args+=1
                try :
                    file= open(list_Args[nbr_Args],"w+")
                    file.close()
                except PermissionError:
                    print("Il existe déjà un fichier/dossier du même nom.")
        elif list_Args[nbr_Args]=="disk": """Change the disk of the Current directory. For example if you got an USB key
            and want to setup the CWD to a directory in this key"""
            nbr_Args+=1
            txt=list_Args[nbr_Args]
            regex = re.compile("^[A-Z]\:\\\\$")
            check_Match = regex.match(txt)
            if (check_Match):
                disk=txt
                print(txt)
                print(disk)
                os.chdir(disk)
            else :
                print("Disque Inexistant")
        elif list_Args[nbr_Args]=="del": """Delete a file"""
            nbr_Args+=1
            if list_Args[nbr_Args]=="-d":   #if it's a directory, you need to add the -d arguments.
                nbr_Args+=1
                shutil.rmtree(list_Args[nbr_Args])
            else:
                try:
                    os.remove(list_Args[nbr_Args])
                except SyntaxError:
                    print("Fichier Introuvable")
                except PermissionError :
                    print("Impossible de supprimer ce fichier")
        else:
            print("Commande Inexistante")      
        nbr_Args+=1
