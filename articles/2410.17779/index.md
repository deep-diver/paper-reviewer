---
title: "ADEM-VL: Adaptive and Embedded Fusion for Efficient Vision-Language Tuning"
summary: "ADEM-VL boosts vision-language model efficiency by using a parameter-free cross-attention mechanism, achieving superior accuracy with reduced computational cost."
categories: ["AI Generated"]
tags: ["🔖 24-10-23", "🤗 24-10-25"]
showSummary: true
date: 2024-10-23
draft: false
---

### TL;DR


{{< lead >}}

The research introduces ADEM-VL, a new approach to improve the efficiency of vision-language models.  It uses a technique called parameter-free cross-attention to reduce the number of parameters in the model and speed up both training and inference, which is important because training large vision-language models usually requires a lot of computing power and memory.  The approach also incorporates multiscale visual features to better represent images. Additionally, they have an adaptive fusion approach that dynamically prioritizes the most important visual details for processing. Experiments on various vision-language tasks such as question answering and captioning show that ADEM-VL performs better than existing methods while being more efficient. The researchers suggest that their approach makes it more feasible to use larger language models in vision-language applications, which opens up new possibilities for building more powerful multimodal systems.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.17779" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
Summarizing the provided research paper on ADEM-VL, a novel vision-language tuning method.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} ADEM-VL significantly improves efficiency in vision-language model tuning by reducing parameters and computational cost. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} The parameter-free cross-attention mechanism and adaptive fusion scheme enhance representation learning in the fusion module. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} ADEM-VL outperforms existing methods on various tasks, demonstrating its effectiveness and broader applicability in multimodal learning. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_4_0.png "🔼 Fig. 1. Comparison of different vision-language tuning frameworks: (a) Methods that directly extend the input space of the language model with extracted vision features. (b) Methods that fuse vision information into the language model via cross-attention. (c) Our proposed ADEM-VL framework, which incorporates parameter-free cross-attention, multiscale visual prompting, and adaptive multimodal fusion designs. This approach ensures both parameter and computational efficiency while delivering promising performance.")

> Figure 1 compares different vision-language tuning frameworks, highlighting the proposed ADEM-VL framework's efficient and adaptive multimodal fusion.





![](charts/charts_11_0.png "🔼 Fig. 2. Comparison of different hyperparameter settings in the ADEM-VL with LLaMA-7B as the language model.")

> The chart displays the impact of varying hyperparameters (weight α, weight β, and drop ratio γ) on the average accuracy of the ADEM-VL model using LLaMA-7B.





{{< table-caption caption="🔽 TABLE I EVALUATION RESULTS ON SCIENCEQA TEST SET. NAT = NATURAL SCIENCE, SOC = SOCIAL SCIENCE, LAN = LANGUAGE SCIENCE, TXT = TEXT CONTEXT, IMG = IMAGE CONTEXT, NO = NO CONTEXT, G1-6 = GRADES 1-6, G7-12 = GRADES 7-12." >}}
<br><table id='4' style='font-size:16px'><tr><td colspan="2">Input: text Xt, image Xi, low-rank projection matrix W',</td></tr><tr><td>Output:</td><td>scales S E Zn, drop ratio 2 fused feature XI</td></tr><tr><td colspan="2"></td></tr><tr><td></td><td>1: Xl ← Tokenizer(xt)</td></tr><tr><td>2:</td><td>X v , Xv,cls ← CLIP(xi)</td></tr><tr><td></td><td>3: X ← concat( [X. v,cls, Xi]) 1</td></tr><tr><td>4:</td><td>X v ← Xv W'</td></tr><tr><td>5:</td><td>X' ← X v v</td></tr><tr><td>6:</td><td>for S in S do</td></tr><tr><td>7:</td><td>さ ← pooling(Xv, s) v,s</td></tr><tr><td>8:</td><td>← concat( [X'⌀,</td></tr><tr><td></td><td>X'o s]) v</td></tr><tr><td>9:</td><td>end for ▷ Multiscale visual prompt (Sec. III-C)</td></tr><tr><td>10:</td><td>for layer in LLM do</td></tr><tr><td>11:</td><td>Xl ← layer(Xi)</td></tr><tr><td>12: 13:</td><td>attention A ← silu(Xt)silu(X.)T ▷ Parameter-free cross- attention (Sec. III-B)</td></tr><tr><td>14:</td><td>Asorted ← torch.sort(A, dim=1)</td></tr><tr><td>15:</td><td>Index 2 ← int(y x A.size(dim=1))</td></tr><tr><td>16:</td><td>threshold T ← Asorted [:,2]</td></tr><tr><td>17:</td><td>mask M ← torch.ones. _like(A)</td></tr><tr><td>18: 19:</td><td>M [torch.where(A < T)] ← 0 Adaptine fusion (Sec. III-D)</td></tr><tr><td></td><td>A ← A · M▷</td></tr><tr><td>20:</td><td>X1 ← Xl + AX⌀T</td></tr><tr><td>21:</td><td>end for</td></tr></table>{{< /table-caption >}}

