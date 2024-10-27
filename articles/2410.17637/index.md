---
title: "MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models"
summary: "MIA-DPO boosts multi-image understanding in large vision-language models by cleverly augmenting data and using attention-aware selection, significantly improving performance."
categories: ["AI Generated"]
tags: ["🔖 24-10-23", "🤗 24-10-24"]
showSummary: true
date: 2024-10-23
draft: false
---

### TL;DR


{{< lead >}}

Large vision-language models (LVLMs) are struggling with multi-image tasks due to limited training data and annotation costs.  MIA-DPO solves this by cleverly augmenting single-image data with unrelated images, creating multi-image collages. The model's attention mechanism is used to identify and remove erroneous responses, improving data quality without relying on human annotation or expensive APIs.  Testing across five multi-image benchmarks showed an average performance boost of 3% on LLaVA-v1.5 and 4.3% on InternLM-XC2.5. Importantly, MIA-DPO's improvements in multi-image tasks did not negatively affect its performance on single-image tasks.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.17637" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
MIA-DPO enhances large vision-language models' understanding of multi-image contexts by cleverly augmenting single-image data and using attention mechanisms to filter out unreliable responses, achieving significant performance gains on various benchmarks.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} MIA-DPO effectively handles multi-image inputs by augmenting existing single-image data, reducing the need for extensive new annotations. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} The method uses attention mechanisms to identify and filter out unreliable model responses, improving the quality of training data. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} MIA-DPO demonstrates significant performance improvements on multiple multi-image benchmarks while maintaining performance on single-image tasks. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: (a) Overview of MIA-DPO. We transform single-image data (e.g., LLaVA 665k) into multi-image data by adding noisy or unrelated images and using language descriptions to specify the target image. Attention values are then used to detect hallucinations in multi-image contexts, filtering out rejected data for DPO optimization. (b) Benchmark Results. MIA-DPO excels across five multi-image benchmarks while maintaining competitive performance on seven single-image benchmarks, demonstrating its robustness in both single and multi-image tasks.")

> The figure shows an overview of the MIA-DPO framework and its performance on single-image and multi-image benchmarks.





![](charts/charts_7_0.png "🔼 Figure 5: Attention Ratio Statistic. We analyze the attention ratios distribution for different image counts across various data types, and use dashed lines to indicate the thresholds for each data set.")

> The chart displays the distribution of attention ratios for different numbers of images across three data types (Sequence, Grid Collage, and Pic-in-Pic), showing how the attention focus changes with the number of images and data type.





