import praw
import logging as log

LOG_FILENAME = "./log_.log"

log.basicConfig(handlers=[
            log.FileHandler(LOG_FILENAME),
            log.StreamHandler()],level=log.INFO,format='%(asctime)s : %(levelname)s : %(message)s')

def work():
	log.info("Lastrun of the script")
	
	_subtocrosspost = 'FuckZhu'
	try:
		reddit = praw.Reddit(client_id="xxxxxxxxxx",
							client_secret="xxxxxxxxxxxxxx",
							password="xxxxxxxxxxxxxx",
							username="Karen-o-matic",
							user_agent="copybot by /u/Karen-o-matic")
		reddit.validate_on_submit=True	
		
		for submission in reddit.subreddit(_subtocrosspost).hot(limit=25):
			
			text = "Title:\n*"+submission.title+"*\n\nText:\n*"+submission.selftext+"*"
			try:
				modcommentid = submission.reply(text)
				comment = reddit.comment(modcommentid)
				comment.mod.distinguish(how="yes", sticky=True)		
				log.info("answered {} {} {}".format(submission.id,submission.title,submission.permalink))
			except Exception as err:
				log.error("can't answer this {} {} {} {}".format(submission.id,submission.title,submission.permalink,str(err)))

	except Exception as err:
		log.error("Run thru all submissions {}".format(str(err)))


work()



	
	

	
	
	
	