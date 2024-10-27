---
title: "LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding"
summary: "LongVU efficiently processes hour-long videos for improved video-language understanding by adaptively compressing video tokens while preserving visual details."
categories: ["AI Generated"]
tags: ["🔖 24-10-22", "🤗 24-10-24"]
showSummary: true
date: 2024-10-22
draft: false
---

### TL;DR


{{< lead >}}

LongVU tackles the challenge of processing long videos with Large Language Models (LLMs) by using a smart compression method.  Current LLMs have limited context windows, making long videos problematic. LongVU cleverly reduces the number of video tokens (data pieces representing video frames) while keeping important visual information. It does this by identifying similar and redundant frames, strategically reducing the number of tokens needed to describe them. The result is that LongVU can efficiently handle much longer videos than before while maintaining accuracy on video understanding tasks, such as answering questions about a video.  Experiments show significant improvements over existing approaches, particularly with very long videos (an hour or more). Importantly, LongVU even works well with smaller LLMs, making it more practical to deploy.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.17434" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
To summarize the academic research paper on LongVU, a spatiotemporal adaptive compression mechanism for long video language understanding.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} LongVU uses a novel spatiotemporal adaptive compression technique to handle long videos within limited context lengths. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} The method outperforms existing approaches on various video understanding benchmarks, especially for hour-long videos. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} LongVU scales effectively to smaller LLMs while maintaining state-of-the-art performance. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_4_0.png "🔼 Figure 2. Architecture of LongVU. Given a densely sampled video frames, we first utilize DINOv2 (Oquab et al., 2023) prior to remove redundant frames, and fuse the remaining frame features from both SigLIP (Zhai et al., 2023) and DINOv2 (Oquab et al., 2023), described in Section 3.1. Then we selectively reduce visual tokens via cross-modal query, detailed in Section 3.2. Finally, as demonstrated in Section 3.3, we conduct spatial token compression based on temporal dependencies to further meet the context length of LLMs.")

> The figure illustrates the architecture of LongVU, detailing its spatiotemporal adaptive token compression mechanism which involves temporal reduction using DINOv2, selective feature reduction via cross-modal query, and spatial token compression based on temporal dependencies.





![](charts/charts_2_0.png "🔼 Figure 1 Effectiveness of our LongVU over commonly-used uniform sampling and dense sampling. Uniform sampling overlooks critical frames due to its sparse nature. Dense sampling may surpass the maximum context length, leading to truncation of tokens from targeted frames. In contrast, our method can adaptively conduct spatiotemporal compression, accommodating long video sequences while preserving more visual details.")

> The chart compares the effectiveness of LongVU against uniform and dense sampling methods for processing long videos, highlighting LongVU's adaptive spatiotemporal compression for better visual detail preservation.





