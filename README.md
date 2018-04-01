Feeds can be added by opening the pyfeeder.py file, and adding the url and title to the dictionary like this 

feeds = {
	'Feed title':'http://www.someurl.com',
}

Make sure you put a comma after the url

the deafault broswer is w3m, but you can change that by editing it in the read function. 
I'll probably add a better way to configure this in the future. 
