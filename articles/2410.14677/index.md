---
title: "Are AI Detectors Good Enough? A Survey on Quality of Datasets With Machine-Generated Texts"
summary: "AI text detectors struggle in real-world scenarios despite high benchmark scores; this study reveals dataset quality issues and proposes evaluation methods for better AI detection."
categories: ["AI Generated"]
tags: ["🔖 24-10-18", "🤗 24-10-21"]
showSummary: true
date: 2024-10-18
draft: false
---

### TL;DR


{{< lead >}}

This research paper investigates the reliability of AI detectors designed to identify machine-generated text.  The authors find that while detectors achieve impressive accuracy on benchmark datasets, their performance significantly drops in real-world applications. This discrepancy is attributed to the poor quality of the evaluation datasets themselves. The paper emphasizes the need for robust and qualitative methods to evaluate datasets used for training AI detectors.  The researchers systematically review existing datasets used in AI-generated content detection competitions and propose methods for evaluating dataset quality. They suggest that using high-quality generated data is essential for training better detectors and improving datasets.  The paper contributes to a better understanding of the complex relationship between human-written and machine-generated text, which is critical for maintaining information integrity in the digital age.  In essence, the paper calls for increased attention to dataset quality and suggests methods for improving both the datasets and the AI detectors.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.14677" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This JSON provides a summary of the research paper focusing on the quality of datasets used for AI-generated text detection.  It highlights the main contribution, provides a TL;DR, lists key takeaways, and explains the importance of the research to the AI community.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} AI text detectors perform poorly outside of controlled benchmark datasets. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Dataset quality significantly influences detector performance; robust evaluation methods are crucial. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} High-quality AI-generated data can improve both detector training and dataset quality. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights





![](charts/charts_7_0.png "🔼 Figure 1: Comparisons of embedding shifts after two types of modifications for the HC3 dataset.")

> The chart displays the distribution of embedding shifts after adversarial token perturbation and sentence shuffling for human and generated texts in the HC3 dataset.





{{< table-caption caption="🔽 Table 1: Statistics of the datasets from the shared tasks." >}}
<table id='0' style='font-size:16px'><tr><td>Dataset</td><td>Year</td><td>Language</td><td>Num. of Texts</td><td>Generated VS Human</td><td>Average Length</td><td>Median Length</td></tr><tr><td>RuATD</td><td>2022</td><td>ru</td><td>129k</td><td>64.5k / 64.5k</td><td>236.86 / 221.47</td><td>99.0 / 95.0</td></tr><tr><td>DAGPap22</td><td>2022</td><td>en</td><td>5.3k</td><td>3.6k / 1.6k</td><td>799.45 / 1180.07</td><td>680.07 1126.5</td></tr><tr><td>AuTex</td><td>2023</td><td>en, es</td><td>65.9k</td><td>33.1k / 32.8k</td><td>315.08 / 297.28</td><td>386.07 351.0</td></tr><tr><td>IberAuTex</td><td>2024</td><td>es, en, ca, gl, eu, pt</td><td>98k</td><td>52.5k / 45.4k</td><td>1036.92 / 1058.36</td><td>981.0/ 1018.0</td></tr><tr><td>PAN24</td><td>2024</td><td>en</td><td>15.2k</td><td>14.1k / 1.1k</td><td>2640.50/ 3007.04</td><td>2731.0 / 2868.0</td></tr><tr><td>SemEval24 Mono</td><td>2024</td><td>en</td><td>34.2k</td><td>18k / 16.2k</td><td>2465.12/ 2358.05</td><td>2570.0 / 2083.5</td></tr><tr><td>SemEval24 Multi</td><td>2024</td><td>en, ar, de, it</td><td>42.3k</td><td>22.1k / 20.2k</td><td>2217.87 / 2256.67</td><td>2270.0 / 2032.0</td></tr><tr><td>MGT Task 1 Mono</td><td>2025</td><td>en</td><td>610.7k</td><td>381.8k / 228.9k</td><td>1448.28 / 1541.18</td><td>1208.0 / 1080.0</td></tr><tr><td>MGT Task 1 Multi</td><td>2025</td><td>en, zh, it, ar, de, ru, bg, ur, id</td><td>674k</td><td>416.1k / 257.9k</td><td>1422.74/ 1445.33</td><td>1195.0 / 1032.0</td></tr></table>{{< /table-caption >}}