{{< table-caption caption="🔽 Table 1 Results on comprehensive video understanding benchmarks" >}}
<table id='5' style='font-size:14px'><tr><td rowspan="2">Models</td><td rowspan="2">Size</td><td rowspan="2">Context Length</td><td rowspan="2">#Frames</td><td rowspan="2">EgoSchema</td><td rowspan="2">MVBench</td><td rowspan="2">MLVU</td><td colspan="2">VideoMME</td></tr><tr><td>Overall</td><td>Long</td></tr><tr><td>Duration</td><td></td><td></td><td></td><td>179.8 sec</td><td>16 sec</td><td>3~120 min</td><td>1〜60 min</td><td>30〜60 min</td></tr><tr><td>Proprietary Models</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GPT4-V (OpenAI, 2023)</td><td>-</td><td>-</td><td>1fps</td><td>55.6</td><td>43.7</td><td>-</td><td>60.7</td><td>56.9</td></tr><tr><td>GPT4-o (OpenAI, 2024)</td><td>-</td><td>-</td><td>1fps</td><td>72.2</td><td>64.6</td><td>66.2</td><td>77.2</td><td>72.1</td></tr><tr><td>Open-Source Video MLLMs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Video-LLaVA (Lin et al., 2023)</td><td>7B</td><td>4k</td><td>8</td><td>38.4</td><td>41.0</td><td>47.3</td><td>40.4</td><td>38.1</td></tr><tr><td>LLaMA-VID (Li et al., 2023d)</td><td>7B</td><td>4k</td><td>1fps</td><td>38.5</td><td>41.9</td><td>33.2</td><td>-</td><td>-</td></tr><tr><td>Chat-UniVi (Jin et al., 2023)</td><td>7B</td><td>4k</td><td>64</td><td>-</td><td>-</td><td>-</td><td>45.9</td><td>41.8</td></tr><tr><td>ShareGPT4Video (Chen et al., 2024)</td><td>8B</td><td>8k</td><td>16</td><td>-</td><td>51.2</td><td>46.4</td><td>43.6</td><td>37.9</td></tr><tr><td>LLaVA-NeXT-Video (Zhang et al., 2024b)</td><td>7B</td><td>8k</td><td>32</td><td>43.9</td><td>33.7</td><td>-</td><td>46.5</td><td>-</td></tr><tr><td>VideoLLaMA2 (Cheng et al., 2024)</td><td>7B</td><td>8k</td><td>32</td><td>51.7</td><td>54.6</td><td>48.5</td><td>46.6</td><td>43.8</td></tr><tr><td>LongVA (Zhang et al., 2024a)</td><td>7B</td><td>224k</td><td>128</td><td>-</td><td>-</td><td>56.3</td><td>54.3</td><td>47.6</td></tr><tr><td>VideoChat2 (Li et al., 2024b)</td><td>7B</td><td>8k</td><td>16</td><td>54.4</td><td>60.4</td><td>47.9</td><td>54.6</td><td>39.2</td></tr><tr><td>LLaVA-OneVision (Li et al., 2024a)</td><td>7B</td><td>8k</td><td>32</td><td>60.1</td><td>56.7</td><td>64.7</td><td>58.2</td><td>46.7</td></tr><tr><td>LongVU (Ours)</td><td>7B</td><td>8k</td><td>1fps</td><td>67.6</td><td>66.9</td><td>65.4</td><td>60.6</td><td>59.5</td></tr></table>{{< /table-caption >}}

> Table 1 presents a quantitative comparison of LongVU against various state-of-the-art video understanding models across four benchmarks, showcasing LongVU's superior performance.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_8_1.png "🔼 Figure 3 Examples for various video understanding capabilities of LongVU model. We showcase that our LongVU is able to complete different types of video understanding tasks.")

> Figure 3 shows examples of LongVU's capabilities in various video understanding tasks, such as spatial-temporal orientation awareness, detailed description, action counting, and hour-long video understanding.


![](figures/figures_8_2.png "🔼 Figure 2. Architecture of LongVU. Given a densely sampled video frames, we first utilize DINOv2 (Oquab et al., 2023) prior to remove redundant frames, and fuse the remaining frame features from both SigLIP (Zhai et al., 2023) and DINOv2 (Oquab et al., 2023), described in Section 3.1. Then we selectively reduce visual tokens via cross-modal query, detailed in Section 3.2. Finally, as demonstrated in Section 3.3, we conduct spatial token compression based on temporal dependencies to further meet the context length of LLMs.")

> The figure illustrates the architecture of LongVU, a spatiotemporal adaptive compression mechanism for processing long videos.


![](figures/figures_16_0.png "🔼 Figure 6. Similarity comparison between SigLIP (Zhai et al., 2023) and DINOv2 (Oquab et al., 2023) features. The similarity is calculated between the first frame and the remainings. DINO concentrating on vision centric task effectively capture subtle frame differences compared with SigLIP (Zhai et al., 2023) which is aligned on semantic space.")

> The figure shows a comparison of feature similarity between SigLIP and DINOv2, illustrating DINOv2's superior ability to capture subtle frame differences due to its focus on visual-centric tasks.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_10_0.png "🔼 Figure 4 We randomly sample hundreds of videos to demonstrate the frames/tokens level reduction rate. (a) The number of frames before/after temporal reduction based on DINOv2 features (Section 3.1). (b) The number of tokens before/after spatial token compression (Section 3.3).")

> The chart displays the number of frames and tokens before and after temporal and spatial reduction, respectively, demonstrating the effectiveness of the proposed compression method.


![](charts/charts_10_1.png "🔼 Figure 7 Needle-In-A-Video-Haystack results. Our spatiotemporal adaptive token compression scheme improves the score for locating the needle frame.")

> The heatmap visualizes the performance of different models (with and without different components) on the needle-in-a-haystack task, showing the impact of the spatiotemporal compression strategy.


![](charts/charts_10_2.png "🔼 Figure 7 Needle-In-A-Video-Haystack results. Our spatiotemporal adaptive token compression scheme improves the score for locating the needle frame.")

> The heatmap visualizes the performance of the needle-in-a-haystack task under different video lengths and compression strategies, showing improved performance with the proposed spatiotemporal adaptive token compression.


![](charts/charts_17_0.png "🔼 Figure 7 Needle-In-A-Video-Haystack results. Our spatiotemporal adaptive token compression scheme improves the score for locating the needle frame.")

> The heatmap shows the performance of different methods for locating a needle frame in a video with varying lengths and depths.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2 Results of small-size video language models across video understanding benchmarks." >}}
<table id='3' style='font-size:14px'><tr><td rowspan="2">Models</td><td rowspan="2">EgoSchema</td><td rowspan="2">MVBench</td><td colspan="2">VideoMME</td><td rowspan="2">MLVU</td></tr><tr><td>Overall</td><td>Long</td></tr><tr><td>InternVL2 (InternLM2-1.8B) (OpenGVLab, 2024)</td><td>-</td><td>60.2</td><td>47.3</td><td>42.6</td><td>-</td></tr><tr><td>VideoChat2 (Phi-3-mini-4B) (Li et al., 2024b)</td><td>56.7</td><td>55.1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Phi-3.5-vision-instruct (Phi-3-mini-4B) (Abdin et al., 2024)</td><td>-</td><td>-</td><td>50.8</td><td>43.8</td><td>-</td></tr><tr><td>LongVU (Ours) (Llama3.2-3B)</td><td>59.1</td><td>60.9</td><td>51.5</td><td>47.2</td><td>55.9</td></tr></table>{{< /table-caption >}}

> Table 2 presents the performance comparison of several small-size video language models on various video understanding benchmarks, including EgoSchema, MVBench, VideoMME (Overall and Long subsets), and MLVU.


{{< table-caption caption="🔽 Table 3 Ablation studies of number of tokens per frame, different context lengths, and our spatiotemporal compression components." >}}
<table id='2' style='font-size:16px'><tr><td>Methods</td><td>Context Length</td><td>#Tokens</td><td>EgoSchema</td><td>VideoMME</td><td>MLVU</td></tr><tr><td>Uniform</td><td>16k</td><td>144</td><td>67.12</td><td>60.01</td><td>64.70</td></tr><tr><td>DINO</td><td>16k</td><td>144</td><td>67.34</td><td>61.25</td><td>64.83</td></tr><tr><td>Uniform</td><td>8k</td><td>64</td><td>66.84</td><td>57.56</td><td>60.87</td></tr><tr><td>Uniform</td><td>8k</td><td>144</td><td>66.28</td><td>58.84</td><td>63.28</td></tr><tr><td>SigLIP</td><td>8k</td><td>64</td><td>66.04</td><td>58.63</td><td>62.17</td></tr><tr><td>DINO</td><td>8k</td><td>64</td><td>66.20</td><td>59.90</td><td>62.54</td></tr><tr><td>DINO + Query</td><td>8k</td><td>64,  144</td><td>67.30</td><td>60.08</td><td>65.05</td></tr><tr><td>DINO + Query + STC (default)</td><td>8k</td><td>dynamic</td><td>67.62</td><td>60.56</td><td>65.44</td></tr></table>{{< /table-caption >}}

> Table 3 shows the ablation study of the number of tokens per frame, different context lengths, and the spatiotemporal compression components of the proposed model LongVU, comparing their performance on EgoSchema, VideoMME, and MLVU benchmarks.


