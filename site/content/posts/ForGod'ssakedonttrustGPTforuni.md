---
title: For God's sake dont trust GPT for uni
date: 2024-09-08
draft: false
tags:
  - featured
  - commentary
  - ai
  - university
---
Clickbait title: [I will fucking piledrive you if you insist on an answer given by ChatGPT again](https://ludic.mataroa.blog/blog/i-will-fucking-piledrive-you-if-you-mention-ai-again/)

*I do not specialise in AI in my research.*

In high school I wrote a paper on the philosophy of Wittgenstein and how it relates to the concept of a programming *language*. One central question was if computers would ever be capable of understanding natural language. I cited the [GPT-2 paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) as state of the art.
Leading up to my time in university then, I was primed 
to GPT-3 being hyped up by select people have gotten access to it. [This Tom Scott video is a good time capsule](https://youtu.be/TfVYxnhuEdU). 
ChatGPT was released in the middle of my first university year, and it took less than a month for someone to copy-paste entire university chats into it and letting it answer. They were figured out after the third message and claimed it to be a social experiment. A social experiment with only 3 data points is lousy, so I wonder how much faith they had in it passing the Turing Test.


Having finished my bachelor's in computer science now, I have helped several people who have studied the same subjects simultaneously or after me. I've used the technology lightly for embarrassing Linux questions (I still need to look up how mountpoints work like every 2 months) or asking it for name suggestions in writing. I have heard from others who have made much more use of the language models in their university life. And every so often I meet one of them **incredibly confused about a topic that ChatGPT mangled for them**. This is my warning to future students.

### Never trust a language model to be correct

Modern Language Models like ChatGPT are statistical models ([3B1B video of technical explanations](https://youtu.be/wjZofJX0v4M)) with enormous storage. This storage does mean that they can remember information given to them. But any output you get from them is probabilistic. For example, if you ask it a controversial Yes or No question, it is entirely possible for it to start with "*Yes*" and then give you a sensible explanation, only for then to be asked the same question in a new chat for it to answer "*No*", and give an equally sensible different answer (This is especially funny if the ChatGPT interface shows you both answers side by side, as has happened to me). The entire output can be determined by the first choice of token. This is of course because GPTs were designed to plausibly continue text, not figure out the truth. There is no "figuring" to done at all.

### Language Models may have poor training material relating to your course content

As is sadly the case, definitions of words are not set into stone. Different disciplines may have completely different definitions, for what can be considered a "rock" or a "function". Even within sub-disciplines of mathematics you have to ask anew if $\mathbb{N}$ contains $0$ or not. Your lecturer may have their own terminology shared by nobody else in the world and all their slides are hidden behind 3 passwords, never falling into Sam Altman's greedy hands. One lecture I had defined a postfixed-point as exactly the *opposite* of what Wikipedia had it as. 

### Language Models can be confidently wrong.

Many will protest now that of course a discrepancy like that would be obvious and could be rectified by simply correcting ChatGPT. But how will you know that it disagrees with what you need to learn, if it is your replacement for engaging with the study material? Do not let it be your primary source on anything. There are no inherent checks in these models that tell you how confident one can be about one statement of theirs vs. another. There is [no fidelity](https://youtu.be/EUrOxh_0leE).

### Language Models are boring.

Maybe you're using these models not as teachers, but more as editors, copywriters. They may be able to write a report for you, as long as you do all the actual knowledge work before. If you've ever tried this on any project you cared about, you will find quickly that ChatGPT has no voice. It will give you the most median of whatever tone you ask of it. If this is menial busywork that you've been forced to do due to outdated systems, then that is acceptable. But if you are serious about building any kind of passion for what you do, this will kill any flame. This goes doubly so if you want to actually bring new ideas to the table in any field. 

### Language Models are still useful.

It turns out, even if the output of the models cannot be trusted, just generating text is still interesting for some applications. I want to go through a few:

**You can instantly verify the result**. This may be the case in asking for the model for a synonym of another word in a certain context (something traditional synonym sites struggle to do). If the synonym was at the tip of your tongue, you can instantly verify if the model is correct or not.

**It is just the start of research**. You may be interested in a certain topic, but the only way to describe it is in 3 sentences. Google will probably fail you unless you have the keywords, but a language model will happily point you to the exact keyword you can then traditionally research.

**You are mentally blocked**. The traditional way to solve this is rubberducky programming. But turns out if your rubberducky sometimes makes obviously wrong statements (because again GPTs are pretty stupid), correcting it can be a good way to force you to engage with the problem at hand. Making the effort of writing a good prompt has often led me directly to a solution without ever sending my GPT pal a text message.

##### Closing words

I hope you don't take my complaints about people insisting on what GPT said too much to heart. One of the best ways to check your understanding is to discuss things with another student. Anyone who I've needed to correct away from what ChatGPT said did well by having the courage to open their mouth. This article is much more meant for students who silently rely on these language models. Check your understanding with colleagues.