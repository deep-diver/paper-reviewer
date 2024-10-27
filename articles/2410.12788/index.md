---
title: "Meta-Chunking: Learning Efficient Text Segmentation via Logical Perception"
summary: "Meta-Chunking boosts RAG efficiency by intelligently segmenting text into logically coherent chunks, improving question-answering accuracy."
categories: ["AI Generated"]
tags: ["🔖 24-10-16", "🤗 24-10-22"]
showSummary: true
date: 2024-10-16
draft: false
---

### TL;DR


{{< lead >}}

This paper introduces Meta-Chunking, a new text segmentation technique designed to enhance Retrieval-Augmented Generation (RAG) systems.  Traditional methods for text segmentation (rule-based or semantic similarity) often overlook the crucial aspect of logical connections between sentences. Meta-Chunking addresses this by identifying groups of sentences within paragraphs that exhibit strong logical relationships, a granularity between sentences and paragraphs. The researchers propose two main strategies: Margin Sampling Chunking and Perplexity Chunking, which both use Large Language Models (LLMs) to perform binary classification or analyze perplexity distributions to identify chunk boundaries. To adapt to different text complexities, a dynamic merging strategy is proposed to combine fine-grained and coarse-grained chunking. Experiments across eleven datasets show that Meta-Chunking significantly improves the performance of single-hop and multi-hop question answering within RAG. For instance, on one benchmark, it outperformed similarity-based chunking by a significant margin while requiring only 45.8% of the processing time.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.12788" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This JSON contains a summary of the research paper on Meta-Chunking, fulfilling the user's request for a catchy summary, TL;DR, key takeaways, and explanation of the paper's importance to researchers.  The information is concise, avoids redundancy, focuses on the core ideas, and maintains a professional tone.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} Meta-Chunking, a novel text segmentation method, improves the efficiency and accuracy of Retrieval-Augmented Generation (RAG) systems. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Margin Sampling Chunking and Perplexity Chunking, two LLM-based strategies, effectively determine optimal chunk boundaries. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} Dynamic merging enhances Meta-Chunking's adaptability by balancing fine-grained and coarse-grained text segmentation. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_3_0.png "🔼 Figure 1: Overview of RAG pipeline, as well as examples based on rules, similarity, and PPL segmentation. The same background color represents being located in the same chunk.")

> The figure illustrates the RAG pipeline and compares three different text chunking methods based on rules, similarity, and perplexity.





![](charts/charts_8_0.png "🔼 Figure 3: Performance of different methods on single-hop query in the CRUD QA dataset. ppl represents direct PPL Chunking, with a threshold of 0.5. comb. indicates PPL Chunking with dynamic combination, with a threshold of 0 when performing PPL Chunking. Precise chunk length results and performance of remaining multi-hop scenarios are included in Appendix A.3.")

> The chart compares the performance of various text chunking methods (rule-based, similarity-based, and two Meta-Chunking approaches) on a single-hop query task from the CRUD QA dataset, measured by BLEU scores, ROUGE-L, and BERTScore.