{{< table-caption caption="🔽 Table 4 Ablation study on each subtask in MLVU (Zhou et al., 2024)." >}}
<table id='4' style='font-size:16px'><tr><td>Stratgy</td><td>count</td><td>ego</td><td>needle</td><td>order</td><td>plotQA</td><td>anomaly</td><td>reasoning</td><td>Avg</td></tr><tr><td>DINO</td><td>24.15</td><td>59.09</td><td>68.16</td><td>52.89</td><td>71.24</td><td>74.00</td><td>86.36</td><td>62.54</td></tr><tr><td>DINO+Query</td><td>28.98</td><td>55.39</td><td>78.87</td><td>56.37</td><td>72.35</td><td>75.50</td><td>87.87</td><td>65.05</td></tr><tr><td>DINO+Query+STC (default)</td><td>28.98</td><td>59.37</td><td>76.33</td><td>58.30</td><td>71.61</td><td>76.00</td><td>87.50</td><td>65.44</td></tr></table>{{< /table-caption >}}

> The table presents ablation study results on each subtask of the MLVU benchmark, comparing different strategies for spatiotemporal compression.


{{< table-caption caption="🔽 Table 1 Results on comprehensive video understanding benchmarks" >}}
<table id='7' style='font-size:20px'><tr><td>Model</td><td>Short</td><td>Medium</td><td>Long</td><td>Overall</td><td>Reduction rate</td></tr><tr><td>1st frame in sliding window (default)</td><td>64.7</td><td>58.2</td><td>59.5</td><td>60.9</td><td>55.47%</td></tr><tr><td>(K/2)th frame in sliding window</td><td>64.7</td><td>58.7</td><td>58.6</td><td>60.7</td><td>54.97%</td></tr><tr><td>frame with high changes</td><td>64.7</td><td>58.2</td><td>58.3</td><td>60.4</td><td>55.62%</td></tr></table>{{< /table-caption >}}

> Table 1 presents the quantitative results of LongVU and other video understanding models across various benchmarks, including EgoSchema, MVBench, VideoMME, and MLVU, showing LongVU's superior performance.


{{< table-caption caption="🔽 Table 6 Training data statistics." >}}
<table id='3' style='font-size:14px'><tr><td>Modality</td><td>Task</td><td># Samples</td><td>Dataset</td></tr><tr><td>Image-Text</td><td>Single-Image</td><td>3.2M</td><td>LLaVA-OneVision</td></tr><tr><td rowspan="4">Video-Text</td><td>Captioning</td><td>43K</td><td>TextVR, MovieChat, YouCook2</td></tr><tr><td>Classification</td><td>1K</td><td>Kinetics-710</td></tr><tr><td>VQA</td><td>424K</td><td>NExTQA, CLEVRER, EgoQA, TGIF, WebVidQA, DiDeMo</td></tr><tr><td>Instruction</td><td>85K</td><td>ShareGPT4Video</td></tr></table>{{< /table-caption >}}

> Table 6 presents the training data statistics, including the modality, task, number of samples, and datasets used for training the LongVU model.


{{< table-caption caption="🔽 Table 1 Results on comprehensive video understanding benchmarks" >}}
<table id='5' style='font-size:16px'><tr><td>Model</td><td>Size</td><td>Frames</td><td>Short</td><td>Medium</td><td>Long</td><td>Overall</td></tr><tr><td>Video-LLa VA (Lin et al., 2023)</td><td>7B</td><td>8</td><td>46.1</td><td>40.7</td><td>38.1</td><td>41.6</td></tr><tr><td>ShareGPT4Video (Chen et al., 2024)</td><td>8B</td><td>16</td><td>53.6</td><td>39.3</td><td>37.9</td><td>43.6</td></tr><tr><td>Chat- Univi-v1.5 (Jin et al., 2023)</td><td>7B</td><td>64</td><td>51.2</td><td>44.6</td><td>41.8</td><td>45.9</td></tr><tr><td>VideoLLaMA2 (Cheng et al., 2024)</td><td>7B</td><td>16</td><td>59.4</td><td>47.6</td><td>43.8</td><td>50.3</td></tr><tr><td>VideoChat2 (Li et al., 2024b)</td><td>7B</td><td>16</td><td>52.8</td><td>39.4</td><td>39.2</td><td>43.8</td></tr><tr><td>LongVA (Zhang et al., 2024a)</td><td>7B</td><td>128</td><td>61.6</td><td>50.4</td><td>47.6</td><td>54.3</td></tr><tr><td>LLaVA-OneVision (Li et al., 2024a)</td><td>7B</td><td>32</td><td>69.1</td><td>53.3</td><td>46.7</td><td>58.2</td></tr><tr><td>LongVU (Ours)</td><td>7B</td><td>1fps</td><td>64.7</td><td>58.2</td><td>59.5</td><td>60.9</td></tr></table>{{< /table-caption >}}

