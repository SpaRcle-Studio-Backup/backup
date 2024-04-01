import os
import subprocess
import sys

print("Backup.py script is running...")

try:
    from github import Github
    from github import Auth
except ImportError:
    subprocess.run([sys.executable, 'pip', 'install', 'pygithub'])
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pygithub'])
    from github import Github
    from github import Auth

token = os.getenv('ciToken')

try:
    print("Trying to login to GitHub.")
    auth = Auth.Token(token)
    backup_g = Github(auth=auth)
    backup_org = backup_g.get_user('SpaRcle-Studio-Backup')
    backup_repos = backup_org.get_repos()
except Exception as e:
    print(f"GitHub login exception occurred: {str(e)}")
    exit(0)

g = Github()
organization = g.get_user('SpaRcle-Studio')
repos = organization.get_repos()

backup_repos_names = []
for backup_repo in backup_repos:
    backup_repos_names.append(backup_repo.full_name)

for repo in repos:
    if repo.full_name in backup_repos_names:
        continue

    fork = backup_org.create_fork(repo, default_branch_only=False)

# backup_repos = backup_org.get_repos()

# for backup_repo in backup_repos:
#   if backup_repo.fork:
