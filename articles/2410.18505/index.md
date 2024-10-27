---
title: "CCI3.0-HQ: a large-scale Chinese dataset of high quality designed for pre-training large language models"
summary: "CCI3.0-HQ: A new, high-quality 500GB Chinese dataset boosts large language model performance by leveraging a novel two-stage filtering pipeline, exceeding existing datasets in benchmark evaluations."
categories: ["AI Generated"]
tags: ["🔖 24-10-24", "🤗 24-10-25"]
showSummary: true
date: 2024-10-24
draft: false
---

### TL;DR


{{< lead >}}

This research introduces CCI3.0-HQ, a significantly improved Chinese language dataset designed for training large language models (LLMs).  The dataset is a 500GB subset of the Chinese Corpora Internet 3.0 (CCI3.0), carefully refined using a two-stage filtering process.  The first stage involves standard data cleaning and quality assessment. The second stage uses a more sophisticated approach involving a 0.5B parameter model trained to identify high-quality samples. This process results in a dataset that is substantially better than existing open-source Chinese datasets. Experiments show that training LLMs on this refined data leads to improved zero-shot performance on a range of benchmarks compared to other similar datasets.  The paper also introduces a new quality classifier tool, making the improvements achieved reproducible. The researchers believe that CCI3.0-HQ will help further the development of better Chinese LLMs by addressing the scarcity of high-quality training data currently available.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18505" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
The paper introduces CCI3.0-HQ, a high-quality 500GB Chinese dataset for pre-training large language models, significantly enhancing data quality via a two-stage filtering process and outperforming existing datasets on various benchmarks.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} CCI3.0-HQ, a 500GB high-quality Chinese dataset, is introduced for pre-training LLMs. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} A novel two-stage hybrid filtering pipeline significantly improves data quality. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} CCI3.0-HQ outperforms existing Chinese datasets on various benchmarks. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: Dataset Curation Pipeline")

> The figure shows the two-stage hybrid filtering strategy for creating the CCI3.0-HQ dataset, starting from raw data and going through fundamental and high-quality processing stages.





![](charts/charts_4_0.png "🔼 Figure 2: Effects of Backbone Freezing and Learning Rate Adjustments on Classifier Tuning Performance")

> The chart displays the effects of locking/unlocking the backbone and using different learning rates on the F1 score during classifier tuning.





{{< table-caption caption="🔽 Table 1: Pre-training Model Configuration Parameters" >}}
<table id='9' style='font-size:18px'><tr><td>Parameter</td><td>Value</td></tr><tr><td>attention_dropout</td><td>0.0</td></tr><tr><td>bos_token_id</td><td>151849</td></tr><tr><td>eos_token_id</td><td>151850</td></tr><tr><td>hidden_act</td><td>silu</td></tr><tr><td>hidden_size</td><td>896</td></tr><tr><td>intermediate_size</td><td>2432</td></tr><tr><td>max_position_embeddings</td><td>4096</td></tr><tr><td>num_attention_heads</td><td>14</td></tr><tr><td>num_hidden_layers</td><td>24</td></tr><tr><td>num_key_value_heads</td><td>2</td></tr><tr><td>pad_token_id</td><td>151643</td></tr><tr><td>rms_norm_eps</td><td>1e-06</td></tr><tr><td>rope_theta</td><td>10000</td></tr><tr><td>tie_ word_embeddings</td><td>True</td></tr><tr><td>torch_dtype</td><td>bfloat16</td></tr><tr><td>vocab_size</td><td>151851</td></tr></table>{{< /table-caption >}}

> Table 1 presents the hyperparameters used in the pre-training configuration of the Qwen2-0.5B model.



### More visual insights



<details>
<summary>More on charts
</summary>


![](charts/charts_4_1.png "🔼 Figure 2: Effects of Backbone Freezing and Learning Rate Adjustments on Classifier Tuning Performance")

> The chart displays the effects of backbone freezing and different learning rates on the F1 score of a classifier during tuning.


