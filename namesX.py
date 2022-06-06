import pathlib
def namesX(path):
    p=pathlib.Path(path)
    for folder in p.iterdir():
        if folder.is_dir():
            renameX(folder)
            text_file=open(folder/"texts.txt","w")
            for file in folder.iterdir():
                if file.suffix==".png":
                    text_file.write(f"{path}\n")
            text_file.close()

path=input("input path : ")
renameX(rf"{path}")