> Table 1 shows the quantitative comparison of different VL model tuning approaches on the ScienceQA dataset, reporting the average accuracy on the test set, and the number of parameters of different methods.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_11_0.png "🔼 Fig. 3. Visualization of image captioning results with LLaMA-7B. In each row, the left figure is the original image, while the middle and right figures demonstrate the dropping decisions for features at two different scales.")

> The figure shows examples of image captioning results, visualizing the model's decisions on which image features to use at each layer for different scales.


![](figures/figures_11_1.png "🔼 Fig. 1. Comparison of different vision-language tuning frameworks: (a) Methods that directly extend the input space of the language model with extracted vision features. (b) Methods that fuse vision information into the language model via cross-attention. (c) Our proposed ADEM-VL framework, which incorporates parameter-free cross-attention, multiscale visual prompting, and adaptive multimodal fusion designs. This approach ensures both parameter and computational efficiency while delivering promising performance.")

> The figure compares different vision-language tuning frameworks, highlighting the proposed ADEM-VL framework's efficiency and effectiveness.


![](figures/figures_11_2.png "🔼 Fig. 1. Comparison of different vision-language tuning frameworks: (a) Methods that directly extend the input space of the language model with extracted vision features. (b) Methods that fuse vision information into the language model via cross-attention. (c) Our proposed ADEM-VL framework, which incorporates parameter-free cross-attention, multiscale visual prompting, and adaptive multimodal fusion designs. This approach ensures both parameter and computational efficiency while delivering promising performance.")

> The figure compares different vision-language tuning frameworks, highlighting the proposed ADEM-VL framework's efficient and adaptive multimodal fusion approach.


![](figures/figures_11_3.png "🔼 Fig. 3. Visualization of image captioning results with LLaMA-7B. In each row, the left figure is the original image, while the middle and right figures demonstrate the dropping decisions for features at two different scales.")

> Figure 3 shows examples of image captioning results, visualizing how the model makes decisions on which image features to use based on their importance for each text token at different scales.


![](figures/figures_11_4.png "🔼 Fig. 1. Comparison of different vision-language tuning frameworks: (a) Methods that directly extend the input space of the language model with extracted vision features. (b) Methods that fuse vision information into the language model via cross-attention. (c) Our proposed ADEM-VL framework, which incorporates parameter-free cross-attention, multiscale visual prompting, and adaptive multimodal fusion designs. This approach ensures both parameter and computational efficiency while delivering promising performance.")

> The figure compares three different vision-language tuning frameworks, highlighting the proposed ADEM-VL framework's efficiency and effectiveness in multimodal fusion.


![](figures/figures_11_5.png "🔼 Fig. 3. Visualization of image captioning results with LLaMA-7B. In each row, the left figure is the original image, while the middle and right figures demonstrate the dropping decisions for features at two different scales.")

> The figure visualizes image captioning results, showing the original image alongside visualizations of the model's decisions on which image features to drop at different scales.