{{< table-caption caption="🔽 Table 1: Main results on multi-image benchmarks. We compare our MIA-DPO along with other DPO algorithms across five multi-image benchmarks. Our method brings significant performance improvements to both the classic LLaVa-v1.5 and the recent InternLM-XC2.5. In contrast, other single-image DPO methods perform poorly on multi-image benchmarks." >}}
<table id='1' style='font-size:14px'><tr><td>Models</td><td>Parameter</td><td>MMMU</td><td>BLINK</td><td>Mantis</td><td>NLVR2</td><td>MVBench</td><td>Average</td></tr><tr><td>GPT-4V (Achiam et al., 2023)</td><td>-</td><td>56.8</td><td>51.1</td><td>62.7</td><td>88.8</td><td>43.5</td><td>60.6</td></tr><tr><td>LLaVA-v1.6 (Li et al., 2024b)</td><td>7B</td><td>35.8</td><td>39.6</td><td>45.6</td><td>58.9</td><td>40.9</td><td>44.2</td></tr><tr><td>Qwen-VL-Chat (Bai et al., 2023)</td><td>7B</td><td>35.9</td><td>31.2</td><td>39.2</td><td>58.7</td><td>42.2</td><td>41.4</td></tr><tr><td>VideoLLaVA (Lin et al., 2023)</td><td>7B</td><td>-</td><td>38.9</td><td>35.9</td><td>56.5</td><td>44.3</td><td>-</td></tr><tr><td>Fuyu (Bavishi et al., 2023)</td><td>8B</td><td>27.9</td><td>36.6</td><td>27.2</td><td>51.1</td><td>30.2</td><td>34.6</td></tr><tr><td>Idefics2 (Lauren�on et al., 2024b)</td><td>8B</td><td>43.0</td><td>45.2</td><td>48.9</td><td>86.9</td><td>29.7</td><td>50.7</td></tr><tr><td>InstructBLIP (Dai et al., 2023)</td><td>13B</td><td>30.6</td><td>42.2</td><td>45.6</td><td>60.3</td><td>32.5</td><td>42.2</td></tr><tr><td>CogVLM (Wang et al., 2023)</td><td>17B</td><td>32.1</td><td>41.5</td><td>45.2</td><td>58.6</td><td>37.3</td><td>42.9</td></tr><tr><td>Emu2-Chat (Sun et al., 2024)</td><td>37B</td><td>36.3</td><td>36.2</td><td>37.8</td><td>58.2</td><td>39.7</td><td>41.6</td></tr><tr><td>LLaVA-v1.5 (Liu et al., 2024a)</td><td>7B</td><td>35.1</td><td>37.1</td><td>41.9</td><td>52.1</td><td>36.0</td><td>40.4</td></tr><tr><td>+ LLaVA-RLHF (Sun et al., 2023)</td><td>7B</td><td>34.6</td><td>40.8</td><td>30.4</td><td>51.8</td><td>38.0</td><td>39.1</td></tr><tr><td>+ HA-DPO (Zhao et al., 2023)</td><td>7B</td><td>35.8</td><td>38.6</td><td>34.6</td><td>51.6</td><td>40.6</td><td>40.2</td></tr><tr><td>+ POVID (Zhou et al., 2024)</td><td>7B</td><td>35.2</td><td>19.9</td><td>37.8</td><td>21.4</td><td>39.4</td><td>30.7</td></tr><tr><td>+ MIA-DPO (Ours)</td><td>7B</td><td>36.3</td><td>42.9</td><td>44.2</td><td>54.2</td><td>39.5</td><td>43.4</td></tr><tr><td>△</td><td>-</td><td>+1.2</td><td>+5.8</td><td>+2.3</td><td>+2.1</td><td>+3.5</td><td>+3.0</td></tr><tr><td>InternLM-XC2.5 (Zhang et al., 2024)</td><td>7B</td><td>41.4</td><td>46.9</td><td>49.3</td><td>70.7</td><td>59.5</td><td>53.6</td></tr><tr><td>+ MIA-DPO (Ours)</td><td>7B</td><td>42.6</td><td>47.7</td><td>60.4</td><td>75.2</td><td>63.6</td><td>57.9</td></tr><tr><td>△</td><td>-</td><td>+1.2</td><td>+0.8</td><td>11.1</td><td>+4.5</td><td>4.1</td><td>+4.3</td></tr></table>{{< /table-caption >}}

> Table 1 presents a comparison of MIA-DPO and other DPO algorithms across five multi-image benchmarks, showing MIA-DPO's superior performance.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_4_0.png "🔼 Figure 2: Examples of Multi-Image Hallucinations. Top: Sequence Confusion that the model is confused about the order in which the images should be referenced. Bottom: Element Interference. The model incorrectly identified the attributes due to visual element interference across different images. Attention values illustrate how the model's focus was dispersed across different images, resulting in the hallucination response.")

> This figure shows examples of two types of multi-image hallucinations: sequence confusion and element interference, illustrating how attention values reveal the model's focus and contribute to these errors.


![](figures/figures_5_0.png "🔼 Figure 1: (a) Overview of MIA-DPO. We transform single-image data (e.g., LLaVA 665k) into multi-image data by adding noisy or unrelated images and using language descriptions to specify the target image. Attention values are then used to detect hallucinations in multi-image contexts, filtering out rejected data for DPO optimization. (b) Benchmark Results. MIA-DPO excels across five multi-image benchmarks while maintaining competitive performance on seven single-image benchmarks, demonstrating its robustness in both single and multi-image tasks.")

> The figure shows an overview of the MIA-DPO framework and its performance on multi-image and single-image benchmarks.


