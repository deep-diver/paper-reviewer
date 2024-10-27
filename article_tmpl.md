---
title: {{ paper_title }}
summary: {{ paper_summary }}
categories: ["AI Generated"]
tags: ["🔖 {{ publish_date[2:] }}", {% if hf_daily_papers_date_tag %}"🤗 {{ hf_daily_papers_date_tag[2:] }}"{% endif %}]
showSummary: true
date: {{ publish_date }}
draft: false
---

### TL;DR

{% raw %}
{{< lead >}}
{% endraw %}
{{ tldr }}
{% raw %}
{{< /lead >}}
{% endraw %}

{% raw %}{{< button{% endraw %} href="{{ arxiv_url }}"{% raw %} target="_self" >}}{% endraw %}
{% raw %}{{< icon "link" >}} &nbsp; read the paper on arXiv{% endraw %}
{% raw %}{{< /button >}}{% endraw %}

#### Why does it matter?
{{ reason_why_matter }}
#### Key Takeaways

{% raw %}{{< alert "star" >}}{% endraw %}
{% raw %}{{< typeit speed=10 lifeLike=true >}}{% endraw %} {{ takeaways[0] }} {% raw %}{{< /typeit >}}{% endraw %}
{% raw %}{{< /alert >}}{% endraw %}

{% raw %}{{< alert "star" >}}{% endraw %}
{% raw %}{{< typeit speed=10 startDelay=1000 lifeLike=true >}}{% endraw %} {{ takeaways[1] }} {% raw %}{{< /typeit >}}{% endraw %}
{% raw %}{{< /alert >}}{% endraw %}

{% raw %}{{< alert "star" >}}{% endraw %}
{% raw %}{{< typeit speed=10 startDelay=2000 lifeLike=true >}}{% endraw %} {{ takeaways[2] }} {% raw %}{{< /typeit >}}{% endraw %}
{% raw %}{{< /alert >}}{% endraw %}

------
#### Visual Insights

{% if first_figure %}

![]({{ first_figure.figure_path }} "🔼 {{ first_figure.caption }}")

> {{ first_figure.description }}

{% endif %}

{% if first_chart %}

![]({{ first_chart.figure_path }} "🔼 {{ first_chart.caption }}")

> {{ first_chart.description }}

{% endif %}

{% if first_table %}

{% raw %}{{< table-caption{% endraw %} caption="🔽 {{ first_table.caption }}"{% raw %} >}}{% endraw %}
{{ first_table.content }}{% raw %}{{< /table-caption >}}{% endraw %}

> {{ first_table.description }}

{% endif %}

### More visual insights
{% if other_figures|length > 1 %}
{% raw %}<details>{% endraw %}
{% raw %}<summary>More on figures{% endraw %}
{% raw %}</summary>{% endraw %}

{% for figure in other_figures %}
![]({{ figure.figure_path }} "🔼 {{ figure.caption }}")

> {{ figure.description }}

{% endfor %}
{% raw %}</details>{% endraw %}
{% endif %}
{% if other_charts|length > 1 %}

{% raw %}<details>{% endraw %}
{% raw %}<summary>More on charts{% endraw %}
{% raw %}</summary>{% endraw %}

{% for chart in other_charts %}
![]({{ chart.figure_path }} "🔼 {{ chart.caption }}")

> {{ chart.description }}

{% endfor %}
{% raw %}</details>{% endraw %}
{% endif %}
{% if other_tables|length > 1 %}

{% raw %}<details>{% endraw %}
{% raw %}<summary>More on tables{% endraw %}
{% raw %}</summary>{% endraw %}

{% for table in other_tables %}
{% raw %}{{< table-caption{% endraw %} caption="🔽 {{ table.caption }}"{% raw %} >}}{% endraw %}
{{ table.content }}{% raw %}{{< /table-caption >}}{% endraw %}

> {{ table.description }}

{% endfor %}
{% raw %}</details>{% endraw %}
{% endif %}

### Full paper

{% raw %}{{< gallery >}}{% endraw %}{% for paper_img in paper_imgs %}
{% raw %}<img {% endraw %}src="{{ paper_img }}" {% raw %}class="grid-w50 md:grid-w33 xl:grid-w25" />{% endraw %}{% endfor %}
{% raw %}{{< /gallery >}}{% endraw %}
