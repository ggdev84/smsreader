from os import system
import sys, base64
from datetime import datetime

code = """
PCFET0NUWVBFIGh0bWw+CjxodG1sPgogICAgPGhlYWQ+CiAgICAgICAgPHRpdGxlPk1ldGVycHJldGVyIFNNUyBkdW1wPC90aXRsZT4KICAgICAgICA8bWV0YSBjaGFyc2V0PSJ1dGYtOCIvPgogICAgICAgIDxzdHlsZT4KCiAgICAgICAgICAgIGJvZHl7CiAgICAgICAgICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2IoMjQ4LCAyNDgsIDI0OCk7CiAgICAgICAgICAgICAgICBwYWRkaW5nOjA7CiAgICAgICAgICAgICAgICBtYXJnaW46MDsKICAgICAgICAgICAgICAgIGZvbnQtZmFtaWx5OiBBcmlhbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICB9CgogICAgICAgICAgICAuY29udGFpbmVyewogICAgICAgICAgICAgICAgd2lkdGg6NjAlOwogICAgICAgICAgICAgICAgbWFyZ2luOjF2aCBhdXRvOwogICAgICAgICAgICAgICAgaGVpZ2h0Ojk3dmg7CiAgICAgICAgICAgICAgICBkaXNwbGF5OiBmbGV4OwogICAgICAgICAgICAgICAgZmxleC1kaXJlY3Rpb246IHJvdzsKICAgICAgICAgICAgICAgIGJvcmRlcjoxcHggc29saWQgcmdiKDQ5LCA0OSwgNDkpOwogICAgICAgICAgICB9CgogICAgICAgICAgICAjYWRkcmVzc2xpc3R7CiAgICAgICAgICAgICAgICB3aWR0aDoyNSU7CiAgICAgICAgICAgICAgICBoZWlnaHQ6MTAwJTsKICAgICAgICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6IHRyYW5zcGFyZW50OwogICAgICAgICAgICAgICAgb3ZlcmZsb3cteTogYXV0bzsKICAgICAgICAgICAgICAgIGRpc3BsYXk6ZmxleDsKICAgICAgICAgICAgICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47CiAgICAgICAgICAgICAgICBib3JkZXItcmlnaHQ6IDFweCBzb2xpZCBncmF5OwogICAgICAgICAgICB9CgogICAgICAgICAgICAjbWVzc2FnZXNkaXZ7CiAgICAgICAgICAgICAgICB3aWR0aDo3NSU7CiAgICAgICAgICAgICAgICBoZWlnaHQ6MTAwJTsKICAgICAgICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6IHRyYW5zcGFyZW50OwogICAgICAgICAgICAgICAgb3ZlcmZsb3cteTogYXV0bzsKICAgICAgICAgICAgfQoKICAgICAgICAgICAgI21lc3NhZ2VzZGl2IGgzewogICAgICAgICAgICAgICAgdGV4dC1hbGlnbjogY2VudGVyOwogICAgICAgICAgICAgICAgZm9udC1zaXplOiAyMnB4OwogICAgICAgICAgICAgICAgbWFyZ2luLXRvcDogMTAwcHg7CiAgICAgICAgICAgIH0KCiAgICAgICAgICAgICNtZXNzYWdlc2RpdiBoMXsKICAgICAgICAgICAgICAgIHdpZHRoOjEwMCU7CiAgICAgICAgICAgICAgICBmb250LXdlaWdodDogbGlnaHRlcjsKICAgICAgICAgICAgICAgIGZvbnQtc2l6ZTogMjZweDsgCiAgICAgICAgICAgICAgICB0ZXh0LWFsaWduOiBjZW50ZXI7CiAgICAgICAgICAgICAgICBoZWlnaHQ6NjBweDsKICAgICAgICAgICAgICAgIGxpbmUtaGVpZ2h0OiA2MHB4OwogICAgICAgICAgICAgICAgbWFyZ2luOjA7CiAgICAgICAgICAgICAgICBib3JkZXItYm90dG9tOiAxcHggc29saWQgcmdiKDE4NSwgMTg1LCAxODUpOwoKICAgICAgICAgICAgfQoKICAgICAgICAgICAgI2FkZHJlc3NsaXN0IGJ1dHRvbnsKICAgICAgICAgICAgICAgIG1hcmdpbjowOwogICAgICAgICAgICAgICAgYm9yZGVyLXJhZGl1czogMDsKICAgICAgICAgICAgICAgIGJvcmRlcjowOwogICAgICAgICAgICAgICAgYm9yZGVyLWJvdHRvbTogMXB4IHNvbGlkIHJnYigxODUsIDE4NSwgMTg1KTsKICAgICAgICAgICAgICAgIGN1cnNvcjogcG9pbnRlcjsKICAgICAgICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6IHJnYigyNDUsIDI0NSwgMjQ1KTsKICAgICAgICAgICAgICAgIHRyYW5zaXRpb246YmFja2dyb3VuZC1jb2xvciAwLjJzIGVhc2Utb3V0OwogICAgICAgICAgICAgICAgZGlzcGxheTogZmxleDsKICAgICAgICAgICAgICAgIGZsZXgtZGlyZWN0aW9uOiByb3c7CiAgICAgICAgICAgICAgICBoZWlnaHQ6ODBweDsKICAgICAgICAgICAgICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgICAgICAgICAgIH0KCiAgICAgICAgICAgICNhZGRyZXNzbGlzdCBidXR0b246aG92ZXJ7CiAgICAgICAgICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2IoMjI1LCAyMjUsIDIyNSk7CiAgICAgICAgICAgIH0KCiAgICAgICAgICAgICNhZGRyZXNzbGlzdCBidXR0b24gcDpmaXJzdC1vZi10eXBlewogICAgICAgICAgICAgICAgaGVpZ2h0OjYwcHg7CiAgICAgICAgICAgICAgICB3aWR0aDo2MHB4OwogICAgICAgICAgICAgICAgbGluZS1oZWlnaHQ6IDYwcHg7CiAgICAgICAgICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjMTM1NmJiOwogICAgICAgICAgICAgICAgYm9yZGVyLXJhZGl1czogMjAwcHg7CiAgICAgICAgICAgICAgICBmb250LXNpemU6IDIycHg7CiAgICAgICAgICAgICAgICBtYXJnaW4tbGVmdDogMTBweDsKICAgICAgICAgICAgICAgIGNvbG9yOndoaXRlOwogICAgICAgICAgICB9CgogICAgICAgICAgICAjYWRkcmVzc2xpc3QgYnV0dG9uIHA6bGFzdC1vZi10eXBlewogICAgICAgICAgICAgICAgY29sb3I6YmxhY2s7CiAgICAgICAgICAgICAgICBmb250LXNpemU6IDE4cHg7CiAgICAgICAgICAgICAgICBtYXJnaW4tbGVmdDogMTBweDsKICAgICAgICAgICAgfQoKICAgICAgICAgICAgI2FkZHJlc3NsaXN0IGgxewogICAgICAgICAgICAgICAgd2lkdGg6MTAwJTsKICAgICAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBsaWdodGVyOwogICAgICAgICAgICAgICAgZm9udC1zaXplOiAyNnB4OyAKICAgICAgICAgICAgICAgIHRleHQtYWxpZ246IGNlbnRlcjsKICAgICAgICAgICAgICAgIGhlaWdodDo2MHB4OwogICAgICAgICAgICAgICAgbGluZS1oZWlnaHQ6IDYwcHg7CiAgICAgICAgICAgICAgICBtYXJnaW46MDsKICAgICAgICAgICAgICAgIGJvcmRlci1ib3R0b206IDFweCBzb2xpZCByZ2IoMTg1LCAxODUsIDE4NSk7CgogICAgICAgICAgICB9CgogICAgICAgICAgICAubWVzc2FnZWluLCAubWVzc2FnZW91dHsKICAgICAgICAgICAgICAgIGJvcmRlci1yYWRpdXM6IDEwcHg7CiAgICAgICAgICAgICAgICBjb2xvcjp3aGl0ZTsKICAgICAgICAgICAgICAgIGZvbnQtc2l6ZTogMThweDsKICAgICAgICAgICAgICAgIHdpZHRoOjYwJTsKICAgICAgICAgICAgfQoKICAgICAgICAgICAgLm1lc3NhZ2VpbnsKICAgICAgICAgICAgICAgIGZsb2F0OmxlZnQ7CiAgICAgICAgICAgICAgICBtYXJnaW46MTVweCAwIDE1cHggMzBweDsKICAgICAgICAgICAgICAgIHBhZGRpbmc6NXB4IDEwcHg7CiAgICAgICAgICAgICAgICBjb2xvcjpibGFjazsKICAgICAgICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6IHJnYigyMzYsIDIzNiwgMjM2KTsKICAgICAgICAgICAgICAgIGJvcmRlcjoxcHggc29saWQgcmdiKDE1NiwgMTU2LCAxNTYpOwogICAgICAgICAgICB9CgogICAgICAgICAgICAubWVzc2FnZW91dHsKICAgICAgICAgICAgICAgIGZsb2F0OnJpZ2h0OwogICAgICAgICAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogIzEzNTZiYjsKICAgICAgICAgICAgICAgIG1hcmdpbjoxNXB4IDMwcHggMTVweCAwOwogICAgICAgICAgICAgICAgcGFkZGluZzo1cHggMTBweDsKICAgICAgICAgICAgICAgIGNvbG9yOndoaXRlOwogICAgICAgICAgICB9CgogICAgICAgICAgICBoNnsKICAgICAgICAgICAgICAgIGZsb2F0OnJpZ2h0OwogICAgICAgICAgICAgICAgbWFyZ2luOjVweCAwOwogICAgICAgICAgICAgICAgZm9udC13ZWlnaHQ6IGxpZ2h0ZXI7CiAgICAgICAgICAgIH0KCiAgICAgICAgICAgIAoKICAgICAgICA8L3N0eWxlPgoKICAgICAgICA8c2NyaXB0PgogICAgICAgICAgICB3aW5kb3cub25sb2FkPSgpPT57CiAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICMjREFUQSMjCgogICAgICAgICAgICAgICAgbGV0IGNoYW5nZW1lc3NhZ2VzID0gKGtleT0iIiwgbGlzdD1bXSk9PnsKICAgICAgICAgICAgICAgICAgICBsZXQgbWVzc2FnZXMgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgibWVzc2FnZXNkaXYiKQogICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VzLmlubmVySFRNTD1gPGgxPiR7a2V5fTwvaDE+YAogICAgICAgICAgICAgICAgICAgIGxpc3QuZm9yRWFjaChpPT57CiAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VzLmlubmVySFRNTCArPSBgCiAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9IiR7aS50eXBlPT09Im91dGdvaW5nIiA/ICJtZXNzYWdlb3V0IiA6ICJtZXNzYWdlaW4ifSI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8cD4ke2kubWVzc2FnZX08L3A+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aDY+JHtpLmRhdGV9PC9oNj4KICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgIGAKICAgICAgICAgICAgICAgICAgICB9KQogICAgICAgICAgICAgICAgfQoKICAgICAgICAgICAgICAgIGxldCBjb250YWN0cyA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJhZGRyZXNzbGlzdCIpCgogICAgICAgICAgICAgICAgZm9yIChjb25zdCBba2V5LHZhbHVlXSBvZiBPYmplY3QuZW50cmllcyhkYXRhKSl7CiAgICAgICAgICAgICAgICAgICAgbGV0IGJ0biA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoImJ1dHRvbiIpCiAgICAgICAgICAgICAgICAgICAgYnRuLmlubmVySFRNTCA9IGAKICAgICAgICAgICAgICAgICAgICAgICAgPHAgY2xhc3M9ImFkaWNvbiI+JHtrZXkuc3BsaXQoIiIpWzBdfTwvcD4KICAgICAgICAgICAgICAgICAgICAgICAgPHA+JHtrZXl9PC9wPgogICAgICAgICAgICAgICAgICAgIGAKICAgICAgICAgICAgICAgICAgICBidG4uYWRkRXZlbnRMaXN0ZW5lcigiY2xpY2siLCAoKT0+ewogICAgICAgICAgICAgICAgICAgICAgICBjaGFuZ2VtZXNzYWdlcyhrZXksdmFsdWUpCiAgICAgICAgICAgICAgICAgICAgfSkKCiAgICAgICAgICAgICAgICAgICAgY29udGFjdHMuYXBwZW5kQ2hpbGQoYnRuKQogICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CgogICAgICAgIDwvc2NyaXB0PgoKICAgIDwvaGVhZD4KICAgIDxib2R5PgoKICAgICAgICA8ZGl2IGNsYXNzPSJjb250YWluZXIiPgogICAgICAgICAgICA8ZGl2IGlkPSJhZGRyZXNzbGlzdCI+CiAgICAgICAgICAgICAgICA8aDE+Q29udGFjdHM8L2gxPgoKCiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICA8ZGl2IGlkPSJtZXNzYWdlc2RpdiI+CiAgICAgICAgICAgICAgICA8aDM+Q2xpY2sgb24gYSBjb250YWN0IHRvIHNlZSBtZXNzYWdlcy48L2gzPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KCiAgICA8L2JvZHk+CjwvaHRtbD4=
"""

