import boto3
from click import command, option
from os import system, chdir
import datetime
import time

@command()
@option("--reponame", help="Name of repo to check/look for/update")
def main(reponame):
	


	temp_dir = str(reponame) + str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H_%M_%S'))	
	
	git_action_str = "git clone --mirror https://github.com/nwHacks-UVic-Pros-2017/mojio-automessage.git {0}".format(temp_dir)

	aws_codecommit_action_str = "git push https://git-codecommit.us-west-2.amazonaws.com/v1/repos/mojio-amazon"	

	client = boto3.client('codecommit')


	response = client.list_repositories(
   		sortBy='repositoryName',
    	order='ascending'
	)

	print(response["repositories"][0]["repositoryName"])	


	for each in response["repositories"]:
		if each["repositoryName"] == reponame:
			
			system(git_action_str)	

			chdir(temp_dir)	
			
			#Hack to get the latest commit from git log. Not pretty, but it
			# works
			system("git log | head -n 1 | tail -c 41 > ../latestcommit.txt")

			system(aws_codecommit_action_str)	
			exit(0)

		else: 
			continue

		print("Repo does not exist. Please enter the name of an existing repo.")
		exit(1)
	

if __name__ == "__main__":
	main()