![](figures/figures_6_0.png "🔼 Figure 1: (a) Overview of MIA-DPO. We transform single-image data (e.g., LLaVA 665k) into multi-image data by adding noisy or unrelated images and using language descriptions to specify the target image. Attention values are then used to detect hallucinations in multi-image contexts, filtering out rejected data for DPO optimization. (b) Benchmark Results. MIA-DPO excels across five multi-image benchmarks while maintaining competitive performance on seven single-image benchmarks, demonstrating its robustness in both single and multi-image tasks.")

> The figure shows an overview of the MIA-DPO framework and its performance on several multi-image and single-image benchmarks.


![](figures/figures_6_1.png "🔼 Figure 3: MIA-DPO Framework. We extend the single-image dataset to multi-image datasets by inserting irrelevant images and using attention values to filter out the hallucination responses for rejected samples of the DPO algorithm.")

> The figure illustrates the MIA-DPO framework, which extends single-image datasets to multi-image datasets and uses attention values to filter out hallucination responses.


![](figures/figures_6_2.png "🔼 Figure 2: Examples of Multi-Image Hallucinations. Top: Sequence Confusion that the model is confused about the order in which the images should be referenced. Bottom: Element Interference. The model incorrectly identified the attributes due to visual element interference across different images. Attention values illustrate how the model's focus was dispersed across different images, resulting in the hallucination response.")

> The figure shows two examples of multi-image hallucinations: sequence confusion and element interference, illustrating how the model's attention is dispersed across different images, resulting in incorrect responses.


![](figures/figures_6_3.png "🔼 Figure 3: MIA-DPO Framework. We extend the single-image dataset to multi-image datasets by inserting irrelevant images and using attention values to filter out the hallucination responses for rejected samples of the DPO algorithm.")

> The figure illustrates the MIA-DPO framework, showing how single-image data is augmented with irrelevant images, attention values are used to filter out hallucinations, and chosen/rejected pairs are created for DPO optimization.


![](figures/figures_10_0.png "🔼 Figure 6: Attention Difference Before and After DPO. We present the attention distribution in the intermediate layers for the original LLaVa-v1.5 (top row), MIA-DPO + LLaVa-v1.5 (second row), and the difference value (bottom row), respectively.")

> The figure visualizes the attention distribution changes in LLaVa-v1.5 before and after applying MIA-DPO on three multi-image examples.


![](figures/figures_21_0.png "🔼 Figure 1: (a) Overview of MIA-DPO. We transform single-image data (e.g., LLaVA 665k) into multi-image data by adding noisy or unrelated images and using language descriptions to specify the target image. Attention values are then used to detect hallucinations in multi-image contexts, filtering out rejected data for DPO optimization. (b) Benchmark Results. MIA-DPO excels across five multi-image benchmarks while maintaining competitive performance on seven single-image benchmarks, demonstrating its robustness in both single and multi-image tasks.")

> This figure shows an overview of the MIA-DPO framework and its performance on various multi-image and single-image benchmarks.


![](figures/figures_23_0.png "🔼 Figure 1: (a) Overview of MIA-DPO. We transform single-image data (e.g., LLaVA 665k) into multi-image data by adding noisy or unrelated images and using language descriptions to specify the target image. Attention values are then used to detect hallucinations in multi-image contexts, filtering out rejected data for DPO optimization. (b) Benchmark Results. MIA-DPO excels across five multi-image benchmarks while maintaining competitive performance on seven single-image benchmarks, demonstrating its robustness in both single and multi-image tasks.")

> The figure shows an overview of the MIA-DPO framework and its performance on single and multi-image benchmarks.


![](figures/figures_24_0.png "🔼 Figure 1: (a) Overview of MIA-DPO. We transform single-image data (e.g., LLaVA 665k) into multi-image data by adding noisy or unrelated images and using language descriptions to specify the target image. Attention values are then used to detect hallucinations in multi-image contexts, filtering out rejected data for DPO optimization. (b) Benchmark Results. MIA-DPO excels across five multi-image benchmarks while maintaining competitive performance on seven single-image benchmarks, demonstrating its robustness in both single and multi-image tasks.")

> The figure shows an overview of the MIA-DPO framework and its superior performance on multi-image and single-image benchmarks.


