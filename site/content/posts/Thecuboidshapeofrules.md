---
title: The cuboid shape of rules
date: 2025-10-21
draft: false
tags:
  - commentary
---
Clickbait title: Death by a thousand cuts exists for a reason.

Before I can make my argument, I will need to warn of the dangerous confluence of geometry and anecdotal evidence underlying this. 

In normal words: I've noticed, that... and it reminds me of...
# Rules
Compared to informal friendgroups, as soon as one creates some sort of formal setting, often for people who are strangers to each other, one defines some rules. Why have rules? For many reasons of course. Mainly as a way to create shared understanding of what the goal of the group is.

Now the initial instinct is to write these rules in a format as follows:
- You should not do A
- You should do B unless C
- You should do D when E happens

How are we supposed to interpret this? Well surely all of these rules are in effect at the same time, so we can rephrase it as

> You should not do A and You should only do B up to x and You should do C when D happens

If you care for formulas (and I do):
$$A \land ((\neg C \rightarrow B) \land (C \rightarrow \neg B)) \land D \rightarrow E$$
Don't worry about the exact values, but rather look at the entire formula: It's a conjunction of several values, AND AND AND AND AND.

So what's the problem with that? It tends to not be the shape of our feelings.

# Rule Shapes
Let's enrich our rules a bit further with the concept of numbers. We have numbers in rules in real life all the time.

- You should do a up to X
- You should keep b between Y and Z
- c must be higher than W

And of course, our logical formula would look like this
$$a < X \land Y < b < Z \land c > W$$
Exercise for the reader: What is the shape of this in 3d space of (a, b, c)?

Answer for the reader: it's a cuboid, an infinite one in this case, but it is very rectangular shaped. The crux here is that any set of rules that define intervals like this *independently* from each other will have this cuboid shape.

# Ruling the border of rules
Now let's talk about sharing sweets between children. Let's have some **A**pples, **B**rownies and **C**ookies. As responsible parents we want to encourage eating Apples but probably keep Brownies and Cookies limited. Let's use our rule list!

Maybe we say
- You have to eat at least one apple
- You cannot have more than 2 brownies
- You cannot have more than 3 cookies

This is a cuboid of course! 
$$a \geq 0 \land b \leq 2 \land c \leq 3$$

Now we all know some rationalist enterprising children. They will of course maximise sweets and minimise fruits. So the solution for the greedy child is clear: Get exactly one apple, 2 brownies and 3 cookies. The solution is at the border of the cuboid. *(This is funnily enough similar to how L1 norm enforces sparsity in some machine learning models)*

Why is this bad? Well our cold-hearted children are pushing the border of what is acceptable in our rule system. We tend to set up rule systems to set the absolutely maximum acceptable thing but hope that nobody even shows up to the borders. A bad solution is to simply make the rules stricter:

- You have to eat at least two apples (healthier!)
- You cannot have more than 1 brownie (less sugar!)
- You cannot have more than 1 cookie (less sugar!)

Finally we have all our children eating healthily. But we may have some very sad child who does not like brownies. Should they not be allowed to have a second cookie? Everyone else got two things. No, says the conjunctive formula of independent rules.


## Solutions for the impatient
You can arrive at these solutions relatively trivially, if you either know children or have taken a course on Machine Learning: We need a better way to define our shapes of accepted behaviors!

Here's a list, raise your hand when you know them
- summing them up (have in total 2 cookies/brownies)
- squared distance (we draw a sphere instead of a cuboid)
- consequences (you can have 1 brownie for every apple you eat)
- non-convexity (you cannot have a cookie unless you worked really hard today)


# Free lunches is not more than zero
My point is not the solutions are hard, but rather that when we define rules in general, especially when by committee we tend to hold ourselves to the list of rules that are only rarely interlinked. 

This makes a lot of social sense. It draws a bunch of really nice borders you can show people stepped over. Any convoluted formula may require a convoluted explanation of a rulebreak and more competent enforcers. Nobody likes being in a community where the rules are nebulous. Plus how do you even calculate with social concepts like harassment/insults.

There is perhaps a simple appeal to be made here, that just a few steps to make our rules more dependent on each other can make them reflect our feelings better.

There is a more controversial appeal hiding in this as well. We can forego the definition of strict rules in general. This is indeed what many social groups already implicitly or explicitly do. "Don't be mean" and "Death by a thousand cuts" are intentionally vague to not fall in the same trap where people trying to exploit the goodwill flexibility of rules to live at the border of what is acceptable.

# Social Dynamics
Now, this essay is not one meant to be actionable. Especially it should not be one that tells you that you should burn your rule documents and just let your forum moderators "ban everyone who is being mean". This approach tends to attract the wrong kind of people and does not scale well.

If there is anything I would like you to take away from this is that you notice when someone is living in the corner of your cuboid rules.