> The table presents statistics of datasets from shared tasks, including the year, language, number of texts, generated vs. human texts, average length, and median length.



### More visual insights



<details>
<summary>More on charts
</summary>


![](charts/charts_8_0.png "🔼 Figure 4: Topological Time Series for remaining datasets from current review. We omitted the results for Au-Tex23en, because virtually all texts there had the dimension of 0.")

> Figure 4 is a set of histograms showing the distribution of topological time series scores for different datasets, illustrating variations in dimensionality between human-written and machine-generated texts.


![](charts/charts_8_1.png "🔼 Figure 3: Attention maps on two excerpts from DAG-Pap22, Layer 15, Head 15.")

> The chart displays attention maps for human and machine-generated text excerpts from the DAGPap22 dataset, highlighting differences in attention patterns.


![](charts/charts_14_0.png "🔼 Figure 4: Topological Time Series for remaining datasets from current review. We omitted the results for AuTex23en, because virtually all texts there had the dimension of 0.")

> The chart displays the topological time series distributions for various datasets, excluding AuTex23es due to its texts having a dimension of 0.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Statistics of the datasets from the research papers." >}}
<table id='0' style='font-size:16px'><tr><td>Dataset</td><td>Year</td><td>Language</td><td>Num. of Texts</td><td>Generated VS Human</td><td>Average Length</td><td>Median Length</td></tr><tr><td>GPT2</td><td>2019</td><td>en</td><td>1250k</td><td>1000k / 250k</td><td>2941.28 / 2616.04</td><td>3245.0/ 2459.0</td></tr><tr><td>HC3</td><td>2023</td><td>en</td><td>85.4k</td><td>26.9k / 58.5k</td><td>1010.50/ 680.68</td><td>1012.0/ 422.0</td></tr><tr><td>GhostBuster</td><td>2023</td><td>en</td><td>21k</td><td>18k / 3k</td><td>3345.07 / 3391.26</td><td>3439.5 / 2911.5</td></tr><tr><td>MGTBench</td><td>2024</td><td>en</td><td>23.7k</td><td>20.7k / 3k</td><td>1595.94 / 3391.26</td><td>1226.0 / 2911.5</td></tr><tr><td>MAGE</td><td>2024</td><td>en</td><td>436k</td><td>152.3k / 284.2k</td><td>1138.75 / 1281.88</td><td>706.0 / 666.0</td></tr><tr><td>M4</td><td>2024</td><td>en</td><td>89.5k</td><td>44.7k / 44.7k</td><td>1587.62/ 3162.40</td><td>1454.0 / 1697.0</td></tr></table>{{< /table-caption >}}

> Table 2 presents statistics for datasets from research papers, including the year, language, number of texts, generated vs. human text counts, average length, and median length.


