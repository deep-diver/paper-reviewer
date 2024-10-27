---
title: "Multi-Draft Speculative Sampling: Canonical Architectures and Theoretical Limits"
summary: "Boosting LLM inference speed, this paper introduces multi-draft speculative sampling, optimizing token selection via importance and speculative sampling for improved efficiency."
categories: ["AI Generated"]
tags: ["🔖 24-10-23", "🤗 24-10-25"]
showSummary: true
date: 2024-10-23
draft: false
---

### TL;DR


{{< lead >}}

This paper tackles the slow speed of Large Language Model (LLM) inference. Current LLMs generate text one word at a time, which is inefficient.  The authors propose 'multi-draft speculative sampling' as a solution.  This involves using several smaller models (drafts) to generate multiple word options simultaneously. A larger, more accurate model then selects the best option from these drafts. The paper shows that the best word selection method can be broken down into two simpler steps.  First, use a technique similar to 'importance sampling' to choose a word from the drafts. Then, use existing 'speculative sampling' to refine the choice and ensure it aligns with the larger model's distribution.  Through theoretical analysis and experiments using the OPT model, they demonstrate consistent improvements in speed and efficiency compared to existing approaches. They also provide new insights into the theoretical limits of this technique.  The improvements are shown across various tasks with a consistent improvement across three tasks, XSum, Dolly, and WMT. Overall, the work offers a novel, efficient method for LLM inference, providing both theoretical and practical advancements.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18234" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This research paper introduces a novel approach to accelerate large language model inference called multi-draft speculative sampling.  It optimizes token selection by decomposing the process into importance sampling and speculative sampling, resulting in significant improvements in efficiency.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} Multi-draft speculative sampling significantly improves the efficiency of large language model inference. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} The optimal token selection scheme can be decomposed into two steps: importance sampling and single-draft speculative sampling. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} A new token-level selection scheme based on weighted importance sampling consistently improves block efficiency and token rates. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_4_0.png "🔼 Figure 1: Optimal Approach for Multi-Draft Speculative Sampling")

> The figure illustrates the optimal two-step approach for multi-draft speculative sampling, which involves importance weighted sampling followed by speculative sampling.





![](charts/charts_6_0.png "🔼 Figure 2: Numerical evaluation of Pr(accept) for the optimal scheme (Theorem 3) as well as two baseline schemes – SpecTr (Sun et al., 2024b) and SpecInfer (Miao et al., 2024). For sake of illustration we select alphabet Ω = {1,2,3} and p = [1/3,1/3, 1/3]. The left plot sets q = [1/3, q2, 2/3-q2] while the right plot sets q = [1/6, q2, 5/6 - q2] where q2 is varied on the x-axis.")

> The chart numerically evaluates the acceptance probability for the optimal scheme and two baseline schemes (SpecTr and SpecInfer) by varying the target distribution parameter q2.





{{< table-caption caption="🔽 Table 3: Comparison of average acceptance probability across different tasks for K = 2, 4, 8 drafts." >}}
<table id='2' style='font-size:16px'><tr><td>Ashish Khisti * 12</td><td>M.Reza Ebrahimi ・1</td><td>Hassan Dbouk1</td></tr><tr><td>Arash Behboodi1</td><td>Roland Memisevic 1</td><td>Christos Louizos t 1</td></tr></table>{{< /table-caption >}}

> This table compares the average acceptance probability across different tasks (XSum, Dolly, WMT) for varying numbers of draft models (K=2, 4, 8) using different methods (Optimal, IS, SpecTr, SpecInfer).



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_24_0.png "🔼 Figure 1: Optimal Approach for Multi-Draft Speculative Sampling")

> The figure illustrates the optimal two-step scheme for multi-draft speculative sampling, showing importance weighted sampling followed by speculative sampling.


![](figures/figures_35_0.png "🔼 Figure 2: Numerical evaluation of Pr(accept) for the optimal scheme (Theorem 3) as well as two baseline schemes – SpecTr (Sun et al., 2024b) and SpecInfer (Miao et al., 2024). For sake of illustration we select alphabet Ω = {1,2,3} and p = [1/3,1/3, 1/3]. The left plot sets q = [1/3, q2, 2/3-q2] while the right plot sets q = [1/6, q2, 5/6 - q2] where q2 is varied on the x-axis.")

> The figure shows a numerical evaluation of the acceptance probability for the optimal scheme and two baseline schemes, SpecTr and SpecInfer, for different values of q2.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_9_0.png "🔼 Figure 3: Performance comparison of different multi-draft schemes, while we vary the temperature of the two draft models.")

> The chart compares the block efficiency and token rate improvement over single-draft speculative decoding for different multi-draft schemes (IS, SpecTr, SpecInfer) across three datasets (Dolly, XSum, WMT) while varying the temperature of the draft models.


![](charts/charts_10_0.png "🔼 Figure 4: Performance comparison of different multi-draft schemes. The temperature of the first draft model is set to 1.2, while we vary the temperature of the other draft.")

> The chart compares the performance of different multi-draft schemes across three datasets (Dolly, XSum, WMT) while varying the temperature of one draft model while keeping the other constant.


![](charts/charts_34_0.png "🔼 Figure 2: Numerical evaluation of Pr(accept) for the optimal scheme (Theorem 3) as well as two baseline schemes – SpecTr (Sun et al., 2024b) and SpecInfer (Miao et al., 2024). For sake of illustration we select alphabet Ω = {1,2,3} and p = [1/3,1/3, 1/3]. The left plot sets q = [1/3, q2, 2/3-q2] while the right plot sets q = [1/6, q2, 5/6 - q2] where q2 is varied on the x-axis.")

> The chart numerically evaluates the acceptance probability for the optimal scheme and compares it with two baseline schemes, SpecTr and SpecInfer, by varying the parameter q2.


![](charts/charts_34_1.png "🔼 Figure 2: Numerical evaluation of Pr(accept) for the optimal scheme (Theorem 3) as well as two baseline schemes – SpecTr (Sun et al., 2024b) and SpecInfer (Miao et al., 2024). For sake of illustration we select alphabet Ω = {1,2,3} and p = [1/3,1/3, 1/3]. The left plot sets q = [1/3, q2, 2/3-q2] while the right plot sets q = [1/6, q2, 5/6 - q2] where q2 is varied on the x-axis.")

> The chart numerically evaluates the acceptance probability for the optimal scheme and two baseline schemes (SpecTr and SpecInfer) by varying the target distribution parameter q2.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 1: Block efficiency achieved in the Dolly task for different number of draft models." >}}
<br><table id='4' style='font-size:16px'><tr><td>Scheme</td><td>K = 2</td><td>K = 3</td><td>K = 4</td><td>K = 5</td><td>K = 6</td></tr><tr><td>IS</td><td>2.13 土 0.05</td><td>2.22 士 0.05</td><td>2.26 土 0.05</td><td>2.27 士 0.05</td><td>2.28 士 0.06</td></tr><tr><td>SpecInfer</td><td>1.76 士 0.04</td><td>1.86 士 0.05</td><td>1.95 土 0.05</td><td>2.00 士 0.04</td><td>2.04 士 0.05</td></tr><tr><td>SpecTr</td><td>1.77 土 0.04</td><td>1.89 土 0.05</td><td>1.96 土 0.05</td><td>2.03 士 0.06</td><td>2.08 土 0.04</td></tr></table>{{< /table-caption >}}

> Table 1 shows the block efficiency achieved by three different multi-draft speculative sampling methods using 2 to 6 draft models on the Dolly task.


{{< table-caption caption="🔽 Table 2: Effect of LP Truncation and Alphabet Truncation" >}}
<br><table id='4' style='font-size:18px'><tr><td></td><td></td><td>Block Efficiency</td><td>Token Rate (% improvement to SD)</td></tr><tr><td rowspan="4">Alphabet Truncation ( 2⌀ )</td><td>10</td><td>1.98 士 0.03</td><td>-0.57 士 3.38%</td></tr><tr><td>20</td><td>2.00 士 0.04</td><td>1.00 土 3.08%</td></tr><tr><td>40</td><td>2.05 士 0.04</td><td>6.63 土 3.18%</td></tr><tr><td>50</td><td>2.03 士 0.05</td><td>3.22 土 3.39%</td></tr><tr><td rowspan="3">LP-Truncation Threshold (s)</td><td>5</td><td>2.05 士 0.04</td><td>6.63 士 3.18%</td></tr><tr><td>10</td><td>2.04 土 0.05</td><td>1.52 土 3.47%</td></tr><tr><td>15</td><td>2.04 士 0.04</td><td>1.74 土 2.36%</td></tr></table>{{< /table-caption >}}