> Table 1 presents the quantitative results of various video understanding models on four benchmarks, including proprietary and open-source models,  comparing their performance across different video lengths.


{{< table-caption caption="🔽 Table 8 Ablation study on with or without FPE." >}}
<table id='1' style='font-size:18px'><tr><td>Methods</td><td>Context Length</td><td>#Tokens</td><td>EgoSchema</td><td>VideoMME</td><td>MLVU</td></tr><tr><td>DINO + Query</td><td>8k</td><td>64, / 144</td><td>67.30</td><td>60.08</td><td>65.05</td></tr><tr><td>DINO + Query + STC (default)</td><td>8k</td><td>dynamic</td><td>67.62</td><td>60.56</td><td>65.44</td></tr><tr><td>DINO + Query + STC + FPE</td><td>8k</td><td>dynamic</td><td>67.87</td><td>60.89</td><td>64.56</td></tr></table>{{< /table-caption >}}

> The table shows the ablation study of the model with or without Frame Positional Encoding (FPE) on EgoSchema, VideoMME, and MLVU datasets.


{{< table-caption caption="🔽 Table 9 Strategy ablations on each subtask in MLVU (Zhou et al., 2024)." >}}
<table id='3' style='font-size:18px'><tr><td>Stratgy</td><td>count</td><td>ego</td><td>needle</td><td>order</td><td>plotQA</td><td>anomaly</td><td>reasoning</td><td>Avg</td></tr><tr><td>DINO</td><td>24.15</td><td>59.09</td><td>68.16</td><td>52.89</td><td>71.24</td><td>74.0</td><td>86.36</td><td>62.54</td></tr><tr><td>DINO+Query</td><td>28.98</td><td>55.39</td><td>78.87</td><td>56.37</td><td>72.35</td><td>75.5</td><td>87.87</td><td>65.05</td></tr><tr><td>DINO +Query+STC (default)</td><td>28.98</td><td>59.37</td><td>76.33</td><td>58.30</td><td>71.61</td><td>76.0</td><td>87.50</td><td>65.44</td></tr><tr><td>DINO + Query+STC+ FPE</td><td>29.46</td><td>60.79</td><td>74.08</td><td>52.12</td><td>71.79</td><td>74.5</td><td>86.74</td><td>64.56</td></tr></table>{{< /table-caption >}}

> Table 9 shows the ablation study of each subtask in MLVU (Zhou et al., 2024) using different strategies for spatial token compression.


{{< table-caption caption="🔽 Table 1 Results on comprehensive video understanding benchmarks" >}}
<table id='3' style='font-size:18px'><tr><td>Model</td><td>SQA-IMG</td><td>MMVP</td><td>POPE</td><td>RealWorldQA</td></tr><tr><td>Before video SFT</td><td>95.44</td><td>51.33</td><td>86.65</td><td>61.06</td></tr><tr><td>After video SFT</td><td>83.94</td><td>32.00</td><td>81.23</td><td>47.65</td></tr></table>{{< /table-caption >}}

> Table 1 presents the performance comparison of LongVU against various video understanding models across four benchmarks (EgoSchema, MVBench, VideoMME, and MLVU), showing its superior performance, especially in long-video tasks.


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
{{< /gallery >}}