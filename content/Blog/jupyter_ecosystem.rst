The Wild West of Jupyter
#############################

:date: 2024-02-13
:authors: Matt Gibson
:modified: 2024-04-20 18:59

There's some wacky stuff in the Jupyter ecosystem. Still, one thing that really stood out for me was the extension of Jupyter notebooks into web development and their interaction with the JavaScript ecosystem. So web assembly is a thing, and you can run C and Rust code inside little isolated JavaScript sandboxes instances, maybe even from `your CDN <https://developers.cloudflare.com/workers/languages/rust/>`_, so of course you want to compile `Python in WASM <https://pyodide.org/en/stable/>`_. Now you're wondering, didn't Jupyter do some fancy refactoring a while ago? I wonder if I can put a webserver up there, too...


Behold `JupyterLite <https://jupyterlite.readthedocs.io/en/latest/quickstart/embed-repl.html>`_:

.. raw:: HTML

 <iframe
 src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&code=print('hello world')"
 width="100%"
 height="100%"
 ></iframe>

Wow! Just what you always wanted: free notebook hosting! you can install packages, you can code, powered by this:

.. figure:: {static}/images/jupyterlite-diagram.svg
    :width: 600px
    :alt: JupyterLite architecture diagram
    :figclass: center

    `(source 1) <https://jupyterlite.readthedocs.io/en/stable/reference/architecture.html>`_

Comparing this with the standard architecture for Jupyter:

.. figure:: {static}/images/notebook_components.png
    :width: 600px
    :alt: Jupyter notebook architecture diagram
    :figclass: center

    `(source 2) <https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html#the-jupyter-notebook-interface>`_


You see, one basically has to reimplement the server side of Jupyter in the browser. This is not a small task because Jupyter Server depends on more hefty libraries like ZeroMQ and Tornado, but presumably, compiling to WASM is useful.

I don't have an excellent knowledge of the history of the Jupyter project. Still, I remember this whole thing blowing up in about 2015 with `the big split <https://blog.jupyter.org/the-big-split-9d7b88a031a7>`_. The big split was a drive to make Jupyter language agnostic, which, as I understand, is more or less successful; nowadays, you can run R, Julia, and even C++ in a Jupyter notebook. It's not really appreciated how much the whole project has ballooned:

.. figure:: {static}/images/repos_map.png
    :width: 600px
    :alt: A map of the Jupyter project repositories
    :figclass: center

    `(source 3) <https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html>`_

and that's just the offical projects! You probably know about related things like `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_, `JupyterLab <https://jupyterlab.readthedocs.io/en/stable/>`_ and `IPython <https://ipython.org/>`_. There are some funny spin-of (besides jupyterlite) that you may or may not be aware of

- `traitlets <https://traitlets.readthedocs.io/en/stable/>`_
- `ipywidgets <https://ipywidgets.readthedocs.io/en/stable/>`_
- `Zeus <https://xeus.readthedocs.io/en/latest/>`_
- `Jupyterhub <https://jupyter.org/hub>`_
- `Lumino <https://github.com/jupyterlab/lumino>`_

Another exciting thing is that Colaboratory and VSCode have non-standard implementations of the client side of the Jupyter (ask me how I know). In fact there's a whole ecosystem (built on the ricketty foundation of ipywidgets) for web development with Jupyter: `voila <https://voila.readthedocs.io/en/stable/>`_, `Mercury <https://runmercury.com/>`_ and `Solara <https://solara.dev/>`_ aiming to compete `streamlit <https://streamlit.io/>`_ for the affluent market consisting of data scientists who would literally prefer to do anything than write javascript.

My use case for Jupyter notebooks is primarily for exploratory data analysis and expository stuff. Early in my PhD, I had a few bad experiences with state preservation, which soured me to use it for more serious projects. You are probably aware `that opinion is controversial <https://www.fast.ai/posts/2020-10-28-code-of-conduct.html#my-talk-at-jupytercon>`_. I like the literate programming approach of `Rmarkdown/quarto <https://quarto.org/>`_ (it supports Python now, so check it out) much more because it solves the issues with the non-transparent notebook blob of JSON in the ipynb format and allows better IDE integration. One direction of this is ipynb to ipynb; Jupyter has an equivalent for a while, `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_. It's only recently that py to ipynb has standardised on `Jupytext <https://jupytext.readthedocs.io/en/latest/index.html>`_ (although there's also `nbdev <https://nbdev.fast.ai/getting_started.html>`_). It's interesting that Jupytext (it's used, for instance, in the VSCode implementation of notebooks) that it's not part of the core ecosystem. Is the whole project a horrible mess in scope creep, or is it a shining example of the power of open source? I don't know, but the Jupyter project has been shaped by the community's needs in unexpected ways. 