![](figures/figures_24_1.png "🔼 Figure 4: Multi-Images DPO Data Format. To address multi-image hallucinations mentioned in Fig. 2, we construct our multi-image prompts in three formats: (a) Sequence. (b) Grid Collage. (c) Pic-in-Pic.")

> The figure shows three different ways of creating multi-image prompts from single-image data to address hallucination issues in large vision language models.


![](figures/figures_24_2.png "🔼 Figure 3: MIA-DPO Framework. We extend the single-image dataset to multi-image datasets by inserting irrelevant images and using attention values to filter out the hallucination responses for rejected samples of the DPO algorithm.")

> The figure illustrates the MIA-DPO framework, showing how single-image data is augmented with irrelevant images to create multi-image data, and attention mechanisms are used to filter out hallucinated responses for constructing chosen/rejected pairs in the DPO algorithm.


</details>




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Main results on single-image benchmarks. We compare MIA-DPO with other DPO approaches across seven single-image benchmarks. MIA-DPO, which not only enhances multi-image performance but also maintains strong proficiency in single-image tasks." >}}
<br><table id='1' style='font-size:14px'><tr><td>Models</td><td>Parameter</td><td>MMStar</td><td>SQA</td><td>MMVet</td><td>POPE</td><td>MMB</td><td>Math</td><td>AI2D</td><td>Average</td></tr><tr><td>LLaVA-v1.6 (Li et al., 2024b)</td><td>7B</td><td>37.6</td><td>87.5</td><td>40.2</td><td>70.3</td><td>69.8</td><td>31.5</td><td>67.0</td><td>57.7</td></tr><tr><td>Qwen-VL-Chat (Bai et al., 2023)</td><td>7B</td><td>34.5</td><td>68.8</td><td>47.3</td><td>74.9</td><td>61.8</td><td>15.5</td><td>63.0</td><td>52.3</td></tr><tr><td>Idefics2 (Lauren�on et al., 2024b)</td><td>8B</td><td>49.5</td><td>88.7</td><td>34.0</td><td>86.2</td><td>75.7</td><td>51.4</td><td>72.3</td><td>65.4</td></tr><tr><td>OpenFlamingo (Awadalla et al., 2023b)</td><td>9B</td><td>36.9</td><td>44.8</td><td>23.2</td><td>52.6</td><td>32.4</td><td>18.6</td><td>31.7</td><td>34.3</td></tr><tr><td>InstructBLIP (Dai et al., 2023)</td><td>13B</td><td>32.7</td><td>54.1</td><td>33.1</td><td>86.1</td><td>38.3</td><td>24.4</td><td>40.6</td><td>44.2</td></tr><tr><td>CogVLM (Wang et al., 2023)</td><td>17B</td><td>39.9</td><td>66.2</td><td>54.5</td><td>88.0</td><td>65.8</td><td>35.0</td><td>63.3</td><td>58.9</td></tr><tr><td>Emu2-Chat (Sun et al., 2024)</td><td>37B</td><td>40.7</td><td>68.2</td><td>31.0</td><td>88.0</td><td>63.4</td><td>30.7</td><td>49.7</td><td>53.1</td></tr><tr><td>LLaVA-v1.5 (Liu et al., 2024a)</td><td>7B</td><td>32.9</td><td>66.6</td><td>30.5</td><td>85.9</td><td>64.3</td><td>25.4</td><td>55.5</td><td>51.6</td></tr><tr><td>+ LLaVA-RLHF Sun et al. (2023)</td><td>7B</td><td>31.6</td><td>64.0</td><td>27.8</td><td>80.8</td><td>60.1</td><td>23.5</td><td>47.9</td><td>48.0</td></tr><tr><td>+ HA-DPO (Zhao et al., 2023)</td><td>7B</td><td>33.5</td><td>67.3</td><td>29.1</td><td>84.3</td><td>64.9</td><td>25.8</td><td>53.9</td><td>51.3</td></tr><tr><td>+ POVID (Zhou et al., 2024)</td><td>7B</td><td>36.2</td><td>68.8</td><td>31.8</td><td>86.3</td><td>64.9</td><td>24.4</td><td>55.2</td><td>52.5</td></tr><tr><td>+ MIA-DPO (ours)</td><td>7B</td><td>32.9</td><td>67.6</td><td>32.1</td><td>87.2</td><td>63.1</td><td>24.4</td><td>54.7</td><td>51.7</td></tr><tr><td>InternLM-XC2.5 (Zhang et al., 2024)</td><td>7B</td><td>59.7</td><td>96.3</td><td>48.7</td><td>87.9</td><td>81.9</td><td>63.3</td><td>81.5</td><td>74.2</td></tr><tr><td>+ MIA-DPO (ours)</td><td>7B</td><td>61.1</td><td>96.2</td><td>46.7</td><td>86.9</td><td>80.4</td><td>61.7</td><td>81.6</td><td>73.5</td></tr></table>{{< /table-caption >}}