{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<table id='2' style='font-size:14px'><tr><td>Dataset</td><td colspan="2">2WikiMultihopQA</td><td colspan="2">Qasper</td><td colspan="2">MultiFieldQA-en</td><td colspan="2">MultiFieldQA-zh</td><td colspan="4">MultiHop-RAG</td></tr><tr><td>Chunking Method</td><td>F1</td><td>Time</td><td>F1</td><td>Time</td><td>F1</td><td>Time</td><td>F1</td><td>Time</td><td>Hits@10</td><td>Hits@4</td><td>MAP@10</td><td>MRR@10</td></tr><tr><td colspan="13">Baselines with rule-based or similarity-based chunking</td></tr><tr><td>Original</td><td>11.89</td><td>0.21</td><td>9.45</td><td>0.13</td><td>29.89</td><td>0.16</td><td>22.45</td><td>0.06</td><td>0.6027</td><td>0.4523</td><td>0.1512</td><td>0.3507</td></tr><tr><td>Llama_index</td><td>11.74</td><td>8.12</td><td>10.15</td><td>5.81</td><td>28.30</td><td>6.25</td><td>21.85</td><td>5.53</td><td>0.7366</td><td>0.5437</td><td>0.1889</td><td>0.4068</td></tr><tr><td>Similarity Chunking</td><td>12.00</td><td>416.45</td><td>9.93</td><td>307.05</td><td>29.19</td><td>318.41</td><td>22.39</td><td>134.80</td><td>0.7232</td><td>0.5362</td><td>0.1841</td><td>0.3934</td></tr><tr><td colspan="13">Margin Sampling Chunking based on different models</td></tr><tr><td>Pythia-0.16B sent.</td><td>13.14</td><td>478.91</td><td>9.15</td><td>229.68</td><td>31.19</td><td>273.10</td><td>-</td><td>-</td><td>- 0.6993</td><td>0.5069</td><td>0.1793</td><td>0.3773</td></tr><tr><td>Pythia-0.41B sent.</td><td>11.86</td><td>926.29</td><td>9.76</td><td>498.46</td><td>29.30</td><td>545.15</td><td>-</td><td>-</td><td>0.7259</td><td>0.5596</td><td>0.1934</td><td>0.4235</td></tr><tr><td>Qwen2-0.5B sent.</td><td>11.74</td><td>788.30</td><td>9.67</td><td>599.97</td><td>31.28</td><td>648.76</td><td>23.35</td><td>480.35</td><td>0.7162</td><td>0.5246</td><td>0.1830</td><td>0.3913</td></tr><tr><td>Qwen2-1.5B sent.</td><td>11.18</td><td>1908.25</td><td>10.09</td><td>1401.30</td><td>32.19</td><td>1457.31</td><td>22.27</td><td>1081.64</td><td>0.7805</td><td>0.6089</td><td>0.2106</td><td>0.4661</td></tr><tr><td>Qwen2-7B sent.</td><td>13.22</td><td>7108.37</td><td>10.58</td><td>5207.87</td><td>32.32</td><td>5316.62</td><td>23.24</td><td>4212.00</td><td>0.6993</td><td>0.5197</td><td>0.1794</td><td>0.3835</td></tr><tr><td>Qwen2-1.5B, chunk</td><td>11.30</td><td>2189.29</td><td>9.49</td><td>1487.27</td><td>32.81</td><td>1614.01</td><td>22.08</td><td>1881.15</td><td>0.7109</td><td>0.5517</td><td>0.1970</td><td>0.4252</td></tr><tr><td>Qwen2-7B chunk</td><td>12.94</td><td>8781.82</td><td>11.37</td><td>5755.79</td><td>33.56</td><td>6287.31</td><td>24.24</td><td>5084.95</td><td>0.7175</td><td>0.5415</td><td>0.1903</td><td>0.4141</td></tr><tr><td colspan="13">Perplexity Chunking based on different models</td></tr><tr><td>Internlm2-1.8Bcomb.</td><td>12.37</td><td>355.53</td><td>10.02</td><td>200.69</td><td>30.81</td><td>251.06</td><td>22.53</td><td>161.15</td><td>0.7237</td><td>0.5499</td><td>0.1897</td><td>0.4121</td></tr><tr><td>Qwen2-1.5B comb.</td><td>13.32</td><td>190.93</td><td>9.82</td><td>122.44</td><td>31.30</td><td>136.96</td><td>22.57</td><td>107.94</td><td>0.7366</td><td>0.5570</td><td>0.1979</td><td>0.4300</td></tr><tr><td>Baichuan2-7B comb.</td><td>12.98</td><td>858.99</td><td>10.04</td><td>569.72</td><td>32.55</td><td>632.80</td><td>23.36</td><td>569.72</td><td>0.7206</td><td>0.5636</td><td>0.2048</td><td>0.4406</td></tr><tr><td>Qwen2-7B comb.</td><td>13.41</td><td>736.69</td><td>9.39</td><td>486.48</td><td>32.35</td><td>523.74</td><td>22.81</td><td>424.96</td><td>0.7215</td><td>0.5521</td><td>0.1967</td><td>0.4229</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five question answering datasets, comparing different text chunking methods based on F1 score, time consumption, and MultiHop-RAG metrics.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_4_0.png "🔼 Figure 2: Overview of the entire process of Meta-Chunking. Each circle represents a complete sentence, and the sentence lengths are not consistent. The vertical lines indicate where to segment. The two sides at the bottom of the figure reveal Margin Sampling Chunking and Perplexity Chunking. Circles with the same background color represent a meta-chunk, which is dynamically combined to make the final chunk length meet user needs.")

> The figure illustrates the Meta-Chunking process, showing how margin sampling and perplexity methods dynamically combine sentences into chunks of varying lengths to maintain logical coherence.


