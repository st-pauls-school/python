
So the files are here, you'll need to download them locally. 

So you'll need to copy all the files (well, strictly not the xml as that will get created/overwritten) from 
  https://drive.google.com/drive/folders/1v6Wvppkr6bf26oOmvIKrxlTZW7JL-moq?usp=sharing 
all into the same folder: the credentials.json are temporary, the token is longer lasting, but they are both necessary and should be in the same folder as the script. 

You will need to have the requisite Google python libraries installed: 

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib 


Then just run house-summary.py and it should create/update house-scoreboard.xml and the term summary (from rows 7 and 8, make sure that they have this term)
