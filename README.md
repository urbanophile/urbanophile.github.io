# Overview

This is contains the code I was using make my personal website hosted on github pages. It contains a lot cruft.

## Build website

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

output is a separate repo for website which is a git submodule. Also the theme is separate submodule, so don't forget to clone that.

## Preview website

Use the following command to preview the website locally:

```
pelican --listen
```

and navigate to <http://localhost:8000/>
