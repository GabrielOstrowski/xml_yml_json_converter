# Task 1 - parsowanie argumentow
import sys,json,xml,yaml
# import xml.etree.ElementTree as ET
import xmltodict
from dicttoxml import dicttoxml
from yaml.loader import SafeLoader
debugmode = 0
srcread = ""
srcfile = ""
dstread = ""
dstfile = ""
filewritten = False

# customowy wyjatek sprawdzajacy poprawnosc formatu plikow
class InvalidFormatException(Exception):
    pass


# sprawdzenie rozszerzenia pliku
def file_ext_check(file):
    if file.endswith('.xml'):
        return "xml"
    elif file.endswith('.yml' or '.yaml'):
        return "yml"
    elif file.endswith('.json'):
        return "json"
    else:
        return "none"


# tryb debugowania
try:
    if str(sys.argv[3]) == "debug":
       debugmode = 1
except IndexError:
    pass

# wstepna weryfikacja
try:
    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])
    if debugmode == 1:
        print(f"Format pierwszego pliku:",file_ext_check(file1),"\nFormat drugiego pliku:",file_ext_check(file2))

    if file_ext_check(file1) == "none" or file_ext_check(file2) == "none": # jesli format plikow nie bedzie podany
        raise InvalidFormatException

except IndexError: # jesli bedzie podanych mniej argumentow
    print(f"""Nieprawidlowe uzycie.
Zastosowanie: fileconverter.py <plik1> <plik2>""")
    sys.exit(1)

except InvalidFormatException: # stworzylem customowy wyjatek i go obsluzylem
    print("Nieprawidlowy format jednego lub obu plikow")
    sys.exit(2)

else:
    print("Pliki zaimportowane prawidlowo")