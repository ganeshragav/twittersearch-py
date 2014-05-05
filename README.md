Twitteri Search

A python app searches tweets based on keywords. Uses Twitter Streaming api tweepy & unicodecsv for csv conversion

Features of this Search script :

Very Tiny
Able to Search multiple Keywords
No Previous Programming knowledge required
Can collect twitter Data based on your keyword preference

Prerequisities needed: 

Before installing any modules, you should place your twitter keys in tweets.py file. 

How to get twitter keys,please check https://spring.io/guides/gs/register-twitter-app/ 

Tweepy (module)
	You can install tweepy module using 
		
		pip install tweepy
	
			(or)
		
		easy_install tweepy

unicodecsv (module)
	You can install unicodecsv using
		
		pip install unicodecsv
		
			(or)
		
		easy_install unicodecsv

Usage :

	You can run this script using below :

		python tweets.py


	Make sure you have keywords listed in keywords.txt file

After installing the foresaid modules, you can modify the keywords.txt file. 
keywords.txt file must contain individual keywords in separate line.

Note : Keywords with space can be accepted. Keywords addition with other special characters are not tested yet. 

