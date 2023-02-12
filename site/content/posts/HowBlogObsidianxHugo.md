---

title: "How Blog? - Obsidian x Hugo"

date: 2023-02-12

draft: false

  
tags: ["featured", "about the blog", "coding", "project"]
---
I will be going through the principal workings of how this blog works, in specific how I've tried to remove the barrier of creating and publishing new content as much as possible.

### Meet the protagonists

#### Hugo
In principle this entire blog runs on [Hugo](https://gohugo.io/) which is a framework to turn [Markdown](https://en.wikipedia.org/wiki/Markdown) files into static "blog-style" web pages. As such, Hugo's greatest feat is probably its functionality to render Markdown into very passable webpages, giving each Markdown syntax its HTML analogue.

Another triumph of Hugo is its modularity in themes. A given website layout is completely compartmentalized in its own folder and as such it is even possible to switch the entire website layout from one theme to another with only a config file edit. After spending a few idle minutes looking through Hugo themes, I fell in love with [m10c](https://github.com/vaga/hugo-theme-m10c) for its slightly non-traditional layout of prioritizing a sidebar over a header and the wonderful simplicity. Changing the green for a purple made it feel like home, even if my home is not made out of bisexual obsidian crystals.

I've had a dream of using tags for blog articles for a while now, even including it in a completely self-written prototype blog site (which is luckily now deleted). I was already expected needing to ham-fist this functionality into Hugo when I was positively surprised to find [Hugo's Taxonomies](https://gohugo.io/content-management/taxonomies/), which basically allowed for many-to-many relations out of the gate.


#### Obsidian
Having already mentioned the stone, I should probably mention the other main player in this blog: [Obsidian](https://obsidian.md/). This productivity tool was picked up as a small holiday distraction for myself, muttering to myself that it might be useful for university. Having been accustomed to a very paper-heavy education system and using LaTeX for everything else, I did not know how essential Obsidian would come to be for myself.

Markdown (and by extension Obsidian), in short, is LaTeX without needing to think. Now, by virtue of interacting in a university environment, I am aware that LaTeX is LaTeX without needing to think for many people. That being said, I have yet to coerce myself into using VIM and Linux and as such, I still like using my mouse sometimes.

By virtue of having full [MathJax ](https://www.mathjax.org/)support, Obsidian was ideal to solve any exercises in. Having been using it extensively for university assignments for 1.5 years now, it is very rare that I feel the need to ever turn to physical paper for any computations. Typing math has become easy and as such thinking math has as well.

Some subjects may require diagrams, and as such I am obligated to mention [Excalidraw's support for Obsidian](https://github.com/zsviczian/obsidian-excalidraw-plugin), making me never miss [TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) for one second. Obsidian's plugin support and "hackability" has been a blessing for anyone who cares to exploit it.


### A difficult marriage
One may notice that both Hugo and Obsidian both operate principally on Markdown files and as such are made for each other. And to extend the relationship metaphor: I'm sure they're good friends, but there's going to be effort to fully understand each other.

Obsidian has a wonderful native feature which exports any Markdown file to PDF of defensible quality. Notably, Markdown was never made to perfectly control output, but Obsidian can very much create output quality of a LaTeX novice (and no wrangling with minipages).
This feature is incredible, as long as your target is and always will be PDF. Which mine is not anymore, it is Markdown *again*, but this time Markdown legible by Hugo.

Obsidian expects to be used in a Vault, which is their fancy name for a working folder. Specifically, all Markdown you write relies on always staying in that vault and only existing in the exported PDF format. Any images (including Excalidraw drawings) embedded into Markdown are saved in the Vault as well and if one wants to move the markdown file out of the vault, all embedded files have to go with it.

Even worse: Excalidraw drawings are not images. They are cryptic markdown files only understood by Excalidraw itself and people with more time than me. If I want to export them, I will need to turn them into images first.

#### Bodging
I remember watching [The Art of the Bodge](https://youtu.be/lIFE7h3m40U) by Tom Scott half a decade ago, being then and admittedly still now infatuated with it. In it, Tom mentions [AutoHotkey](https://www.autohotkey.com/) as his tool of choice for cobbling together interactions between different programs. Specifically, AutoHotkey tends to excel at simulating mouse and keyboard input. I'm glad I didn't need to do that.

Obsidian's plug-in support for casual users is wonderful, but for programmers? It is paradise on earth. Specifically I want to highlight two plugins here: [Templater](https://github.com/SilentVoid13/Templater) and [Excalidraw Automate](https://zsviczian.github.io/obsidian-excalidraw-plugin/API/attributes_functions_overview.html) the latter being already included in Excalidraw. Most Templater script tutorials online will happily tell you how powerful Templater is at writing the current date in a file or repeating the title. But Templater has the entire industrious strength of JavaScript running on Electron behind it.

As such, I was able to write a script which searches all occurrences of Excalidraw embeds in a given file:
```js
let content = tp.file.content;
let re = /!\[\[(([\w\d\s\.-]*)\.excalidraw)\]\]/g;
let matches = [...content.matchAll(re)];
```
and export the given Excalidraw files as PNGs
```js
for (m of matches) {
	let fullname = m[1];
	let head = m[2];
	let f = await ea.createPNG("Excalidraw/" + fullname, 2);
	
	var fileReader = new FileReader();
	fileReader.onload = function() {
	  fs.writeFileSync(app.vault.adapter.basePath + "/Files/" + head + ".png", Buffer.from(new Uint8Array(this.result)));
	};
	fileReader.readAsArrayBuffer(f);
}
```
For anyone trying this yourself, the entire Templater file is found [here](https://github.com/chluebi/website/blob/main/blog/templater/export_no_git.md).

What remains now is to pre-process the given markdown file, including adjusting all the Obsidian style links to Markdown links and moving the file over. This can and will easily be done by calling a seperate python script, but as mentioned, I want to remove most barriers to posting content for myself and such running a separate file is undesirable. As such, we can turn to Templater's last ace up its sleeve: [System Commands](https://silentvoid13.github.io/Templater/user-functions/system-user-functions.html).

As such, with a bit of editing of Obsidian configurations (or using the UI), one is able to create hooks in the JavaScript to run arbitrary system commands, including Python code.

Python has been my language of choice ever since I went really into programming. As such, it is very natural for me to use it for any project where I'm the only person who needs to run the code. The actual essence of the python scripts is nothing but a few file edits, moving some media files into the corresponding Hugo folder structure and some system commands. Notably, these system commands are mainly Git Version Control which pushes the newly created article online. In the end, we have to host them after all.


### Hosting
Hugo is wonderfully compatible with many cloud services which will host your static website for you, and I hate it. Not the mandatory fees of most services, mind you. I still pay those, just to host my own server. It is just that a fully-managed service, as extensive as it may be, will never compare to the freedom of hosting your own service. Naturally this comes with its own problems like DNS which I will obligatorily mention, but not focus on. Namely, the final core pieces are the file server and how to control it easily.

[Nginx](https://www.nginx.com/) probably remains the easiest solution for any enthusiast-level hosting and proxying needs. Namely, this abridged site config file in my ``sites-available`` folder is responsible for serving any files.

```conf
server {
	server_name chluebi.com;
	root /home/Projects/website/site/public;
	error_page 404 /404.html;
	
	location / {
		   root /home/Projects/website/site/public;
	}
	
	
	location = /404.html {
			internal;
	}
	
	listen [::]:443 ssl ipv6only=on; # managed by Certbot
	listen 443 ssl; # managed by Certbot
	
	# More Certbot stuff below
}
```

People who know nginx may notice that this means this is a purely static site.
This is intentional for a few reasons, mainly computing and simplicity. As such, unless the underlying files in the public folder change, the site does not change.

Notably, though, nginx is not limited to serving static files.
```conf
location /project {
	proxy_pass http://localhost:1313/;
}
```
Adding this to my server block, allows me to serve whatever content I want locally on my server on port 1313 and have it be accessible via ``chluebi.com/project``. One domain for several different processes, a so-called [reverse-proxy](https://en.wikipedia.org/wiki/Reverse_proxy) the functionality of which is [built into nginx](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/).

The underlying problem of having the main blog be a static site still remains. It will not change unless acted upon by an unbalanced command. As such, I will need to communicate to my server in some way or another. I have been prompted by others to potentially use [Django](https://www.djangoproject.com/), a very popular and bulky python web server with a built-in admin panel. Django is certainly a solution to many problems, but it is not a solution in a project where I desire to retain maximum control over everything executed (within reason).

As such, one of the easiest connections from anything to me is through my phone, and there are several messaging services which I use on both phone and computer. The natural choice was Discord, as I am very intimate with the Bot API and the corresponding [discord.py](https://discordpy.readthedocs.io) library. As such, my fate was sealed: I was to make a Discord Bot to control trivial server functions.

Currently, the only function of those is refreshing the server.
```python
@commands.check(util.is_owner)
@admin.group(name='reload')
async def place_start(self, ctx):
	os.system('git pull')
	os.system('rm -rf site/public')
	os.system('cd site && hugo')
	await util.send_embed(ctx, util.success_embed(ctx, f'Reloaded Site.'))
```
As this is not a tutorial, I will not be elaborating on the exact nature of e.g., my ``util`` module, but I invite you to inspect [my source code](https://github.com/chluebi/website). As such, I can easily prompt the server to reload the blog part of the site via a simple text message.


### Conclusion
My current setup allows me to add a new article to my blog via a single Templater script accessible through Obsidian and then send a message from anywhere to have the website carry the new article. Updating and removing articles works similarly. I did all this whilst still retaining reasonably maximal control over every process of the [data pipeline](https://xkcd.com/2054/).

Making a blog is so easy, there are entire industries which do it for you. Making one's own blog is easy as well, but it is more pure effort and willpower to bend existing programs and libraries to one's own creative will. The end result looks passable, maybe even good if I were better at design. It would probably look better on Medium or Tumblr and would get a lot more engagement. But it would be an account, not a website.