![](charts/charts_10_0.png "🔼 Figure 3: Mixed Dataset Experiment")

> The chart displays the performance of various datasets (Wanjuan-v1, CCI3.0, CCI3.0-HQ, and SkyPile) across different training token amounts in a mixed dataset experiment, showing average and average Chinese scores.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Comparison of Dataset Impacts on Model Performance in Mixed and Chinese Dataset Experiments" >}}
<table id='1' style='font-size:20px'><tr><td colspan="5">Mixed Dataset Experiment Results</td></tr><tr><td>Metrics</td><td>SkyPile</td><td>Wanjuan-v1</td><td>CCI3.0</td><td>CCI3.0-HQ</td></tr><tr><td>ARC-C</td><td>0.270</td><td>0.277</td><td>0.265</td><td>0.269</td></tr><tr><td>ARC-E</td><td>0.521</td><td>0.517</td><td>0.539</td><td>0.542</td></tr><tr><td>HellaSwag</td><td>0.355</td><td>0.347</td><td>0.36</td><td>0.357</td></tr><tr><td>Winograd</td><td>0.507</td><td>0.502</td><td>0.498</td><td>0.523</td></tr><tr><td>MMLU</td><td>0.286</td><td>0.287</td><td>0.289</td><td>0.292</td></tr><tr><td>OpenbookQA</td><td>0.334</td><td>0.312</td><td>0.326</td><td>0.318</td></tr><tr><td>PIQA</td><td>0.651</td><td>0.651</td><td>0.652</td><td>0.648</td></tr><tr><td>SIQA</td><td>0.38</td><td>0.387</td><td>0.375</td><td>0.394</td></tr><tr><td>CEval</td><td>0.279</td><td>0.275</td><td>0.278</td><td>0.296</td></tr><tr><td>CMMLU</td><td>0.294</td><td>0.286</td><td>0.292</td><td>0.309</td></tr><tr><td>AverageEnglish</td><td>0.413</td><td>0.410</td><td>0.413</td><td>0.418</td></tr><tr><td>AverageChinese</td><td>0.287</td><td>0.280</td><td>0.285</td><td>0.303</td></tr><tr><td>Average</td><td>0.388</td><td>0.384</td><td>0.388</td><td>0.395</td></tr><tr><td colspan="5">Chinese Dataset Experiment Results</td></tr><tr><td>Metrics</td><td>SkyPile</td><td>Wanjuan-v1</td><td>CCI3.0</td><td>CCI3.0-HQ</td></tr><tr><td>ARC-C</td><td>0.192</td><td>0.217</td><td>0.202</td><td>0.235</td></tr><tr><td>ARC-E</td><td>0.313</td><td>0.282</td><td>0.323</td><td>0.388</td></tr><tr><td>HellaSwag</td><td>0.279</td><td>0.269</td><td>0.283</td><td>0.295</td></tr><tr><td>Winograd</td><td>0.490</td><td>0.487</td><td>0.485</td><td>0.481</td></tr><tr><td>MMLU</td><td>0.244</td><td>0.254</td><td>0.245</td><td>0.259</td></tr><tr><td>OpenbookQA</td><td>0.254</td><td>0.232</td><td>0.232</td><td>0.242</td></tr><tr><td>PIQA</td><td>0.528</td><td>0.539</td><td>0.53</td><td>0.556</td></tr><tr><td>SIQA</td><td>0.387</td><td>0.377</td><td>0.372</td><td>0.382</td></tr><tr><td>CEval</td><td>0.305</td><td>0.279</td><td>0.294</td><td>0.331</td></tr><tr><td>CMMLU</td><td>0.304</td><td>0.298</td><td>0.296</td><td>0.328</td></tr><tr><td>AverageEnglish</td><td>0.336</td><td>0.332</td><td>0.334</td><td>0.355</td></tr><tr><td>AverageChinese</td><td>0.304</td><td>0.289</td><td>0.295</td><td>0.329</td></tr><tr><td>Average</td><td>0.330</td><td>0.324</td><td>0.326</td><td>0.350</td></tr></table>{{< /table-caption >}}

