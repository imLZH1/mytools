
- Based on ARP protocol,
- LAN scan only(Intranet)

```shell
vim ~/.bashrc
vim ~/.zshrc
```
add 
`alias scssip='python3 /etc/myscript/scssIP/scpy-ip.py 2>/dev/null'`

```shell
┌──[root🐲KaliBug]-[~]
└─➤ ip addr    
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: `eth0`: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:8f:3f:a7 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.102/24 brd 192.168.0.255 scope global dynamic noprefixroute eth0
       valid_lft 3965sec preferred_lft 3965sec
    inet6 2408:8244:9c20:967::1002/128 scope global dynamic noprefixroute 
       valid_lft 83972sec preferred_lft 83972sec
    inet6 2408:8244:9c20:967:2fa0:eedc:89db:52e1/64 scope global temporary dynamic 
       valid_lft 86299sec preferred_lft 14299sec
    inet6 2408:8244:9c20:967:20c:29ff:fe8f:3fa7/64 scope global dynamic mngtmpaddr noprefixroute 
       valid_lft 86299sec preferred_lft 14299sec
    inet6 fe80::20c:29ff:fe8f:3fa7/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
                                                                                                                                                              
┌──[root🐲KaliBug]-[~]
└─➤ scssip eth0

┌─[*] Start Scaning !
└─────────────────────────────────────────────────────────
        IP:192.168.0.1         MAC:54:a7:03:2f:f2:25
        IP:192.168.0.103       MAC:08:00:27:9e:4a:5d
        IP:192.168.0.101       MAC:40:23:43:d2:53:8f
┌─────────────────────────────────────────────────────────
|[*] Network segment: 192.168.0.0/24
|[*] Alive IP number: 3
|[*] Elapsed real time: 6.63 sec
└─[+] Scan complete !
```