{{< table-caption caption="🔽 Table 3: Classification results with different detectors estimated using F₁-score. Binoculars and DetectGPT work only with English texts, thus we could not apply them to datasets with non-English texts." >}}
<br><table id='8' style='font-size:14px'><tr><td>Dataset</td><td>DeBERTa</td><td>Binoculars</td><td>DetectGPT</td></tr><tr><td>GPT-2</td><td>0.972</td><td>0.495</td><td>0.412</td></tr><tr><td>HC3</td><td>0.998</td><td>0.931</td><td>0.972</td></tr><tr><td>GhostBuster</td><td>0.910</td><td>0.683</td><td>0.711</td></tr><tr><td>MGTBench</td><td>0.961</td><td>0.164</td><td>0.344</td></tr><tr><td>MAGE</td><td>0.835</td><td>0.632</td><td>0.654</td></tr><tr><td>M4</td><td>0.987</td><td>0.171</td><td>0.381</td></tr><tr><td>SemEval24 Mono</td><td>0.999</td><td>0.943</td><td>0.983</td></tr><tr><td>SemEval24 Multi</td><td>0.997</td><td>一</td><td>-</td></tr><tr><td>RuATD</td><td>0.765</td><td>-</td><td>-</td></tr><tr><td>DAGPap22</td><td>0.968</td><td>0.333</td><td>0.562</td></tr><tr><td>PAN24</td><td>0.826</td><td>0.411</td><td>0.890</td></tr><tr><td>AuTex23en</td><td>0.941</td><td>0.783</td><td>0.911</td></tr><tr><td>AuTex23es</td><td>0.933</td><td>-</td><td>-</td></tr><tr><td>IberAuTex</td><td>0.964</td><td>-</td><td>-</td></tr><tr><td>MGT-1 Mono</td><td>0.904</td><td>0.665</td><td>0.683</td></tr><tr><td>MGT-1 Multi</td><td>0.934</td><td>一</td><td>-</td></tr></table>{{< /table-caption >}}

> Table 3 presents the F1-scores achieved by three different detectors (DeBERTa, Binoculars, and DetectGPT) on various datasets, highlighting their performance on English and multilingual texts.


{{< table-caption caption="🔽 Table 4: Calculated statistics on texts from chosen datasets. In 'Attention Columns' we show the mean difference between the highest attention column and the second-placed. The first value is for human texts; the second value is for machine-generated. Some values for KLTTS are underlined, because texts are too short, see Section 7." >}}
<table id='2' style='font-size:20px'><tr><td>Dataset</td><td>KLTTS ↓</td><td>Attention Columns (h / m)</td><td>△ shift ↓</td><td>KLshuffle</td></tr><tr><td>GPT-2</td><td>0.014</td><td>3.430 / 4.094</td><td>0.084</td><td>1.255</td></tr><tr><td>HC3</td><td>0.053</td><td>0.459 / 0.967</td><td>0.264</td><td>1.167</td></tr><tr><td>GhostBuster</td><td>0.053</td><td>2.822 / 2.988</td><td>0.024</td><td>0.359</td></tr><tr><td>MGTBench</td><td>0.043</td><td>1.961 / 2.639</td><td>0.031</td><td>0.421</td></tr><tr><td>MAGE</td><td>0.011</td><td>2.289 /2.166</td><td>0.094</td><td>0.310</td></tr><tr><td>M4</td><td>0.036</td><td>3.842 / 2.256</td><td>0.107</td><td>0.483</td></tr><tr><td>SemEval24 Mono</td><td>0.012</td><td>1.540 / 0.766</td><td>0.191</td><td>2.576</td></tr><tr><td>SemEval24 Multi</td><td>0.001</td><td>2.123 / 0.830</td><td>0.059</td><td>2.046</td></tr><tr><td>RuATD</td><td>0.007</td><td>1.631 / 1.391</td><td>0.315</td><td>14.028</td></tr><tr><td>DAGPap22</td><td>0.083</td><td>0.637 / 0.675</td><td>0.039</td><td>0.472</td></tr><tr><td>PAN24</td><td>0.053</td><td>3.463 / 2.588</td><td>0.050</td><td>0.331</td></tr><tr><td>AuTex23-en</td><td>0.021</td><td>3.179 / 2.740</td><td>0.110</td><td>4.331</td></tr><tr><td>AuTex23-es</td><td>0.001</td><td>3.072 / 3.244</td><td>0.105</td><td>1.306</td></tr><tr><td>IberAuTex</td><td>0.012</td><td>2.049 / 1.946</td><td>0.223</td><td>5.516</td></tr><tr><td>MGT-1 Mono</td><td>0.019</td><td>2.070 / 1.783</td><td>0.031</td><td>0.587</td></tr><tr><td>MGT-1 Multi</td><td>0.006</td><td>3.313 / 3.117</td><td>0.027</td><td>0.522</td></tr></table>{{< /table-caption >}}