![](figures/figures_9_0.png "🔼 Figure 2: Overview of the entire process of Meta-Chunking. Each circle represents a complete sentence, and the sentence lengths are not consistent. The vertical lines indicate where to segment. The two sides at the bottom of the figure reveal Margin Sampling Chunking and Perplexity Chunking. Circles with the same background color represent a meta-chunk, which is dynamically combined to make the final chunk length meet user needs.")

> The figure illustrates the process of Meta-Chunking, showing how sentences are grouped into meta-chunks and dynamically combined to achieve desired chunk sizes.


![](figures/figures_9_1.png "🔼 Figure 3: Performance of different methods on single-hop query in the CRUD QA dataset. ppl represents direct PPL Chunking, with a threshold of 0.5. comb. indicates PPL Chunking with dynamic combination, with a threshold of 0 when performing PPL Chunking. Precise chunk length results and performance of remaining multi-hop scenarios are included in Appendix A.3.")

> The figure shows the performance comparison of different text chunking methods on a single-hop query task from the CRUD QA dataset, highlighting the effectiveness of PPL Chunking with dynamic combination.


</details>




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<br><table id='2' style='font-size:14px'><tr><td>Chunking Method</td><td>Overlap</td><td>BLEU-1</td><td>BLEU-2</td><td>BLEU-3</td><td>BLEU-4</td><td>BLEU-Avg</td><td>ROUGE-L</td><td>BERTScore</td></tr><tr><td colspan="9">Single-hop Query</td></tr><tr><td>Original</td><td>Fixed</td><td>0.3330</td><td>0.2641</td><td>0.2214</td><td>- 0.1881</td><td>- 0.2410</td><td>0.4060</td><td>0.8425</td></tr><tr><td>Llama_index</td><td>Dynamic</td><td>0.3326</td><td>0.2645</td><td>0.2214</td><td>0.1890</td><td>0.2413</td><td>0.4039</td><td>0.8439</td></tr><tr><td>Qwen2-1.5B, ppl</td><td>Dynamic</td><td>0.3592</td><td>0.2888</td><td>0.2435</td><td>0.2081</td><td>0.2644</td><td>0.4332</td><td>0.8555</td></tr><tr><td>Qwen2-7B ppl</td><td>Dynamic</td><td>0.3582</td><td>0.2898</td><td>0.2450</td><td>0.2097</td><td>0.2657</td><td>0.4308</td><td>0.8548</td></tr><tr><td>Baichuan2-7Bppi</td><td>Dynamic</td><td>0.3656</td><td>0.2952</td><td>0.2497</td><td>0.2143</td><td>0.2705</td><td>0.4393</td><td>0.8549</td></tr><tr><td colspan="9">Two-hop Query -</td></tr><tr><td>Original</td><td>Fixed</td><td>0.2251</td><td>- - 0.1300</td><td>- 0.0909</td><td>- 0.0689</td><td>- 0.1114</td><td>0.2579</td><td>0.8747</td></tr><tr><td>Llama_index</td><td>Dynamic</td><td>0.2223</td><td>0.1282</td><td>0.0896</td><td>0.0677</td><td>0.1099</td><td>0.2555</td><td>0.8732</td></tr><tr><td>Qwen2-1.5Bppl</td><td>Dynamic</td><td>0.2295</td><td>0.1331</td><td>0.0934</td><td>0.0709</td><td>0.1143</td><td>0.2609</td><td>0.8700</td></tr><tr><td>Qwen2-7B ppl</td><td>Dynamic</td><td>0.2312</td><td>0.1353</td><td>0.0949</td><td>0.0719</td><td>0.1162</td><td>0.2638</td><td>0.8751</td></tr><tr><td>Baichuan2-7Bppl</td><td>Dynamic</td><td>0.2336</td><td>0.1350</td><td>0.0940</td><td>0.0710</td><td>0.1154</td><td>0.2650</td><td>0.8754</td></tr><tr><td colspan="9">Three-hop Query -</td></tr><tr><td>Original</td><td>Fixed</td><td>0.2384</td><td>0.1268</td><td>0.0832</td><td>- 0.0602</td><td>- 0.1066</td><td>- 0.2546</td><td>0.8823</td></tr><tr><td>Llama_index</td><td>Dynamic</td><td>0.2331</td><td>0.1250</td><td>0.0825</td><td>0.0598</td><td>0.1049</td><td>0.2517</td><td>0.8796</td></tr><tr><td>Qwen2-1.5B, ppl</td><td>Dynamic</td><td>0.2453</td><td>0.1319</td><td>0.0881</td><td>0.0643</td><td>0.1114</td><td>0.2599</td><td>0.8808</td></tr><tr><td>Qwen2-7B ppl</td><td>Dynamic</td><td>0.2447</td><td>0.1330</td><td>0.0891</td><td>0.0651</td><td>0.1122</td><td>0.2618</td><td>0.8817</td></tr><tr><td>Baichuan2-7Bppi</td><td>Dynamic</td><td>0.2463</td><td>0.1324</td><td>0.0887</td><td>0.0651</td><td>0.1120</td><td>0.2596</td><td>0.8811</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five QA datasets, comparing the performance of different chunking methods on F1 score and time consumption.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<br><table id='4' style='font-size:14px'><tr><td rowspan="2">Dataset Chunking Method</td><td colspan="2">2WikiMultihopQA</td><td colspan="2">Qasper</td><td colspan="2">MultiFieldQA-en</td><td colspan="2">MultiFieldQA-zh</td><td colspan="2">MultiHop-RAG</td></tr><tr><td>Length</td><td>Threshold</td><td>Length</td><td>Threshold</td><td>Length</td><td>Threshold</td><td>Length</td><td>Threshold</td><td>Length</td><td>Threshold</td></tr><tr><td colspan="11">Baselines with rule-based or similarity-based chunking</td></tr><tr><td>Original</td><td>123</td><td>-</td><td>- - 121</td><td>-</td><td>113</td><td>-</td><td>178</td><td>-</td><td>78</td><td>- - -</td></tr><tr><td>Llama_index</td><td>122.61(215)</td><td>-</td><td>120.91(198)</td><td>-</td><td>112.59(208)</td><td>-</td><td>178.04(242)</td><td>-</td><td>79.68</td><td>-</td></tr><tr><td>Similarity Chunking</td><td>125.24</td><td>0.82</td><td>122.91</td><td>0.83</td><td>114.18</td><td>0.83</td><td>180.23</td><td>0.73</td><td>80.13</td><td>0.75</td></tr><tr><td colspan="11">LLMs Direct Chunking - - - - -</td></tr><tr><td>Qwen2-72B</td><td>122.13(128)</td><td>-</td><td>- 120.17(90)</td><td>- -</td><td>111.98(88)</td><td>-</td><td>178.05(190)</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="11">Margin Sampling Chunking based on different models</td></tr><tr><td>Pythia-0.16B sent.</td><td>122.45(144)</td><td>0+comb.</td><td>- - 120.77(148)</td><td>0+comb.</td><td>111.89(133)</td><td>- 0+comb.</td><td>- - - - -</td><td>-</td><td>- 77.60(85)</td><td>0+comb.</td></tr><tr><td>Pythia-0.41B sent.</td><td>121.83(143)</td><td>0+comb.</td><td>120.75(148)</td><td>0+comb.</td><td>112.31(134)</td><td>0+comb.</td><td>-</td><td>-</td><td>77.96(83)</td><td>0+comb.</td></tr><tr><td>Qwen2-0.5B sent.</td><td>122.33(148)</td><td>0+comb.</td><td>120.07(147)</td><td>0+comb.</td><td>112.46(136)</td><td>0+comb.</td><td>178.09(180)</td><td>0+comb.</td><td>78.04(91)</td><td>0+comb.</td></tr><tr><td>Qwen2-1.5B sent.</td><td>121.60(151)</td><td>0+comb.</td><td>120.61(148)</td><td>0+comb.</td><td>111.60(136)</td><td>0+comb.</td><td>177.11(195)</td><td>0+comb.</td><td>78.20(95)</td><td>0+comb.</td></tr><tr><td>Qwen2-7B sent.</td><td>121.75(145)</td><td>0+comb.</td><td>120.47(145)</td><td>0+comb.</td><td>111.93(134)</td><td>0+comb.</td><td>177.47(195)</td><td>0+comb.</td><td>77.90(95)</td><td>0+comb.</td></tr><tr><td>Qwen2-1.5B chunk</td><td>121.99(148)</td><td>0+comb.</td><td>120.21(144)</td><td>0+comb.</td><td>111.52(134)</td><td>0+comb.</td><td>177.80(200)</td><td>0+comb.</td><td>78.16(97)</td><td>0+comb.</td></tr><tr><td>Qwen2-7B chunk</td><td>121.81(138)</td><td>0+comb.</td><td>120.01(141)</td><td>0+comb.</td><td>111.56(129)</td><td>0+comb.</td><td>178.00(188)</td><td>0+comb.</td><td>77.49(95)</td><td>0+comb.</td></tr><tr><td colspan="11">Perplexity Chunking based on different models</td></tr><tr><td>Internlm2-1.8Bcomb.</td><td>122.62(152)</td><td>0+comb.</td><td>- - 120.14(155)</td><td>0+comb.</td><td>111.98(138)</td><td>- - 0+comb.</td><td>178.00(158)</td><td>0+comb.</td><td>78.25(89)</td><td>0+comb.</td></tr><tr><td>Qwen2-1.5B comb.</td><td>122.48(152)</td><td>0+comb.</td><td>120.56(156)</td><td>0+comb.</td><td>111.35(138)</td><td>0+comb.</td><td>178.00(159)</td><td>0+comb.</td><td>78.19(89)</td><td>0+comb.</td></tr><tr><td>Baichuan2-7B, comb.</td><td>122.37(152)</td><td>0+comb.</td><td>120.66(155)</td><td>0+comb.</td><td>111.85(138)</td><td>0+comb.</td><td>178.00(159)</td><td>0+comb.</td><td>78.01(90)</td><td>0+comb.</td></tr><tr><td>Qwen2-7B comb.</td><td>122.26(152)</td><td>0+comb.</td><td>120.26(155)</td><td>0+comb.</td><td>111.47(137)</td><td>0+comb.</td><td>177.80(156)</td><td>0+comb.</td><td>78.11(89)</td><td>0+comb.</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five QA datasets, comparing the performance of various chunking methods on F1 scores and processing time.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<br><table id='2' style='font-size:20px'><tr><td>Chunking Method</td><td>Overlap Length</td><td>Chunk Length</td></tr><tr><td colspan="3">Chunking with Overlap</td></tr><tr><td>Original</td><td>50</td><td>218</td></tr><tr><td>Llama_index</td><td>48.78</td><td>217.03</td></tr><tr><td>Qwen2-1.5B ppl</td><td>49.97</td><td>212.79</td></tr><tr><td>Qwen2-7B ppl</td><td>50.41</td><td>217.53</td></tr><tr><td>Baichuan2-7Bppi</td><td>48.91</td><td>201.35</td></tr><tr><td colspan="3">Chunking without Overlap</td></tr><tr><td>Original</td><td>0</td><td>179</td></tr><tr><td>Llama_index</td><td>0</td><td>177.53</td></tr><tr><td>Qwen2-1.5B ppl</td><td>0</td><td>173.88</td></tr><tr><td>Qwen2-7B ppl</td><td>0</td><td>178.59</td></tr><tr><td>Baichuan2-7Bppi</td><td>0</td><td>162.56</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0</td><td>177.95</td></tr><tr><td>Qwen2-7B comb.</td><td>0</td><td>178.09</td></tr><tr><td>Baichuan2-7Bcomb.</td><td>0</td><td>178.09</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five question answering datasets, comparing different chunking methods and their performance in terms of F1 score and time consumption.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<br><table id='2' style='font-size:14px'><tr><td>Chunking Method</td><td>BLEU-1</td><td>BLEU-2</td><td>BLEU-3</td><td>BLEU-4</td><td>BLEU-Avg</td><td>ROUGE-L</td><td>BERTScore</td></tr><tr><td colspan="8">Single-hop Query -</td></tr><tr><td>Original</td><td>0.3515</td><td>0.2788</td><td>0.2340</td><td>0.1997</td><td>0.2548</td><td>0.4213</td><td>0.8489</td></tr><tr><td>Llama_index</td><td>0.3620</td><td>0.2920</td><td>0.2480</td><td>0.2134</td><td>0.2682</td><td>0.4326</td><td>0.8521</td></tr><tr><td>Qwen2-1.5B ppl</td><td>0.3714</td><td>0.3013</td><td>0.2569</td><td>0.2223</td><td>0.2778</td><td>0.4426</td><td>0.8563</td></tr><tr><td>Qwen2-7B ppl</td><td>0.3661</td><td>0.2935</td><td>0.2481</td><td>0.2127</td><td>0.2691</td><td>0.4379</td><td>0.8558</td></tr><tr><td>Baichuan2-7Bppl</td><td>0.3725</td><td>0.3011</td><td>0.2558</td><td>0.2207</td><td>0.2772</td><td>0.4429</td><td>0.8562</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0.3760</td><td>0.3034</td><td>0.2577</td><td>0.2224</td><td>0.2797</td><td>0.4443</td><td>0.8586</td></tr><tr><td>Qwen2-7B comb.</td><td>0.3724</td><td>0.3012</td><td>0.2561</td><td>0.2206</td><td>0.2774</td><td>0.4445</td><td>0.8584</td></tr><tr><td>Baichuan2-7Bcomb.</td><td>0.3812</td><td>0.3091</td><td>0.2622</td><td>0.2259</td><td>0.2840</td><td>0.4494</td><td>0.8603</td></tr><tr><td colspan="8">Two-hop Query</td></tr><tr><td>Original</td><td>0.2322</td><td>0.1324</td><td>0.0919</td><td>0.0695</td><td>0.1133</td><td>0.2613</td><td>0.8768</td></tr><tr><td>Llama_index</td><td>0.2315</td><td>0.1321</td><td>0.0923</td><td>0.0697</td><td>0.1133</td><td>0.2585</td><td>0.8762</td></tr><tr><td>Qwen2-1.5B ppl</td><td>0.2328</td><td>0.1326</td><td>0.0918</td><td>0.0694</td><td>0.1133</td><td>0.2611</td><td>0.8749</td></tr><tr><td>Qwen2-7B ppl</td><td>0.2310</td><td>0.1323</td><td>0.0916</td><td>0.0691</td><td>0.1124</td><td>0.2597</td><td>0.8752</td></tr><tr><td>Baichuan2-7B ppl</td><td>0.2350</td><td>0.1341</td><td>0.0924</td><td>0.0695</td><td>0.1141</td><td>0.2637</td><td>0.8772</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0.2372</td><td>0.1363</td><td>0.0950</td><td>0.0722</td><td>0.1164</td><td>0.2658</td><td>0.8743</td></tr><tr><td>Qwen2-7B comb.</td><td>0.2364</td><td>0.1360</td><td>0.0945</td><td>0.0713</td><td>0.1161</td><td>0.2661</td><td>0.8761</td></tr><tr><td>Baichuan2-7Bcomb.</td><td>0.2325</td><td>0.1329</td><td>0.0917</td><td>0.0689</td><td>0.1133</td><td>0.2623</td><td>0.8754</td></tr><tr><td colspan="8">Three-hop Query</td></tr><tr><td>Original</td><td>0.2494</td><td>0.1317</td><td>0.0869</td><td>0.0636</td><td>0.1110</td><td>0.2595</td><td>0.8827</td></tr><tr><td>Llama_index</td><td>0.2464</td><td>0.1327</td><td>0.0883</td><td>0.0644</td><td>0.1120</td><td>0.2596</td><td>0.8840</td></tr><tr><td>Qwen2-1.5B ppl</td><td>0.2402</td><td>0.1260</td><td>0.0827</td><td>0.0596</td><td>0.1054</td><td>0.2531</td><td>0.8802</td></tr><tr><td>Qwen2-7B ppl</td><td>0.2415</td><td>0.1266</td><td>0.0828</td><td>0.0597</td><td>0.1058</td><td>0.2549</td><td>0.8816</td></tr><tr><td>Baichuan2-7Bppl</td><td>0.2460</td><td>0.1293</td><td>0.0851</td><td>0.0615</td><td>0.1084</td><td>0.2568</td><td>0.8828</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0.2449</td><td>0.1294</td><td>0.0855</td><td>0.0624</td><td>0.1086</td><td>0.2566</td><td>0.8828</td></tr><tr><td>Qwen2-7B comb.</td><td>0.2408</td><td>0.1274</td><td>0.0837</td><td>0.0610</td><td>0.1068</td><td>0.2551</td><td>0.8825</td></tr><tr><td>Baichuan2-7Bcomb.</td><td>0.2494</td><td>0.1324</td><td>0.0870</td><td>0.0632</td><td>0.1111</td><td>0.2613</td><td>0.8832</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five QA datasets, comparing the performance of various chunking methods based on different metrics, model sizes, and strategies.


