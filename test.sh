cd /dev/shm
git clone https://github.com/gurujerry/dvparser.git
cd /dev/shm/dvparser
touch /dev/shm/dvparser/test.txt
git add .
i=1
until [ $i -gt 5 ]
do
  echo $i > /dev/shm/dvparser/test.txt
  git commit -am "commit $i"
  ((i++))
done