import requests
import pprint
from bs4 import BeautifulSoup
import time
import datetime
from colorama import Fore
import os
import sys

class webScrammer:
    def __init__(self, url):
        """That class is only for downloading data from web pages"""
        self.url = url
        self.old_url = url
        self.data = None
        self.name = "Software"

    def scramFromUrl(self, urlFormat='html', returnText=True):
        """This Function scramms from initialized url"""
        page = requests.get(self.url)
        print(f'Connecting to url {self.url}...')
        time.sleep(1)
        print(f'Checking url status...')
        time.sleep(1)
        if self.check_url_status(self.url) == "Ok":
            data = BeautifulSoup(page.text, urlFormat)
            if returnText == True:
                text = data.text
                print(f'Downloading text...')
                time.sleep(2)
                self.data = text
                return text
            else:
                html_code = data
                print(f'Downloading data in {urlFormat} format...')
                time.sleep(2)
                self.data = html_code
                return html_code
        else:
            return False
        
    def writeToFile(self, filename='url_output.txt', urlFormat='html', encoding='utf-8', text=False):
        """This Function writes data to file"""
        data = self.scramFromUrl(urlFormat=urlFormat, returnText=text)
        with open(filename, 'w', encoding=encoding)as url_output:
            url_output.write('{\n')
            url_output.write(f'    url:{self.url}\n')
            url_output.write(f'     date of download data:{str(datetime.datetime.now())}\n')
            url_output.write(f'     script:{self.name}\n')
            url_output.write(f'     success:{True}\n')
            url_output.write(f'     filename:{filename}\n')
            url_output.write(f'     initialized url:True\n')
            url_output.write(f'     data:\n')
            try:
                if text == False:
                    url_output.write(f'     {str(data.encode("utf-8"))}\n')
                else:
                    url_output.write(f'     {str(data)}\n')
                url_output.write('}\n')
            except:
                print('Something went wrong:(')
        
        return 'Done!'
    
    def readFromFile(self, filename='url_output.txt', encoding='utf-8', timeSpace=0.05):
        """This Function returns data from file"""
        data = ''
        with open(filename, 'r', encoding=encoding) as url_output:
            data = url_output.readlines()
        
        for line in data:
            pprint.pprint(line)
            time.sleep(timeSpace)
    
    def change_url(self, new_url):
        self.url = new_url
        return self.url

    def restart(self, filenameToRestart):
        """This Function is deleting data, if user wants to"""
        self.change_url(self.old_url)
        self.data = None
        with open(filenameToRestart, 'w') as file:
            file.write('Data Lost')
        return f'{Fore.RED}data lost{Fore.WHITE}'

    def returnData(self):
        return f'Data from: {self.url}\nData:{self.data}'
    
    @staticmethod
    def scram_from_uninitialized_url(url, returnText=True, urlFormat='html'):
        """This Function is for url, that isn't inserted to scrammer"""
        page = requests.get(url)
        print(f'Connecting to uninitialized url {url}...')
        time.sleep(1)
        print(f'Checking uninitialized url status...')
        time.sleep(1)
        if page.status_code == 200:
            data = BeautifulSoup(page.text, urlFormat)
            if returnText == True:
                text = data.text
                print(f'Downloading text...')
                time.sleep(2)
                return text
            else:
                html_code = data
                print(f'Downloading data in {urlFormat} format...')
                time.sleep(2)
                return html_code
        else:
            return False
    
    @staticmethod
    def check_url_status(url):
        url = requests.get(url)
        if url.ok:
            return "Ok"
        else:
            return "No"

  

class Tester:
    def calulateTimeOfFunctionOperations(function):
        now = datetime.datetime.now()
        function()
        now2 = datetime.datetime.now()
        return now2-now
    
class Software:
    def __init__(self, operator):
        self.operator = operator
        self.name = ""

class HUD:
    """HUD class contains options, operators, software and console's color"""
    class HUD_COLOR:
        """This class contains HUD's colors"""
        def __init__(self, color_1, color_2, color_3, color_4, color_5, color_6, color_7):
            """
            Here, there are created colors by adding Fore 
            and color with caps and writing them to variables
            """
            self.c_1 = eval("Fore."+color_1)
            self.c_2 = eval("Fore."+color_2)
            self.c_3 = eval("Fore."+color_3)
            self.c_4 = eval("Fore."+color_4)
            self.c_5 = eval("Fore."+color_5)
            self.c_6 = eval("Fore."+color_6)
            self.c_7 = eval("Fore."+color_7)

    def __init__(self, url, software_name):
        """
        This is HUD. There are: Software, Colors and Options
        """
        self.software = Software(operator=webScrammer(url))
        self.software.name = software_name
        self.colors = self.HUD_COLOR("GREEN", "YELLOW", "MAGENTA", "RED", "LIGHTBLUE_EX", "CYAN", "LIGHTRED_EX")

        self.option_1 = "Scram from url;" 
        self.option_2 = "Write to file;"
        self.option_3 = "Create file;"
        self.option_4 = "Delete file;"
        self.option_5 = "Clear file;"
        self.option_6 = "Read from file;"
        self.option_7 = "Exit;"

    