> Table 2 shows the effect of LP truncation and alphabet truncation on the block efficiency and token rate improvement over the single-draft baseline.


{{< table-caption caption="🔽 Table 3: Comparison of average acceptance probability across different tasks for K = 2, 4, 8 drafts." >}}
<br><table id='8' style='font-size:16px'><tr><td>Scheme</td><td colspan="3">XSum</td><td colspan="3">Dolly</td></tr><tr><td></td><td>K=2</td><td>K=4</td><td>K=8</td><td>K=2</td><td>K=4</td><td>K=8</td></tr><tr><td>Optimal</td><td>0.5009</td><td>0.5226</td><td>0.5419</td><td>0.6384</td><td>0.6731</td><td>0.6962</td></tr><tr><td>IS</td><td>0.4933</td><td>0.5145</td><td>0.5333</td><td>0.6348</td><td>0.6691</td><td>0.6919</td></tr><tr><td>SpecTr</td><td>0.4889</td><td>0.5083</td><td>0.5263</td><td>0.6246</td><td>0.6560</td><td>0.6800</td></tr><tr><td>SpecInfer</td><td>0.4875</td><td>0.5058</td><td>0.5227</td><td>0.6202</td><td>0.6489</td><td>0.6722</td></tr></table>{{< /table-caption >}}

> Table 3 compares the token-level acceptance probability across different methods for K=2, 4, and 8 drafts on three different tasks.


{{< table-caption caption="🔽 Table 4: Block Efficiency achieved in the Dolly Task with top-k sampling" >}}
<br><table id='12' style='font-size:18px'><tr><td rowspan="2">Sampling</td><td rowspan="2">Scheme</td><td colspan="2">K = 2 drafts</td><td colspan="2">K = 3 drafts</td></tr><tr><td>Block Efficiency</td><td>Loss</td><td>Block Efficiency</td><td>Loss</td></tr><tr><td rowspan="3">top-k (k = 10)</td><td>IS</td><td>2.48 土 0.01</td><td></td><td>2.59 士 0.02</td><td></td></tr><tr><td>SpecTr</td><td>2.43 土 0.01</td><td>98%</td><td>2.55 士 0.01</td><td>98%</td></tr><tr><td>SpecInfer</td><td>2.38 士 0.02</td><td>96%</td><td>2.49 士 0.02</td><td>96%</td></tr><tr><td rowspan="3">top-k (k = 5)</td><td>IS</td><td>2.52 士 0.02</td><td></td><td>2.63 士 0.03</td><td></td></tr><tr><td>SpecTr</td><td>2.48 土 0.02</td><td>98%</td><td>2.56 士 0.03</td><td>97%</td></tr><tr><td>SpecInfer</td><td>2.47 士 0.01</td><td>98%</td><td>2.55 士 0.04</td><td>97%</td></tr></table>{{< /table-caption >}}

> Table 4 compares the block efficiencies for different methods using K=2 and K=3 drafts, applying top-k sampling with k=10 and k=5, and using temperature of 1.0 for both models.


{{< table-caption caption="🔽 Table 5: ROUGE-L scores on the XSum task across various decoders and sampling temperatures." >}}
<br><table id='3' style='font-size:16px'><tr><td>Draft Temp.</td><td>1.2</td><td>1.4</td><td>1.6</td><td>2.0</td><td>2.4</td></tr><tr><td colspan="6">Decoder</td></tr><tr><td>IS</td><td>0.186 士 0.004</td><td>0.188 土 0.002</td><td>0.191 土 0.003</td><td>0.186 土 0.004</td><td>0.187 士 0.003</td></tr><tr><td>Signle-draft SD</td><td>0.190 士 0.006</td><td>0.185 士 0.005</td><td>0.190 士 0.004</td><td>0.186 士 0.003</td><td>0.186 士 0.004</td></tr><tr><td>SpecInfer</td><td>0.184 土 0.004</td><td>0.190 土 0.002</td><td>0.187 土 0.001</td><td>0.186 士 0.003</td><td>0.186 士 0.004</td></tr><tr><td>SpecTr</td><td>0.188 土 0.002</td><td>0.182 土 0.006</td><td>0.188 士 0.001</td><td>0.185 土 0.006</td><td>0.188 土 0.001</td></tr></table>{{< /table-caption >}}

