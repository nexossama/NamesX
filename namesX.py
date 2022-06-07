import pathlib
def NamesX(path,extentions,add_text="N",Frow=None):
    p=pathlib.Path(path)
    for folder in p.iterdir():
        if folder.is_dir():
            NamesX(folder,extentions,add_text,Frow)
            text_file=open(folder/"texts.txt","w")
            if add_text=="Y":
                text_file.write(f"{Frow}\n")
            for file in folder.iterdir():
                if file.suffix in extentions:
                    text_file.write(f"{file.name}\n")
            text_file.close()

path=input("input path : ")

add_text=input("do you want to add a row ? (Y/N) ")
Frow=None
if add_text == 'Y':
    Frow = input("write first row text to add : ")

extentions=input("enter file extention to select (ex .png-.jpg) : ").split("-")
NamesX(rf"{path}",extentions,add_text,Frow)