class User:
    """This is user's class. It's for settuping HUD, Scrammer and Software name."""
    def __init__(self, URL):
        self.url = URL
        self.HUD = HUD(url=URL, software_name="Scramming Software 1.0")
        self.scrammer = webScrammer(URL)
        self.scrammer.name = self.HUD.software.name

    def manage(self, url):
        """This function is a applicacion console. If user make 3 warnings, app will automaticaly turn off"""

        self.url = url 
        Warnings = 0
        manage = "1"

        while manage != 6:
            if Warnings < 3:
                try:
                    print(f"""
{self.HUD.colors.c_1}1. {self.HUD.option_1}
{self.HUD.colors.c_2}2. {self.HUD.option_2}
{self.HUD.colors.c_3}3. {self.HUD.option_3}
{self.HUD.colors.c_4}4. {self.HUD.option_4}
{self.HUD.colors.c_5}5. {self.HUD.option_5}
{self.HUD.colors.c_6}6. {self.HUD.option_6}
{self.HUD.colors.c_7}7. {self.HUD.option_7}
                    """)
                    manage = int(input(f"{Fore.GREEN}>>> "f"{Fore.WHITE}"))
                    if manage == 1:
                        Format = input("Insert format: ")
                        print(self.scrammer.scramFromUrl(urlFormat=Format))
                    elif manage == 2:
                        Filename = input("Filename: ")
                        self.scrammer.writeToFile(filename=Filename)
                    elif manage == 3:
                        Filename = input("Filename: ")
                        self.scrammer.readFromFile(filename=Filename)  
                    elif manage == 4:
                        Filename = input("Filename: ")
                        try:
                            os.remove(Filename)
                        except:
                            print(f"{Fore.RED}FILE DOESN'T EXIST!")
                    elif manage == 5:
                        Filename = input("Filename: ")
                        print("This functino will clean entire data from file.\nDo you want to continue?")
                        a = input("y/n ")
                        if a == "y":
                            self.scrammer.restart(Filename)
                        else:
                            pass
                    elif manage == 6:
                        Filename = input("Filename: ")
                        TimeSpace = float(input("Timespace: "))
                        Encoding = input("Encoding: ")
                        self.scrammer.readFromFile(filename=Filename,encoding=Encoding,timeSpace=TimeSpace)
                    elif manage == 7:
                        a = input("Do you want to exit? y/n ")
                        if a == "y":
                            print(f"{Fore.LIGHTBLACK_EX}The application will be closed in 3 seconds"+f"{Fore.WHITE}")
                            time.sleep(3)
                            break

                except:
                    print(f"{Fore.RED}INSERT PROPER VALUE" + "!"*Warnings + f"{Fore.WHITE}")
                    Warnings += 1
            else:
                sys.exit()

class Application:
    """That's the application's class. It contains: Console class and Help() function"""
    class Console:
        def __manage__(self):
            url = input("Please, insert url: ")
            self.user1 = User(URL=url)
            self.user1.manage(url=url)

        def __setColor(self, color_1:str, color_2:str, color_3:str, color_4:str, color_5:str, color_6:str, color_7:str):
            self.user1.HUD.colors.c_1 = eval("Fore."+color_1.upper())
            self.user1.HUD.colors.c_2 = eval("Fore."+color_2.upper())
            self.user1.HUD.colors.c_3 = eval("Fore."+color_3.upper())
            self.user1.HUD.colors.c_4 = eval("Fore."+color_4.upper())
            self.user1.HUD.colors.c_5 = eval("Fore."+color_5.upper())
            self.user1.HUD.colors.c_6 = eval("Fore."+color_6.upper())
            self.user1.HUD.colors.c_7 = eval("Fore."+color_7.upper())

    @staticmethod
    def Help(Class):
        print(help(Class))


if __name__ == "__main__":
    try:
        App = Application()
        App.Console().__manage__()
    except:
        print(f"{Fore.RED}Error! Closing application!")
    else:
        print(f"{Fore.LIGHTGREEN_EX}Application opened and closed correctly :D")
    finally:
        print("Application is closed!")
        input("Press enter to exit ")
