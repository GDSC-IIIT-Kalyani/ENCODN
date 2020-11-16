import hashlib
import re
from urllib.request import Request, urlopen

def encrypt(string):
	try:
		if string==b"":
			return "The string is empty!!!"
		else:
			hashed = hashlib.sha1(string).hexdigest()
			return hashed
	except ValueError:
		return "The entered value is not a string!!!"

def decrypt(hashed):
	try:
		res = not bool(re.search(r"\s", hashed))
		if res:
			web = 'http://hashtoolkit.com/decrypt-hash/?hash=' + hashed
			req = Request(web, headers={'User-Agent': 'XYZ/3.0'})
			response = urlopen(req).read().decode('utf-8')
			match = re.search(r'(<span title="decrypted .+ hash">)(.+)(</span>)', response)
			sample=match.group(2)
			start=sample.find('">') + len('">')
			end=sample.find('</')
			substring = sample[start:end]
			return substring
		else:
			raise ValueError
			
	except ValueError:
		return "The entered value is incorrect!!!"