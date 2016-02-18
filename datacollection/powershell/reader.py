import xml.etree.ElementTree as ET

#filepath = 'scripts/GetCertificateInfo.zep'
filepath = 'scripts/WatchAndKillProcesses.zep'
# Module
#   name
#   description
#   platforms
#       platform
# parameters
    # parameter
# extension

def parse_parameter(filepath):

    tree = ET.parse(filepath)
    root = tree.getroot()

    name = root.find("name").text
    description = root.find("description").text
    extension = root.find("extension").text

    parameter_types = [p.text for p in root.findall("parameters/parameter/type")]
    parameter_values = [p.text for p in root.findall("parameters/parameter/value")]
    parameter_names = [p.text for p in root.findall("parameters/parameter/name")]

    return (parameter_types, parameter_values, parameter_names)