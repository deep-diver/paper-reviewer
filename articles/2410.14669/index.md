---
title: "NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples"
summary: "NaturalBench: A new benchmark exposes VLMs' weaknesses on natural adversarial samples, revealing significant biases and highlighting the need for improved visio-linguistic skills."
categories: ["AI Generated"]
tags: ["🔖 24-10-18", "🤗 24-10-21"]
showSummary: true
date: 2024-10-18
draft: false
---

### TL;DR


{{< lead >}}

Current vision-language models (VLMs) excel at existing benchmarks, but struggle with simple image-text pairings that humans find easy.  This paper introduces NaturalBench, a new benchmark using 'natural adversarial samples'—images and questions easy for humans but difficult for VLMs.  These samples are semi-automatically generated using CLIP and ChatGPT. NaturalBench includes 10,000 human-verified samples and a novel design preventing 'blind' solutions (those not using image information). Testing 53 VLMs reveals a substantial performance gap (50-70%) between VLMs and humans. The paper analyzes this performance gap from two perspectives: compositionality (VLMs lack diverse visio-linguistic skills) and bias (VLMs often choose the same answer regardless of the image).  NaturalBench's methodology is flexible, adapting easily to different data sources and languages for dynamic evaluations, ensuring it remains a relevant tool for future VLM research.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.14669" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
The paper introduces NaturalBench, a new benchmark for evaluating vision-language models (VLMs) that uses naturally occurring adversarial samples, which are images and questions that humans can easily answer but current VLMs struggle with.  This benchmark addresses limitations of existing benchmarks by preventing 'blind' solutions that don't use the image.  It's shown to be more challenging than previous benchmarks and reveals significant biases in current VLMs.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} NaturalBench is a new benchmark for evaluating vision-language models (VLMs) that uses naturally occurring adversarial samples. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} NaturalBench is more challenging than existing benchmarks and reveals significant biases in current VLMs. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The benchmark's design prevents 'blind' solutions and allows for dynamic evaluation, adapting to new data sources. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: NaturalBench examples consist of two questions and two images with alternating answers to prevent 'blind' models from scoring well (e.g., those that predict the same answer regardless of the image or question, as discussed in Section 3). We compare the ground-truth answer for each (image, question) pair with predictions from leading VLMs including GPT-40 (gpt-40-2024-08-06), Qwen2-VL (72B), Llama3.2-Vision (90B), and Molmo (72B) (see Section 4). Even the best models like GPT-40 lags far behind human performance (which is above 90%). Figure 2 shows the pipeline for collecting these natural adversarial examples.")

> Figure 1 shows examples from NaturalBench, a new benchmark for evaluating vision-language models, highlighting the difficulty of the task even for state-of-the-art models compared to human performance.





![](charts/charts_6_0.png "🔼 Figure 4: Performance of GPT-3.5 vs. LLaVA-1.5 on previous VQA benchmarks. We split each benchmark into equal-sized training and test sets, and report zero-shot (in blue) and finetuned (in green) results. Previous benchmarks show strong language biases, allowing blind GPT-3.5 to exploit spurious answer patterns (see Section 4) by finetuning on QA data without images. As a result, blind GPT-3.5 greatly surpasses random chance (see the red dotted line) and sometimes even matches the performance of LLaVA-1.5-7B finetuned using images. In contrast, Figure 5 shows that NaturalBench can effectively prevent blind solutions from exceeding chance.")

> The chart compares the performance of GPT-3.5 and LLaVA-1.5 models on several existing VQA benchmarks, highlighting the susceptibility of these benchmarks to language biases that allow blind models to achieve high accuracy without image understanding.