![](figures/figures_11_6.png "🔼 Fig. 3. Visualization of image captioning results with LLaMA-7B. In each row, the left figure is the original image, while the middle and right figures demonstrate the dropping decisions for features at two different scales.")

> The figure shows how the adaptive fusion scheme in ADEM-VL dynamically discards less relevant visual features for improved efficiency and performance in image captioning.


![](figures/figures_12_0.png "🔼 Fig. 4. Examples of zero-shot instruction-following tasks with LLaMA-7B.")

> The figure shows example outputs from a vision-language model performing zero-shot instruction following tasks, demonstrating its ability to generate coherent and relevant responses based on image and instruction inputs.


![](figures/figures_12_1.png "🔼 Fig. 1. Comparison of different vision-language tuning frameworks: (a) Methods that directly extend the input space of the language model with extracted vision features. (b) Methods that fuse vision information into the language model via cross-attention. (c) Our proposed ADEM-VL framework, which incorporates parameter-free cross-attention, multiscale visual prompting, and adaptive multimodal fusion designs. This approach ensures both parameter and computational efficiency while delivering promising performance.")

> The figure compares three different vision-language tuning frameworks, highlighting the proposed ADEM-VL framework's efficient and adaptive multimodal fusion approach.


![](figures/figures_12_2.png "🔼 Fig. 1. Comparison of different vision-language tuning frameworks: (a) Methods that directly extend the input space of the language model with extracted vision features. (b) Methods that fuse vision information into the language model via cross-attention. (c) Our proposed ADEM-VL framework, which incorporates parameter-free cross-attention, multiscale visual prompting, and adaptive multimodal fusion designs. This approach ensures both parameter and computational efficiency while delivering promising performance.")

> The figure compares different vision-language tuning frameworks, highlighting the proposed ADEM-VL framework's efficiency and effectiveness through parameter-free cross-attention, multiscale visual prompting, and adaptive fusion.


![](figures/figures_12_3.png "🔼 Fig. 1. Comparison of different vision-language tuning frameworks: (a) Methods that directly extend the input space of the language model with extracted vision features. (b) Methods that fuse vision information into the language model via cross-attention. (c) Our proposed ADEM-VL framework, which incorporates parameter-free cross-attention, multiscale visual prompting, and adaptive multimodal fusion designs. This approach ensures both parameter and computational efficiency while delivering promising performance.")

> The figure compares different vision-language tuning frameworks, highlighting the proposed ADEM-VL framework's efficiency and effectiveness through parameter-free cross-attention, multiscale visual prompting, and adaptive fusion.


