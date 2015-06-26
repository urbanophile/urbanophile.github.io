=== Quickly setup a wiki with web2py and aws


Get a AWS EC2 instance:
Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-69631053

=== Configure security group to allow HTTP, HTTPS and email traffic

Launch instance and wait for it to boot

Note the IP address

=== Secure the server
1) fail2ban
2) cloudflare
3) logwatch

Otherwise should should down specific ports

=== Update DNS records

Go to your domain name registrar, and update the records this will take a while

update the @ and www record to point to the IP address of the host.

This the propagates through the dns servers can be observed here:

=== SSH in to the box
ssh -i mac_book_air.pem ubuntu@52.64.54.3



=== Reassuring hello world


=== Nginx in front


=== uWSGI in the middle


=== That's a wrap!
