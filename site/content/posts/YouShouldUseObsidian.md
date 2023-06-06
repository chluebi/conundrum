---

title: "You Should Use Obsidian"

date: 2023-02-21

draft: false

  
tags: ["featured", "productivity"]
---
Blatant Obsidian Propaganda.

##### Updates
2023-06-06: Fixed mistakenly saying that Obsidian by itself is open-source, sadly it is not. Additionally, updated the negative point about the Obsidian PDF viewer because it's actually good now.


### What is Obsidian? Why is it so Great?
Obsidian is an open-source friendly (but sadly by itself closed-source) "hackable" Markdown editor, endlessly expendable with plugins. It could be called a dedicated IDE for note-taking, writing and solving exercises. As an IDE, if configured correctly, it becomes an all-in-one solution for tons of usage cases: Being a student, creative writing or even typesetting. It can be used in pure source editing mode, but I find myself using Live Preview (WYSIWYG) mode more often than not.

The whole thing operates on the [Markdown](https://en.wikipedia.org/wiki/Markdown) format, which, although it comes with some limitations, has some immense strengths: Clean PDF output, intuitive syntax and easily expendable. As a STEM student, I am most delighted by its support for LaTeX Math mode, to the point that it basically works exactly like TeX. Importantly though, Markdown is a much less restrained format than LaTeX, which directly leads to great simplicity compared to using LaTeX. No overfull hboxes or minipage pain here.


### How to best reap the benefits of Obsidian

#### Everything in one place
Baseline Obsidian is a perfectly adequate tool for a lot of jobs. I'd say it is by far the best one-off markdown editor out there, despite its chunkiness for one-off editing. But the true power of Obsidian comes from the fact that it wants to be your main hub for studying/writing. Namely, Obsidian always operates on a root folder, a so-called "vault". This functions very similar to a project folder in IDEs. As such, Obsidian wants you to have your notes and attachments (like images) in one place. This is obviously objectively a limitation, but it can also be a benefit: Obsidian tends to force good organization unto you.

#### Everything is linked
One thing you will quickly notice is the ease with which you can insert images into Markdown files in Obsidian. Coming from other applications, one may suspect that the image is somehow embedded in the document. It is not, it is purely *linked*. More importantly, this linking is a core functionality of Obsidian and makes organization of complex thought processes easy. Even files in completely different folders can be linked from other files, and a single click on the link changes your view to that new file. Say you want to organize a list of 100 complicated technical words as to better study and access them. You may put all of them into a single alphabetical list. Or you give them each a different Markdown file and whenever they are related you link them to each other. Most wonderfully, Obsidian's "Graph View" visualizes the entire network of links for you!

#### Plugins for everything else
It is predictable that an open-source application used by a lot of programmers has plugins. But it might be a bit of a shock how incredibly powerful these plugins are:
- **Excalidraw** is the answer to the lack of drawing/sketching functionality in Obsidian. It is wonderfully simple to draw in and incredibly powerful, including insertion of entire LaTeX math formulas! It is beautifully integrated into Obsidian, with Excalidraw Drawings being easily inserted in Markdown files and editable all the way throughout.
- **Pandoc** deals with any nasty document conversion.
- **Latex suite** comes with very powerful math snippets which you can append and edit.
- **LanguageTool Integration** brings a very customizable spellcheck.
- ...

#### Become god
Notably, in the previous section, I did not mention my probably favorite plugin **Templater**. In basic use, it allows you to make some very nice templates for snippets to insert into your documents. Notably, these snippets can also have dynamic content like, e.g., the title of the document they're inserted into or the current date. And then one might notice: Templates let you just straight up write JavaScript, and many other plugins have Templater Integration!

In practice this means that without even writing your own plugins, you can automate entire productivity steps like e.g., moving files around, inserting text or even drawing things. I invite you to look through the [Excalidraw Automate How-To](https://zsviczian.github.io/obsidian-excalidraw-plugin/) to see how intricate this can get. Templater can even be configured to run system commands, at which point the floodgates are opened for whatever bash/python/etc. script you can write.


### Obsidian isn't perfect 
Being so focused on Markdown, Obsidian inherits the limitations of Markdown in its output, namely the limits on your influence on the output formatting. If you are prolific in LaTeX, you will miss a lot of control. In general, a lot of people who are high in the "tech-y" scale will probably scoff at Obsidian for many reasons. Basically, the types of people who will be turned off from Obsidian due to the fact that it's Electron, will probably be right in not wanting to use it.

Obsidian is a good main hub for all your needs, but it is not good at *everything*. For the love of god, do not use Obsidian to write any code, except for Templater JavaScript. Additionally, special formats may require specialized editors or viewers. That being said, with the newest updates, the Obsidian PDF viewer is now wonderful.

### Conclusion
Obsidian is a wonderful little application and I hope to have convinced you to give it a try.

Time to go https://obsidian.md/ and try it out yourself!


In case you want some inspiration, you might be interest to know that [all articles in this blog are written in Obsidian](https://chluebi.com/posts/howblogobsidianxhugo/).