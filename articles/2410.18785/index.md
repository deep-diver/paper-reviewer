---
title: "Should We Really Edit Language Models? On the Evaluation of Edited Language Models"
summary: "Current LLM editing methods are great for small updates, but scaling them negatively impacts performance and safety."
categories: ["AI Generated"]
tags: ["🔖 24-10-24", "🤗 24-10-25"]
showSummary: true
date: 2024-10-24
draft: false
---

### TL;DR


{{< lead >}}

This paper examines the effectiveness and safety of model editing techniques for Large Language Models (LLMs).  Researchers used various editing methods on different LLMs, assessing their performance across multiple benchmarks. They found that while model editing is useful for small updates, it causes performance deterioration and safety issues as the number of edits increases. Instruction-tuned models proved more robust, while larger models showed better resistance. The study highlights that existing methods are unsuitable for large-scale knowledge updates and stresses the need for improved, safer editing techniques.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18785" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This research paper investigates the impact of model editing techniques on the general capabilities and safety of Large Language Models (LLMs).  The authors perform a comprehensive evaluation of various editing methods and find that current methods, while effective for small-scale knowledge updates, significantly impair LLM performance and safety when applied at larger scales.  This challenges the prevailing assumption that model editing is a safe and efficient method for updating LLMs.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} Model editing degrades LLM performance on general benchmarks, especially with many edits. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Instruction-tuned LLMs are more robust to editing than base models. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} Edited models, even safety-aligned ones, exhibit significantly reduced safety. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: Illustration about the model editing and its pitfalls in retaining edited knowledge. Left panel: model editing methods can efficiently update knowledge within language models; Right panel: when scaling editing to thousands, the model can't retain edited knowledge, see [16] for details.")

> The figure illustrates the effectiveness of model editing methods in updating knowledge within language models and their limitations when scaling to a large number of edits.





![](charts/charts_5_0.png "🔼 Figure 2: Performance trends of evaluating edited Llama2-7B base model across different benchmarks using six editing methods. Results reveal that PMET and MEND can effectively preserve the model's abilities across all tasks. While KN drastically drops even less than ten edits.")

> The chart displays the performance trends of six different model editing methods on Llama2-7B base model across five different benchmark tasks, showing that PMET and MEND are more robust to editing than others.





