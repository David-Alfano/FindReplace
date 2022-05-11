# Find & Replace
![findReplaceSplash](https://user-images.githubusercontent.com/104654015/167918361-38675a62-43e0-4156-b186-e96a5ef7109a.png)

## What this tool does
Ever wish there was a fast and simple way to update device references in Nav, without having click through Nav's never ending drop down menus? Well now there is! 
This find and replace tool updates device references for almost all processes including groups, rules, cues, I/Os, and panels. Simply supply the Nav process XML and a CSV file with the new keys and get an updated XML ready to be pushed back to Nav. Really its that simple! 

## How to install it
This tool is really just a simple Python script. That said, in order to run it you must have Python installed on you machine. 
1. Use this installer to get python up and running: [python-3.10.4-amd64.exe](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
2. Make sure to click the Add Python 3.10 to PATH checkbox when prompted, then click on Customize installation 
   
   ![addToPath](https://user-images.githubusercontent.com/104654015/167918415-e04ebd35-1ba4-4744-90b2-2a3832ec8e65.png)
4. Select all the optional features 
   
   ![allOptionalFeatures](https://user-images.githubusercontent.com/104654015/167918457-281e448a-4ab5-4465-9e46-6748c5f26e23.png)
6. Make sure the advanced options match the selected options below
   >NOTE: You can always install the latest version from the web but this one is tested and works.
   
   ![installOptions](https://user-images.githubusercontent.com/104654015/167918501-e512d365-444e-4ca9-98be-0fb61632a0e2.png)
6. Download the tool from here: [FindReplace.zip](https://github.com/David-Alfano/FindReplace/releases/download/v1.0.0/FindReplace.zip)
7. Unzip the zipped folder

That's it - install done!

## How to use it

1. Copy and paste the XML from the Nav process you wish to update into a new file saved on your desktop.
2. Create a csv file saved to your desktop
   * The file should have two columns, one called `oldProcessID` and the other called `newProcessID`
   * In the `oldProcessID` column type the process ID you wish to be replaced
   * In the `newProcessID` column type the process ID that should replace the current process ID
   * In the below example, when exectued the script will update all refrences of `server_tait_156/axis.1` to `usr_hoist_1/axis.2` and all refrences of `server_tait_156/io.1` to `server_main/io.10`

       | oldProcessID | newProcessID |
       | --- | --- |
       | server_tait_156/axis.1 | usr_hoist_1/axis.2 |
       | server_tait_156/io.1 | server_main/io.10 |
2. Navigate to the FindReplace unzipped folder and open FindReplace.exe
3. When prompted, type in the filename of the newly created Nav XML file and press enter 
4. When prompted, type in the filename of the newly created keys CSV file and press enter
   > NOTE: Both of these files must be on your desktop
 
   ![enterFilenames](https://user-images.githubusercontent.com/104654015/167918614-73d6faf0-10df-403f-89cc-2ce2f42b73c6.png)

4. If all goes as planed, the updated XML file will be stored to your desktop with the specified filename. Copy the contents of the updated file back into Nav and save.

   ![success](https://user-images.githubusercontent.com/104654015/167920318-707df221-6b40-476e-bff4-f324b7962aeb.png)

5. All device references should now be up to date, but as with all XML edits, a quick spot check is highly recommended.
6. Need to update more processes with the same keys? Just update the contents of the XML file on your desktop, save, type "y" and hit enter to run the program again.
