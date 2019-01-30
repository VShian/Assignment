# from pip._internal import main as pipmain
import pip
import json
from pprint import pprint

def install(package, version):
	print('installing ',package)
	try:
		import package
	except ImportError:
		check = pip.main(['install', package+"=="+version])
		if check==1:
			print("Failed")
			return False
		print("Success")
		return True


with open('dependencies.json') as f:
	data = json.load(f)

failed=[]
for ele in data['Dependencies']:
    if not install(ele, data['Dependencies'][ele]):
    	failed+=[ele]

if len(failed)>0:
	print(len(failed)+"/"+len(data['Dependencies'])+" installed successfully")
	print("Failed installing:")
	for ele in failed:
		print("/t"+ele)
else:
	print("Installed succesfully")