> Table 2 presents a comparison of the performance of different datasets (SkyPile, Wanjuan-v1, CCI3.0, and CCI3.0-HQ) on various metrics in both mixed and Chinese-only language model pre-training experiments.


{{< table-caption caption="🔽 Table 3: Comparison of Two Quality Annotation Methods" >}}
<table id='2' style='font-size:20px'><tr><td>Metrics</td><td>DCLM</td><td>FineWeb-edu</td></tr><tr><td>ARC-C</td><td>0.211</td><td>0.235</td></tr><tr><td>ARC-E</td><td>0.378</td><td>0.388</td></tr><tr><td>HellaSwag</td><td>0.310</td><td>0.295</td></tr><tr><td>Winograd</td><td>0.485</td><td>0.481</td></tr><tr><td>MMLU</td><td>0.259</td><td>0.259</td></tr><tr><td>OpenbookQA</td><td>0.262</td><td>0.242</td></tr><tr><td>PIQA</td><td>0.571</td><td>0.556</td></tr><tr><td>SIQA</td><td>0.389</td><td>0.382</td></tr><tr><td>CEval</td><td>0.298</td><td>0.331</td></tr><tr><td>CMMLU</td><td>0.311</td><td>0.328</td></tr><tr><td>AverageEnglish</td><td>0.358</td><td>0.355</td></tr><tr><td>AverageChinese</td><td>0.305</td><td>0.329</td></tr><tr><td>Average</td><td>0.348</td><td>0.350</td></tr></table>{{< /table-caption >}}

> Table 3 compares the performance of two quality annotation methods, DCLM and FineWeb-edu, across various metrics, showing FineWeb-edu's superior performance in Chinese-specific tasks.


{{< table-caption caption="🔽 Table 4: Evaluation of Different Quality Classifiers" >}}
<table id='1' style='font-size:16px'><tr><td>Classifier</td><td>Precision</td><td>Recall</td><td>F1-score</td></tr><tr><td colspan="4">classifierFineWeb-edu</td></tr><tr><td>Positive</td><td>0.91</td><td>0.02</td><td>0.03</td></tr><tr><td>Negative</td><td>0.82</td><td>1.00</td><td>0.90</td></tr><tr><td>Macro F1</td><td>0.87</td><td>0.51</td><td>0.47</td></tr><tr><td colspan="4">classifierChineseWebText</td></tr><tr><td>Positive</td><td>0.18</td><td>0.58</td><td>0.27</td></tr><tr><td>Negative</td><td>0.80</td><td>0.38</td><td>0.52</td></tr><tr><td>Macro F1</td><td>0.49</td><td>0.48</td><td>0.39</td></tr><tr><td colspan="4">classifierIndustryCorpus2</td></tr><tr><td>Positive</td><td>0.32</td><td>0.86</td><td>0.47</td></tr><tr><td>Negative</td><td>0.95</td><td>0.59</td><td>0.73</td></tr><tr><td>Macro F1</td><td>0.64</td><td>0.73</td><td>0.60</td></tr><tr><td colspan="4">classifiercc13.0-HQ</td></tr><tr><td>Positive</td><td>0.86</td><td>0.38</td><td>0.53</td></tr><tr><td>Negative</td><td>0.88</td><td>0.99</td><td>0.93</td></tr><tr><td>Macro F1</td><td>0.87</td><td>0.68</td><td>0.73</td></tr></table>{{< /table-caption >}}

> Table 4 compares the performance of four different quality classifiers (classifierFineWeb-edu, classifierChineseWebText, classifierIndustryCorpus2, and classifierCC13.0-HQ) in terms of precision, recall, and F1-score for both positive and negative classes, along with macro averages.


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
{{< /gallery >}}