{{< table-caption caption="🔽 Table 2: Debiased performance on NaturalBench. Many models underperform on NaturalBench due to biases towards certain answers like “Yes” and “B”. To illustrate this, we compute a debiased Q-Acc by adjusting the prediction threshold (as described in Section 5) to ensure the model predict different answers for the two images of the same question. Similarly, debiased I-Acc ensures different predicted answers for the two questions of the same image. For debiased G-Acc, we tune the threshold so that the model predicts one answer for two (out of four) image-question pairs, and a different answer for the other two pairs. The substantial performance gains of these metrics suggest that proper debiasing can greatly improve performance. Our Appendix evaluates existing debiasing techniques that do not require prior knowledge of image-question pairings." >}}
<br><table id='1' style='font-size:16px'><tr><td rowspan="2">Model</td><td rowspan="2">Image Encoder</td><td rowspan="2">Language Model</td><td colspan="2">Q-Acc</td><td colspan="2">I-Acc</td><td colspan="2">G-Acc</td></tr><tr><td>Original</td><td>Debiased</td><td>Original</td><td>Debiased</td><td>Original</td><td>Debiased</td></tr><tr><td>LLaVA-1.5</td><td>CLIP-L-14</td><td>Vicuna-13B</td><td>38.6</td><td>86.2</td><td>43.5</td><td>78.6</td><td>14.4</td><td>49.7</td></tr><tr><td>DeepSeek-VL-7B-Chat</td><td>SigLIP-L</td><td>DeepSeek-LLM-7B</td><td>45.8</td><td>86.6</td><td>49.9</td><td>81.8</td><td>19.4</td><td>54.8</td></tr><tr><td>BLIP-3 (XGen-MM)</td><td>CLIP-H-14</td><td>Phi-3-Mini</td><td>46.8</td><td>88.6</td><td>51.1</td><td>81.9</td><td>19.5</td><td>55.3</td></tr><tr><td>Intern VL-Chat-V1.5</td><td>Intern ViT-6B</td><td>InternLM2-Chat-20B</td><td>52.6</td><td>92.3</td><td>56.0</td><td>86.1</td><td>24.3</td><td>66.0</td></tr><tr><td>Intern VL-Chat-V1.2</td><td>Intern ViT-6B</td><td>Nous-Hermes-2- Yi-34B</td><td>52.6</td><td>91.6</td><td>56.0</td><td>86.0</td><td>26.2</td><td>65.8</td></tr><tr><td>Intern VL2-26B</td><td>Intern ViT-6B</td><td>InternLM2-Chat-20B</td><td>55.7</td><td>92.2</td><td>58.5</td><td>87.2</td><td>28.2</td><td>67.7</td></tr><tr><td>LLaVA-OneVision</td><td>SigLIP-S-14</td><td>Qwen2-7B</td><td>55.4</td><td>92.1</td><td>58.2</td><td>87.2</td><td>28.6</td><td>67.8</td></tr><tr><td>GPT-4o</td><td>-</td><td>GPT-4</td><td>65.0</td><td>94.0</td><td>67.0</td><td>90.5</td><td>40.5</td><td>75.6</td></tr></table>{{< /table-caption >}}

> Table 2 presents the original and debiased performance of several models on NaturalBench, highlighting the significant performance gains achieved through debiasing techniques.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_3_0.png "🔼 Figure 1: NaturalBench examples consist of two questions and two images with alternating answers to prevent 'blind' models from scoring well (e.g., those that predict the same answer regardless of the image or question, as discussed in Section 3). We compare the ground-truth answer for each (image, question) pair with predictions from leading VLMs including GPT-40 (gpt-40-2024-08-06), Qwen2-VL (72B), Llama3.2-Vision (90B), and Molmo (72B) (see Section 4). Even the best models like GPT-40 lags far behind human performance (which is above 90%). Figure 2 shows the pipeline for collecting these natural adversarial examples.")

> Figure 1 shows examples from NaturalBench, demonstrating how even state-of-the-art vision-language models struggle with simple questions about natural images, highlighting the challenge posed by the benchmark.


![](figures/figures_5_0.png "🔼 Figure 1: NaturalBench examples consist of two questions and two images with alternating answers to prevent 'blind' models from scoring well (e.g., those that predict the same answer regardless of the image or question, as discussed in Section 3). We compare the ground-truth answer for each (image, question) pair with predictions from leading VLMs including GPT-40 (gpt-40-2024-08-06), Qwen2-VL (72B), Llama3.2-Vision (90B), and Molmo (72B) (see Section 4). Even the best models like GPT-40 lags far behind human performance (which is above 90%). Figure 2 shows the pipeline for collecting these natural adversarial examples.")

