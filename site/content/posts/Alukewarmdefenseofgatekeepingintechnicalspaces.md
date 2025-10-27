---
title: A lukewarm defense of gatekeeping in technical spaces
date: 2025-10-27
draft: false
tags:
  - technology
  - commentary
  - coding
---
Clickbait title: That one YouTuber who keeps copying from ChatGPT and watching tutorial videos instead of just reading the Arch wiki.

This is a discussion mainly informed by online coding forums, communities and open-source projects. The author is not a prolific contributor.

I think the stereotype of the elitist tech user does not even need to be mentioned at this point. They think they're better than you or are at least projecting that online. It's no fun interacting with them. I am not going to defend this behaviour, but I will try to motivate the reasoning behind it.

## Knowledge repositories
If you spend any time in beginner programming forums, you will see StackOverflow praised as a resource, but the users lamented as arrogant. "Closed as duplicate" is a very common joke. (This trend is probably decreasing as new users are now better served by text chats with linear algebra.)

What I do find interesting is that many of these users seem to never consider why StackOverflow is such a good resource when looking stuff up on Google. If you have contributed to StackOverflow, you will very quickly find that the site is not for answering questions, it's for creating a QnA resource. 

Those are two very different goals. "Closed as duplicate" makes no sense for the original question asker, who would've probably just waited for someone bored at their job to solve their specific problem for them. It makes a lot of sense for creating **the answer** for a common problem, as all community resources can be focused into a single thread.

This means that information on StackOverflow tends to also be organised around the deeper semantics around a problem, not the wording of an error message. Consider [the problem of "Help my code said segfault"](https://meta.stackoverflow.com/questions/397168/segmentation-fault-code-dumped-to-stack-overflow) posts.

> It appears that people either do not know how to debug or just don't want to; and just dump whatever code that is segfaulting onto Stack Overflow.

Now I don't want to imply that the people of StackExchange are so high-minded geniuses who should be paid for their time (they tend to browse the forum whilst already on payroll), but even assuming their labour is completely free and altruistic, allowing thousands of segfault questions to populate Google search results with different fixes would confuse so many new users.

The solution? Downvotes, removing posts, marking as duplicate, karma system that gates those powers etc. If StackOverflow ever had a good implementation of that is another question (I find my karma to be wholly undeserved).

## Here's the script that can destroy your computer
Here's another question, is it responsible to tell tech-naive users what program to run so they can reformat their hard-drive? What about putting them in very close vicinity of that program? 

Looking at the basic linux installation instructions, after getting your ISO on your usb-drive and booting into it, installers tend to ask you where you want to install the new linux you just downloaded. One of the devices it will show you will delete all of your data from Windows.

Is it responsible to give that to new users? Well, they had to at least figure out how to boot from a USB-drive, so maybe that's alright? What if they followed a super-helpful YouTube tutorial that holds their hand through every step? How many of the viewers of such a YouTube video will actually respect the plea to camera to back up their data? How many more views could the creator get if they remove the annoying backup part everyone skips over?

This is of course a constant debate in Linux forums, probably best exemplified by "Is ``archinstall`` good for the arch ecosystem" (I used it for my arch installations). At this point if a tech YouTuber tries out Linux, it's a 50/50 about if they're gonna somehow fail catastrophically because they blindly followed a forum post.

So the fundamental question becomes, at what point are you endangering new users by helping them to achieve their own stated goals? Is it your responsibility to care? In my opinion it is. New users simply do not have the conception of all the ways something like this can go wrong, but a cautious approach can teach them the basics before putting them into danger. Plus, I like people, I think they don't deserve all their photos to be deleted.


## This is not for me, and I'm gonna complain
Quick question, if a program does not work, where do you search for help? If you wrote "Googling the program", then you may be very wrong. The program may work perfectly, you just installed it wrong. I'd say experienced Linux users tend to be quite good at this, looking at what version they're running and debugging the package manager's install instructions. Windows users? :)

Now, again, I am harping on newbies here, because in some sense they are the problem. But they are not a problem to be solved by being complained about. They are the default assumption and if we want adoption of great programs to grow, we need to accommodate them. This includes packaging working software for them. 

I am not going to rehash any upstream/downstream packaging drama, but the general playbook tends to be something like this: 
- Someone makes a program
- Someone else packages it for a specific package manager
- After some time, the packaged version has problems not reflected in the original version
- Frustrated users blame the original authors (who did nothing wrong but make their code available!), creating extra moderation work 

The proposed solution tends to be, to then make the program unavailable, i.e. stopping the packaging on that system. But you know what? New users can be relentless in getting what they want. I think no experience in writing software and decades of frustration via proprietary software has eroded all empathy in these situations.

We all know the infamous post about someone complaining that there is no ``.exe`` available of a certain program hosted on Github. I've seen this frustration in several situations, most recently with the AI hype, everyone wants a locally running setup, the same way they saw on YouTube. And they will complain if there's a Github link, because they have probably already tried to find their way around Github a few times and there wasn't a download link for an .exe! And when they typed the python command from the Readme in the console, Windows tells them unrecognised command.

Now I think that the best reason for not giving these people what they want is that you don't have to. They are entitled. Not their fault, the always-free software economy taught them this behaviour.

But I do think there are a few other good reasons, I've already discussed the fact that the software can endanger them and their data. But it can also endanger others, depends on the software. It can also just bring a lot of people into a tightly-knit community who will have disproportionately many problems with the program and will take up a lot of social energy. Communities have absolutely died from this, core maintainers have quietly or loudly quit. So sometimes I think it's good to have a Readme file that is written for an advanced audience in mind.

This is probably just a sign I should read ["Working in Public"](https://press.stripe.com/working-in-public)finally.


## The AI of it all
I've seen AI be described as very empowering for people. This is a great narrative if you're selling AI. It allows you to do things that were too hard before!

The AI companies are trying more or less to put safety stuff in their models. [I am not an expert in how well they are doing](https://arxiv.org/abs/2501.17805). I will trust them to have their safety concerns aligned with the safety of their business and maybe even their users. But how much do they care about open-source maintainers being flooded by bullshit? [Probably not much](https://gist.github.com/bagder/07f7581f6e3d78ef37dfbfc81fd1d1cd).

I think there's a good danger with AI helping people "start using" software, they don't understand. And if it's not working, who are they going to blame?