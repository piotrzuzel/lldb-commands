#!/usr/bin/python

import lldb
import fblldbbase as fb

def lldbcommands():
	return [ PrintCallStackSymbols() ]

class PrintCallStackSymbols(fb.FBCommand):
	def name(self):
		return 'calls'

	def description(self):
		return 'Prints [NSThread callStackSymbols] return value'

	def run(self, arguments, options):
			lldb.debugger.HandleCommand('po [NSThread callStackSymbols]')