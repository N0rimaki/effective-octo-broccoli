import praw
import logging as log
import textwrap

LOG_FILENAME = "./log_.log"

log.basicConfig(handlers=[
            log.FileHandler(LOG_FILENAME),
            log.StreamHandler()],level=log.INFO,format='%(asctime)s : %(levelname)s : %(message)s')

def work():
	log.info("Lastrun of the script")
	
	_subtocrosspost = 'UnpopularFacts'
	try:
		reddit = praw.Reddit(client_id="xxxxxxxxx",
							client_secret="xxxxxxxxxxxxxx",
							password="xxxxxxxxx",
							username="unpopularcummybot",
							user_agent="UnpopularCummyBot by /u/unpopularcummybot")
		reddit.validate_on_submit=True	
		
		for submission in reddit.subreddit(_subtocrosspost).top('all',limit=1000):
		
			shorten= textwrap.shorten(submission.selftext,width=990, placeholder="...")
			
			text = "Backup in case something happens to the post:\n\nTitle:\n*"+submission.title+"*\n\nText of the post:\n"+shorten
			try:
				modcommentid = submission.reply(text)
				comment = reddit.comment(modcommentid)
				comment.mod.distinguish(how="yes")		
				log.info("answered {};{};{}".format(submission.id,submission.title,submission.permalink))
			except Exception as err:
				log.error("can't answer this {};{};{};{}".format(submission.id,submission.title,submission.permalink,str(err)))

	except Exception as err:
		log.error("Run thru all submissions {}".format(str(err)))


work()



	
	

	
	
	
	