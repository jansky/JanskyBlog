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
import ConfigParser
import cgitb
import misc
from os import listdir, path
from os.path import isfile, join
import operator
import cgitb
import cgi




def GetAllBlogPosts(postDir):
	posts = [ f for f in listdir(postDir) if isfile(join(postDir,f)) ]
	postsParsed = []
	

	for post in posts:
		postData = {}
		postId = 0
		onText = False
		blogPostText = ""

		with open(join(postDir,post), 'r') as template_file:
			blogPost = template_file.read()

		blogPostLines = blogPost.splitlines()

		for line in blogPostLines:
			if onText == False:
				if line == "---":
					onText = True
				else:
					dataAndKey = line.split('=')
					postData[dataAndKey[0]] = dataAndKey[1]
					
			else:
				blogPostText += line + os.linesep

		postsParsed.append({'Data':postData, 'ID':postData["id"],'content':blogPostText})

	postsParsed.sort(key=operator.itemgetter('ID'), reverse=True)

	return postsParsed

def DisplayBlogPosts(postDir, templateDir):

	posts = [ f for f in listdir(postDir) if isfile(join(postDir,f)) ]

	postsParsed = []
	content = ""

	for post in posts:
		postData = {}
		postId = 0
		onText = False

		with open(join(postDir,post), 'r') as template_file:
			blogPost = template_file.read()

		blogPostLines = blogPost.splitlines()

		for line in blogPostLines:
			if onText == False:
				if line == "---":
					onText = True
				else:
					dataAndKey = line.split('=')
					postData[dataAndKey[0]] = dataAndKey[1]
					
			else:
				blogPost += line

		postsParsed.append({'Data':postData, 'ID':postData["id"]})

	postsParsed.sort(key=operator.itemgetter('ID'), reverse=True)

	for postParsed in postsParsed:

		content += "<a href='blog.py?method=post&id=" + str(postParsed["ID"]) + "' class='postlink'><h2>" + postParsed["Data"]["name"] + "</h2></a>"
		content += "<p><b>By " + postParsed["Data"]["author"] + "<br/>" + postParsed["Data"]["date"] + "</b></p>"
		content += "<p>" + postParsed["Data"]["blurb"] + "</p>"
		content += "<p><i>Post ID: " + str(postParsed["ID"]) + "</i></p>"
		content += "<hr/>"

	templateData = {'title':'Posts', 'posts':content}

	misc.DoDocumentTemplating(templateData, join(templateDir, "home.html"))



def DisplayBlogPost(postID, templateDir):
	
	posts = GetAllBlogPosts("posts")
	content = ""

	for post in posts:
		

		if postID == post["ID"]:

			content += "<h2>" + post["Data"]["name"] + "</h2>"
			content += "<p><b>By " + post["Data"]["author"] + "<br/>" + post["Data"]["date"] + "</b></p>"
			content += post["content"]
			

			templateData = {'title':post["Data"]["name"], 'post':content}

			misc.DoDocumentTemplating(templateData, join(templateDir, "post.html"))



def Main():

	misc.PrintHeaders("200 OK")
	
	form = cgi.FieldStorage()

	if "method" not in form:
		DisplayBlogPosts("posts", "template")

	elif form["method"].value == "post":
		try:
			DisplayBlogPost(form["id"].value, "template")
		except KeyError:
			templateData = {'title':'Error', 'content':'<h2>Error</h2><p>You did not specify a post to view.</p>'}
			misc.DoDocumentTemplating(templateData, join("template", "error.html"))
	else:
		templateData = {'title':'Error', 'content':'<h2>Error</h2><p>That method does not exist.</p>'}
		misc.DoDocumentTemplating(templateData, join("template", "error.html"))


cgitb.enable()
Main()



