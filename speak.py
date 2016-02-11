#this scripneed internet connection(uses google api for voice recognition)
#different programs can be opened/closed by voice command

import subprocess
import speech_recognition as sr
import os
import ctypes
import signal
r = sr.Recognizer()
notepad_path='C:\\Program Files\\Notepad++\\notepad++.exe';
chrome_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
firefox_path='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
matlab_path='C:\\Program Files\\MATLAB\\R2014a\\bin\\matlab.exe'
eclipse_path='C:\\Users\\ABHKUMKU\\Documents\\New folder\\eclipse.exe - Shortcut.lnk'
auto_saver_path='D:\\Softwares\\Auto_saver\\Auto_saver1.0 with screen capture +gday.jar'

paint_path='C:\\Windows\\system32\\mspaint.exe'
sticky_notes_path='C:\\Windows\\system32\\StikyNot.exe';
calculator_path='C:\\Windows\\system32\\calc.exe'
skype_path='C:\\Program Files\\Skype\\Phone\\Skype.exe'
sniping_path='C:\\Windows\\system32\SnippingTool.exe';

# recognize speech using Google Speech Recognition
def print_audio(audio):
    try:
  

        words=r.recognize_google(audio);
    except sr.UnknownValueError:
        print ("Google Speech Recognition could not understand audio... \n ");
        words=raw_input("Please type the commands.....\n")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e));
        words=raw_input("Please type the commands......\n")
    #print(words);
    return words;


# obtain audio from the microphone
def get_audio_input():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    return audio;

audio=get_audio_input();
commands=print_audio(audio).lower();
#commands='dfd  close   notepad chrome'
print commands;

if ('open' in commands)  or ('start' in commands) or ('run' in commands):
    print 'open...'
    if 'chrome' in commands:
        print ('opening.. chrome...');
        os.startfile(chrome_path)
    if 'notepad' in commands:
        print ('opening notepad');
        os.startfile(notepad_path)
    if 'eclipse' in commands:
        print('opening eclipse...');
        os.startfile(eclipse_path)
    if 'matlab' in commands:
        print('opening matlab...');
        os.startfile(matlab_path)
    if 'firefox' in commands:
        print('opening firefox...');
        os.startfile(firefox_path)
    if ('sticky' in commands) or ('notes' in commands):
        print('opening sticky notes...');
        os.startfile(sticky_notes_path)
    if ('paint' in commands):
        print('opening paints ...');
        os.startfile(paint_path)
    if ('calci' in commands) or ('calculator' in commands):
        print('opening calculator ...');
        os.startfile(calculator_path)
    if ('skype' in commands) or ('skypi' in commands):
        print('opening skype ...');
        os.startfile(skype_path)
    if ('sniping' in commands) or ('snipping' in commands) or ('snapping' in commands):
        print('opening snipping tool ...');
        os.startfile(sniping_path)
        
    if ('autosaver' in commands)or ('autosave' in commands) or (('auto' in commands) and ('saver' in commands)):
        print('opening autosaver...');
        os.startfile(auto_saver_path)
        
        
if ('close' in commands) or ('stop' in commands) or ('exit' in commands):
    print ('close...');
    cmd = 'WMIC PROCESS get Caption,Processid'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        list=line.split()
        if not list:
            continue;
        proc_name=list[0]
        proc_id=list[1]
        if ('chrome' in commands) and ('chrome' in proc_name.lower()):
            print('closing chrome...');
            os.system("taskkill /im "+proc_name)
        if ('firefox' in commands) and ('firefox' in proc_name.lower()):
            print('closing firefox...');
            os.system("taskkill /im "+proc_name)
        if ('notepad' in commands) and ('notepad' in proc_name.lower()):
            print('closing notepad...');
            os.system("taskkill /im "+proc_name)
        if ('eclipse' in commands) and ('eclipse' in proc_name.lower()):
            print('closing eclipse...');
            os.system("taskkill /im "+proc_name)
        if ('matlab' in commands) and ('matlab' in proc_name.lower()):
            print('closing matlab...');
            os.system("taskkill /im "+proc_name)
        if ('skype' in commands) and ('skype' in proc_name.lower()):
            print('closing skype...');
            os.system("taskkill /im "+proc_name)
        if (('paint' in commands)  or ('pant' in commands ))and ('paint' in proc_name.lower()):
            print('closing paint...');
            os.system("taskkill /im "+proc_name)
        if ('calculator' in commands) and ('calc' in proc_name.lower()):
            print('closing calculator...');
            os.system("taskkill /im "+proc_name)
        if ('sticky' in commands) and ('stiky' in proc_name.lower()):
            print('closing sticky notes...');
            os.system("taskkill /im "+proc_name)
        if (('sniping' in commands) or ('snapping' in commands) or ('napping' in commands and 'tool' in commands)) and ('snipping' in proc_name.lower()):
            print('closing snipping tool...');
            os.system("taskkill /im "+proc_name)
            
if ('lock'in commands) and (('screen' in commands) or 'window' in commands):
    print('locking windows...');
    ctypes.windll.user32.LockWorkStation();
    ctypes.windll.user32
if ('hibernate' in commands):
    os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
