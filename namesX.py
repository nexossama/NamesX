import pathlib
def NamesX(path,extention,add_text="N",Frow=None):
    p=pathlib.Path(path)
    for folder in p.iterdir():
        if folder.is_dir():
            NamesX(folder)
            text_file=open(folder/"texts.txt","w")
            if add_text=="Y":
                text_file.write(f"{Frow}\n")
            for file in folder.iterdir():
                if file.suffix==extention:
                    text_file.write(f"{file.name}\n")
            text_file.close()

path=input("input path : ")

add_text=input("do you want to add a row ? (Y/N) ")
Frow=None
if add_text == 'Y':
    Frow = input("write first row text to add : ")

extention=input("enter file extention to select (ex .png) : ")
NamesX(rf"{path}",extention,add_text,Frow)