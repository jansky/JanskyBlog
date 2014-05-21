"""
The MIT License (MIT)

Copyright (c) 2014 Janský Důnska

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import os
from string import Template


def PrintHeaders(httpcode):

	print "HTTP/1.0 " + httpcode
	print "Content-type: text/html; charset=utf-8"
	print

# Uncomment below to enable the simple WriteDocument function
#def WriteDocument(content,title=""):

#	print "<!DOCTYPE html>"
#	print "<html>"
#	print "<head>"
#	if title == "":
#		print "<title>Blog</title>"
#	else:
#		print "<title>" + title + " | Blog</title>"
#	print "<meta charset='utf-8'/>"
#	print "<meta name='author' content='PyBloggingSystem v0.1'/>"
#	print "<body>"
#	print content
#	print "</body>"
#	print "</html>"

def DoDocumentTemplating(data, templateFile):

	templateFileString = ""

	with open(templateFile, 'r') as template_file:
		templateFileString = template_file.read()

	print Template(templateFileString).safe_substitute(data)