> Figure 1 shows examples from the NaturalBench dataset, demonstrating how state-of-the-art vision-language models struggle with simple questions about natural images, even when humans find them easy to answer.


![](figures/figures_9_0.png "🔼 Figure 1: NaturalBench examples consist of two questions and two images with alternating answers to prevent 'blind' models from scoring well (e.g., those that predict the same answer regardless of the image or question, as discussed in Section 3). We compare the ground-truth answer for each (image, question) pair with predictions from leading VLMs including GPT-40 (gpt-40-2024-08-06), Qwen2-VL (72B), Llama3.2-Vision (90B), and Molmo (72B) (see Section 4). Even the best models like GPT-40 lags far behind human performance (which is above 90%). Figure 2 shows the pipeline for collecting these natural adversarial examples.")

> Figure 1 shows examples from the NaturalBench dataset, demonstrating how even state-of-the-art vision-language models struggle with simple questions about natural images, highlighting the need for a more robust benchmark.


![](figures/figures_17_0.png "🔼 Figure 1: NaturalBench examples consist of two questions and two images with alternating answers to prevent 'blind' models from scoring well (e.g., those that predict the same answer regardless of the image or question, as discussed in Section 3). We compare the ground-truth answer for each (image, question) pair with predictions from leading VLMs including GPT-40 (gpt-40-2024-08-06), Qwen2-VL (72B), Llama3.2-Vision (90B), and Molmo (72B) (see Section 4). Even the best models like GPT-40 lags far behind human performance (which is above 90%). Figure 2 shows the pipeline for collecting these natural adversarial examples.")

> Figure 1 shows examples from the NaturalBench benchmark, demonstrating how state-of-the-art vision-language models struggle with simple questions about natural images, even when humans find them easy to answer.


![](figures/figures_21_0.png "🔼 Figure 1: NaturalBench examples consist of two questions and two images with alternating answers to prevent 'blind' models from scoring well (e.g., those that predict the same answer regardless of the image or question, as discussed in Section 3). We compare the ground-truth answer for each (image, question) pair with predictions from leading VLMs including GPT-40 (gpt-40-2024-08-06), Qwen2-VL (72B), Llama3.2-Vision (90B), and Molmo (72B) (see Section 4). Even the best models like GPT-40 lags far behind human performance (which is above 90%). Figure 2 shows the pipeline for collecting these natural adversarial examples.")

> Figure 1 shows examples from the NaturalBench dataset, illustrating how even state-of-the-art vision-language models struggle with simple questions about natural images, while humans easily answer them.


</details>




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 1: Performance on NaturalBench. We report the performance of 53 leading VLMs on NaturalBench. All models significantly lag behind human performance, with the performance gap (in G-Acc) between humans and models highlighted in red. The latest models, such as BLIP-3 (XGen-MM), Cambrian-1, LLaVA-OneVision, Llama3.2-Vision, Molmo, and Qwen2-VL lag significantly behind humans by 55% to 70%. Even the best closed-source GPT-40 is still 52% behind humans." >}}
<table id='3' style='font-size:14px'><tr><td colspan="4">Benchmark Statistics</td><td colspan="3">Collection Details</td></tr><tr><td>Source</td><td>Question Type</td><td>Language</td><td># VQA Samples</td><td># VLMs Used</td><td># Mismatched Pairs</td><td># Verified Pairs</td></tr><tr><td colspan="7">NaturalBench</td></tr><tr><td>Flickr30K 63</td><td>Yes-or-No</td><td>English</td><td>2,600</td><td>CLIP-L, BLIP-2, GPT-4</td><td>2,000</td><td>1,200</td></tr><tr><td>Flickr30K 63</td><td>Multiple-Choice</td><td>English</td><td>1,000</td><td>CLIP-L, BLIP-2, GPT-4</td><td>2,000</td><td>1,200</td></tr><tr><td>DOCCI [59]</td><td>Yes-or-No</td><td>English</td><td>3,200</td><td>LongCLIP, GPT-4</td><td>3,300</td><td>1,000</td></tr><tr><td>DOCCI 59</td><td>Multiple-Choice</td><td>English</td><td>800</td><td>LongCLIP, GPT-4</td><td>3,300</td><td>1,000</td></tr><tr><td>All</td><td>Yes-or-No, Multiple-Choice</td><td>English</td><td>7,600</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="7">NaturalBench (Multi-lingual)</td></tr><tr><td>XM3600 69</td><td>Yes-or-No</td><td>Chinese</td><td>1,200</td><td>NLLB-CLIP, GPT-4</td><td>2,400</td><td>400</td></tr><tr><td>XM3600 69</td><td>Yes-or-No</td><td>Hindi</td><td>1,200</td><td>NLLB-CLIP, GPT-4</td><td>2,400</td><td>400</td></tr><tr><td>All</td><td>Yes-or-No</td><td>Chinese, Hindi</td><td>2,400</td><td>-</td><td>-</td><td>-</td></tr></table>{{< /table-caption >}}

