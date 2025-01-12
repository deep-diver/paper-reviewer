---
title: {{ paper_title }}
summary: {{ paper_summary }}
categories: []
tags: [{% if category %}"{{ category }}",{% endif %} {% if sub_category %}"{{ sub_category }}",{% endif %} {% if affiliation %}"🏢 {{ affiliation }}",{% endif %}]
showSummary: true
date: {{ publish_date }}
draft: false
---

<br>

{% raw %}{{< keywordList >}}{% endraw %}
{% raw %}{{< keyword icon="fingerprint" >}}{% endraw %} {{ arxiv_id }} {% raw %}{{< /keyword >}}{% endraw %}
{% raw %}{{< keyword icon="writer" >}}{% endraw %} {{ author }} {% raw %}{{< /keyword >}}{% endraw %}
{% if hf_daily_papers_date_tag %} 
{% raw %}{{< keyword >}}{% endraw %} 🤗 {{ hf_daily_papers_date_tag }} {% raw %}{{< /keyword >}}{% endraw %}
{% endif %} 
{% raw %}{{< /keywordList >}}{% endraw %}

{% raw %}{{< button{% endraw %} href="{{ arxiv_url }}"{% raw %} target="_self" >}}{% endraw %}
{% raw %}↗ OpenReview{% endraw %}
{% raw %}{{< /button >}}{% endraw %}
{% raw %}{{< button{% endraw %} href="{{ neurips_link }}"{% raw %} target="_self" >}}{% endraw %}
{% raw %}↗ NeurIPS Homepage{% endraw %}
{% raw %}{{< /button >}}{% endraw %}

{% if podcast %}
<audio controls>
    <source src="{{ podcast }}" type="audio/wav">
    Your browser does not support the audio element.
</audio>
{% endif %}

### TL;DR

{% raw %}
{{< lead >}}
{% endraw %}
{{ tldr }}
{% raw %}
{{< /lead >}}
{% endraw %}

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

#### Why does it matter?
{{ reason_why_matter }}

------
#### Visual Insights

{% if first_figure %}

![]({{ first_figure.figure_path }})

> {{ first_figure.description }}

{% endif %}

{% if first_table %}

![]({{ first_table.figure_path }})

> {{ first_table.description }}

{% endif %}

{% if other_figures|length > 1 or other_tables|length > 1 %}

### In-depth insights

{% for section in sections %}
#### {{ section.heading_title }}
{{ section.details.summary }}
{% endfor %}

### More visual insights
{% if other_figures|length > 1 %}
{% raw %}<details>{% endraw %}
{% raw %}<summary>More on figures{% endraw %}
{% raw %}</summary>{% endraw %}

{% for figure in other_figures %}
![]({{ figure.figure_path }})

> {{ figure.description }}

{% endfor %}
{% raw %}</details>{% endraw %}
{% endif %}

{% if other_tables|length > 1 %}

{% raw %}<details>{% endraw %}
{% raw %}<summary>More on tables{% endraw %}
{% raw %}</summary>{% endraw %}

{% for table in other_tables %}
![]({{ table.figure_path }})
> {{ table.description }}
{% endfor %}
{% raw %}</details>{% endraw %}
{% endif %}

{% endif %}

### Full paper

{% raw %}{{< gallery >}}{% endraw %}{% for paper_img in paper_imgs %}
{% raw %}<img {% endraw %}src="{{ paper_img }}" {% raw %}class="grid-w50 md:grid-w33 xl:grid-w25" />{% endraw %}{% endfor %}
{% raw %}{{< /gallery >}}{% endraw %}