> Table 2 compares MIA-DPO's performance on seven single-image benchmarks against other DPO approaches, demonstrating its ability to maintain strong single-image performance while enhancing multi-image capabilities.


{{< table-caption caption="🔽 Table 3: Ablation Studies. The top row refers to the LLaVa-v1.5 baseline. We conduct experiments about the impact of without (w/o) and with (w) post-selection techniques and dpo data types." >}}
<br><table id='2' style='font-size:14px'><tr><td></td><td></td><td>35.1</td><td>37.1</td><td>41.9</td><td>52.1</td><td>36.0</td><td>40.4</td></tr><tr><td>1</td><td>w/o post sel.</td><td>35.3</td><td>38.7</td><td>44.2</td><td>53.7</td><td>39.4</td><td>42.3</td></tr><tr><td>2</td><td>W post sel.</td><td>36.3</td><td>42.9</td><td>44.2</td><td>54.2</td><td>39.5</td><td>43.4</td></tr><tr><td>3</td><td>sequence</td><td>37.3</td><td>39.5</td><td>44.2</td><td>51.7</td><td>40.1</td><td>42.6</td></tr><tr><td>4</td><td>grid collage</td><td>37.1</td><td>40.4</td><td>44.2</td><td>51.0</td><td>39.4</td><td>42.4</td></tr><tr><td>5</td><td>pic-in-pic</td><td>37.9</td><td>40.8</td><td>41.9</td><td>53.2</td><td>39.8</td><td>42.7</td></tr></table>{{< /table-caption >}}

> Table 3 shows the ablation study results on MIA-DPO, comparing the performance with and without post-selection and different data types.


{{< table-caption caption="🔽 Table 1: Main results on multi-image benchmarks. We compare our MIA-DPO along with other DPO algorithms across five multi-image benchmarks. Our method brings significant performance improvements to both the classic LLaVa-v1.5 and the recent InternLM-XC2.5. In contrast, other single-image DPO methods perform poorly on multi-image benchmarks." >}}
<table id='0' style='font-size:14px'><tr><td>#</td><td>MMMU</td><td>BLINK</td><td>Mantis</td><td>NLVR2</td><td>MVBench</td><td></td><td>Average</td></tr><tr><td></td><td></td><td>35.1</td><td>37.1</td><td>41.9</td><td>52.1</td><td>36.0</td><td>40.4</td></tr><tr><td>1</td><td>�=0.1</td><td>35.9</td><td>41.3</td><td>46.1</td><td>53.2</td><td>39.9</td><td>43.3</td></tr><tr><td>2</td><td>y=0.2</td><td>37.1</td><td>39.2</td><td>42.4</td><td>51.8</td><td>39.4</td><td>42.0</td></tr><tr><td>3</td><td>�=0.3</td><td>35.8</td><td>39.8</td><td>42.9</td><td>52.0</td><td>39.7</td><td>42.0</td></tr><tr><td>4</td><td>epoch=1</td><td>35.9</td><td>41.3</td><td>46.1</td><td>53.2</td><td>39.9</td><td>43.3</td></tr><tr><td>5</td><td>epoch=2</td><td>37.0</td><td>38.5</td><td>45.2</td><td>52.0</td><td>39.6</td><td>42.5</td></tr><tr><td>6</td><td>epoch=3</td><td>36.3</td><td>42.9</td><td>44.2</td><td>54.2</td><td>39.5</td><td>43.4</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MIA-DPO and other direct preference optimization methods across five multi-image benchmarks, showing MIA-DPO's significant performance improvement on both LLaVa-v1.5 and InternLM-XC2.5.