> Table 1 presents the performance of 53 vision-language models on the NaturalBench benchmark, highlighting the significant gap between model and human performance.


{{< table-caption caption="🔽 Table 5: Performance on NaturalBench-Chinese and NaturalBench-Hindi. We report G-Acc for each dataset, evaluating only models with claimed multilingual capabilities. For both datasets, we also provide G-Acc after translating the original Chinese or Hindi questions into English. This simple translation often boosts performance, except for top models like InternVL-Chat-V1.2-Plus and GPT-40, which seem extensively trained in Chinese. NaturalBench-Hindi remains particularly challenging for open-source models." >}}
<br><table id='1' style='font-size:14px'><tr><td rowspan="2">Model</td><td colspan="2">NaturalBench-Chinese</td><td colspan="2">NaturalBench-Hindi</td></tr><tr><td>Chinese</td><td>English</td><td>Hindi</td><td>English</td></tr><tr><td>Random Chance</td><td>6.3</td><td>6.3</td><td>6.3</td><td>6.3</td></tr><tr><td colspan="5">Open-source Models</td></tr><tr><td>DeepSeek-VL-7B-Chat</td><td>10.9</td><td>28.4</td><td>0.6</td><td>29.0</td></tr><tr><td>Intern VL-Chat-V1.2-Plus</td><td>34.6</td><td>33.4</td><td>11.5</td><td>36.2</td></tr><tr><td>InternLM-XC2-7B</td><td>32.5</td><td>34.6</td><td>15.9</td><td>35.6</td></tr><tr><td colspan="5">Closed-source Models</td></tr><tr><td>GPT-4o</td><td>41.2</td><td>38.7</td><td>40.3</td><td>40.9</td></tr></table>{{< /table-caption >}}

> Table 5 presents the performance of various vision-language models on the NaturalBench-Chinese and NaturalBench-Hindi subsets, evaluating their performance with and without English translation of the questions and answers.


{{< table-caption caption="🔽 Table 6: Ablation on different collection methods. We report G-Acc on datasets generated by different collection methods from Flickr30K. Our adversarial procedure results in a much more challenging dataset. Note that Flickr-Adversarial is the combination of Flickr-YN and Flickr-MCQ." >}}
<br><table id='3' style='font-size:16px'><tr><td rowspan="2">Model</td><td colspan="2">Model Performance (G-Acc)</td></tr><tr><td>Flickr-Adversarial</td><td>Flickr-Random</td></tr><tr><td>Random Chance</td><td>6.3</td><td>6.3</td></tr><tr><td colspan="3">Open-source Models</td></tr><tr><td>DeepSeek-VL-7B-Chat</td><td>15.2</td><td>80.7</td></tr><tr><td>BLIP-3(XGen-MM)</td><td>15.2</td><td>69.0</td></tr><tr><td>LLaVA-NeXT (Mistral-7B)</td><td>15.9</td><td>86.0</td></tr><tr><td>Phi-3-Vision</td><td>16.0</td><td>75.0</td></tr><tr><td>Intern VL-Chat- V1.2-Plus</td><td>27.8</td><td>83.0</td></tr><tr><td>InternLM-XC2-7B</td><td>29.0</td><td>84.5</td></tr><tr><td colspan="3">Closed-source Models</td></tr><tr><td>GPT-4o</td><td>38.3</td><td>72.5</td></tr></table>{{< /table-caption >}}

