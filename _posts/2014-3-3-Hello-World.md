---
layout: post
title: You're up and running!
use_math: true
published: true
---

Next you can update your site name, avatar and other options using the _config.yml file in the root of your repository (shown below).

![_config.yml]({{ site.baseurl }}/images/config.png)

The easiest way to make your first post is to edit this one. Go into /_posts/ and update the Hello World markdown file. For more instructions head over to the [Jekyll Now repository](https://github.com/barryclark/jekyll-now) on GitHub.

Integrating MathJax with Jekyll is a very convenient way of typesetting mathematics in a blog hosted on github pages. There are a few guides online, which were (almost) helpful in acheiving this on a github hosted site. The steps, as of September 2016, are:

Ensure the markdown engine is set to `kramdown` in `_config.yml`. This is now the [only supported markdown processor](https://help.github.com/articles/updating-your-markdown-processor-to-kramdown/) on github pages, so this should be set anyway.

Include a new file in `_includes` named `_mathjax_support.html` (a clever idea from [here](http://haixing-hu.github.io/programming/2013/09/20/how-to-use-mathjax-in-jekyll-generated-github-pages/)):

```
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    TeX: {
      equationNumbers: {
        autoNumber: "AMS"
      }
    },
    tex2jax: {
    inlineMath: [ ['$', '$'] ],
    displayMath: [ ['$$', '$$'] ],
    processEscapes: true,
  }
});
MathJax.Hub.Register.MessageHook("Math Processing Error",function (message) {
	  alert("Math Processing Error: "+message[1]);
	});
MathJax.Hub.Register.MessageHook("TeX Jax - parse error",function (message) {
	  alert("Math Processing Error: "+message[1]);
	});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```
The bottom two hooks alert the user/writer about math and tex errors. 

Importantly, in contrast to older guides online, note the https in the MathJax CDN. Unencrypted access to the CDN is a security risk and now will either not render in some browsers (didn't work in Chrome for me), or will issue warnings in other browsers (Firefox). See the MathJax [documentation](http://docs.mathjax.org/en/latest/start.html#secure-access-to-the-cdn) for more information.

Next, include in the `<head>` of `_layouts/default.html`:
{% raw %}
```
{% if page.use_math %}
{% include mathjax_support.html %}
{% endif %}
```
{% endraw %}

Now to include $\LaTeX$ in a post you just need set the variable `use_math: true` in the YAML front-matter of the page/post! Enclose inline formulas in `$`s and display formulas in `$$`s. For instance,

{% raw %}
```
$$
K(a,b) = \int \mathcal{D}x(t) \exp(2\pi i S[x]/\hbar)
$$
```
produces:
{% endraw %}
<div>
$$
K(a,b) = \int \mathcal{D}x(t) \exp(2\pi i S[x]/\hbar)
$$
</div>

## Alignment

Note that any equations requiring alignment (use of ampersand &) need some care. The solution I found was to wrap any of these elements in <div>'s. 

## Changing typeset fontsize 

Add the following to `MathJax.Hub.Config`:

```
CommonHTML: {
  scale: 85
}
```