</details>




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 TABLE I EVALUATION RESULTS ON SCIENCEQA TEST SET. NAT = NATURAL SCIENCE, SOC = SOCIAL SCIENCE, LAN = LANGUAGE SCIENCE, TXT = TEXT CONTEXT, IMG = IMAGE CONTEXT, NO = NO CONTEXT, G1-6 = GRADES 1-6, G7-12 = GRADES 7-12." >}}
<table id='4' style='font-size:18px'><tr><td rowspan="2">Method</td><td colspan="2">#Param</td><td colspan="3">Subject</td><td colspan="3">Context Modality</td><td colspan="2">Grade</td><td rowspan="2">Average</td></tr><tr><td>Trainable</td><td>LLM</td><td>NAT</td><td>SOC</td><td>LAN</td><td>TXT</td><td>IMG</td><td>NO</td><td>G1-6 G7-12</td><td></td></tr><tr><td colspan="12">Zero-/few-shot methods</td></tr><tr><td>Human [68]</td><td>-</td><td>-</td><td>90.23</td><td>84.97</td><td>87.48</td><td>89.60</td><td>87.50</td><td>88.10</td><td>91.59</td><td>82.42</td><td>88.40</td></tr><tr><td>GPT-3.5 [68]</td><td>-</td><td>-</td><td>74.64</td><td>69.74</td><td>76.00</td><td>74.44</td><td>67.28</td><td>77.42</td><td>76.80</td><td>68.89</td><td>73.97</td></tr><tr><td>GPT-3.5 [68]</td><td>-</td><td>-</td><td>75.44</td><td>70.87</td><td>78.09</td><td>74.68</td><td>67.43</td><td>79.93</td><td>78.23</td><td>69.68</td><td>75.17</td></tr><tr><td>GPT-4 []</td><td>-</td><td>-</td><td>84.06</td><td>73.45</td><td>87.36</td><td>81.87</td><td>70.75</td><td>90.73</td><td>84.69</td><td>79.10</td><td>82.69</td></tr><tr><td colspan="12">Full training methods</td></tr><tr><td>UnifiedQA [68]</td><td>223M</td><td>-</td><td>71.00</td><td>76.04</td><td>78.91</td><td>66.42</td><td>66.53</td><td>81.81</td><td>77.06</td><td>68.82</td><td>74.11</td></tr><tr><td>MM-CoTBase [69]</td><td>223M</td><td>-</td><td>87.52</td><td>77.17</td><td>85.82</td><td>87.88</td><td>82.90</td><td>86.83</td><td>84.65</td><td>85.37</td><td>84.91</td></tr><tr><td>MM-CoTLarge [69]</td><td>733M</td><td>-</td><td>95.91</td><td>82.00</td><td>90.82</td><td>95.26</td><td>88.80</td><td>92.89</td><td>92.44</td><td>90.31</td><td>91.68</td></tr><tr><td>LLaVA []</td><td>7B</td><td>7B</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>89.84</td></tr><tr><td>LLaVA []</td><td>13B</td><td>13B</td><td>90.36</td><td>95.95</td><td>88.00</td><td>89.49</td><td>88.00</td><td>90.66</td><td>90.93</td><td>90.90</td><td>90.92</td></tr><tr><td colspan="12">PEFT methods with LLaMA</td></tr><tr><td>LLaMA-Adapter []</td><td>1.8M</td><td>7B</td><td>84.37</td><td>88.30</td><td>84.36</td><td>83.72</td><td>80.32</td><td>86.90</td><td>85.83</td><td>84.05</td><td>85.19</td></tr><tr><td>LLaVA-LoRA []</td><td>4.4M</td><td>7B</td><td>91.70</td><td>94.60</td><td>86.09</td><td>91.25</td><td>90.28</td><td>88.64</td><td>91.52</td><td>89.65</td><td>90.85</td></tr><tr><td>LaVIN [10]</td><td>3.8M</td><td>7B</td><td>89.25</td><td>94.94</td><td>85.24</td><td>88.51</td><td>87.46</td><td>88.08</td><td>90.16</td><td>88.07</td><td>89.41</td></tr><tr><td>LaVIN [10]</td><td>5.4M</td><td>13B</td><td>90.32</td><td>94.38</td><td>87.73</td><td>89.44</td><td>87.65</td><td>90.31</td><td>91.19</td><td>89.26</td><td>90.50</td></tr><tr><td>Mem VP [59]</td><td>3.9M</td><td>7B</td><td>94.45</td><td>95.05</td><td>88.64</td><td>93.99</td><td>92.36</td><td>90.94</td><td>93.10</td><td>93.01</td><td>93.07</td></tr><tr><td>Mem VP [59]</td><td>5.5M</td><td>13B</td><td>95.07</td><td>95.15</td><td>90.00</td><td>94.43</td><td>92.86</td><td>92.47</td><td>93.61</td><td>94.07</td><td>93.78</td></tr><tr><td>ADEM-VL</td><td>4.5M</td><td>7B</td><td>95.52</td><td>95.39</td><td>89.18</td><td>95.36</td><td>93.95</td><td>90.94</td><td>93.87</td><td>93.80</td><td>93.85</td></tr><tr><td>ADEM-VL</td><td>5.5M</td><td>13B</td><td>96.00</td><td>94.94</td><td>91.27</td><td>95.45</td><td>93.95</td><td>93.03</td><td>94.46</td><td>94.73</td><td>94.55</td></tr><tr><td colspan="12">PEFT methods with LLaMA2</td></tr><tr><td>Mem VP [59]</td><td>3.9M</td><td>7B</td><td>93.12</td><td>94.60</td><td>89.27</td><td>92.86</td><td>91.13</td><td>91.15</td><td>92.51</td><td>92.29</td><td>92.43</td></tr><tr><td>ADEM-VL</td><td>4.5M</td><td>7B</td><td>95.74</td><td>94.83</td><td>90.00</td><td>95.50</td><td>93.75</td><td>91.78</td><td>94.16</td><td>93.87</td><td>94.06</td></tr></table>{{< /table-caption >}}

