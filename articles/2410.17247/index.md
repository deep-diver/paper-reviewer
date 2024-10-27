---
title: "PyramidDrop: Accelerating Your Large Vision-Language Models via Pyramid Visual Redundancy Reduction"
summary: "PyramidDrop boosts Large Vision-Language Model efficiency by 40% in training and 55% in inference, dropping redundant visual tokens in deeper layers while maintaining performance."
categories: ["AI Generated"]
tags: ["🔖 24-10-22", "🤗 24-10-23"]
showSummary: true
date: 2024-10-22
draft: false
---

### TL;DR


{{< lead >}}

Large Vision-Language Models (LVLMs) are computationally expensive due to the numerous image tokens used.  This paper introduces PyramidDrop, a method that speeds up both training and inference. PyramidDrop analyzes the importance of image tokens at different layers of the model, finding that shallower layers heavily utilize all tokens while deeper layers have increased redundancy.  Leveraging this, PyramidDrop strategically drops a portion of image tokens in deeper layers.  Experimental results using LLaVA-NeXT show a 40% reduction in training time and a 55% reduction in inference FLOPs without significant performance decline.  It also works as a plug-and-play method for faster inference, outperforming comparable methods.  This research highlights the importance of analyzing token redundancy within models for efficiency improvements.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.17247" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This research paper introduces PyramidDrop, a novel visual redundancy reduction strategy for Large Vision-Language Models (LVLMs). It significantly accelerates both training and inference times by selectively dropping visual tokens in deeper layers, with minimal performance loss. The study reveals that visual tokens are increasingly redundant as models progress through deeper layers, which is a crucial insight for optimizing LVLM efficiency.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} PyramidDrop accelerates LVLM training by 40% and inference by 55% with negligible performance loss. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Visual token redundancy progressively increases in deeper LVLM layers. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} PyramidDrop is a plug-and-play method for inference acceleration without additional training. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_4_0.png "🔼 Figure 2: Overview of PyramidDrop. We divide the forward pass of the LLM into multiple stages, and drop part of the image tokens at the end of each stage with a pre-defined ratio. The dropping is based on a lightweight attention calculation with a negligible time overhead, and according to this criterion, the LLM accurately selects important image tokens related to instruction. Due to the efficient redundancy reduction strategy, the average sequence length decreases rapidly.")

> The figure illustrates the PyramidDrop method, showing how the model divides the forward pass into stages and drops image tokens at the end of each stage based on attention weights, reducing the sequence length.





![](charts/charts_3_0.png "🔼 Figure 1: Observatioins about visual redundancy acoross layers. Left: TextVQA performance of LLaVA-1.5 with varying ratio of retained image tokens at different layer. The preserved image tokens are those that receive the highest attention from the text tokens. Right: Visualization of attention map in shallow and deep layers.")

> The chart displays the TextVQA performance of LLaVA-1.5 with varying ratios of retained image tokens at different layers, and visualizes the attention map in shallow and deep layers to show that visual redundancy progressively increases in deeper layers of the model.





{{< table-caption caption="🔽 Table 1: LVLM w and w/o our method on 6 benchmarks. Benchmark names are abbreviated due to space limits. MMB: MMBenchmark (Liu et al., 2023); MMBCN: MMBench-Chinese (Liu et al., 2023); SEED¹: SEED-Bench (Image) (Li et al., 2023b). We denote PyramidDrop as PDrop." >}}
<br><table id='1' style='font-size:14px'><tr><td>Model</td><td>Train & Infer</td><td>GPU hours</td><td>#patches</td><td>Infer Flops(T)</td><td>MME</td><td>MMB</td><td>MMB CN</td><td>SEEDI</td><td>MM Star</td><td>POPE</td><td>Avg</td></tr><tr><td rowspan="4">LLaVA -NeXT-7B</td><td>vanilla</td><td>366</td><td>5</td><td>20.8</td><td>1534.1</td><td>68.7</td><td>60.5</td><td>71.1</td><td>41.1</td><td>86.1</td><td>67.4</td></tr><tr><td>PDrop</td><td>218</td><td>5</td><td>9.46</td><td>1540.8</td><td>67.8</td><td>60.6</td><td>69.9</td><td>41.7</td><td>86.5</td><td>67.3</td></tr><tr><td>vanilla</td><td>483</td><td>9</td><td>40.6</td><td>1544.7</td><td>67.4</td><td>60.0</td><td>69.5</td><td>40.0</td><td>86.3</td><td>66.7</td></tr><tr><td>PDrop</td><td>269</td><td>9</td><td>18.1</td><td>1542.0</td><td>68.1</td><td>61.0</td><td>70.3</td><td>40.9</td><td>86.6</td><td>67.3</td></tr><tr><td rowspan="2">LLaVA -1.5-7B</td><td>vanilla</td><td>104</td><td>1</td><td>3.82</td><td>1510.7</td><td>64.3</td><td>58.3</td><td>66.1</td><td>33.2</td><td>85.9</td><td>63.9</td></tr><tr><td>PDrop</td><td>79</td><td>1</td><td>1.78</td><td>1467.3</td><td>66.1</td><td>58.5</td><td>65.5</td><td>34.0</td><td>86.0</td><td>63.9</td></tr></table>{{< /table-caption >}}