> This table shows the Group Accuracy (G-Acc) performance of various vision-language models on different subsets of the Flickr30K dataset, comparing the results obtained using the adversarial method proposed in the paper versus a random sampling method, highlighting the effectiveness of the adversarial approach in creating a more challenging benchmark.


{{< table-caption caption="🔽 Table 1: Performance on NaturalBench. We report the performance of 53 leading VLMs on NaturalBench. All models significantly lag behind human performance, with the performance gap (in G-Acc) between humans and models highlighted in red. The latest models, such as BLIP-3 (XGen-MM), Cambrian-1, LLaVA-OneVision, Llama3.2-Vision, Molmo, and Qwen2-VL lag significantly behind humans by 55% to 70%. Even the best closed-source GPT-4o is still 52% behind humans." >}}
<table id='1' style='font-size:14px'><tr><td rowspan="2">Method</td><td rowspan="2">Source</td><td rowspan="2">Model</td><td rowspan="2">Data Size</td><td rowspan="2">Model Size (M)</td><td colspan="3">Retrieval Performance</td></tr><tr><td>Group</td><td>Image</td><td>Text</td></tr><tr><td>Random</td><td>-</td><td>-</td><td>-</td><td>-</td><td>16.67</td><td>25.00</td><td>25.00</td></tr><tr><td rowspan="17">CLIP 65</td><td rowspan="7">OpenAI</td><td>RN50</td><td rowspan="7">400M</td><td>102</td><td>12.22</td><td>32.60</td><td>36.76</td></tr><tr><td>RN101</td><td>120</td><td>13.61</td><td>35.04</td><td>33.33</td></tr><tr><td>ViT-B-32</td><td>151</td><td>15.89</td><td>36.43</td><td>36.92</td></tr><tr><td>RN50x4</td><td>178</td><td>14.75</td><td>37.49</td><td>36.27</td></tr><tr><td>RN50x16</td><td>291</td><td>24.61</td><td>44.01</td><td>43.93</td></tr><tr><td>ViT-L-14</td><td>428</td><td>23.15</td><td>44.99</td><td>41.81</td></tr><tr><td>RN50x64</td><td>623</td><td>26.24</td><td>46.21</td><td>47.35</td></tr><tr><td rowspan="6">LAION</td><td>roberta-ViT-B-32</td><td rowspan="4">2B</td><td>212</td><td>16.22</td><td>39.36</td><td>38.79</td></tr><tr><td>ViT-H-14</td><td>986</td><td>24.04</td><td>49.31</td><td>48.82</td></tr><tr><td>ViT-g-14</td><td>1367</td><td>21.35</td><td>46.21</td><td>46.54</td></tr><tr><td>ViT-bigG-14</td><td>2540</td><td>21.04</td><td>44.49</td><td>43.69</td></tr><tr><td>xlm-roberta-base-ViT-B-32</td><td rowspan="2">5B</td><td>366</td><td>16.79</td><td>37.49</td><td>40.91</td></tr><tr><td>xlm-roberta-large-ViT-H-14</td><td>1193</td><td>22.82</td><td>47.35</td><td>47.51</td></tr><tr><td rowspan="4">DataComp</td><td>small: ViT-B-32</td><td>13M</td><td>151</td><td>12.06</td><td>22.90</td><td>21.19</td></tr><tr><td>medium: ViT-B-32</td><td>128M</td><td>151</td><td>16.95</td><td>28.28</td><td>33.01</td></tr><tr><td>large: ViT-B-16</td><td>1B</td><td>150</td><td>16.71</td><td>36.43</td><td>35.86</td></tr><tr><td>xlarge: ViT-L-14</td><td>13B</td><td>428</td><td>21.84</td><td>44.01</td><td>45.72</td></tr><tr><td rowspan="3">SigLIP 85</td><td rowspan="3">WebLI (English portion)</td><td>ViT-B</td><td rowspan="3">13B</td><td>172</td><td>24.29</td><td>48.57</td><td>49.06</td></tr><tr><td>ViT-L</td><td>430</td><td>31.21</td><td>54.93</td><td>54.44</td></tr><tr><td>ViT-SOViT</td><td>800</td><td>42.14</td><td>62.67</td><td>63.90</td></tr></table>{{< /table-caption >}}

