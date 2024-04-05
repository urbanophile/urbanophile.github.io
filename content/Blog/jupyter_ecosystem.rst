The Wild West of Jupyter
#############################

:date: 2024-02-13
:authors: Matt Gibson

There's some wacky stuff in the Jupyter ecosystem, but I think on thing that really stood out for me is the extension of jupyter notebooks into web development and the interaction with javascript. So web assembly is a thing and you can run C code little isolated javascripts instances, maybe even from your CDN, so of course you want to compile `Python in WASM <https://pyodide.org/en/stable/>`_, and now you're wondering, didn't Jupyter do some fancy refactoring  and that I think about I can put a webserver in there too...


Behold `JupyterLite <https://jupyterlite.readthedocs.io/en/latest/quickstart/embed-repl.html>`_:

.. raw:: html

    <iframe
    src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&code=print('hello world')"
    width="100%"
    height="100%"
    ></iframe>

Wow! Just what you always wanted free notebook hosting! you can install packages, you can code, 

powered by this:
https://jupyterlite.readthedocs.io/en/latest/_images/jupyterlite-diagram.svg