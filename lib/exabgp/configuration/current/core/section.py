# encoding: utf-8
"""
generic/__init__.py

Created by Thomas Mangin on 2015-06-04.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""


class Section (object):
	name = 'undefined'
	known = dict()     # command/section and code to handle it
	default = dict()   # command/section has a a defult value, use it if no data was provided
	action = {}        # how to handle this command ( append, add, assign, route )
	assign = {}        # configuration to class variable lookup for setattr

	def __init__ (self, tokerniser, scope, error, logger):
		self.tokeniser = tokerniser
		self.scope = scope
		self.error = error
		self.logger = logger

	def clear (self):
		raise RuntimeError('not implemented in subclass as should be')

	@classmethod
	def register (cls, name):
		def inner (function):
			if name in cls.known:
				raise RuntimeError('more than one registration per command attempted')
			cls.known[name] = function
			return function
		return inner

	def pre (self):
		return True

	def post (self):
		return True

	def parse (self, name, command):
		if command not in self.known:
			return self.error.set('unknown command')

		try:
			if command in self.default:
				insert = self.known[command](self.tokeniser.iterate,self.default[command])
			else:
				insert = self.known[command](self.tokeniser.iterate)

			action = self.action[command]

			if action == 'set':
				self.scope.set(command,insert)
			elif action == 'extend':
				self.scope.extend(name,insert)
			elif action == 'append':
				self.scope.append(name,insert)
			elif action == 'attribute-add':
				self.scope.attribute_add(name,insert)
			elif action == 'nlri-set':
				self.scope.nlri_assign(name,self.assign[command],insert)
			elif action == 'nlri-add':
				self.scope.nlri_add(name,insert)
			else:
				raise RuntimeError('name %s command %s has no action set' % (name,command))
			return True
		except ValueError, exc:
			return self.error.set(str(exc))