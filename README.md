# Overview 

This is contains the code I was using make my personal website hosted on github pages. It contains a lot cruft.

# to make changes

Compile the website from source with 
```
pelican content
```

then deploy new changes with 
```
cd output 
git add . 
git commit -m "a change to my website" 
git push origin master
```

output is a separate repo for website which is a git submodule.