> Table 4 presents calculated statistics for several datasets, showing the mean difference in attention columns between human and machine-generated texts, and also includes KL divergence scores measuring the similarity of text distributions after adversarial modifications.


{{< table-caption caption="🔽 Table 7: Best results from each analysed competition. PAN24 used mean of 5 metrics, such as accuracy, F1 and other to evaluate efficiency of the system." >}}
<br><table id='10' style='font-size:16px'><tr><td>Competition</td><td>Metric</td><td>Best result</td></tr><tr><td>RuATD</td><td>Accuracy</td><td>0.820</td></tr><tr><td>AuTex-en</td><td>Macro-F1</td><td>0.809</td></tr><tr><td>AuTex-es</td><td>Macro-F1</td><td>0.708</td></tr><tr><td>IberAuTex</td><td>Macro-F1</td><td>0.805</td></tr><tr><td>SemEval24 Mono</td><td rowspan="2">Accuracy</td><td rowspan="2">0.975</td></tr><tr><td></td></tr><tr><td>SemEval24</td><td rowspan="2">Accuracy</td><td rowspan="2">0.959</td></tr><tr><td>Multi</td></tr><tr><td>PAN24</td><td>Avg. of 5 metrics*</td><td>0.924</td></tr><tr><td>DAGPap22</td><td>Avg. F1-score</td><td>0.994</td></tr></table>{{< /table-caption >}}

> Table 7 presents the best results obtained in various AI-generated text detection competitions, indicating the performance of different methods evaluated using various metrics.


{{< table-caption caption="🔽 Table 1: Statistics of the datasets from the shared tasks." >}}
<table id='13' style='font-size:18px'><tr><td>Hyperparameters</td><td>Values</td></tr><tr><td>Epochs</td><td>5*</td></tr><tr><td>Learning rate (LR)</td><td>5e-5</td></tr><tr><td>Warmup steps</td><td>50</td></tr><tr><td>Weight decay</td><td>0.01</td></tr></table>{{< /table-caption >}}

> This table presents statistics of datasets from shared tasks, including the year, language, number of texts, number of human and generated texts, average length, and median length.