> Table 1 presents the performance comparison of vanilla LVLMs and LVLMs using PyramidDrop on six benchmarks, showing training and inference efficiency improvements.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_10_0.png "🔼 Figure 5: Visualization of token dropping in LLM of LLaVA -1.5. We compute the attention score of image tokens received from the last instruction token as the ranking criterion, and find LLM accurately retain image tokens according to instruction.")

> The figure visualizes how PyramidDrop effectively preserves image tokens related to the instruction, as shown by LLaVA-1.5, accurately retaining relevant tokens for accurate answers.


![](figures/figures_10_1.png "🔼 Figure 5: Visualization of token dropping in LLM of LLaVA-1.5. We compute the attention score of image tokens received from the last instruction token as the ranking criterion, and find LLM accurately retain image tokens according to instruction.")

> The figure visualizes how PyramidDrop effectively preserves image tokens related to the instruction by showing examples of retained image tokens at different layers of the LLaVA-1.5 model.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_8_0.png "🔼 Figure 3: We compare the performance of the original LLaVA-1.5 and LLaVA-1.5 trained using PDrop, where we preserve different ratios of image tokens at layer 2, 8, 16, and 24, respectively. The horizontal axis represents the proportion of retained image tokens according to attention score.")

> The chart displays the TextVQA performance of LLaVA-1.5 models (original and trained with PyramidDrop) at different layers with varying ratios of retained image tokens, demonstrating the impact of PyramidDrop on model performance at different depths.


![](charts/charts_8_1.png "🔼 Figure 3: We compare the performance of the original LLaVA-1.5 and LLaVA-1.5 trained using PDrop, where we preserve different ratios of image tokens at layer 2, 8, 16, and 24, respectively. The horizontal axis represents the proportion of retained image tokens according to attention score.")

> The chart compares the performance of the original LLaVA-1.5 and the model trained with PyramidDrop across different layers and varying ratios of retained image tokens, showing that PyramidDrop maintains or improves performance while reducing tokens.


![](charts/charts_10_0.png "🔼 Figure 4: The performance of LLaVA-NeXT-7B with different inference acceleration strategies. PDrop (without training) outperforms FastV on DocVQA, ChartQA, and GQA with across various inference cost budgets.")

> The chart compares the performance of PyramidDrop and FastV inference acceleration strategies across various inference cost budgets (TFLOPs) on three vision-language benchmarks (DocVQA, ChartQA, and GQA).


![](charts/charts_10_1.png "🔼 Figure 1: Observatioins about visual redundancy acoross layers. Left: TextVQA performance of LLaVA-1.5 with varying ratio of retained image tokens at different layer. The preserved image tokens are those that receive the highest attention from the text tokens. Right: Visualization of attention map in shallow and deep layers.")

