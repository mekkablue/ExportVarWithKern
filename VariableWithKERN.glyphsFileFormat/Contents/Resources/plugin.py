# encoding: utf-8

###########################################################################################################
#
#
#	File Format Plugin
#	Implementation for exporting fonts through the Export dialog
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/File%20Format
#
#	For help on the use of Xcode:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from copy import copy


# Preference key names
# Part of the example. You may delete them
axisName = 'com.mekkablue.VariableWithKERN.axisName'
axisTag = 'com.mekkablue.VariableWithKERN.axisTag'



class VariableWithKERN(FileFormatPlugin):
	
	# Definitions of IBOutlets
	
	# The NSView object from the User Interface. Keep this here!
	dialog = objc.IBOutlet()
	
	# Example variables. You may delete them
	axisTagTextField = objc.IBOutlet()
	axisNameTextField = objc.IBOutlet()

	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'VAR with KERN',
			'de': 'VAR mit KERN',
		})
		self.icon = 'ExportIcon'
		self.toolbarPosition = 100
		
		# Load .nib dialog (with .extension)
		self.loadNib('IBdialog', __file__)

	@objc.python_method
	def start(self):
		
		# Init user preferences if not existent and set default value
		Glyphs.registerDefault(axisName, "Kerning")
		Glyphs.registerDefault(axisTag, "KERN")
		
		# Set initial state of checkboxes according to user variables
		self.axisTagTextField.setStringValue_(Glyphs.defaults[axisTag])
		self.axisNameTextField.setStringValue_(Glyphs.defaults[axisName])

	# Example function. You may delete it
	@objc.IBAction
	def setAxisTag_(self, sender):
		Glyphs.defaults[axisTag] = sender.stringValue()
		# self.updateFeedBackTextField()
	
	# Example function. You may delete it
	@objc.IBAction
	def setAxisName_(self, sender):
		Glyphs.defaults[axisName] = sender.stringValue()
		# self.updateFeedBackTextField()
	
	@objc.python_method
	def export(self, font):
		# Ask for export destination and write the file:
		folder = GetFolder(
			message="Choose export destination",
			allowsMultipleSelection=False,
			path=None,
			)
		
		if folder:
			print(folder)
			
			exportFont = font.copy()
			newAxis = GSAxis()
			newAxis.name = Glyphs.defaults[axisName].strip()
			newAxis.axisTag = (Glyphs.defaults[axisTag].strip().replace(" ","") + "    ")[:4].upper()
			exportFont.axes.append(newAxis)
			axisID = newAxis.id

			for master in exportFont.masters:
				master.setAxisValueValue_forId_(100, axisID)

			for masterIndex in range(len(exportFont.masters)):
				unkernedMaster = exportFont.addFontAsNewMaster_(exportFont.masters[masterIndex])
				unkernedMaster.setAxisValueValue_forId_(0, axisID)
				unkernedMaster.name += " Unkerned"
				exportFont.kerning[unkernedMaster.id] = {}
			
			success = False
			for instance in exportFont.instances:
				print(instance)
				if instance.type != INSTANCETYPEVARIABLE:
					continue
				path = folder.stringByAppendingPathComponent_(instance.fileName()).stringByDeletingPathExtension().stringByAppendingPathExtension_("ttf")
				success = instance.generate(FontPath=path)
				
				print("SUCCESS", success)
			
			if success == True:
				return (success, "Exported successfully")
			else:
				return (False, str(success))
		else:
			return (False, 'No file chosen')

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