{{< table-caption caption="🔽 Table 5: Ablation Studies. The top row refers to the LLaVa-v1.5 baseline. We conducted an ablation study using GPT-40-mini for data selection." >}}
<table id='1' style='font-size:14px'><tr><td colspan="2">#</td><td>MMMU</td><td>BLINK</td><td>Mantis</td><td>NLVR2</td><td>MVBench</td><td>Average</td></tr><tr><td></td><td></td><td>35.1</td><td>37.1</td><td>41.9</td><td>52.1</td><td>36.0</td><td>40.4</td></tr><tr><td>1</td><td>GPT-Selection</td><td>36.3</td><td>41.7</td><td>42.9</td><td>53.0</td><td>39.5</td><td>42.7</td></tr><tr><td>2</td><td>MIA-DPO</td><td>36.3</td><td>42.9</td><td>44.2</td><td>54.2</td><td>39.5</td><td>43.4</td></tr><tr><td>3</td><td></td><td>0.0</td><td>+1.2</td><td>+1.3</td><td>+1.2</td><td>0.0</td><td>+0.7</td></tr></table>{{< /table-caption >}}

> This table compares the performance of MIA-DPO against a baseline and an alternative approach using GPT-40-mini for data selection across five multi-image benchmarks.


{{< table-caption caption="🔽 Table 1: Main results on multi-image benchmarks. We compare our MIA-DPO along with other DPO algorithms across five multi-image benchmarks. Our method brings significant performance improvements to both the classic LLaVa-v1.5 and the recent InternLM-XC2.5. In contrast, other single-image DPO methods perform poorly on multi-image benchmarks." >}}
<br><table id='1' style='font-size:16px'><tr><td>Models</td><td>Parameter</td><td>Release Time</td><td>Source</td></tr><tr><td>GPT-4V (Achiam et al., 2023)</td><td>-</td><td>2023-09</td><td>Source Link: OpenAI</td></tr><tr><td>Kosmos2 (Peng et al., 2023)</td><td>1.6B</td><td>2023-06</td><td>Source Link: Kosmos2</td></tr><tr><td>VideoLLaVA (Lin et al., 2023)</td><td>7B</td><td>2023-11</td><td>Source Link: Video-LLaVa</td></tr><tr><td>Fuyu (Bavishi et al., 2023)</td><td>8B</td><td>2023-10</td><td>Source Link: Fuyu-8B</td></tr><tr><td>VILA (Lin et al., 2024)</td><td>8B</td><td>2023-12</td><td>Source Link: VILA</td></tr><tr><td>Otter-Image (Li et al., 2023a)</td><td>9B</td><td>2023-05</td><td>Source Link: Otter</td></tr><tr><td>Idefics1 (Lauren�on et al., 2024a)</td><td>9B</td><td>2023-08</td><td>Source Link: Idefices1</td></tr><tr><td>BLIP-2 (Li et al., 2023b)</td><td>13B</td><td>2023-01</td><td>Source Link: BLIP-2</td></tr><tr><td>OpenFlamingo (Awadalla et al., 2023b)</td><td>9B</td><td>2023-08</td><td>Source Link: OpenFlamingo</td></tr><tr><td>InstructBLIP (Dai et al., 2023)</td><td>13B</td><td>2023-05</td><td>Source Link: InstructBLIP</td></tr><tr><td>Qwen-VL-Chat (Bai et al., 2023)</td><td>7B</td><td>2023-8</td><td>Source Link: Qwen-VL-Chat</td></tr><tr><td>Emu2-Chat (Sun et al., 2024)</td><td>37B</td><td>2023-12</td><td>Source Link: Emu2-Chat</td></tr><tr><td>CogVLM (Wang et al., 2023)</td><td>17B</td><td>2023-10</td><td>Source Link: CogVLM</td></tr><tr><td>Idefics2 (Lauren�on et al., 2024b)</td><td>8B</td><td>2024-04</td><td>Source Link: Idefices2</td></tr><tr><td>LLaVA-v1.6 (Li et al., 2024b)</td><td>7B</td><td>2024-01</td><td>Source Link: LLaVa-Next11</td></tr><tr><td>LLaVA-v1.5 (Liu et al., 2024a)</td><td>7B</td><td>2023-10</td><td>Source Link: LLaVa-v1.5</td></tr><tr><td>InternLM-XC2.5 (Zhang et al., 2024)</td><td>7B</td><td>2024-07</td><td>Source Link: InternLM-XC2d5</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MIA-DPO and other direct preference optimization methods across five multi-image benchmarks, showing MIA-DPO's significant performance improvements over existing methods for both LLaVa-v1.5 and InternLM-XC2.5.


