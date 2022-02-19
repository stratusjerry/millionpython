import fs
import git

#from git import Repo
#pip3 install gitpython --user
#pip3 install fs --user
git.Repo.clone
git.commit

gitrepo = "https://github.com/gurujerry/dvparser.git"
mem_fs = fs.open_fs('mem://')
mem_fs.makedirs('fruit')
with mem_fs.open('fruit/apple.txt', 'w') as apple:
    apple.write('braeburn')
mem_fs.listdir("/apple/")

mem_fs.makedirs('gitstuff')
mem_fs.listdir
# Examples
r = git.Repo.clone_from(git_url, repo_dir, branch=branch, recursive=True)
bare_repo = git.Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
# My tries
r = git.Repo.clone_from(gitrepo, mem_fs, branch="main", recursive=True)
bare_repo = git.Repo.init(os.path.join(rw_dir, mem_fs), bare=True)
fs.opener.tempfs

