import sys,time,os,re,shutil
Disk="C:"
def JumpBackWD(jump_Nbr) : #WD is for working directory
    new_Cwd=os.getcwd()
    list_Cwd=new_Cwd.split("\\")
    del list_Cwd[len(list_Cwd)-jump_Nbr]
    del list_Cwd[0]
    list_Cwd = '\\'.join(list_Cwd)
    os.chdir(Disk+list_Cwd)
    
print("-help pour une liste des commandes disponibles et -exit pour quitter le programme proprement\n")
while True:
    
    cwd = os.getcwd()
    string_With_Args =input(cwd+">>>")
    list_Args = string_With_Args.split(" ")
    nbr_Args=0
    help="Liste des différentes commandes disponibles :\n   -quit : Quitte le programme proprement"
    while nbr_Args<len(list_Args):
        if list_Args[nbr_Args]=="help":
            print(help)

            
        elif list_Args[nbr_Args]=="quit" or list_Args[nbr_Args]=="exit":
            sys.exit()

            
        elif list_Args[nbr_Args]=="cwd":
            nbr_Args+=1
            print(cwd)            
        elif list_Args[nbr_Args]=="cd": #check if a directory exists, and setup the cwd(current working directory) on this directory if he is a son of the cwd. 
            nbr_Args+=1
            if list_Args[nbr_Args]=="-b":
                nbr_Args+=1
                nbr_Jump_Back = list_Args[nbr_Args]
                try:
                    nbr_Jump_Back=int(nbr_Jump_Back)
                    JumpBackWD(nbr_Jump_Back)
                except ValueError:
                    print("Arguments invalides")
            elif os.path.exists(list_Args[nbr_Args]):
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
        elif list_Args[nbr_Args]=="disk":
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
        elif list_Args[nbr_Args]=="del":
            nbr_Args+=1
            if list_Args[nbr_Args]=="-d":   #if it's a directory, you need to ad the -d arguments.
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
