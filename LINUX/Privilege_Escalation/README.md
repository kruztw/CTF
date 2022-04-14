## step1

find executable files with [SUID](https://en.wikipedia.org/wiki/Setuid) and owned by root

```shell
find / -perm -u=s [-type f] -print 2>/dev/null
```

## step2

Go to [gftobins](https://gtfobins.github.io/gtfobins/time/) and get the exploitation
