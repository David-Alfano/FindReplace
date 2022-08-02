#! python3
import os, typer, csv

app = typer.Typer()

@app.command()
def guided_creation(oldFilename: str = "", replaceKeysFilename: str = ""):
    typer.echo(typer.style(
"\n /$$$$$$$$ /$$$$$$ /$$   /$$ /$$$$$$$         /$$$ \n\
| $$_____/|_  $$_/| $$$ | $$| $$__  $$       /$$ $$ \n\
| $$        | $$  | $$$$| $$| $$  \ $$      |  $$$ \n\
| $$$$$     | $$  | $$ $$ $$| $$  | $$       /$$ $$/$$ \n\
| $$__/     | $$  | $$  $$$$| $$  | $$      | $$  $$_/ \n\
| $$        | $$  | $$\  $$$| $$  | $$      | $$\  $$ \n\
| $$       /$$$$$$| $$ \  $$| $$$$$$$/      |  $$$$/$$\n\
|__/      |______/|__/  \__/|_______/        \____/\_/ \n\
\n\
 /$$$$$$$  /$$$$$$$$ /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$$$$$$$ \n\
| $$__  $$| $$_____/| $$__  $$| $$       /$$__  $$ /$$__  $$| $$_____/ \n\
| $$  \ $$| $$      | $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ \n\
| $$$$$$$/| $$$$$   | $$$$$$$/| $$      | $$$$$$$$| $$      | $$$$$ \n\
| $$__  $$| $$__/   | $$____/ | $$      | $$__  $$| $$      | $$__/ \n\
| $$  \ $$| $$      | $$      | $$      | $$  | $$| $$    $$| $$ \n\
| $$  | $$| $$$$$$$$| $$      | $$$$$$$$| $$  | $$|  $$$$$$/| $$$$$$$$ \n\
|__/  |__/|________/|__/      |________/|__/  |__/ \______/ |________/\n\n\
                        BY: DAVID ALFANO   v1.1\n",fg=typer.colors.CYAN))                                                                        
                                                                                                                                                     
    typer.echo(typer.style("This program will guide you through the process of updating NAV XML files to use new device references.\n",fg=typer.colors.GREEN, bold=True))
    typer.echo(typer.style("To use, you will enter the filename you wish to update and csv filename with the keys to replace desired elements.\n\n",fg=typer.colors.GREEN, bold=True))

    continueRoutine = True

    if oldFilename == "":
        oldFilename = typer.prompt("Please enter the filename of the XLM on your Desktop you wish to update")
    if replaceKeysFilename == "":
        replaceKeysFilename = typer.prompt("Please enter the filename of the key file on your Desktop")
    newFilename = f"{oldFilename.split('.')[0]}_Updated.{oldFilename.split('.')[1]}"

    typer.echo(typer.style("\nGenerating new file...",fg=typer.colors.YELLOW, bold=True))

    while continueRoutine:

        generateXML(oldFilename,replaceKeysFilename,newFilename)

        os.system('cls||clear')

        typer.echo(typer.style(
    "\n\n     $$$$$$\                                                       $$ \n\
    $$  __$$\                                                      $$ | \n\
    $$ /  \__$$\   $$\ $$$$$$$\ $$$$$$$\ $$$$$$\  $$$$$$$\ $$$$$$$\$$ | \n\
    \$$$$$$\ $$ |  $$ $$  _____$$  _____$$  __$$\$$  _____$$  _____$$ | \n\
     \____$$\$$ |  $$ $$ /     $$ /     $$$$$$$$ \$$$$$$\ \$$$$$$\ \__| \n\
    $$\   $$ $$ |  $$ $$ |     $$ |     $$ ____|  \____$$\ \____$$\    \n\
    \$$$$$$  \$$$$$$  \$$$$$$$\\\$$$$$$$\\\$$$$$$$\$$$$$$$  $$$$$$$  $$\ \n\
     \______/ \______/ \_______|\_______|\_______\_______/\_______/\__|",fg=typer.colors.GREEN, bold=True, blink=True))

        typer.echo(f"\n\nThe updated file has now been saved to you desktop with the filename: {typer.style(newFilename,fg=typer.colors.CYAN)}")

        continueRoutine = typer.confirm("\nDo you wish to convert another file with the same file paths?")

def generateXML(oldFilename,replaceKeysFilename,newFilename):
    
    with open(f'C:\\Users\\{os.getlogin()}\\Desktop\\{oldFilename}','r') as oldFile, open(f'C:\\Users\\{os.getlogin()}\\Desktop\\{replaceKeysFilename}','r', newline='') as replaceKeysFile, open(f'C:\\Users\\{os.getlogin()}\\Desktop\\{newFilename}','w+') as newFile:
        oldXML = oldFile.read()
        replaceKeys = csv.DictReader(replaceKeysFile)
        for row in replaceKeys:
            oldXML = oldXML.replace(f"\"{row['oldProcessID']}\"",f"\"{row['newProcessID']}\"")
            oldXML = oldXML.replace(f":{row['oldProcessID']}:",f":{row['newProcessID']}:")
            oldXML = oldXML.replace(f"Device={row['oldProcessID']}\"",f"Device={row['newProcessID']}\"")
        newFile.write(oldXML)
   

if __name__ == "__main__":
	app()