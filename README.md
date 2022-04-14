# cs50

https://cs50.harvard.edu/x/2022/

## install cs50 tools on local computer
```
curl -s https://packagecloud.io/install/repositories/cs50/repo/script.deb.sh | sudo bash
sudo apt install libcs50
```

before compilation with make

```
export LDLIBS="-lcrypt -lcs50 -lm"
make credit
```
