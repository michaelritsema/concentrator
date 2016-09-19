import os
import xml.etree.ElementTree as ET
import base64



class ZextContainer:
	"""
		Container for data in a .zep file
	"""

	def __init__(self,zep, name,extension_text,params):
		self.name = name
		self.zep = zep
		self.extension_text = extension_text
		self.extension_b64 = base64.encodestring(extension_text)
		self.params = params

	@staticmethod
	def parse_params(root):
		"""
			Parse the parameters of the zep
			returns 
			[
				{'displayname': '<value>'},
				{'name': '<value>'},
				{'type': '<value>'}
			]
		"""
		params = []
		for p in root.find('parameters'):
			displayname = p.find('displayName').text
			name = p.find('name').text
			p_type = p.find('type').text
			params.append({
					'displayname': displayname,
					'type': p_type,
					'name': name
				})

		return params

	@staticmethod
	def BuildZext(zep):
		"""
			Constructs an Zext object from the string contents of a .zep file
		"""

		root = ET.fromstring(zep)
		#root = tree.getroot()

		n = root.find('name').text
		e = root.find('extension').text.strip()
		params = ZextContainer.parse_params(root)

		z = ZextContainer(zep=zep,name=n,extension_text=e,params=params)
		return z



if __name__ == "__main__":
	files = os.listdir('powershell/scripts')
	z = None
	for name in files:
		filepath = 'powershell/scripts/' + name
		o = open('powershell/scripts/' + name)
		zep = o.read()
		zext = ZextContainer.BuildZext(zep)
		print zext.name