> Table 1 presents the group accuracy (G-Acc) performance of 53 vision-language models on the NaturalBench benchmark, highlighting the significant performance gap between these models and human performance.


{{< table-caption caption="🔽 Table 1: Performance on NaturalBench. We report the performance of 53 leading VLMs on NaturalBench. All models significantly lag behind human performance, with the performance gap (in G-Acc) between humans and models highlighted in red. The latest models, such as BLIP-3 (XGen-MM), Cambrian-1, LLaVA-OneVision, Llama3.2-Vision, Molmo, and Qwen2-VL lag significantly behind humans by 55% to 70%. Even the best closed-source GPT-4o is still 52% behind humans." >}}
<table id='1' style='font-size:14px'><tr><td>Skill Type</td><td>Definition</td><td>Examples</td></tr><tr><td>Object</td><td>Basic entities within an image, including animals, humans, food, buildings, natural elements (nature), vehicles, common items, and others.</td><td>Is there a car parked near the path? Is there a person in this image? Is there a referee behind the table? Is the dog fully submerged in the water except for its head? Is the water body filled with visible rocks and emanating ripples?</td></tr><tr><td>Attribute</td><td>Visual properties of entities, including emotion, shape, size, color, state, activity, gender, and abstract attributes (e.g., helpful, lucky).</td><td>Is anyone in the picture sad or scared? Is the woman extremely surprised? Is the woman alone behind a glass partition? Is the man wearing brown? Is the man wearing a red and white striped apron? Is the old man in the image wearing reflective safety jackets?</td></tr><tr><td>Spatial Relation</td><td>Physical arrangements of multiple entities relative to each other 46 including proximity (e.g., near, far), topological (e.g., at, on, in, with, surround, between, inside, outside) , projective (e.g., left of, right of, under, in front of, below), orientation and direction (e.g., facing, towards, across, away from).</td><td>Is there a referee behind the table? Is the dog looking up at the sky? Is there only one person in the canoe? Is there a group of people standing looking outside the gates? Is the man in the image at the object to his left? Is the smiling woman standing next to the bus?</td></tr><tr><td>Action Relation</td><td>Action interactions between entities, e.g., pushing, kissing, hugging, hitting, helping, and so on.</td><td>Is there a person holding a water bottle? Is the black dog biting a stick? Is anyone using an umbrella? Is the man holding a red pen? Is the dog chasing after a toy outdoors? Is the person jumping directly off a building without any equipment?</td></tr><tr><td>Part Relation</td><td>Part-whole relationships between entities - one entity is a component of another, such as body part, clothing, and accessories.</td><td>Is there a person wearing orange and yellow shirt and jacket? Is anyone wearing yellow and orange safety vests? Is the woman in the black dress wearing gloves? Is a player using his back to play the ball? Is the boy's tongue sticking out?</td></tr><tr><td>Counting</td><td>Determining the quantity, size, or volume of entities, e.g., objects, attribute-object pairs, and object-relation-object triplets.</td><td>Are there four people in the image? Does the dog have two visible colors? Are there more than four performers in the image?</td></tr><tr><td>Differentiation</td><td>Differentiating objects within a category by their attributes or relations, such as distinguishing between "old" and "young" people by age, or "the cat on top of the table" versus "the cat under the table" by their spatial relations.</td><td>Does the girl on the left look sad while the girl on the right look happy? Is there a cat sitting on a grey cabinet in front of another cat sitting on the stairs? Is one dog biting the ear of the other dog? Is a man standing behind another man sitting at a desk?</td></tr><tr><td>Comparison</td><td>Comparing characteristics like number, attributes, area, or volume between entities.</td><td>Does the scene involve players from three different team colors? Does the tallest building feature glass windows and side slopes? Is the older person following the younger one? Are there two dogs that are significantly different in size? Is the man wearing the same color as the woman in the image?</td></tr><tr><td>Logic</td><td>Understanding logical operators. We only consider negation (as indicated by "no" , "not", or "without") and , universality (as indicated by "every", "all". "each". "both"). Other logical · , relations such as conjunction (as indicated by "and", "or") are omitted.</td><td>Does the image show all men performing the same action? Are both people looking in the same direction? Is the bicycle rider performing a trick without any audience? Is the main subject not wearing shirt and lying down? Is the main activity potentially related to craft or construction?</td></tr><tr><td>World Knowledge</td><td>Answering based on external commonsense knowledge, including social, symbolic, functional, physical, natural knowledge and so</td><td>Is the event related to the Olympics? Is there a vertical depiction of Ramses III in the image? Does the image suggest a relatively informal social gathering? Is a single individual attempting on. to score regardless of multiple defenders?</td></tr></table>{{< /table-caption >}}