> The chart visualizes the impact of dropping different ratios of image tokens at various layers of a Large Vision Language Model (LLaVM) on TextVQA task performance and attention patterns, revealing that visual redundancy increases with depth.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: LLaVA -NeXT-7B on other 8 benchmarks. We report more benchmarks which contain lots of fine-grained content to examine the performance." >}}
<br><table id='3' style='font-size:14px'><tr><td>Model</td><td>Train & Infer</td><td>GPU hours</td><td>#patches</td><td>Doc VQA</td><td>Info VQA</td><td>Text VQA</td><td>Chart QA</td><td>OCR VQA</td><td>VQA V2</td><td>Viz Wiz</td><td>GQA</td><td>Avg</td></tr><tr><td rowspan="4">LLaVA -NeXT-7B</td><td>vanilla</td><td>366</td><td>5</td><td>70.0</td><td>33.3</td><td>67.2</td><td>64.0</td><td>63.7</td><td>81.7</td><td>59.6</td><td>64.2</td><td>63.0</td></tr><tr><td>PDrop</td><td>218</td><td>5</td><td>69.0</td><td>31.7</td><td>67.7</td><td>63.0</td><td>63.1</td><td>81.5</td><td>61.0</td><td>63.9</td><td>62.6</td></tr><tr><td>vanilla</td><td>483</td><td>9</td><td>74.3</td><td>36.2</td><td>67.6</td><td>63.0</td><td>63.8</td><td>81.6</td><td>58.0</td><td>63.5</td><td>63.5</td></tr><tr><td>PDrop</td><td>269</td><td>9</td><td>75.0</td><td>37.4</td><td>68.4</td><td>64.3</td><td>63.5</td><td>81.7</td><td>60.6</td><td>64.1</td><td>64.4</td></tr></table>{{< /table-caption >}}

> Table 2 presents the performance comparison of the LLaVA-NeXT-7B model with and without PyramidDrop across eight benchmarks, showcasing the model's performance on benchmarks containing detailed information.


{{< table-caption caption="🔽 Table 3: Performance gain with models trained with PyramidDrop. Directly applying efficient inference strategies like FastV to models trained with PyramidDrop yields substantial improvement." >}}
<br><table id='4' style='font-size:18px'><tr><td>Model</td><td>Train</td><td>Infer</td><td>Infer Flops(T)</td><td>ChartQA</td><td>DocVQA</td><td>TextVQA</td><td>MME</td><td>SQAI</td><td>POPE</td><td>Average</td></tr><tr><td rowspan="5">LLaVA -NeXT-7B</td><td>vanilla</td><td>vanilla</td><td>20.8</td><td>64.0</td><td>70.0</td><td>67.2</td><td>1534.1</td><td>70.4</td><td>86.1</td><td>72.4</td></tr><tr><td>PDrop</td><td>PDrop</td><td>9.46</td><td>63.0</td><td>69.0</td><td>67.7</td><td>1540.8</td><td>70.1</td><td>86.5</td><td>72.2</td></tr><tr><td>vanilla</td><td>FastV</td><td>10.6</td><td>55.9</td><td>62.1</td><td>66.0</td><td>1482.0</td><td>69.2</td><td>85.5</td><td>68.8</td></tr><tr><td>PDrop</td><td>FastV</td><td>10.6</td><td>59.9</td><td>63.9</td><td>65.6</td><td>1492.7</td><td>68.9</td><td>86.8</td><td>70.0</td></tr><tr><td>A</td><td></td><td></td><td>+4.0</td><td>+1.8</td><td>-0.4</td><td>+0.5</td><td>-0.3</td><td>+1.3</td><td>+1.2</td></tr></table>{{< /table-caption >}}

> Table 3 shows the performance improvement achieved by applying FastV inference strategy to models trained with PyramidDrop, demonstrating the substantial performance gains obtained.


