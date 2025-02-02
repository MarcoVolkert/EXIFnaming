from collections import OrderedDict

from EXIFnaming.helpers import settings

__all__ = ["CameraModelShort", "RecModes", "hdr_algorithm", "tm_preset"]

CameraModelShort = OrderedDict()
CameraModelShort['DMC-TZ7'] = 'TZ7'
CameraModelShort['DMC-TZ101'] = 'TZ101'
CameraModelShort['E4800'] = 'N'
CameraModelShort['SM-G900F'] = 'S5'
CameraModelShort['SM-G991B'] = 'S21'
CameraModelShort['DCR-TRV25E'] = 'VS'
CameraModelShort['HDC-SD300'] = 'V'
CameraModelShort['M2002J9G'] = 'MI10'
CameraModelShort['SM-A536B'] = 'A53'
CameraModelShort['SM-G973F'] = 'S10'
CameraModelShort['SM-G990B2'] = 'S21FE'
CameraModelShort['Canon EOS 450D'] = '450D'
CameraModelShort['Canon EOS 5D Mark II'] = '5DMarkII'
CameraModelShort['Canon EOS 600D'] = '600D'
CameraModelShort['COOLPIX P7800'] = 'P7800'
CameraModelShort['ILCE-6300'] = '6300'

RecModes = ["4KB", "4K", "HS", "FHD"]

hdr_algorithm = OrderedDict()
hdr_algorithm["A"] = "Average"
hdr_algorithm["E"] = "Entropy"
hdr_algorithm["Ld"] = "Luminance distance"
hdr_algorithm["C"] = "Colourmix"
hdr_algorithm["Le"] = "Luminance entropy"
hdr_algorithm["LRGB"] = "Luminance RGB"
hdr_algorithm["Lil"] = "Linear luminance"
hdr_algorithm["Ll"] = "Logarithmic luminance"
hdr_algorithm["Ql"] = "Quadratic luminance"
hdr_algorithm["Cr"] = "Chroma"
hdr_algorithm["Ad"] = "Absolute distance"
hdr_algorithm["Ls"] = "Luminance sharpness"
hdr_algorithm["Cs"] = "Colour sharpness"
hdr_algorithm["Rn"] = "Repro neutral"
hdr_algorithm["Ri"] = "Repro intense"

tm_preset = OrderedDict()
tm_preset["Nb"] = "Natural balanced"
tm_preset["Ns"] = "Natural sharp"
tm_preset["Nbl"] = "Natural back light"
tm_preset["NBbl"] = "Natural Bright back light"
tm_preset["NDbl"] = "Natural Dark back light"
tm_preset["Nhd"] = "Natural highlight details"
tm_preset["Ndb"] = "Natural details brightened"
tm_preset["Npc"] = "Natural powerful colours"
tm_preset["Nds"] = "Natural deep shadows"
tm_preset["Nso"] = "Natural soft"
tm_preset["Lb"] = "Landscape backlit"
tm_preset["Ls"] = "Landscape sunset"
tm_preset["Lpc"] = "Landscape powerful colours"
tm_preset["Lcad"] = "Landscape colour and detail"
tm_preset["LB"] = "Landscape Brilliant"
tm_preset["Afd"] = "Architecture fine detail"
tm_preset["Abi"] = "Architecture brighten interior"
tm_preset["Ss"] = "Surreal standard"
tm_preset["Spc"] = "Surreal powerful colours"
tm_preset["SE"] = "Surreal Extreme"
tm_preset["SRL"] = "Surreal Extreme"
tm_preset["CNF"] = "Custom Nacht Farbe"
