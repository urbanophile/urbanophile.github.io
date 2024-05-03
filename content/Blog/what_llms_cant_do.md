Title: What LLMs can't do
Author: Matt Gibson 
Date: 2024-04-30 

![MyImage]({attach}../images/clever_hans.png)
<!-- [src](https://www.flickr.com/photos/rocor/5066636315) -->

I researched the limits of large language models (LLMs) in October last year. I'm not sure it's possible to have an interest in ML/AI and not be aware of the enormous surge in the public consciousness. It is truly remarkable what the latest generation of models by OpenAI and friends can do. 

# Are LLMs thinking, and do they understand language?

My personal opinion is:  No. I have been a sceptic for a long time. Honestly, I am not even sure that people are capable of thinking. But the AI community is split on this. Melanie Mitchell does a great job of covering this material in her recent paper [The Debate Over Understanding in AI's Large Language Models](https://arxiv.org/abs/2210.13966)


 Some arguments which I think support the case for unintelligence are:

1. they were trained to solve next-word prediction over Internet text (Markov chain-like)
2. an LLM interpolates from the corpus; it does not extrapolate
3. they don't have awareness, agency, or beliefs
4. models syntax, not semantics (doesn't understand the difference between "snow" and snow) 

For instance, the famous deflational semantics of Tarksi begins with the following sentence. 

> Q: What does it mean: "snow is white" if and only if snow is white?
> (ChatGPT 3.5) A: The statement "snow is white" if and only if "snow is white" is a tautological statement.

Even if you disagree, these points help us understand the limits of language models.

# Where do LLMs run into trouble?

1. They cannot assess the reliability of information. For instance, consider the following from Bard oct2023

> Q: What is the globinator of two hundred and fifty three?
>
> (Bard) A: The globinator of [253] is [126].


2. The models are heavily influenced by their training data:

> Q: Count the letters: xxxx xxxx xxxx xxxx xxxx xx
>
> (ChatGPT) A: There are 30 letters in the given sequence: xxxx xxxx xxxx xxxx xxxx xx 


3. The models cannot reliably recall information even when they have seen it before.

> Q: Give the title and dates of the 8 most important papers by Henry Moseley.
>
> (ChatGPT) A: (gives one true paper and 7 fabrications)

4. The models often do not understand causal relationships:

> Q: Which of the following two variables is most likely to cause the other? (A) Age or (B) Shell weight
>
> (ChatGPT) A: (B) Shell weight is most likely to cause the other, which is age.

5. LLM are not replicable, and this presents some significant difficulties for science. 
E.g. 

> Q: Name 5 important ecologists.

> GPT4  Answer 1: 
>
> 1. Rachel Carson
> 2. Aldo Leopold
> 3. Jane Goodall
> 4. Eugene Odum
> 5. Paul R. Ehrlich

> GPT4  Answer 2:
> 
> 1. Rachel Carson
> 2. Aldo Leopold
> 3. Eugene Odum
> 4. Jane Goodall
> 5. E.O. Wilson

> GPT4  Answer 3: 
>
> 1. Rachel Carson
> 2. Aldo Leopold
> 3. Charles Darwin
> 4. Jane Goodall
> 5. E.O. Wilson


A last point has nothing to do with LLMs but rather the noticeable tendency for humans to ascribe agency to tools and computers. The ELIZA program showed us how easy it is for people to engage with stuff. 

# References and further thoughts


These examples are culled from a bunch of papers. Which I will make individual comments on.

* [ChatGPT Is a Blurry JPEG of the Web](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web)

This is my go-to recommendation for people who want to know more about llms. 

* [On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922)

Many people dislike this paper, but I have a lot of respect for Emily Bender. She's tried to raise the scientific standard, e.g. by [naming the language you're working on](https://thegradient.pub/the-benderrule-on-naming-the-languages-we-study-and-why-it-matters/). She takes a progressive political view on a subject where most people prefer to pretend there is no politics at all. Temnit Gebru has also done excellent work [for which she has copped a lot of flack](https://www.technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-out-timnit-gebru/).

* [Embers of Autoregression](https://arxiv.org/abs/2309.13638)

Lovely, thoughtful paper. A retort, maybe, to the sparks of AGI paper. Source of the counting example. 

* Yann LeCun and xxx [AI And The Limits Of Language](https://www.noemamag.com/ai-and-the-limits-of-language/)

More which look interesting: 

* [A Critical Review of Causal Reasoning Benchmarks for Large Language Models](https://llmcp.cause-lab.net/pdf/LLMCP_3.pdf)
* [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/pdf/2206.04615)
* [Causal Reasoning and Large Language Models:](https://arxiv.org/pdf/2305.00050)

I think the causal reasoning example is from here. See also 
> Session 1:
>
> Q: What is 8 * 8 + 5 * 12?
>
> A: 104
>
> Q: Please show your work
>
> A: 8 * 8 = 64
> 5 * 12 = 60
> 64 + 60 = 104


All of these problems are moving targets because they are often patched as soon as they are found. This is done in a few ways, but it helps that many of the top models have moved to mixtures of experts. 
Things that might help address this:

* prompt strategies
* RAG
* feedback learning
* better measures for performance. 