{{< table-caption caption="🔽 Table 1: Main results on multi-image benchmarks. We compare our MIA-DPO along with other DPO algorithms across five multi-image benchmarks. Our method brings significant performance improvements to both the classic LLaVa-v1.5 and the recent InternLM-XC2.5. In contrast, other single-image DPO methods perform poorly on multi-image benchmarks." >}}
<table id='3' style='font-size:20px'><tr><td>Setting</td><td>Models</td><td>Evaluation Metric</td><td>Number</td><td>Source</td></tr><tr><td rowspan="5">Multi-Images Benchmark</td><td>MMMU (Yue et al., 2024)</td><td>Multiple Choice</td><td>1,050</td><td>MMMU</td></tr><tr><td>BLINK (Fu et al., 2024)</td><td>Multiple Choice</td><td>3,807</td><td>BLINK</td></tr><tr><td>NLVR2 (Suhr et al., 2018)</td><td>Multiple Choice</td><td>6,967</td><td>NLVR2</td></tr><tr><td>Mantis-Eval (Jiang et al., 2024)</td><td>Multiple Choice</td><td>217</td><td>Mantis-Eval</td></tr><tr><td>MVBench (Li et al., 2024c)</td><td>Multiple Choice</td><td>4,000</td><td>MVBench</td></tr><tr><td rowspan="7">Single-Image Benchmark</td><td>MMStar (Chen et al., 2024a)</td><td>Multiple Choice</td><td>1,500</td><td>MMStar</td></tr><tr><td>Sci-QA (Lu et al., 2022)</td><td>Multiple Choice</td><td>4,241</td><td>ScienceQA</td></tr><tr><td>MMVet (Yu et al., 2023)</td><td>Subjective Questions</td><td>218</td><td>MM-Vet</td></tr><tr><td>POPE (Li et al., 2023c)</td><td>Yes/No</td><td>9,000</td><td>POPE</td></tr><tr><td>MMB (Liu et al., 2023)</td><td>Multiple Choice</td><td>1,164</td><td>MMBench</td></tr><tr><td>Math (Lu et al., 2023)</td><td>Multiple Choice</td><td>6,141</td><td>Math Vista</td></tr><tr><td>AI2D (Kembhavi et al., 2016)</td><td>Multiple Choice</td><td>3,090</td><td>AI2D</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MIA-DPO and other DPO methods across five multi-image benchmarks, showing MIA-DPO's superior performance on both LLaVa-v1.5 and InternLM-XC2.5.


{{< table-caption caption="🔽 Table 8: DPO Data Statistic. We listed in the table the data volume used for DPO with LLaVa-v1.5 and InternLM-XC2d5, along with the proportion of each type of data." >}}
<br><table id='1' style='font-size:20px'><tr><td>Models</td><td>Total</td><td>Sequence</td><td>Grid Collage</td><td>Pic-in-Pic</td></tr><tr><td>LLaVa-v1.5 (Liu et al., 2024a)</td><td>28.9k</td><td>15.1k</td><td>9.3k</td><td>4.5k</td></tr><tr><td>InternLM-XC2d5 (Zhang et al., 2024)</td><td>23.1k</td><td>11.7k</td><td>7.8k</td><td>3.6k</td></tr></table>{{< /table-caption >}}

> The table shows the number of data samples used for direct preference optimization (DPO) in the MIA-DPO model, broken down by data type and language model.


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
{{< /gallery >}}