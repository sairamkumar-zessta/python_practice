sec = int(input("Seconds:"))
out = ""
if sec >=(24*60*60):
    out += "{} Days ".format(sec // (24*60*60)) 
    sec = sec % (24*60*60)
if sec >=(60*60):
    out += "{} Hours ".format(sec // (60*60)) 
    sec = sec % (60*60)
if sec >=(60):
    out += "{} Minutes ".format(sec // (60)) 
    sec = sec % (60)
if sec >0:
    out +="{} Seconds ".format(sec) 
print(out)