> Table I presents a comparison of various vision-language models' performance on the ScienceQA dataset, categorized by method type (zero-/few-shot, full training, parameter-efficient fine-tuning), model size, and context modality, showing the average accuracy achieved.


{{< table-caption caption="🔽 TABLE II EVALUATION RESULTS ON COCO CAPTION USING THE KARPATHY TEST SPLIT WITH LLAMA-13B AS THE LANGUAGE MODEL. #T. = TRAINABLE PARAMETERS. *PEFT METHODS." >}}
<table id='9' style='font-size:18px'><tr><td>Method</td><td>#T.</td><td>BLEU-4</td><td>CIDEr</td></tr><tr><td>ClipCap [77]</td><td>-</td><td>33.5</td><td>113.1</td></tr><tr><td>VisionLLM-H [78]</td><td>-</td><td>32.1</td><td>114.2</td></tr><tr><td>BLIP [60]</td><td>583M</td><td>40.4</td><td>136.7</td></tr><tr><td>BLIP-2 [35]</td><td>188M</td><td>43.7</td><td>145.3</td></tr><tr><td>*LLaMA-Adapter V2 [29]</td><td>14M</td><td>36.2</td><td>122.2</td></tr><tr><td>*LaVIN [10]</td><td>5.4M</td><td>37.8</td><td>131.7</td></tr><tr><td>* ADEM-VL</td><td>5.5M</td><td>38.5</td><td>133.2</td></tr></table>{{< /table-caption >}}

> The table presents quantitative results of different vision-language models on the COCO Caption dataset, comparing the performance of various approaches in terms of BLEU-4 and CIDEr scores, along with the number of trainable parameters.


{{< table-caption caption="🔽 TABLE III EVALUATION RESULTS ON THE MME BENCHMARK WITH LLAMA-13B AS THE LANGUAGE MODEL. MME-C AND MME-P MEASURE THE PERCEPTION AND COGNITION ABILITIES OF THE MODEL, RESPECTIVELY. EXTRA TOKENS REFER TO THE NUMBER OF ADDITIONAL TOKENS PROCESSED BY THE LLM BEYOND THE STANDARD TEXT TOKENS. #T. = TRAINABLE PARAMETERS. *PEFT METHODS." >}}
<table id='4' style='font-size:18px'><tr><td>Method</td><td>#Trainable param</td><td>#Extra tokens</td><td>MME-P</td><td>MME-C</td></tr><tr><td>LLaVA []</td><td>13B</td><td>256</td><td>502.8</td><td>214.6</td></tr><tr><td>* Prompt-Aware Adapter [79]</td><td>-</td><td>256</td><td>1375.0</td><td>289.3</td></tr><tr><td>* MiniGPT-4 [36]</td><td>-</td><td>256</td><td>866.5</td><td>292.1</td></tr><tr><td>* LayerNorm [80]</td><td>325M</td><td>256</td><td>929.3</td><td>254.3</td></tr><tr><td>LayerNorm-simp. [80]</td><td>0.4M</td><td>256</td><td>824.3</td><td>221.1</td></tr><tr><td>* LLaMA-Adapter [9]</td><td>14M</td><td>-</td><td>972.6</td><td>248.9</td></tr><tr><td>** LaVIN [10]</td><td>5.4M</td><td>7</td><td>963.6</td><td>249.6</td></tr><tr><td>ADEM-VL</td><td>5.5M</td><td>1</td><td>966.2</td><td>270.7</td></tr></table>{{< /table-caption >}}

> Table III presents a comparison of different vision-language models on the MME benchmark, showing the number of trainable parameters, extra tokens, and performance scores for perception and cognition.


{{< table-caption caption="🔽 TABLE IV COMPARISON AMONG DIFFERENT VL MODELS ON MORE IMAGE UNDERSTANDING TASKS. * BASELINE RESULTS EVALUATED THROUGH OUR IMPLEMENTATION USING THE OFFICIAL CHECKPOINT." >}}
<table id='6' style='font-size:16px'><tr><td rowspan="2">Method</td><td colspan="2">#Param</td><td colspan="2">Image QA</td><td colspan="2">Benchmark</td></tr><tr><td>Trainable</td><td>LLM</td><td>VQAv2</td><td>GQA</td><td>MMB</td><td>MMMU</td></tr><tr><td colspan="7">Full training methods</td></tr><tr><td>LLaVA []</td><td>13B</td><td>13B</td><td>-</td><td>-</td><td>34.1</td><td>32.3</td></tr><tr><td>mPLUG-Owl2 [81]</td><td>8.2B</td><td>8.2B</td><td>79.4</td><td>56.1</td><td>64.5</td><td>-</td></tr><tr><td>InternLM-XComposer2 [32]</td><td>7B</td><td>7B</td><td>-</td><td>-</td><td>79.6</td><td>42.0</td></tr><tr><td>MoE-LLaVA-1.6Bx4-Top2 [82]</td><td>6.4B</td><td>6.4B</td><td>76.7</td><td>60.3</td><td>60.2</td><td>-</td></tr><tr><td colspan="7">PEFT methods</td></tr><tr><td>MiniGPT-4 [36]</td><td>-</td><td>13B</td><td>-</td><td>-</td><td>23.0</td><td>-</td></tr><tr><td>LaVIN [10]</td><td>5.4M</td><td>13B</td><td>68.6*</td><td>48.8*</td><td>56.7*</td><td>35.0*</td></tr><tr><td>ADEM-VL</td><td>4.5M</td><td>7B</td><td>71.7</td><td>52.4</td><td>52.4</td><td>34.2</td></tr><tr><td>ADEM-VL</td><td>5.5M</td><td>13B</td><td>73.5</td><td>56.0</td><td>58.4</td><td>38.3</td></tr></table>{{< /table-caption >}}

> Table IV compares the performance of different vision-language models on various image understanding tasks, including the number of trainable parameters and the performance on VQAv2, GQA, MMB, and MMMU benchmarks.


{{< table-caption caption="🔽 TABLE V TRAINING AND INFERENCE SPEED OF DIFFERENT APPROACHES. MEMORY-SAVING OR SPEED-UP APPROACHES SUCH AS CHECKPOINTING AND FLAASHATTENTION ARE NOT ADOPTED. FLOPS ARE ESTIMATED FOR GENERATING A SINGLE NEW TOKEN WITH A TEXT SEQUENCE LENGTH OF 256. EXPERIMENTS ON COCO CAPTIONING AND INSTRUCTION-FOLLOWING WERE NOT IMPLEMENTED IN THE ORIGINAL PAPERS OF LLAVA-LORA AND MEMVP, SO THE OVERALL TRAINING TIME FOR THESE TASKS IS UNAVAILABLE." >}}
<table id='4' style='font-size:18px'><tr><td rowspan="2">Method</td><td colspan="2">#Param</td><td rowspan="2">FLOPs</td><td colspan="2">#Time (s/batch)</td><td colspan="3">#Overall training time (GPU Hours)</td></tr><tr><td>T.</td><td>LLM</td><td>Training</td><td>Inference</td><td>ScienceQA</td><td>COCO caption</td><td>Instruction</td></tr><tr><td>LLaVA-LoRA [59]</td><td>4.4M</td><td>7B</td><td>110.44T</td><td>0.49</td><td>3.42</td><td>8.8</td><td>-</td><td>-</td></tr><tr><td>LaVIN [10]</td><td>3.8M</td><td>7B</td><td>56.19T</td><td>0.39</td><td>2.06</td><td>6.8</td><td>12.7</td><td>211.4</td></tr><tr><td>MemVP [59]</td><td>3.9M</td><td>7B</td><td>54.81T</td><td>0.28</td><td>1.88</td><td>5.1</td><td>-</td><td>-</td></tr><tr><td>MemVP [59]</td><td>5.5M</td><td>13B</td><td>132.76T</td><td>0.46</td><td>3.07</td><td>8.1</td><td>-</td><td>-</td></tr><tr><td>ADEM-VL</td><td>4.5M</td><td>7B</td><td>54.93T</td><td>0.25</td><td>1.86</td><td>4.3</td><td>8.0</td><td>134.8</td></tr><tr><td>ADEM-VL</td><td>5.5M</td><td>13B</td><td>133.26T</td><td>0.39</td><td>2.97</td><td>6.9</td><td>12.5</td><td>212.9</td></tr></table>{{< /table-caption >}}

> This table compares the training and inference speed, along with the number of parameters and FLOPs, of various vision-language models.


{{< table-caption caption="🔽 TABLE VI ABLATION STUDY OF EACH MODULE IN OUR ADEM-VL FRAMEWORK WITH LLAMA-7B AS THE LANGUAGE MODEL." >}}
<table id='7' style='font-size:18px'><tr><td rowspan="2">Setting</td><td rowspan="2">#Trainable</td><td colspan="3">Subject</td><td colspan="3">Context Modality</td><td colspan="2">Grade</td><td rowspan="2">Average</td></tr><tr><td>NAT</td><td>SOC</td><td>LAN</td><td>TXT</td><td>IMG</td><td>NO</td><td>G1-6</td><td>G7-12</td></tr><tr><td>Baseline</td><td>3.4M</td><td>93.49</td><td>95.05</td><td>88.21</td><td>92.85</td><td>91.28</td><td>90.92</td><td>92.50</td><td>92.35</td><td>92.45</td></tr><tr><td>+ [cls] token</td><td>4.0M</td><td>93.70</td><td>95.00</td><td>88.46</td><td>93.19</td><td>91.85</td><td>90.63</td><td>92.37</td><td>93.05</td><td>92.61</td></tr><tr><td>+ Parameter-free xattn</td><td>4.0M</td><td>94.60</td><td>95.65</td><td>89.00</td><td>94.56</td><td>93.19</td><td>90.89</td><td>93.42</td><td>93.27</td><td>93.37</td></tr><tr><td>+ Multiscale VP</td><td>4.5M</td><td>95.10</td><td>95.50</td><td>88.50</td><td>94.87</td><td>93.48</td><td>90.66</td><td>93.61</td><td>93.21</td><td>93.47</td></tr><tr><td>+ Adaptive fusion</td><td>4.5M</td><td>95.52</td><td>95.39</td><td>89.18</td><td>95.36</td><td>93.95</td><td>90.94</td><td>93.87</td><td>93.80</td><td>93.85</td></tr></table>{{< /table-caption >}}

> Table VI presents the ablation study of each component in the ADEM-VL framework using LLaMA-7B as the language model, showing the impact of each module on the average accuracy across various categories and grades.


{{< table-caption caption="🔽 TABLE VII COMPARISON OF DIFFERENT LOCATIONS FOR INSERTING CROSS-ATTENTION MODULES WITH LLAMA-7B AS THE LANGUAGE MODEL. 'QUERY FROM' INDICATES WHICH FEATURES OF THE LANGUAGE MODEL SERVE AS INPUTS TO THE CROSS-ATTENTION MODULES, WHILE 'ADD TO' INDICATES WHERE THE OUTPUT OF THESE MODULES IS FUSED INTO THE FEATURES OF THE LANGUAGE MODEL BY ADDITION." >}}
<table id='10' style='font-size:20px'><tr><td>Query from</td><td>Add to</td><td>Average</td></tr><tr><td>MHSA (in)</td><td>MHSA (in)</td><td>92.19</td></tr><tr><td>MHSA (in)</td><td>MHSA (out)</td><td>93.18</td></tr><tr><td>MHSA (out)</td><td>MHSA (out)</td><td>92.00</td></tr><tr><td>MLP (in)</td><td>MLP (in)</td><td>91.77</td></tr><tr><td>MLP (in)</td><td>MLP (out)</td><td>93.85</td></tr><tr><td>MLP (out)</td><td>MLP (out)</td><td>92.27</td></tr></table>{{< /table-caption >}}

> The table compares the average accuracy on the ScienceQA dataset using different configurations of cross-attention module placement within the language model.


{{< table-caption caption="🔽 TABLE VIII COMPARISON OF DIFFERENT NON-PARAMETERIZED LINEAR PROJECTION IN EQUATION 3 WITH LLAMA-7B AS THE LANGUAGE MODEL." >}}
<table id='12' style='font-size:18px'><tr><td>Projection</td><td>formula</td><td>Average</td></tr><tr><td>None</td><td>x → x</td><td>92.16</td></tr><tr><td>Softmax</td><td>x → softmax(x)</td><td>79.42</td></tr><tr><td>ReLU</td><td>x → relu(x)</td><td>91.99</td></tr><tr><td>ELU</td><td>x → elu(x)</td><td>92.45</td></tr><tr><td>SiLU</td><td>x → silu(x)</td><td>93.85</td></tr><tr><td>SiLU (positive)</td><td>x → silu(x) - min(x)</td><td>38.58</td></tr></table>{{< /table-caption >}}

> Table VIII compares different non-parameterized linear projection methods used in Equation 3 of the ADEM-VL framework, showing their impact on the average accuracy when using LLaMA-7B as the language model.


{{< table-caption caption="🔽 TABLE IX COMPARISON OF DIFFERENT DOWNSAMPLING METHODS AND SCALES IN GENERATING MULTIMODAL VISUAL PROMPTS WITH LLAMA-7B AS THE LANGUAGE MODEL." >}}
<table id='5' style='font-size:20px'><tr><td>Down sample</td><td>Size</td><td>Average</td></tr><tr><td>None</td><td>256</td><td>93.70</td></tr><tr><td>Avg. pooling</td><td>64</td><td>92.82</td></tr><tr><td>Avg. pooling</td><td>16</td><td>91.65</td></tr><tr><td>Avg. pooling</td><td>concat(64,16)</td><td>93.24</td></tr><tr><td>Avg. pooling</td><td>concat(256,16)</td><td>93.65</td></tr><tr><td>Avg. pooling</td><td>concat(256,64)</td><td>93.85</td></tr><tr><td>Avg. pooling</td><td>concat(256,64,16)</td><td>93.59</td></tr><tr><td>Max pooling</td><td>concat(256,64)</td><td>93.55</td></tr></table>{{< /table-caption >}}

> Table IX shows the comparison of different downsampling methods and scales in generating multimodal visual prompts with LLaMA-7B as the language model, presenting average accuracy results for various configurations.


{{< table-caption caption="🔽 TABLE X INTEGRATION WITH DIFFERENT INPUT-STAGE FUSION SCHEMES WITH LLAMA-7B AS THE LANGUAGE MODEL." >}}
<table id='7' style='font-size:16px'><tr><td colspan="2">Visual input</td><td rowspan="2">Average</td></tr><tr><td>#Visual tokens</td><td>[cls] token</td></tr><tr><td>0</td><td>X</td><td>92.97</td></tr><tr><td>0</td><td>V</td><td>93.85</td></tr><tr><td>64</td><td>X</td><td>92.47</td></tr><tr><td>64</td><td>V</td><td>92.86</td></tr><tr><td>256</td><td>X</td><td>89.86</td></tr><tr><td>256</td><td>V</td><td>90.17</td></tr></table>{{< /table-caption >}}

> Table X shows the impact of integrating different input-stage fusion schemes on the performance of the ADEM-VL model using LLaMA-7B, comparing the use of [cls] tokens and different numbers of visual tokens.


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