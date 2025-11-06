---
title: Lean for learning Mathematics
date: 2025-11-05
draft: false
tags:
  - featured
  - lean
  - proof-assistants
---
Clickbait title: Is Lean about to do the impossible?

Some techno-optimism for a change. Disclaimer for people who know more about this than me: I am not a contributor to Lean or MetaRocq and am stepping into these programs as a Computer Science student and primarily a user with some interest in understanding their internals.

Depends on what sphere of computer science you are in, but if you are staunchly not interested in Machine Learning, then I think there are few things as interesting as the grassroots movement of Lean4 and Mathlib.

[Lean4](https://github.com/leanprover/lean4) is a proof assistant based on the calculus of constructions, which for normal people means: It's a pain to work with. Or at least it should be. Proof assistants require you to write mathematical proofs which are not only correct, but in such a meticulous way that the computer can understand it.

[Mathlib](https://github.com/leanprover-community/mathlib4) is the biggest project in the Lean4 community and it's about the equivalent of building the Tower of Babel of mathematics. With disparate fields all trying to integrate their proofs in this behemoth of a library. Everyone can see and use each other's theorems and abstractions. It is probably also at this point the biggest single collection of proofs in our world. The Second Foundation would be proud.

## Technological foundations
As previously stated, Lean4 is based on the calculus of (inductive) constructions which is an example of dependent type theory, a field of logic/mathematics/computer science deservedly reserved for gradschool and up due to its inherent complexity. [Look at this book](https://www.danielgratzer.com/papers/type-theory-book.pdf).

Of course abstract logic systems don't have the most empathy for performant programming or usability. Well, Lean has a lot going for it. For once it is not the first time this was attempted, most notably there is the very mature Rocq (formerly Coq) which has done immense trailblazing in terms of performance, metaprogramming and tactics.

Let's talk about these things. 

**Performance** is of concern for multiple reasons. For one we want our proofs to be checkable quickly so we don't get annoyed (for programmers: this is basically about having a fast LSP), so we want our type resolution basics to run quickly. Lean4 is bootstrapped in very good C++, in part thanks to the fantastic [Leonardo de Moura](https://leodemoura.github.io/). We also have the act of reducing our terms to a normal form, most often used to calculate singular values. E.g. evaluating a simple function or approximating an integral. Rocq has decades of research into fast-reduction machines (one written in C and another transpiling to OCaml) and their stability. Lean4 has its own version of this as ``#eval`` and ``native_decide`` but notably with stronger restrictions on their effects on proofs leading to fewer unsoundness bugs (so far).

**Metaprogramming** again has a long history in Rocq, which has its own [MetaRocq](https://github.com/MetaRocq/metarocq) as a separate project. It provides an ongoing implementation of Rocq implemented in itself, quotation functionality and more unsavoury/fun ways to mess with Rocq at runtime. But notably Rocq itself is implemented in OCaml, which means that much of MetaRocq needs to be as well, to interact with the deepest layer of Rocq. Lean is fully bootstrapped in itself (so cool!), except for the aforementioned C++ compiler for eval. This means that to study how e.g. Definitons are implemented in Lean, all you need to do is read the kernel code and if you want to do so, you can simply copy-paste it into your own lean file with your modifications, giving you "my_def" where I don't know whenever you define a new definition it wraps it into a giftbox and plays the saxophone. [We've got a whole book in metaprogramming in Lean!](https://leanprover-community.github.io/lean4-metaprogramming-book/)

**Tactics** are the most outside of my area of expertise. This is primarily because I am neither a mathematician nor an avid user of the most advanced ones. I'm a dirty computer scientist and maybe logician, so I like building up my proof trees from ``exact`` and ``refine``.  People other than me (especially mathematicians!) actually like their proofs to make human-readable sense. This is what tactics are for: They are a way to write your proofs in a human-readable way by chaining together different ways of "adding building blocks" to your proof. [Rocq has a lot of experience with tactics](https://rocq-prover.org/doc/V9.1.0/refman/coq-tacindex.html) and how to correctly combine your tactics in different ways (Ltac, Ltac2, Mtac, Mtac2 (!)). What you want for your tactics is that they basically help users over every part that seems trivial or tedious to them. In the most extreme case you might put [an entire SMT-solver](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/#grind) into your tactic. And this incredibly broadens the usability of your tool for non-logicians.

More things to mention: How Lean4 handles similar features to Rocq's extensions, [inferring Typeclasses](https://arxiv.org/pdf/2001.04301), partial functions, [non-computability](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/), and FFI.

## Community and advocacy
If you've heard about Lean4, there's about a 50% chance you've heard about it from [Terence Tao](https://en.wikipedia.org/wiki/Terence_Tao). Very smart guy, very well-spoken guy! He of course has a very wide reach, being immensely respected by other mathematicians and you can recognise this through his footprint on the Lean4 community. Mathematicians have been flooding in and they have been hard at work writing proofs, interactive books and entire libraries.

The signature work of Terence Tao and other prominent mathematicians has been starting a blueprint to prove a famous theorem, [most prominently Fermat's Last Theorem](https://github.com/ImperialCollegeLondon/FLT) that would get any 3blue1brown viewer excited. 
Indeed [Lawrence Paulson](https://en.wikipedia.org/wiki/Lawrence_Paulson) has [recently written](https://lawrencecpaulson.github.io//2025/11/02/Why-not-dependent.html):
> The only aspects of Lean that I envy are its huge community and the [Blueprint tool](https://github.com/PatrickMassot/leanblueprint).

Secondarily there is also the [ongoing advocacy](https://ai-math.zulipchat.com/#narrow/channel/539992-Web-public-channel---AI-Math/topic/Best.20practices.20for.20incorporating.20AI.20etc.2E.20in.20papers/near/546518354) by Tao and others to formalise new discoveries or unproven theorems in Lean4 from the start.

I think I cannot overstate just how much of a boon the growing community for Lean4 has been. Apart from the very tangible benefits of gigantic proof corpora, I think it brings with it an air of excitement and a need to focus on the user experience of a proof assistant. Something that someone who has only been using Rocq might never believe.

[It also means we get silly things.](https://unnamed.website/posts/bad-apple-lean-tactic/)


## AI
Yes, I'm afraid we do also need to talk about AI here. It is no secret that many people have been using Large Language Models for many things. This includes writing mathematical proofs. Maybe you're a TA or someone else grading take-home assignments, but you've probably felt it. Right now there is little stopping someone from stating they solved a big theorem other than thoroughly checking their proof. Well, if they can churn 100 pages in a minute, that becomes infeasible. And they tend to not be the only one doing it.

On the more measure side of the spectrum you may also have somewhat respectable people being able to assist their writing of proofs in some ways, just producing more, but having less of a hand in every single step of the way, mayyyybe producing things which have a higher chance of mistakes.

Other people would not be so gentle. And some suggest an informal standard to formalise future discoveries in Lean. In this case, we have the very powerful idea of a machine that can produce a lot of maybe-correct things (LLMs) being hooked up to a machine which cares veryyy much about correctness (Lean4). It feels like every NLP lab has realised this and is currently working on an agentic framework that builds Lean4 proofs automatically (with varying success). The beautiful thing as a "corrector" is that now all the sifting through incorrect proofs is again on the side of the submitter. You can simply insist that something is formalised in Lean4 and get a reasonable baseline of quality.

Looking at how much effort is involved at "vibe-proofing" is an ongoing question. Coming back to Terence Tao, he is of course one of the main faces people associate with this style, constantly trying out different approaches. He has of course excellent expert knowledge in a lot of areas of mathematics he tries LLMs in and as such I trust to give trustworthy accounts. [Here's a nice recent example](https://mathstodon.xyz/@tao/115493668304518132).

I am not an AI researcher, but the people who work with LLMs *and* proof assistants seem to complain a lot about [not large enough training corpora](https://arxiv.org/pdf/2505.22846). Even worse, I suspect, might be the situation with ecosystems which are as split as Rocq when it comes to LLMs inferring incorrect knowledge from one library to another, just because their code looks similar. I think the fact that Lean4 has this unquestionable standard of Mathlib4 ([which is indeed very well indexed](https://leanprover-community.github.io/mathlib4_docs/index.html)! including [natural text search](https://leansearch.net/)) and its typeclasses leading to a high degree in abstraction.


## So... is Lean4 usable for studying new concepts?
Well, there are certainly [some efforts](https://www.youtube.com/watch?v=0QZI_m8WZ0Q) to do it. I like the work [done by Philip Zucker](https://www.philipzucker.com/dirty_lean/). Lean4 has a very challenging proposition in front of it, if it wants to be useable to new learners. It needs to be more efficient than pen and paper, or at least solve a different purpose.

Here's the good news: Lean has some very exciting things it can do better than a good book and a piece of paper. Computations and simplifications are very well automated. That is the main benefit of an "interactive notebook". Additionally, it can of course tell you if your proof is wrong and finish some parts of proofs for you (which you may sweat needing to explain or lest you make a mistake).

Now there are some less tangible, but maybe even more exciting things. Collaboration through version control software has become very tangible for mathematicians now. And the immense libraries like Mathlib have also enabled mathematicians to do the famous programmer practice of "copying something from someone else into your code" (please care about licenses!). Even better is including Mathlib as a dependency of your project and benefiting from a lot of theorems in problems similar to yours, including theorems and automation mechanisms.

But I do also have some concerns. Currently introductions to Lean still require students to learn some pretty strong abstractions in interacting with a proof assistant, which I think may be too much for many undergraduate students. Yes, automation is improving on this, but the automation from tactics like ``ring`` and ``grind`` tends to work well in well-trodden territory of well-known numbers. As soon as you define your own datatype and don't define 30 theorems with @, the process becomes a lot more manual. So I think this strong foundation is one that will stay.

There is also an ongoing tension between objects which are "correct by construction" and trying to relate them to more human-understandable concepts. My favourite example: How do you prove a sorting algorithm is correct? Well it should create a sorted list and it should not "change" the elements of the original list. How do you define the latter? Well just prove that your sorting algorithm only consists of a sequences of swaps of two elements! (Even worse when proving stable sort). Talking about Fin (maybe the purest idea of correct by construction), there is of course also [the image](https://mathstodon.xyz/@markusde/115446833462451380). 


## Should you learn Lean?
On average, considering you made it through this entire blog post, yes you should. You're weird in the right way to do it.

Try out the natural game in Lean:
https://adam.math.hhu.de/

I think what the general question boils down to is at what age should we be teaching mathematicians and computer science students Lean? And I think the answer may move lower and lower over the years, but at this moment I do not think it is as essential as writing a proof with pen and paper. Maybe the year after that you should be able to write it in Lean as well. Or whatever the newest coolest proof assistant is.