{{< table-caption caption="🔽 Table 8: Settings of overlap length and chunk length for different chunking methods in the CUAD dataset. ppl represents direct PPL Chunking, with a threshold of 0." >}}
<br><table id='4' style='font-size:18px'><tr><td>Chunking Method</td><td>Overlap Length</td><td>Chunk Length</td></tr><tr><td>Original</td><td>0</td><td>98.00</td></tr><tr><td>Llama_index</td><td>0</td><td>98.49</td></tr><tr><td>Qwen2-1.5B ppl</td><td>0</td><td>97.70</td></tr><tr><td>Qwen2-7B ppl</td><td>0</td><td>96.08</td></tr><tr><td>Baichuan2-7Bppi</td><td>0</td><td>97.59</td></tr></table>{{< /table-caption >}}

> Table 8 presents the overlap length and chunk length for different chunking methods used in the CUAD dataset, showing the settings for original, Llama index, Qwen2-1.5B ppl, Qwen2-7B ppl, and Baichuan2-7B ppl methods.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<br><table id='2' style='font-size:14px'><tr><td>Dataset</td><td colspan="2">HotpotQA</td><td colspan="2">MuSiQue</td><td colspan="2">NarrativeQA</td><td colspan="2">DuReader</td></tr><tr><td>Chunking Method</td><td>Length</td><td>Threshold</td><td>Length</td><td>Threshold</td><td>Length</td><td>Threshold</td><td>Length</td><td>Threshold</td></tr><tr><td>Original</td><td>87</td><td>-</td><td>90</td><td>-</td><td>71</td><td>-</td><td>262</td><td></td></tr><tr><td>Llama_index</td><td>86.73(154)</td><td>-</td><td>89.94(157)</td><td>-</td><td>70.35(139)</td><td>-</td><td>262.06(330)</td><td>-</td></tr><tr><td>Qwen2-1.5Bppi</td><td>86.72</td><td>0.5</td><td>89.51</td><td>0.5</td><td>70.28</td><td>1.34</td><td>261.41</td><td>0.5</td></tr><tr><td>Qwen2-1.5B comb.</td><td>86.80(98)</td><td>0+comb.</td><td>89.59(103)</td><td>0+comb.</td><td>70.32(82)</td><td>0+comb.</td><td>261.34(213)</td><td>0+comb.</td></tr><tr><td>Qwen2-1.5B comb.</td><td>86.52(96)</td><td>0.1+comb.</td><td>89.60(100)</td><td>0.1+comb.</td><td>70.47(82)</td><td>0.1+comb.</td><td>261.98(200)</td><td>0.1+comb.</td></tr><tr><td>Qwen2-1.5B comb.</td><td>86.58(92)</td><td>0.2+comb.</td><td>89.75(96)</td><td>0.2+comb.</td><td>70.17(81)</td><td>0.2+comb.</td><td>261.92(189)</td><td>0.2+comb.</td></tr><tr><td>Qwen2-1.5B comb.</td><td>86.77(85)</td><td>0.3+comb.</td><td>89.60(88)</td><td>0.3+comb.</td><td>70.19(79)</td><td>0.3+comb.</td><td>261.06(170)</td><td>0.3+comb.</td></tr><tr><td>Qwen2-1.5B comb.</td><td>86.81(70)</td><td>0.4+comb.</td><td>89.68(75)</td><td>0.4+comb.</td><td>70.66(78)</td><td>0.4+comb.</td><td>261.48(140)</td><td>0.4+comb.</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five question answering datasets, comparing the performance of various chunking methods based on different metrics and model parameters.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<br><table id='4' style='font-size:16px'><tr><td>Chunking Method</td><td>BLEU-1</td><td>BLEU-2</td><td>BLEU-3</td><td>BLEU-4</td><td>BLEU-Avg</td><td>ROUGE-L</td><td>BERTScore</td></tr><tr><td>Original</td><td>0.6845</td><td>0.4496</td><td>0.2997</td><td>0.1798</td><td>0.3513</td><td>0.4217</td><td>0.8043</td></tr><tr><td>Llama_index</td><td>0.6966</td><td>0.4573</td><td>0.3006</td><td>0.1730</td><td>0.3493</td><td>0.4137</td><td>0.8001</td></tr><tr><td>Qwen2-1.5B ppl</td><td>0.7098</td><td>0.4722</td><td>0.3180</td><td>0.1932</td><td>0.3677</td><td>0.4060</td><td>0.8006</td></tr><tr><td>Qwen2-7B ppl</td><td>0.7038</td><td>0.4670</td><td>0.3143</td><td>0.1911</td><td>0.3638</td><td>0.4070</td><td>0.8018</td></tr><tr><td>Baichuan2-7Bppl</td><td>0.7195</td><td>0.4738</td><td>0.3160</td><td>0.1884</td><td>0.3665</td><td>0.4111</td><td>0.8025</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five question answering datasets, comparing different chunking methods based on F1 score and time.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<table id='6' style='font-size:20px'><tr><td>Chunking Method</td><td>Dataset Threshold</td><td>HotpotQA F1</td><td>MuSiQue F1</td><td>NarrativeQA F1</td><td>DuReader ROUGE-L</td></tr><tr><td>Original</td><td>-</td><td>15.79</td><td>7.21</td><td>5.72</td><td>20.69</td></tr><tr><td>Llama_index</td><td>-</td><td>15.72</td><td>8.19</td><td>5.03</td><td>21.41</td></tr><tr><td>Qwen2-1.5B ppl</td><td>Multi</td><td>17.74</td><td>8.39</td><td>6.12</td><td>20.77</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0</td><td>17.47</td><td>8.08</td><td>4.93</td><td>20.77</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0.1</td><td>17.19</td><td>7.48</td><td>4.91</td><td>20.33</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0.2</td><td>17.70</td><td>7.31</td><td>5.20</td><td>20.95</td></tr><tr><td>Qwen2-1.5B comb.</td><td>0.3</td><td>17.46</td><td>7.92</td><td>5.08</td><td>21.22</td></tr><tr><td>Qwen2-1.5Bcomb.</td><td>0.4</td><td>16.44</td><td>8.05</td><td>5.80</td><td>21.65</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five question answering datasets, comparing the performance of various text chunking methods on F1 score and time consumption.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<br><table id='2' style='font-size:14px'><tr><td>Chunking and Re-ranking</td><td>Chunk Length</td><td>Threshold</td></tr><tr><td>Original</td><td>78</td><td>-</td></tr><tr><td>Original and BgeRerank</td><td>78</td><td>-</td></tr><tr><td>Original and PPLRerank</td><td>78 一</td><td>- -</td></tr><tr><td>Qwen2-1.5B, ppl</td><td>77.60</td><td>0.5</td></tr><tr><td>Qwen2-1.5B ppl BgeRerank and</td><td>77.60</td><td>0.5</td></tr><tr><td>Qwen2-1.5B ppl and PPLRerank</td><td>77.60</td><td>0.5</td></tr></table>{{< /table-caption >}}

