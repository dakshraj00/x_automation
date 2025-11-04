from tweet import post_tweet
import schedule, time

schedule.every().day.at("11:41").do(post_tweet)

print("⏰ Bot started. Waiting for scheduled time...")
while True:
    schedule.run_pending()
    time.sleep(60)