> Table 1 presents the performance of 53 vision-language models on the NaturalBench benchmark, highlighting the significant gap between model and human performance.


{{< table-caption caption="🔽 Table 10: Model performance on Relation and Reasoning. We report Q-Acc on each tag." >}}
<br><table id='3' style='font-size:16px'><tr><td rowspan="2">Model</td><td colspan="6">Relation</td><td colspan="5">Reasoning</td></tr><tr><td>Action</td><td>Part</td><td>Proximity</td><td>Topological</td><td>Projective</td><td>Orientation</td><td>Count</td><td>Logic</td><td>Differ</td><td>Compar</td><td>World</td></tr><tr><td>BLIP-3(XGen-MM)</td><td>18.3</td><td>17.4</td><td>27.5</td><td>22.8</td><td>19.6</td><td>15.5</td><td>20.6</td><td>15.9</td><td>13.0</td><td>20.9</td><td>5.3</td></tr><tr><td>Phi-3-Vision</td><td>16.0</td><td>19.5</td><td>19.6</td><td>17.9</td><td>13.9</td><td>9.5</td><td>16.1</td><td>18.5</td><td>17.6</td><td>13.0</td><td>8.5</td></tr><tr><td>DeepSeek-VL-7B-Chat</td><td>17.5</td><td>16.2</td><td>29.4</td><td>21.4</td><td>17.9</td><td>14.7</td><td>19.6</td><td>16.4</td><td>11.1</td><td>11.3</td><td>10.6</td></tr><tr><td>LLaVA-NeXT(Mistral-7B)</td><td>15.9</td><td>18.6</td><td>18.6</td><td>17.0</td><td>16.1</td><td>13.8</td><td>17.1</td><td>21.2</td><td>17.6</td><td>12.2</td><td>9.6</td></tr><tr><td>InternLM-XC-V2-7B</td><td>27.3</td><td>29.3</td><td>29.4</td><td>27.9</td><td>24.4</td><td>24.1</td><td>30.7</td><td>25.9</td><td>27.8</td><td>27.8</td><td>17.0</td></tr><tr><td>InternVL-Chat-V1.2-Plus</td><td>23.6</td><td>28.1</td><td>31.4</td><td>24.4</td><td>19.3</td><td>18.1</td><td>23.9</td><td>26.9</td><td>25.0</td><td>15.7</td><td>12.8</td></tr><tr><td>GPT-4o</td><td>39.4</td><td>43.1</td><td>40.2</td><td>41.7</td><td>38.7</td><td>35.3</td><td>39.2</td><td>42.9</td><td>38.9</td><td>37.4</td><td>35.1</td></tr></table>{{< /table-caption >}}

> Table 10 presents the model's question accuracy (Q-Acc) on different relation and reasoning skills within the NaturalBench benchmark.


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
{{< /gallery >}}