> Table 5 presents ROUGE-L scores on the XSum task for different decoders (IS, single-draft, SpecInfer, SpecTr) and draft model temperatures.


{{< table-caption caption="🔽 Table 6: BLEU scores on the WMT dataset across various decoders and sampling temperatures." >}}
<br><table id='5' style='font-size:18px'><tr><td>Draft Temp.</td><td>1.2</td><td>1.4</td><td>1.6</td><td>2.0</td><td>2.4</td></tr><tr><td colspan="6">Decoder</td></tr><tr><td>IS</td><td>0.037 士 0.002</td><td>0.038 土 0.004</td><td>0.034 土 0.002</td><td>0.039 士 0.003</td><td>0.039 土 0.002</td></tr><tr><td>Signle-draft SD</td><td>0.036 土 0.000</td><td>0.037 土 0.003</td><td>0.038 土 0.004</td><td>0.037 士 0.003</td><td>0.038 土 0.002</td></tr><tr><td>SpecInfer</td><td>0.035 土 0.003</td><td>0.039 土 0.004</td><td>0.035 士 0.003</td><td>0.034 士 0.009</td><td>0.036 土 0.003</td></tr><tr><td>SpecTr</td><td>0.039 土 0.001</td><td>0.037 土 0.001</td><td>0.039 土 0.001</td><td>0.036 士 0.002</td><td>0.035 士 0.001</td></tr></table>{{< /table-caption >}}

> Table 6 presents BLEU scores on the WMT dataset for different decoding methods (IS, single-draft speculative decoding, SpecInfer, and SpecTr) across various draft and target model temperatures.


{{< table-caption caption="🔽 Table 7: ROUGE-L scores on the XSum task across various decoders and sampling temperatures." >}}
<table id='8' style='font-size:16px'><tr><td></td><td colspan="5">Temperature</td></tr><tr><td>Draft 1</td><td colspan="5">1.2</td></tr><tr><td>Draft 2</td><td>1.2</td><td>1.6</td><td>2.0</td><td>2.4</td><td>N/A</td></tr><tr><td>Decoder</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IS</td><td>0.187 士 0.004</td><td>0.189 土 0.007</td><td>0.189 士 0.001</td><td>0.191 士 0.002</td><td>-</td></tr><tr><td>SpecInfer</td><td>0.184 士 0.004</td><td>0.190 土 0.003</td><td>0.185 土 0.006</td><td>0.189 土 0.006</td><td></td></tr><tr><td>Single-draft SD</td><td>-</td><td></td><td></td><td>-</td><td>0.190 土 0.006</td></tr></table>{{< /table-caption >}}

> Table 7 compares the ROUGE-L scores for different multi-draft schemes across various decoders and sampling temperatures on the XSum task.


{{< table-caption caption="🔽 Table 8: BLEU scores on the WMT dataset across various decoders and sampling temperatures." >}}
<table id='10' style='font-size:14px'><tr><td></td><td colspan="5">Temperature</td></tr><tr><td>Draft 1</td><td colspan="5">1.2</td></tr><tr><td>Draft 2</td><td>1.2</td><td>1.6</td><td>2.0</td><td>2.4</td><td>N/A</td></tr><tr><td>Decoder</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IS</td><td>0.036 土 0.003</td><td>0.035 土 0.002</td><td>0.036 土 0.002</td><td>0.035 士 0.002</td><td>-</td></tr><tr><td>SpecInfer</td><td>0.035 士 0.003</td><td>0.038 土 0.005</td><td>0.041 土 0.002</td><td>0.040 土 0.002</td><td></td></tr><tr><td>Single-draft SD</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.036 士 0.000</td></tr></table>{{< /table-caption >}}

> Table 8 shows the BLEU scores on the WMT dataset for different multi-draft schemes while varying the temperature of the two draft models.


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
<img src="paper_images/37.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/38.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
{{< /gallery >}}