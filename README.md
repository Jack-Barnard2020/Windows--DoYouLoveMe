# Windows--DoYouLoveMe
Computer will ask you every hour if you love them, untill you say yes.

# Set-up
## Download the files
Download all the files and save them inside a folder, in your documments on the 'C:\' Drive.
## Installing the mdoulea
For python to communicate with windows to display pop-up messages we meed tp install [python](https://www.python.org/) and the pyhthon module [tkinter](https://docs.python.org/3/library/tkinter.html).

To install python follow the steps on the link above.

Python mmust be installed before this step is followed. To install tkinter, open up the command prompt and run the commands below:
```
python --version
pip -V
pip install tk
```
The first two commands must run sucsesfully before being able to install tkinter
## Setting up batch file
The batch file meeds to be given two adress where the 'python.exe' file is located and where the python program to run is located.
```
@echo off
"Your python.exe adress" "The pyhton file to run adress"
exit
```
## Setting up windows scheduler
We can now use windwos scheduler to run the .bat file, intern running the python file, when a specifc event is triggered, in this exsample every hour.

To do this go to the search bar and search for
> Windows Administrative Tools

Then click on the spp. Then search for

> Task Scheduler

Noe we can start creating our task. Navigate over to the right side bar and click 'Create Task...'. Now on the window that just appeared, give your task a name I named mine 'Run Message Box'. This is the only thing we need to do on this page.

So, click triggers > new. We are doing our task on a schedule so select from the drop down menu. Under settings click daily. Then for start put todays date and the upcomming hour. Now look down at advanced settings. Click 'Repeat task every' and select from the drop down menu '1 hour'. Then under the drop down menu 'for a duration of' select 'indefinetly' Click ok.

Next, click actions > new. Select start a program form the drop down menu 'Action'. Then click 'Browse..' and select the .bat file used tp run the python script. click ok.

Then click ok again, and your done!