def printname():
    print("""
 _____ __  __  _____ _____                _           
/ ____|  \/  |/ ____|  __ \              | |          
| (___| \  / | (___ | |__) |___  __ _  __| | ___ _ __ 
\___ \| |\/| |\___ \|  _  // _ \/ _` |/ _` |/ _ \ '__|
____) | |  | |____) | | \ \  __/ (_| | (_| |  __/ |   
|____/|_|  |_|_____/|_|  \_\___|\__,_|\__,_|\___|_|   
                                                        
""")

printname()
print("\n[+] Generating html file...\n")

mylist = {}

sfile = open(sys.argv[1], "r")
text = sfile.read().split("#")
text.remove(text[0])
for i in range(len(text)):
    newi = text[i].split("\n")
    newi.remove(newi[0])

    if not newi[2].split(":")[1].strip() in mylist.keys():
        contact = newi[2].split(":")[1].strip()
        mylist[contact] =[]


        #Ca fout la merde au niveau des dates, car le temps est séparé par : aussi.
        texttowrite = {
            "date":newi[1].split(": ")[1].strip(),
            "message":newi[4].split(":")[1].strip(),
            "type":newi[0].split(":")[1].strip().lower()
        }
        
        mylist[contact].append(texttowrite)  


    else:
        contact = newi[2].split(":")[1].strip()

        texttowrite = {
            "date":newi[1].split(": ")[1].strip(),
            "message":newi[4].split(":")[1].strip(),
            "type":newi[0].split(":")[1].strip().lower()
        }

        date=newi[1].split(": ")[1]
        tmp = date.split(" ")
        times = tmp[1].split(":")
        tmp = tmp[0].split("-")

        tmp = datetime(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(times[0]), int(times[1]), int(times[2]))  

        for i in range(len(mylist[contact])):
            idate=mylist[contact][i]["date"]
            itmp = idate.split(" ")
            itimes = itmp[1].split(":")
            itmp = itmp[0].split("-")
            itmp = datetime(int(itmp[0]), int(itmp[1]), int(itmp[2]), int(itimes[0]), int(itimes[1]), int(itimes[2]))  

            if tmp <= itmp:
                mylist[contact].insert(i, texttowrite)
                break
            elif not tmp<itmp and i == len(mylist[contact])-1:
                mylist[contact].append(texttowrite)
                break

            


ftow = open("result.html","w")
code = base64.b64decode(code).decode("utf-8")

towrite = "let data = {\n"
for key, value in mylist.items():
    towrite+= "{} : {},\n".format(key, value)
towrite += "\n}"

code = code.replace("##DATA##", towrite)
ftow.write(code)
ftow.close()

sfile.close()

print("\n[+] Generated html file : result.html\n")
system("firefox "+ __file__.replace(sys.argv[0], "result.html"))