{{< table-caption caption="🔽 Table 4: Ablation studies results. We adjust λ form 0.4 to 0.6 for investigating the influence on performance and training time." >}}
<br><table id='6' style='font-size:16px'><tr><td>Model</td><td>入</td><td>GPU hours</td><td>#patches</td><td>Infer Flops(T)</td><td>MME</td><td>MMB</td><td>GQA</td><td>MMB⌀N</td><td>SEEDI</td><td>Doc VQA</td><td>Info VQA</td><td>Avg</td></tr><tr><td rowspan="4">LLaVA -NeXT-7B</td><td>vanilla</td><td>366</td><td>5</td><td>20.8</td><td>1534.1</td><td>68.7</td><td>64.2</td><td>60.5</td><td>71.1</td><td>70.0</td><td>33.3</td><td>63.5</td></tr><tr><td>0.4</td><td>204</td><td>5</td><td>8.22</td><td>1558.4</td><td>68.1</td><td>63.7</td><td>60.5</td><td>69.5</td><td>66.6</td><td>31.8</td><td>62.6</td></tr><tr><td>0.5</td><td>218</td><td>5</td><td>9.46</td><td>1540.8</td><td>67.8</td><td>63.9</td><td>60.6</td><td>69.9</td><td>69.0</td><td>31.7</td><td>62.8</td></tr><tr><td>0.6</td><td>240</td><td>5</td><td>11.0</td><td>1511.4</td><td>68.1</td><td>64.1</td><td>60.5</td><td>70.4</td><td>69.8</td><td>33.0</td><td>63.1</td></tr><tr><td rowspan="4">LLaVA -1.5-7B</td><td>vanilla</td><td>104</td><td>1</td><td>3.82</td><td>1510.7</td><td>64.3</td><td>62.0</td><td>58.3</td><td>66.1</td><td>21.4</td><td>20.4</td><td>52.6</td></tr><tr><td>0.4</td><td>75</td><td>1</td><td>1.54</td><td>1478.8</td><td>66.2</td><td>61.7</td><td>58.0</td><td>64.5</td><td>21.1</td><td>19.9</td><td>52.2</td></tr><tr><td>0.5</td><td>79</td><td>1</td><td>1.78</td><td>1467.3</td><td>66.1</td><td>61.9</td><td>58.5</td><td>65.5</td><td>21.5</td><td>20.2</td><td>52.4</td></tr><tr><td>0.6</td><td>82</td><td>1</td><td>2.06</td><td>1471.8</td><td>65.9</td><td>62.0</td><td>58.9</td><td>65.1</td><td>22.5</td><td>21.0</td><td>52.7</td></tr></table>{{< /table-caption >}}

> Table 4 presents the ablation study results of varying the hyperparameter λ (drop ratio) from 0.4 to 0.6, showing its impact on model performance and training time for two different LVLMs.


{{< table-caption caption="🔽 Table 5: Inference acceleration performance. We compare PDrop, FastV and vanilla model, and find PDrop outperforms FastV on almost all benchmarks. PDrop here is as an inference-only strategy." >}}
<br><table id='1' style='font-size:14px'><tr><td>Model</td><td>Inference Strategy</td><td>TFLOPS</td><td>MME</td><td>SQAI</td><td>MMB�N</td><td>GQA</td><td>POPE</td><td>TextVQA</td><td>ChartQA</td><td>DocVQA</td><td>Avg</td></tr><tr><td rowspan="4">LLaVA -NeXT-7B</td><td>vanilla</td><td>20.8</td><td>1534.1</td><td>70.4</td><td>60.5</td><td>64.2</td><td>86.1</td><td>67.2</td><td>64.0</td><td>70.0</td><td>69.9</td></tr><tr><td>FastV</td><td>10.6</td><td>1482.0</td><td>69.2</td><td>60.0</td><td>63.0</td><td>85.5</td><td>66.0</td><td>55.9</td><td>62.1</td><td>67.0</td></tr><tr><td>PDrop</td><td>9.5</td><td>1533.0</td><td>69.4</td><td>59.9</td><td>63.9</td><td>86.4</td><td>67.0</td><td>59.1</td><td>65.6</td><td>68.5</td></tr><tr><td>A</td><td></td><td>+2.5</td><td>+0.2</td><td>+0.1</td><td>+0.9</td><td>+0.9</td><td>+1.0</td><td>+3.2</td><td>+3.5</td><td>+1.5</td></tr><tr><td rowspan="4">LLaVA -1.5-7B</td><td>vanilla</td><td>3.82</td><td>1510.7</td><td>66.8</td><td>58.3</td><td>62</td><td>85.9</td><td>58.2</td><td>18.2</td><td>21.4</td><td>55.8</td></tr><tr><td>FastV</td><td>2.01</td><td>1475.6</td><td>68.5</td><td>56.8</td><td>59.6</td><td>84.8</td><td>57.1</td><td>17.8</td><td>19.2</td><td>54.7</td></tr><tr><td>PDrop</td><td>1.78</td><td>1500.8</td><td>69.2</td><td>58.5</td><td>60.1</td><td>84.8</td><td>57.5</td><td>18.6</td><td>21.1</td><td>55.6</td></tr><tr><td>A</td><td></td><td>+1.3</td><td>+0.7</td><td>+1.7</td><td>+0.5</td><td>+0.0</td><td>+0.4</td><td>+0.8</td><td>+1.9</td><td>+0.9</td></tr></table>{{< /table-caption >}}

> Table 5 compares the inference acceleration performance of PyramidDrop, FastV, and a vanilla model across various benchmarks, showing PyramidDrop's superior performance when used as an inference-only strategy.


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
{{< /gallery >}}