{{< table-caption caption="🔽 Table 1: Statistics of the datasets from the shared tasks." >}}
<table id='0' style='font-size:18px'><tr><td>Dataset</td><td>Year</td><td>Themes</td><td>Sources</td></tr><tr><td>RuATD</td><td>2022</td><td>News, Social media, Wikipedia, Strategic Documents, Diaries</td><td>M-BART, M-BART50, M2M-100, OPUS-MT, mT5-Large, mT5-Small, ruGPT2-Large, ruGPT3-Large, ruGPT3-Medium, ruGPT3-Small, ruT5-Base, ruT5-Base-Multitask, ruT5-Large</td></tr><tr><td>DAGPap</td><td>2022</td><td>Scopus papers</td><td>Led-Large-Book-Summary, GPT-3, Spinbot, GPT-Neo-125M</td></tr><tr><td>AuTex</td><td>2023</td><td>Legal documents, So- cial media, How-to ar- ticles</td><td>BLOOM-1B7, BLOOM-3B, BLOOM- 7B1, GPT-3 (Babbage, Curie, text- davinci-003)</td></tr><tr><td>IberAuTex</td><td>2024</td><td>News, Reviews, Emails, Essays, Di- alogues, Wikipedia, Wikihow, Tweets</td><td>GPT, LLama, Mistral, Cohere, An- thropic, MPT, Falcon</td></tr><tr><td>PAN</td><td>2024</td><td>News</td><td>Alpaca-7B, BLOOM-7B1, Alpaca- 13B, Gemini-Pro, ChatGPT (gpt- turbo-3.5, gpt-4-turbo), Llama-2-70B, Llama-2-7b, Mistral-7B, Mistral- 8X7B, Qwen1.5-72B, GPT-2</td></tr><tr><td>SemEval Mono</td><td>2024</td><td>Wikipedia, WikiHow, Reddit, arXiv, Peer- Read, Student Essays</td><td>ChatGPT (text-davinci-003, gpt-4), Cohere, Dolly-v2, BLOOMz</td></tr><tr><td>SemEval Multi</td><td>2024</td><td>Wikipedia, WikiHow, Reddit, arXiv, and PeerRead, Student Essays, News</td><td>ChatGPT (text-davinci-003, gpt- 4), LLaMA2, Cohere, Dolly-v2, BLOOMz, Jais</td></tr><tr><td>MGT Detection Task 1 Mono</td><td>2025</td><td>CNN, DialogSum, Wikipedia, Wiki- How, Eli5, Finance, Medicine, XSum, PubMed, SQuAD, IMDb, Reddit, arXiv, PeerRead</td><td>ChatGPT (text-davinci-002, text- davinci-003, gpt-turbo-3.5), OPT, LLama3, BLOOMz, FLAN-T5, Co- here, Dolly, Gemma, Mixtral</td></tr><tr><td>MGT Detection Task 1 Multi</td><td>2025</td><td>CNN, DialogSum, Baike, QA Wikipedia, WikiHow, Eli5, Fi- nance, Medicine, Psychology, XSum, PubMed, SQuAD, IMDb, Reddit, arXiv, PeerRead</td><td>ChatGPT (text-davinci-002, text- davinci-003, gpt-turbo-3.5, gpt4o), GLM, GPT-J, GPT-Neo, OPT, Llama2, LLama3, BLOOMz, FLAN-T5, Co- here, Dolly, Gemma, Mixtral, Jais</td></tr></table>{{< /table-caption >}}

> This table presents statistics of datasets from shared tasks, including the year, language, number of texts, number of generated vs human texts, and average and median length.


{{< table-caption caption="🔽 Table 2: Statistics of the datasets from the research papers." >}}
<table id='0' style='font-size:18px'><tr><td>Dataset</td><td>Year</td><td>Themes</td><td>Sources</td></tr><tr><td>GPT2</td><td>2019</td><td>WebText</td><td>GPT-2-117M, GPT-2-345M, GPT-2- 762M, GPT-2-1542M</td></tr><tr><td>HC3</td><td>2023</td><td>ELI5, WikiQA, Wikipedia, Medicine, Finance</td><td>ChatGPT (gpt-turbo-3.5)</td></tr><tr><td>GhostBuster</td><td>2023</td><td>Student Essays, News Articles, Creative Writing</td><td>ChatGPT (gpt-3.5-turbo), Claude</td></tr><tr><td>MGTBench</td><td>2024</td><td>Student Essays, News Articles, Creative Writing</td><td>ChatGLM, Dolly, ChatGPT-turbo, GPT4All, StableLM, Claude</td></tr><tr><td>MAGE</td><td>2024</td><td>Opinions, Reviews, News, QA, Story Generation, Com- monsense Reasoning, Knowledge Illus- tration, Scientific Writing</td><td>ChatGPT (text-davinci-002, text- davinci-003, gpt-turbo-3.5), LLaMA, GLM-130B, FLAN-T5, OPT, Big- Science, EleutherAI</td></tr><tr><td>M4</td><td>2024</td><td>Wikipedia, Reddit ELI5, WikiHow, Peer- Read, arXiv abstract</td><td>ChatGPT (text-davinci-003, gpt-turbo- 3.5), Cohere, Dolly-v2, BLOOMz</td></tr></table>{{< /table-caption >}}

> This table presents statistics for datasets from research papers, including year, language, number of texts, generated vs. human texts, average length, and median length.


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
{{< /gallery >}}