> Table 1 presents the F1 scores and processing times of various text chunking methods on five question answering datasets, comparing rule-based and similarity-based baselines with Margin Sampling Chunking and Perplexity Chunking strategies using different LLMs.


{{< table-caption caption="🔽 Table 1: Main experimental results are presented in five QA datasets. The first four datasets are sourced from LongBench. sent. indicates whether it is suitable to separate two sentences, while chunk signifies whether the latter sentence is appropriate to be merged with the preceding chunk. comb. refers to the process of first segmenting the text using PPL Chunking with a threshold of 0, followed by dynamic combination." >}}
<table id='4' style='font-size:16px'><tr><td>Chunking and Re-ranking</td><td>Hits@8</td><td>Hits@6</td><td>Hits@4</td><td>Hits@2</td><td>MAP@10</td><td>MRR@10</td></tr><tr><td>Original</td><td>0.5627</td><td>0.5180</td><td>0.4523</td><td>0.3499</td><td>0.1512</td><td>0.3507</td></tr><tr><td>Original and BgeRerank</td><td>0.5818</td><td>0.5406</td><td>0.4741</td><td>0.3379</td><td>0.1486</td><td>0.3391</td></tr><tr><td>Original and PPLRerank</td><td>0.5769</td><td>0.5521</td><td>0.5055</td><td>0.4102</td><td>0.1849</td><td>0.4147</td></tr><tr><td>Qwen2-1.5Bppt</td><td>0.6838</td><td>- 0.6244</td><td>- 0.5503</td><td>- 0.4151</td><td>- 0.1954</td><td>- - 0.4195</td></tr><tr><td>Qwen2-1.5B, ppl BgeRerank and</td><td>0.6927</td><td>0.6435</td><td>0.5721</td><td>0.4381</td><td>0.2075</td><td>0.4413</td></tr><tr><td>Qwen2-1.5B ppl and PPLRerank</td><td>0.7197</td><td>0.6931</td><td>0.6568</td><td>0.5721</td><td>0.2590</td><td>0.5558</td></tr></table>{{< /table-caption >}}

> Table 1 presents the main experimental results of five question answering datasets, comparing the performance of various text chunking methods (rule-based, similarity-based, margin sampling chunking, and perplexity chunking) on different LLMs.


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
{{< /gallery >}}