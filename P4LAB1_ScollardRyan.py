
import re


user_text = 'Listen, Mr. Jones, calm down?.'

#user_text run through regular expression module which removes identifed characters. Then len() is used to get length count.
print(len(re.sub('[^A-Za-z0-9?]+', '', user_text)))