{{< table-caption caption="🔽 Table 1: Evaluation results of GPT2-XL. experiments are conducted on a sever with 8 RTX 4090 GPUs." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="3">Method w/o Edit</td><td rowspan="2"># Edits</td><td colspan="4">GPT2-XL</td></tr><tr><td>MMLU</td><td>GSM8K</td><td>BBH</td><td>CSQA</td></tr><tr><td>0</td><td>0.2098</td><td>0.0144</td><td>0.0382</td><td>0.1941</td></tr><tr><td rowspan="6">PMET</td><td>10</td><td>0.2104</td><td>0.0159</td><td>0.0377</td><td>0.1941</td></tr><tr><td>20</td><td>0.1081</td><td>0.0144</td><td>0.0117</td><td>0.2048</td></tr><tr><td>50</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>500</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1000</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="5">MEND</td><td>10</td><td>0.2096</td><td>0.0144</td><td>0.0377</td><td>0.1949</td></tr><tr><td>30</td><td>0.2094</td><td>0.0152</td><td>0.0388</td><td>0.1941</td></tr><tr><td>100</td><td>0.2098</td><td>0.0144</td><td>0.0380</td><td>0.1957</td></tr><tr><td>500</td><td>0.2100</td><td>0.0144</td><td>0.0382</td><td>0.1941</td></tr><tr><td>1000</td><td>0.2099</td><td>0.0144</td><td>0.0381</td><td>0.1933</td></tr><tr><td rowspan="2">KN</td><td>500</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1000</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="2">MEMIT</td><td>500</td><td>0.2112</td><td>0.0159</td><td>0.0363</td><td>0.1957</td></tr><tr><td>1000</td><td>0.2097</td><td>0.0152</td><td>0.0193</td><td>0.199</td></tr></table>{{< /table-caption >}}

> Table 1 presents the evaluation results of GPT2-XL model with different editing methods and various numbers of edits on MMLU, GSM8K, BBH, and CSQA benchmarks.



### More visual insights



<details>
<summary>More on charts
</summary>


![](charts/charts_6_0.png "🔼 Figure 2: Performance trends of evaluating edited Llama2-7B base model across different benchmarks using six editing methods. Results reveal that PMET and MEND can effectively preserve the model's abilities across all tasks. While KN drastically drops even less than ten edits.")

> The chart displays the performance trends of six different model editing methods on the Llama2-7B base model across multiple benchmarks, showing that PMET and MEND effectively preserve model abilities, while KN shows a drastic drop in performance with fewer than ten edits.


![](charts/charts_6_1.png "🔼 Figure 2: Performance trends of evaluating edited Llama2-7B base model across different benchmarks using six editing methods. Results reveal that PMET and MEND can effectively preserve the model's abilities across all tasks. While KN drastically drops even less than ten edits.")

> The chart displays the performance trends of six different model editing methods on Llama2-7B across multiple benchmarks, showing that PMET and MEND maintain model abilities better than other methods, while KN shows significant performance decline.


![](charts/charts_7_0.png "🔼 Figure 2: Performance trends of evaluating edited Llama2-7B base model across different benchmarks using six editing methods. Results reveal that PMET and MEND can effectively preserve the model’s abilities across all tasks. While KN drastically drops even less than ten edits.")

> The chart displays performance trends of six different model editing methods on the Llama2-7B base model across multiple benchmarks, showing that PMET and MEND effectively preserve model abilities while KN's performance drastically declines.


![](charts/charts_8_0.png "🔼 Figure 2: Performance trends of evaluating edited Llama2-7B base model across different benchmarks using six editing methods. Results reveal that PMET and MEND can effectively preserve the model's abilities across all tasks. While KN drastically drops even less than ten edits.")

> The chart displays the performance trends of six different model editing methods on the Llama2-7B base model across various benchmarks, showing that PMET and MEND effectively preserve model abilities while KN shows a drastic performance drop.


![](charts/charts_21_0.png "🔼 Figure 2: Performance trends of evaluating edited Llama2-7B base model across different benchmarks using six editing methods. Results reveal that PMET and MEND can effectively preserve the model's abilities across all tasks. While KN drastically drops even less than ten edits.")

> The chart displays the performance trends of six different model editing methods on Llama2-7B across five benchmark tasks, revealing that PMET and MEND effectively preserve model abilities, while KN shows a sharp decline with fewer than ten edits.


![](charts/charts_21_1.png "🔼 Figure 2: Performance trends of evaluating edited Llama2-7B base model across different benchmarks using six editing methods. Results reveal that PMET and MEND can effectively preserve the model's abilities across all tasks. While KN drastically drops even less than ten edits.")

> The chart displays the performance trends of six different model editing methods on the Llama2-7B base model across various benchmark tasks, revealing that PMET and MEND preserve model abilities while KN shows significant degradation with fewer than ten edits.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Results on evaluating the impact of different editing methods and numbers of edits on edited language models (base model). All editing is conducted on COUNTERFACT dataset with a fixed seed for a fair comparison. For all 4 tasks in this table, the higher score indicates a better performance. MEND and GRACE are not available for Mistral-7B." >}}
<table id='0' style='font-size:14px'><tr><td>Model</td><td>Method</td><td># Edits</td><td>MMLU↑</td><td>GSM8K↑</td><td>BBH↑</td><td>CSQA↑</td></tr><tr><td rowspan="7">Pythia-160M</td><td>w/o Edit</td><td>0</td><td>0.2435</td><td>0.0174</td><td>0.0742</td><td>0.1884</td></tr><tr><td rowspan="3">ROME</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>50</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">MEMIT</td><td>10</td><td>0.2460</td><td>0.0212</td><td>0.0785</td><td>0.2056</td></tr><tr><td>50</td><td>0.2447</td><td>0.0227</td><td>0.0755</td><td>0.1982</td></tr><tr><td>100</td><td>0.2468</td><td>0.0235</td><td>0.0743</td><td>0.1990</td></tr><tr><td rowspan="7">Pythia-410M</td><td>w/o Edit</td><td>0</td><td>0.2614</td><td>0.0144</td><td>0.2497</td><td>0.2064</td></tr><tr><td rowspan="3">ROME</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>50</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">MEMIT</td><td>10</td><td>0.2628</td><td>0.0182</td><td>0.2476</td><td>0.2015</td></tr><tr><td>50</td><td>0.2629</td><td>0.0144</td><td>0.2482</td><td>0.2080</td></tr><tr><td>100</td><td>0.2627</td><td>0.0190</td><td>0.2490</td><td>0.2048</td></tr><tr><td rowspan="7">Pythia-1B</td><td>w/o Edit</td><td>0</td><td>0.2552</td><td>0.0273</td><td>0.2535</td><td>0.1892</td></tr><tr><td rowspan="3">ROME</td><td>10</td><td>0.2547</td><td>0.0083</td><td>0.0052</td><td>0.2039</td></tr><tr><td>50</td><td>0.0017</td><td>0</td><td>0</td><td>0</td></tr><tr><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">MEMIT</td><td>10</td><td>0.2562</td><td>0.0265</td><td>0.2545</td><td>0.1908</td></tr><tr><td>50</td><td>0.2539</td><td>0.0265</td><td>0.2544</td><td>0.2015</td></tr><tr><td>100</td><td>0.2547</td><td>0.0258</td><td>0.2532</td><td>0.2064</td></tr><tr><td rowspan="7">Pythia-2.8B</td><td>w/o Edit</td><td>0</td><td>0.2800</td><td>0.0364</td><td>0.2870</td><td>0.2146</td></tr><tr><td rowspan="3">ROME</td><td>10</td><td>0.2272</td><td>0.0008</td><td>0.0004</td><td>0.1990</td></tr><tr><td>50</td><td>0.0001</td><td>0.0191</td><td>0</td><td>0</td></tr><tr><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">MEMIT</td><td>10</td><td>0.2547</td><td>0.0303</td><td>0.2774</td><td>0.2154</td></tr><tr><td>50</td><td>0.2554</td><td>0.0349</td><td>0.2758</td><td>0.2269</td></tr><tr><td>100</td><td>0.2559</td><td>0.0318</td><td>0.2749</td><td>0.2179</td></tr><tr><td rowspan="14">Pythia-6.9B Pythia-12B</td><td>w/o Edit</td><td>0</td><td>0.2565</td><td>0.0318</td><td>0.2762</td><td>0.2260</td></tr><tr><td rowspan="3">ROME</td><td>10</td><td>0.0189</td><td>0</td><td>0</td><td>0</td></tr><tr><td>50</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">MEMIT</td><td>10</td><td>0.2547</td><td>0.0303</td><td>0.2774</td><td>0.2154</td></tr><tr><td>50</td><td>0.2554</td><td>0.0349</td><td>0.2758</td><td>0.2269</td></tr><tr><td>100</td><td>0.2559</td><td>0.0318</td><td>0.2749</td><td>0.2179</td></tr><tr><td rowspan="4">w/o Edit ROME</td><td>0</td><td>0.2621</td><td>0.0485</td><td>0.2868</td><td>0.2375</td></tr><tr><td>10</td><td>0.0263</td><td>0.0380</td><td>0</td><td>0</td></tr><tr><td></td><td>0</td><td>0.0380</td><td>0</td><td>0</td></tr><tr><td>50 100</td><td>0</td><td>0.0380</td><td>0</td><td>0</td></tr><tr><td rowspan="3">MEMIT</td><td>10</td><td>0.2615</td><td>0.0462</td><td>0.2878</td><td>0.2408</td></tr><tr><td>50</td><td>0.2633</td><td>0.0531</td><td>0.2916</td><td>0.2514</td></tr><tr><td>100</td><td>0.2587</td><td>0.0523</td><td>0.2925</td><td>0.2465</td></tr></table>{{< /table-caption >}}

> This table presents the results of evaluating the impact of different model editing methods and numbers of edits on the general abilities of base language models across various benchmarks.


{{< table-caption caption="🔽 Table 2: Results on evaluating the impact of different editing methods and numbers of edits on edited language models (base model). All editing is conducted on COUNTERFACT dataset with a fixed seed for a fair comparison. For all 4 tasks in this table, the higher score indicates a better performance. MEND and GRACE are not available for Mistral-7B." >}}
<table id='0' style='font-size:14px'><tr><td rowspan="2">Method</td><td rowspan="2"># Edits</td><td colspan="2">Llama2-7B</td><td colspan="2">Llama2-7B-chat</td><td colspan="2">Mixtral-7B</td><td colspan="2">Mixtral-7B-Instruct</td></tr><tr><td>TruthfulQA</td><td>Toxigen</td><td>TruthfulQA</td><td>Toxigen</td><td>TruthfulQA</td><td>Toxigen</td><td>TruthfulQA</td><td>Toxigen</td></tr><tr><td rowspan="2">w/o Edits</td><td>0</td><td>0.2521</td><td>0.4284</td><td>0.3023</td><td>0.5177</td><td>0.2815</td><td>0.4247</td><td>0.3917</td><td>0.4896</td></tr><tr><td>1</td><td>0.2521</td><td>0.4296</td><td>0.2921</td><td>0.5196</td><td>0.2815</td><td>0.4247</td><td>0.3941</td><td>0.4810</td></tr><tr><td rowspan="5">ROME</td><td>5</td><td>0.2497</td><td>0.4272</td><td>0.2997</td><td>0.5072</td><td>0.2815</td><td>0.4247</td><td>0.3929</td><td>0.4896</td></tr><tr><td>10</td><td>0.2485</td><td>0.4296</td><td>0.2962</td><td>0.5080</td><td>0.2742</td><td>0.4235</td><td>0.3892</td><td>0.4737</td></tr><tr><td>20</td><td>0.2411</td><td>0.4284</td><td>0.2913</td><td>0.4871</td><td>0.2742</td><td>0.4247</td><td>0.3868</td><td>0.4737</td></tr><tr><td>50</td><td>0.2411</td><td>0.4101</td><td>0.2497</td><td>0.4957</td><td>0.2350</td><td>0.4247</td><td>0.2644</td><td>0.4504</td></tr><tr><td>100</td><td>0.2729</td><td>0.4982</td><td>0.2974</td><td>0.5141</td><td>0.2509</td><td>0.5667</td><td>0.2827</td><td>0.5251</td></tr><tr><td rowspan="6">MEMIT</td><td>1</td><td>0.2509</td><td>0.4284</td><td>0.2999</td><td>0.5116</td><td>0.2815</td><td>0.4272</td><td>0.3905</td><td>0.4859</td></tr><tr><td>5</td><td>0.2497</td><td>0.4272</td><td>0.2950</td><td>0.5116</td><td>0.2803</td><td>0.4272</td><td>0.3929</td><td>0.4908</td></tr><tr><td>10</td><td>0.2497</td><td>0.4284</td><td>0.2925</td><td>0.5153</td><td>0.2815</td><td>0.4259</td><td>0.3929</td><td>0.4847</td></tr><tr><td>20</td><td>0.2460</td><td>0.4308</td><td>0.2999</td><td>0.5018</td><td>0.2791</td><td>0.4259</td><td>0.3917</td><td>0.4908</td></tr><tr><td>50</td><td>0.2399</td><td>0.4308</td><td>0.2815</td><td>0.5153</td><td>0.2668</td><td>0.4308</td><td>0.3807</td><td>0.4774</td></tr><tr><td>100</td><td>0.1922</td><td>0.4321</td><td>0.2472</td><td>0.4896</td><td>0.2375</td><td>0.4627</td><td>0.2350</td><td>0.5838</td></tr><tr><td rowspan="8">PMET</td><td>1</td><td>0.2521</td><td>0.4296</td><td>0.2974</td><td>0.5163</td><td>0.2815</td><td>0.4247</td><td>0.3917</td><td>0.4823</td></tr><tr><td>5</td><td>0.2497</td><td>0.4272</td><td>0.2988</td><td>0.5175</td><td>0.2815</td><td>0.4247</td><td>0.3917</td><td>0.4835</td></tr><tr><td>10</td><td>0.2485</td><td>0.4296</td><td>0.2964</td><td>0.5190</td><td>0.2840</td><td>0.4235</td><td>0.3929</td><td>0.4847</td></tr><tr><td>20</td><td>0.2411</td><td>0.4284</td><td>0.2974</td><td>0.5141</td><td>0.2740</td><td>0.4247</td><td>0.3905</td><td>0.4908</td></tr><tr><td>50</td><td>0.2411</td><td>0.4100</td><td>0.2962</td><td>0.5129</td><td>0.2350</td><td>0.4247</td><td>0.2375</td><td>0.4333</td></tr><tr><td>100</td><td>0.2729</td><td>0.4982</td><td>0.2962</td><td>0.5165</td><td>0.2509</td><td>0.5667</td><td>0.2350</td><td>0.4333</td></tr><tr><td>500</td><td>0.2350</td><td>0.4259</td><td>0.2362</td><td>0.5667</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1000</td><td>0.2362</td><td>0.4308</td><td>0.2350</td><td>0.5667</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="6">MEND</td><td>10</td><td>0.2472</td><td>0.4308</td><td>0.2974</td><td>0.5141</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>20</td><td>0.2546</td><td>0.4296</td><td>0.2999</td><td>0.5104</td><td></td><td></td><td>-</td><td></td></tr><tr><td>50</td><td>0.2521</td><td>0.4296</td><td>0.2938</td><td>0.5153</td><td>-</td><td>、</td><td>-</td><td></td></tr><tr><td>100</td><td>0.2521</td><td>0.4296</td><td>0.3035</td><td>0.5153</td><td>、</td><td>-</td><td>-</td><td></td></tr><tr><td>500</td><td>0.2521</td><td>0.4308</td><td>0.3035</td><td>0.5080</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>1000</td><td>0.2485</td><td>0.4308</td><td>0.2950</td><td>0.5055</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="5">KN</td><td>10</td><td>0.2350</td><td>0.4333</td><td>0.2277</td><td>0.4333</td><td>0.2889</td><td>0.4308</td><td></td><td></td></tr><tr><td>50</td><td>0.2399</td><td>0.5667</td><td>0.2399</td><td>0.4590</td><td>0.2558</td><td>0.5667</td><td>-</td><td></td></tr><tr><td>100</td><td>0.2350</td><td>0.5667</td><td>0.2399</td><td>0.4590</td><td>0.2583</td><td>0.5667</td><td>-</td><td>-</td></tr><tr><td>500</td><td>0.2362</td><td>0.4333</td><td>0.2392</td><td>0.4590</td><td>0.2583</td><td>0.5667</td><td>-</td><td>-</td></tr><tr><td>1000</td><td>0.2313</td><td>0.4333</td><td>0.2399</td><td>0.4590</td><td>0.2583</td><td>0.5667</td><td>-</td><td></td></tr></table>{{< /table-caption >}}

> Table 2 presents the results of evaluating the impact of various model editing methods and different numbers of edits on the general abilities of base language models across multiple benchmarks.


{{< table-caption caption="🔽 Table 2: Results on evaluating the impact of different editing methods and numbers of edits on edited language models (base model). All editing is conducted on COUNTERFACT dataset with a fixed seed for a fair comparison. For all 4 tasks in this table, the higher score indicates a better performance. MEND and GRACE are not available for Mistral-7B." >}}
<table id='3' style='font-size:14px'><tr><td>DATASET</td><td>TASK TYPE</td><td># FEW-SHOT</td><td># TEST</td><td>METRIC</td><td>EVALUATION METHOD</td></tr><tr><td>MMLU 27</td><td>World Knowledge</td><td>5</td><td>14,079</td><td>Accuracy</td><td>Generation-Based</td></tr><tr><td>BBH 28</td><td>World Knowledge</td><td>3</td><td>6,511</td><td>Accuracy</td><td>Generation-Based</td></tr><tr><td>GSM8K 39</td><td>Arithmetic</td><td>8</td><td>1,319</td><td>Exact match</td><td>Generation-Based</td></tr><tr><td>CSQA* 40</td><td>Commonsense</td><td>7</td><td>1,221</td><td>Accuracy</td><td>Generation-Based</td></tr><tr><td>TriviaQA 41</td><td>Reading Comprehension</td><td>0</td><td>17,900</td><td>Exact match</td><td>Generation-Based</td></tr><tr><td>TruthfulQA 42</td><td>Truthful</td><td>0</td><td>817</td><td>Accuracy</td><td>Sequence-Based</td></tr><tr><td>ToxiGen 43</td><td>Hate Speech</td><td>0</td><td>940</td><td>Accuracy</td><td>Sequence-Based</td></tr></table>{{< /table-caption >}}

> Table 2 presents the performance of various language models (base models) after applying different editing methods with varying numbers of edits, evaluated across four benchmarks.


{{< table-caption caption="🔽 Table 7: Comparison of time costs for different benchmarks with and without vLLM using the Llama2-7B model. The unit is minutes. The table demonstrates that using vLLM significantly reduces the time costs across all benchmarks." >}}
<table id='7' style='font-size:16px'><tr><td rowspan="2">Method</td><td colspan="3">With vLLM</td><td colspan="3">Without vLLM</td></tr><tr><td>MMLU</td><td>GSM8K</td><td>CSQA</td><td>MMLU</td><td>GSM8K</td><td>CSQA</td></tr><tr><td>Llama2-7B</td><td>103</td><td>5</td><td>26</td><td>840</td><td>7</td><td>42</td></tr></table>{{< /table-caption >}}

> Table 7 compares the time costs of running benchmarks with and without the vLLM inference framework to show that using vLLM significantly reduces the time costs.


{{< table-caption caption="🔽 Table 2: Results on evaluating the impact of different editing methods and numbers of edits on edited language models (base model). All editing is conducted on COUNTERFACT dataset with a fixed seed for a fair comparison. For all 4 tasks in this table, the higher score indicates a better performance. MEND and GRACE are not available for Mistral-7B." >}}
<table id='2' style='font-size:16px'><tr><td rowspan="2">Method</td><td colspan="3">Llama2-7B</td><td colspan="3">GPT2-XL</td></tr><tr><td>10</td><td>50</td><td>100</td><td>10</td><td>50</td><td>100</td></tr><tr><td>ROME</td><td>2m1s</td><td>9m53s</td><td>16m31s</td><td>59s</td><td>4m4s</td><td>8mlls</td></tr><tr><td>MEMIT</td><td>4m30s</td><td>20m29s</td><td>40m14s</td><td>2m10s</td><td>8m24s</td><td>17m23s</td></tr><tr><td>GRACE</td><td>10s</td><td>1m3s</td><td>2mls</td><td>5s</td><td>31s</td><td>1m2s</td></tr><tr><td>MEND</td><td>24s</td><td>1m34s</td><td>2m17s</td><td>11s</td><td>52s</td><td>1m24s</td></tr><tr><td>SERAC</td><td>20s</td><td>1m7s</td><td>1m24s</td><td>14s</td><td>1m12s</td><td>2m15s</td></tr></table>{{< /table-caption >}}

> Table 2 presents a quantitative evaluation of different model editing methods' impact on the general abilities of base language models (Llama2-7B and Mistral-7B) across various numbers of edits.


</details>


### Full paper

{{< gallery >}}
<img src="paper_images/1.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/2.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/3.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/4.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/5.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/6.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/7.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/8.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/9.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/10.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/11.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/12.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/13.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/14.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/15.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/16.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/17.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/18.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/19.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/20.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/21.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/22.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/23.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/24.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/25.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/26.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/27.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/28.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/29.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/30.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/31.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/32.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/33.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/34.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/35.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/36.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
{{< /gallery >}}