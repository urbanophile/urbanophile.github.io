vagrant development env

setting up a vagrant dev environtmnet has a pain in the butt.

Well, not setting up

introduce small number of vagrant commands

vagrant up
vagrant ssh
vagrant ssh-config
vagrant destroy

ansible commands

ansible-playbook

I don't like debugging things on line servers. There are a couple of ways to avoid doing this but

Ansible is a nice wraper around ssh, which gets you using something very similiar to YAML annotated BASH. So we are one step up on the hierarchy of developer righteousness, but not quite at the puppet, chef, docker level.  It is not a super complicated tool, but it guarantees a number of nice properties like idempotence of commands.
