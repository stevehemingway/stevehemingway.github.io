+++

+++

## Upgrading mail-in-a-box

I just upgraded [Mail-in-a-Box](https://mailinabox.email). 

The upgrade process is delicious. I just typed 
````
  curl -s https://mailinabox.email/setup.sh | sudo bash
````
and it just ... upgraded itself. See the transcript here. It really was that easy. Look at the set of packages it upgrade!

````
password for steve:
Updating Mail-in-a-Box to v0.21c . . .
remote: Counting objects: 8, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 8 (delta 6), reused 6 (delta 4), pack-reused 0
Unpacking objects: 100% (8/8), done.
From https://github.com/mail-in-a-box/mailinabox
 * [new tag]         v0.21c     -> v0.21c

WARNING: Your Mail-in-a-Box has less than 768 MB of memory.
         It might run unreliably when under heavy load.

.. (couple of curses dialog boxes to confirm host name etc.)

Primary Hostname: box.acksam.com
Public IP Address: 46.101.14.93
Public IPv6 Address: 2a03:b0c0:1:d0::bd4:e001
Mail-in-a-Box Version:  v0.21c

Updating system packages...

Installing system packages...
Initializing system random number generator...
Firewall is active and enabled on system startup
Installing nsd (DNS server)...
Installing Postfix (SMTP server)...
Installing Dovecot (IMAP server)...
Installing OpenDKIM/OpenDMARC...
Installing SpamAssassin...
Installing Nginx (web server)...
Installing Roundcube (webmail)...
Installing ownCloud (contacts/calendar)...
ownCloud is already latest version
Installing Z-Push (Exchange/ActiveSync server)...
Installing Mail-in-a-Box system management daemon...
Installing Munin (system monitoring)...
updated DNS: OpenDKIM configuration
No domains hosted on this box need a new TLS certificate at this time.

-----------------------------------------------

Your Mail-in-a-Box is running.

Please log in to the control panel for further instructions at:

https://box.acksam.com/admin

If you have a DNS problem put the box's IP address in the URL
(https://46.101.14.93/admin) but then check the SSL fingerprint:
EA:EB:03:AD:49:D3:7D:A6:6E:34:1A:E5:C1:9E:2B:9D:8B:FF:D1:01
````
