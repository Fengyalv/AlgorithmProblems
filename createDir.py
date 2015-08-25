import datetime
import os , sys
import shutil
import string

newPath = raw_input("Please input the model name:")
filePath = "./testFile/"
fileName = newPath.capitalize()

nameModel = fileName + "Model"
nameCtrl = fileName + "Ctrl"
nameView = fileName + "View"

fileAuthor = "LvNanchun"
createData = datetime.datetime.now().strftime("%Y-%m-%d")

fp = open(filePath + nameModel + ".lua" , 'w')
fp.write(
        "-- FileName: %s.lua\n" %nameModel +
        "-- Author: %s\n" %fileAuthor +
        "-- Date: %s\n" %createData +
        "-- Purpose: function description of module\n"
        "--[[TODO List]]\n\n"
        "module(\"%s\", package.seeall)\n\n" %nameModel +
        "-- UI variable --\n\n"
        "-- module local variable --\n\n"
        "local function init(...)\n\n"
        "end\n\n"
        "function destroy(...)\n"
        "    package.loaded[\"%s\"] = nil\n" %nameModel +
        "end\n\n"
        "function moduleName()\n"
        "    return \"%s\"\n" %nameModel +
        "end\n\n"
        "function create(...)\n\n"
        "end\n\n"
	)
fp.close()

fp = open(filePath + nameView + ".lua" , 'w')
fp.write(
        "-- FileName: %s.lua\n" %nameView +
        "-- Author: %s\n" %fileAuthor +
        "-- Date: %s\n" %createData +
        "-- Purpose: function description of module\n"
        "--[[TODO List]]\n\n"
        "module(\"%s\", package.seeall)\n\n" %nameView +
        "-- UI variable --\n\n"
        "-- module local variable --\n\n"
        "local function init(...)\n\n"
        "end\n\n"
        "function destroy(...)\n"
        "    package.loaded[\"%s\"] = nil\n" %nameView +
        "end\n\n"
        "function moduleName()\n"
        "    return \"%s\"\n" %nameView +
        "end\n\n"
        "function create(...)\n\n"
        "end\n\n"
	)
fp.close()

fp = open(filePath + nameCtrl + ".lua" , 'w')
fp.write(
        "-- FileName: %s.lua\n" %nameCtrl +
        "-- Author: %s\n" %fileAuthor +
        "-- Date: %s\n" %createData +
        "-- Purpose: function description of module\n"
        "--[[TODO List]]\n\n"
        "%s = class(\"%s\")\n\n" %(nameCtrl,nameCtrl) +
        "-- UI variable --\n\n"
        "-- module local variable --\n\n"
        "function %s:moduleName()\n" %nameCtrl +
        "    return \"%s\"\n" %nameCtrl +
        "end\n\n"
        "function %s:ctor(...)\n\n" %nameCtrl +
        "end\n\n"
        "function %s:create(...)\n\n" %nameCtrl +
        "end\n\n"
	)
fp.close()


print filePath
print newPath
print nameModel , nameCtrl , nameView
