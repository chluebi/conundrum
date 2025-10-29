---
title: Mfw when rust
date: 2025-10-29
draft: false
tags:
  - personal
  - coding
---
Clickbait title: Local programmer cannot believe how good Rust is.

I've taken a crack at learning C++ (again). I'm approaching this the same way someone would approach reading Shakespeare: It's a classic, you gotta know it. The most I can say about it is that I'm learning a lot about templating and preprocessors.

Having stayed optimistic with C++, I've tried starting projects in it. I tried, and I went back to Rust. This is a me problem. There's a joke going around that you should learn Haskell (or the obviously superior OCaml) first before you're learning Rust. And it is kind of true. Not because the knowledge from those languages is essential (Result Monad is very neat tho), but rather that if you've ever used stuff like typed unions (= Haskell datatypes, Rust enums), you will miss them so much.

## Rust is perfect
Rust's biggest claim to fame is of course an actually useable borrow checker which is deeply integrated with its type system to the point it offers very good security against certain bugs. But I think it took me a while to understand just how perfect of a cube of features Rust is, with everything reinforcing each other.

Designing my own languages, I tend to wreck my brain about how to make the perfect system all the time of course. Now every programmer has the dream of perfectly planning an abstract system from the start that anticipates every need (premature extensibility is evil). The thing is, programming language design is one of the few times where that might actually be justifiable. So it's obviously where the idealists go. (In practice languages will make mistakes and hopefully early enough in the release cycle to be able to deprecate the old version and just continue. Poor PHP.)

So then I look at Rust, and my god it feels so perfect in many ways. I can't explain the exact interplay of the features, but the trips I've taken to try and break some security guarantees of Rust (without unsafe), there was always a perfectly designed stopping point. (A good example is the ``Sized`` trait)

Obviously Rust is not actually perfect, smarter people than me have stuff to complain about (e.g. I've heard complaints about async and the lack of first-class support for purely stack-based code, you might see better done in C or Zig).

## Rust is useful
Your normal perfect programming language (e.g. Standard ML) will be very neat, but it will end up not supporting every usecase you want. I would not want to do baremetal programming with Standard ML for example. Rust seems different, or at least a lot wider. (This is part of the "rewrrite in Rust" evangelism)

What is surprising to me is just how many things Rust still allows me to do. Having a formal methods background, I was shocked to see that Rust allows you to step beyond the monomorphisation default with ``dyn``. Doesn't the whole neatness of the type system just blow up? Surprisingly not!

The big caveat of Rust being useful widely is of course the wide range of dedicated libraries running unsafe code under the hood for our safe benefits. But I think this also speaks to Rust's qualities, the fact that it has convinced so many talented people to spend their time and effort into creating so much for the ecosystem.

Indeed, Rust is so useful, that we are starting to see efforts to verify its entire standard library. Many people are accepting Rust as a new de-facto standard.


## Statement of underqualification
I know I'm late (I think peak Rust discourse was 3 years ago) and that there will be smarter people than me disagreeing with me. Please don't take this as some sort of tech manifesto, but rather as an emotional timestamp. I'm very excited about Rust and I think it's sort of wonderful that Rust has survived its novelness period turning into stone-cold realism. Rust is elegant and useful. The fact that this is possible is very nice.