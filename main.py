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
mem_fs.listdir("/fruit/")

with mem_fs.open('fruit/apple.txt', 'r') as rapple:
    rapple.read()

mem_fs.listdir("/fruit/")

mem_fs.makedirs('gitstuff')
mem_fs.listdir
# Examples
r = git.Repo.clone_from(git_url, repo_dir, branch=branch, recursive=True)
bare_repo = git.Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
# My tries
r = git.Repo.clone_from(gitrepo, mem_fs, branch="main", recursive=True)
bare_repo = git.Repo.init(os.path.join(rw_dir, mem_fs), bare=True)
fs.opener.tempfs

# Runs pretty fast, remove print to run faster
foo = 0
while foo < 1000000:
  foo += 1
  print(foo)

# This below write a million times, writes a lot of data
with mem_fs.open('fruit/apple.txt', 'w') as apple:
    while foo < 1000000:
        foo += 1
        apple.write(f'{foo}')

# This runs much slower as it opens and closes multiple times
while foo < 1000000:
    with mem_fs.open('fruit/apple.txt', 'w') as apple:
        foo += 1
        apple.write(f'{foo}')

## Test
repo = git.Repo.init("/dev/shm/awesome-project", mkdir=True)
repo.git.add("hello.py")
status = repo.git.status()
repo.git.commit(m="foo commit")
## Using Pure Python Function #
repo.index.add('hello.py')
repo.index.commit("first commit")
## Testing more
foo = 0
repo.git.add("foo.txt")
# Make sure git config user name and email are done
# Runs decently fast, need investigate appending less data or overwriting
with open("/dev/shm/awesome-project/foo.txt","w") as file:
    while foo < 10000000:
        foo += 1
        file.write(f'{foo}')
        repo.index.commit(f"commit {foo}")

f = open("/dev/shm/awesome-project/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
