
# News Article Extractor
# Under work
# To Do
# add headers
# add user agent
# crack wsj article encryption
# add url textbox, with error checking
# add article search, with error checking
# add saving to a file (easiest part - done)
# add file opening in new tab (done)
# add more news websites
# separate everything into new files (can be done easily)
# make a GUI

# import beautifulsoup to parse HTML and requests to visit website + os for commands
import subprocess
import urllib
from pageparser import parser

# css classes of main body paragraphs in nyt, usa today, wsj and foreign policy
classes = {"nytimes" : "css-1fanzo5",
"usatoday" : "gnt_ar_b_p",       
"wsj" : "wsj-snippet-body",
"foreignpolicy" : "post-content-main initial-drop-cap shares-position",
"kognity" : "content-editable",
"economist" : "article__body-text",
"fortune" : "gutenbergContent__content--1FgGp"}

def runoperations():
    parser()
    # save results to html file and auto-close
    with open("news.html","w") as f:
        f.write(f"""<!DOCTYPE HTML PUBLIC " -//W3C//DTD HTML 4.01 Transition//EN" 
    "http://www.w3.org/TR/htm14/loose.dtd">
    <html>
      <head>
        <title>{link}</title>
        <link rel="stylesheet" href="webpage.css" type="text/css"/>
      </head>
      <body>
        <h3> The link of this webpage is {link} </h3>
        {content}
      </body>
    </html>""")
    # open said html file in chrome
    subprocess.run(["open", "-a", "/Applications/Google Chrome.app", "news.html"])

#parse url of link automatically, and use class based on that, or save url later to add to database
print("Enter link here")
print(" ")
link = input()
domain = urllib.parse.urlparse(link).netloc.replace("www.","").replace(".com","")
print(domain)
if domain in classes:
    runoperations()
else:
    print(f"adding {domain} to sites list")
    with open("sitestoadd.txt","a") as f:
        f.write(domain)


# In[ ]:




