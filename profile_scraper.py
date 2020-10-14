import instaloader
import os.path
import csv
import sys

profile_list = []
scrapecount = 0
file_exists = os.path.isfile("profiles.csv")
L = instaloader.Instaloader()
htag = input("Enter a hashtag (without the # symbol) to begin scraping:")
scount = int(input("Enter number of profiles to scrape:"))
# print("Scraping",scount"using #:",htag)
if file_exists:
    with open("profiles.csv", "r") as csvread:
        csvreader = csv.reader(csvread, delimiter=",")
        for row in csvreader:
            pro = row[1]
            profile_list.append(pro)
with open ("profiles.csv", 'a') as csvfile:
    headers = ['Name','Username', 'Picture Url', 'Bio']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
    if not file_exists:
        writer.writeheader()  # file doesn't exist yet, write a header
    while scrapecount != scount:
        for post in L.get_hashtag_posts(htag):
            for profile in post.get_likes():
                if scrapecount==scount:
                                sys.exit("Profiles scraped,Goodbye")
                try:
                    uname = profile.username
                    if uname not in profile_list:
                        print("Scraping profile no:",scrapecount+1)
                        writer.writerow({'Name': profile.full_name,'Username': uname, 'Picture Url': profile.profile_pic_url, 'Bio': profile.biography})
                        scrapecount+= 1
                        profile_list.append(uname)      
                except:
                        print("Exception occured")



    

