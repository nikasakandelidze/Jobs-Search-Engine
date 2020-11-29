import fbchat
from fbchat import Client
from fbchat.models import *

from vacancy_response_generator import generate_response_depending_on_input

#configurations for using fbchat library
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')


username='zoro58767@gmail.com'
password='zorozoro1234'

response_default_positive_resposne='yes, here are the results: \n\n'


class CustomJarvis(Client):
	def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):

		actual_message = message_object.text

		response=response_default_positive_resposne+generate_response_depending_on_input(actual_message)

		self.markAsRead(author_id)

		if author_id != self.uid:
			self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)


my_jarvis=CustomJarvis(username, password)

my_jarvis.listen()