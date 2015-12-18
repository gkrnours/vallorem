import sys
from functools import wraps
from io import StringIO

from flask import request, render_template

def templated(template=None):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			template_name = template
			if template_name is None:
				template_name = request.endpoint.replace('.', '/') + '.html'
			ctx = f(*args, **kwargs)
			if ctx is None:
				ctx = {}
			elif not isinstance(ctx, dict):
				return ctx
			return render_template(template_name, **ctx)
		return decorated_function
	return decorator

class Capturing(list):
	def __enter__(self):
		self._stdout = sys.stdout
		sys.stdout = self._stringio = StringIO()
		"""XXX hack for pelican 3.6"""
		self._stringio.fileno = lambda: 0
		return self
	def __exit__(self, *args):
		self.extend(self._stringio.getvalue().splitlines())
		sys.stdout = self._stdout
