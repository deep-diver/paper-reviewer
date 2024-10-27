---
title: "MotionCLR: Motion Generation and Training-free Editing via Understanding Attention Mechanisms"
summary: "MotionCLR: Training-free motion editing via attention mechanism manipulation.  Versatile editing, good generation, and explainability."
categories: ["AI Generated"]
tags: ["🔖 24-10-24", "🤗 24-10-25"]
showSummary: true
date: 2024-10-24
draft: false
---

### TL;DR


{{< lead >}}

MotionCLR is an innovative method for generating and editing human motion. Unlike previous models that struggle with fine-grained control and lack explainability, MotionCLR utilizes attention mechanisms (specifically self-attention and cross-attention) to achieve precise control over motion generation and editing.  Self-attention focuses on sequential similarity between frames, influencing the order of motion features. Cross-attention establishes word-sequence correspondence, activating relevant timesteps in the motion sequence. This enables various editing methods like motion de-emphasizing, in-place replacement, and example-based generation.  Experiments show MotionCLR generates high-quality motions comparable to existing methods and supports the proposed edits with good explainability.  Additionally, the model demonstrates the potential for action counting and grounded generation using attention maps, effectively addressing cases of hallucination.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18977" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
MotionCLR is a novel attention-based motion diffusion model that enables versatile, training-free motion editing by leveraging attention mechanisms.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} MotionCLR, a new attention-based diffusion model, provides comparable motion generation quality to state-of-the-art methods. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} MotionCLR enables versatile, training-free motion editing through simple yet effective manipulation of attention maps. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The paper clarifies the roles of self- and cross-attention mechanisms in motion generation and editing, enhancing model explainability. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_1_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing through attention mechanism manipulations.





![](charts/charts_6_0.png "🔼 Figure 4: Motion editing via manipulating attention maps.")

> The figure illustrates three motion editing methods (motion de-emphasizing, in-place motion replacement, and motion sequence shifting) by manipulating attention maps.





{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<table id='0' style='font-size:16px'><tr><td rowspan="2">Methods</td><td colspan="3">R-Precision↑</td><td rowspan="2">FID↓</td><td rowspan="2">MM-Dist↓</td><td rowspan="2">Multi-Modality↑</td></tr><tr><td>Top 1</td><td>Top 2</td><td>Top 3</td></tr><tr><td>TM2T [2022b]</td><td>0.424±0.003</td><td>0.618±0.003</td><td>0.729±0.002</td><td>1.501 ±0.017</td><td>3.467±0.011</td><td>2.424±0.093</td></tr><tr><td>T2M [2022a]</td><td>0.455±0.003</td><td>0.636±0.003</td><td>0.736±0.002</td><td>1.087±0.021</td><td>3.347±0.008</td><td>2.219±0.074</td></tr><tr><td>MDM [2022b]</td><td>-</td><td>-</td><td>0.611 ±0.007</td><td>0.544±0.044</td><td>5.566±0.027</td><td>2.799±0.072</td></tr><tr><td>MLD [2023b]</td><td>0.481 ±0.003</td><td>0.673±0.003</td><td>0.772±0.002</td><td>0.473±0.013</td><td>3.196±0.010</td><td>2.413±0.079</td></tr><tr><td>MotionDiffuse [2024b]</td><td>0.491 ±0.001</td><td>0.681 ±0.001</td><td>0.782±0.001</td><td>0.630±0.001</td><td>3.113±0.001</td><td>1.553±0.042</td></tr><tr><td>T2M-GPT [2023a]</td><td>0.492±0.003</td><td>0.679±0.002</td><td>0.775±0.002</td><td>0.141 士0.005</td><td>3.121 ±0.009</td><td>1.831 ±0.048</td></tr><tr><td>ReMoDiffuse [2023b]</td><td>0.510±0.005</td><td>0.698±0.006</td><td>0.795±0.004</td><td>0.103±0.004</td><td>2.974±0.016</td><td>1.795±0.043</td></tr><tr><td>MoMask [2024a]</td><td>0.521 ±0.002</td><td>0.713±0.002</td><td>0.807±0.002</td><td>0.045 ±0.002</td><td>2.958±0.008</td><td>1.241 ±0.040</td></tr><tr><td>MotionCLR</td><td>0.542±0.001</td><td>0.733±0.002</td><td>0.827±0.003</td><td>0.099±0.003</td><td>2.981±0.011</td><td>2.145±0.043</td></tr><tr><td>MotionCLR*</td><td>0.544±0.001</td><td>0.732±0.001</td><td>0.831 士0.002</td><td>0.269±0.001</td><td>2.806±0.014</td><td>1.985±0.044</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MotionCLR with other state-of-the-art methods on the HumanML3D dataset, using metrics such as R-Precision, FID, MM-Dist, and Multi-Modality.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_1_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulation, showing examples of de-emphasizing, in-place replacement, diverse generation, style transfer, and sequential editing.


![](figures/figures_1_2.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention maps, showcasing motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_1_3.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention maps to achieve motion (de-)emphasizing, in-place motion replacement, example-based motion generation, motion style transfer, and motion sequence shifting.


![](figures/figures_1_4.png "🔼 Figure 4: Motion editing via manipulating attention maps.")

> The figure shows three different motion editing methods by manipulating attention maps: motion (de-)emphasizing, in-place motion replacement, and motion sequence shifting.


![](figures/figures_1_5.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention maps, showcasing motion de-emphasizing, emphasizing, in-place replacement, style transfer, and sequence editing.


![](figures/figures_1_6.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention mechanisms.


![](figures/figures_1_7.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing, including de-emphasizing, emphasizing, in-place replacing, style transferring, and editing the sequentiality of a motion.


![](figures/figures_1_8.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention mechanisms.


![](figures/figures_4_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention maps, showcasing motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_5_0.png "🔼 Figure 3: Empirical study of attention mechanisms. We use 'a person jumps.' as an example. (a) Key frames of generated motion. (b) The root trajectory along the Y-axis (vertical height). The character jumps on ~15-40f, ~60-80f, and ~125-145f, respectively. (c) The cross-attention between timesteps and words. The 'jump' word is highly activated aligning with the 'jump' action. (d) The self-attention map visualization. It is obvious that the character jumps three times. Different jumps share similar local motion patterns.")

> Figure 3 empirically studies attention mechanisms by visualizing key frames of generated motion, root trajectory, cross-attention between timesteps and words, and self-attention map for the sentence 'a person jumps.'


![](figures/figures_7_0.png "🔼 Figure 3: Empirical study of attention mechanisms. We use 'a person jumps.' as an example. (a) Key frames of generated motion. (b) The root trajectory along the Y-axis (vertical height, in Fig. 3b). As can be seen in Fig. 3, the character jumps at ~ 15-40f, ~ 60-80f, and ~ 125-145f, respectively. (c) The cross-attention between timesteps and words. The 'jump' word is highly activated aligning with the 'jump' action. (d) The self-attention map visualization. It is obvious that the character jumps three times. Different jumps share similar local motion patterns.")

> Figure 3 shows an empirical study of attention mechanisms by visualizing key frames, root trajectory, cross-attention between timesteps and words, and self-attention map of a generated motion for the sentence 'a person jumps.'


![](figures/figures_8_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via several methods, including de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_8_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing, including de-emphasizing, emphasizing, in-place replacement, style transfer, and sequentiality editing.


![](figures/figures_8_2.png "🔼 Figure 3: Empirical study of attention mechanisms. We use 'a person jumps.' as an example. (a) Key frames of generated motion. (b) The root trajectory along the Y-axis (vertical height, in Fig. 3b). As can be seen in Fig. 3, the character jumps at ~ 15 - 40f, ~ 60 - 80f, and ~ 125-145f, respectively. (c) The cross-attention between timesteps and words. The 'jump' word is highly activated aligning with the 'jump' action. (d) The self-attention map visualization. It is obvious that the character jumps three times. Different jumps share similar local motion patterns.")

> Figure 3 shows an empirical study of attention mechanisms in MotionCLR, visualizing key frames, root trajectory, cross-attention between timesteps and words, and self-attention map for a 'person jumps.' example.


![](figures/figures_8_3.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing through attention mechanism manipulations.


![](figures/figures_9_0.png "🔼 Figure 10: Diverse generated motions driven by the same example. Prompt: “a person steps sideways to the left and then sideways to the right.”. (a) The diverse generated motions driven by the same example motion share similar movement content. (b) The root trajectories of diverse motions are with similar global trajectories, but not the same.")

> Figure 10 shows diverse generated motions sharing similar movement content but different trajectories, driven by the same example prompt.


![](figures/figures_9_1.png "🔼 Figure 10: Diverse generated motions driven by the same example. Prompt: “a person steps sideways to the left and then sideways to the right.” (a) The diverse generated motions driven by the same example motion share similar movement content. (b) The root trajectories of diverse motions are with similar global trajectories, but not the same.")

> Figure 10 shows diverse generated motions with similar movement content but different root trajectories, all driven by the same example prompt.


![](figures/figures_10_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention mechanisms.


![](figures/figures_10_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing, including de-emphasizing, emphasizing, in-place replacement, style transfer, and sequentiality editing.


![](figures/figures_10_2.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing through attention mechanism manipulations.


![](figures/figures_10_3.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention mechanisms.


![](figures/figures_10_4.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulations.


![](figures/figures_10_5.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention mechanisms, as shown through examples of de-emphasizing, in-place replacement, diverse generation, style transfer, and sequential editing.


![](figures/figures_24_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention mechanisms.


![](figures/figures_24_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention mechanisms to de-emphasize, emphasize, replace, transfer, and shift motion sequences.


![](figures/figures_24_2.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulation.


![](figures/figures_24_3.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention mechanisms.


![](figures/figures_24_4.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing through various methods including motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_24_5.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanisms, showcasing motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_24_6.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via several methods, including de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_24_7.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulation.


![](figures/figures_24_8.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing, including de-emphasizing, emphasizing, in-place replacement, style transfer, and sequentiality editing.


![](figures/figures_24_9.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention mechanisms.


![](figures/figures_24_10.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention maps, showing examples of de-emphasizing, in-place replacement, diverse generation, style transfer, and sequential editing.


![](figures/figures_24_11.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing through attention mechanism manipulations.


![](figures/figures_25_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing, including de-emphasizing, emphasizing, in-place replacement, style transfer, and sequentiality editing.


![](figures/figures_25_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing, including de-emphasizing, emphasizing, in-place replacement, style transfer, and sequentiality editing.


![](figures/figures_26_0.png "🔼 Figure 10: Diverse generated motions driven by the same example. Prompt: 'a person steps sideways to the left and then sideways to the right.'. (a) The diverse generated motions driven by the same example motion share similar movement content. (b) The root trajectories of diverse motions are with similar global trajectories, but not the same.")

> Figure 10 shows diverse generated motions with similar movement content but different trajectories driven by the same example motion prompt.


![](figures/figures_26_1.png "🔼 Figure 10: Diverse generated motions driven by the same example. Prompt: 'a person steps sideways to the left and then sideways to the right.'. (a) The diverse generated motions driven by the same example motion share similar movement content. (b) The root trajectories of diverse motions are with similar global trajectories, but not the same.")

> Figure 10 shows diverse generated motions driven by the same example motion, demonstrating both similar movement content and diverse root trajectories.


![](figures/figures_27_0.png "🔼 Figure 13: Comparison between w/ vs. w/o grounded motion generation settings. The root height and motion visualization of the textual prompt “a person jumps four times”.")

> The figure compares the results of motion generation with and without temporal grounding, showing how grounding corrects hallucination in the number of jumps.


![](figures/figures_28_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulations, including de-emphasizing, emphasizing, in-place replacement, style transfer, and sequence shifting.


![](figures/figures_29_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention mechanisms.


![](figures/figures_30_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention mechanisms.


![](figures/figures_30_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing through various methods, including de-emphasizing, emphasizing, in-place replacement, style transfer, and sequence editing.


![](figures/figures_31_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention maps.


![](figures/figures_33_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing by manipulating attention mechanisms, enabling various editing operations such as de-emphasizing, emphasizing, replacing, generating, and shifting motions.


![](figures/figures_37_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulations, including de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_37_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanisms, showcasing motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequential editing.


![](figures/figures_38_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulation, showcasing motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequential editing.


![](figures/figures_39_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via manipulating attention maps, showcasing motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequential editing.


![](figures/figures_39_1.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulations.


![](figures/figures_40_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via attention mechanism manipulations, showcasing motion de-emphasizing, in-place replacement, example-based generation, style transfer, and sequentiality editing.


![](figures/figures_41_0.png "🔼 Figure 1: MotionCLR (/'moυ∫n klır/) supports versatile motion generation and editing. The blue and red figures represent original and edited motions. (a) Motion deemphasizing and emphasizing via adjusting the weight of 'jump'. (b) In-place replacing the action of 'walks' with 'jumps' and 'dances'. (c) Generating diverse motion with the same example motion. (d) Transferring motion style referring to two motions (style and content reference). (e) Editing the sequentiality of a motion.")

> MotionCLR supports versatile motion generation and editing via several methods including motion de-emphasizing, in-place motion replacement, example-based motion generation, motion style transfer, and motion sequence shifting.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_6_1.png "🔼 Figure 4: Motion editing via manipulating attention maps.")

> The chart illustrates three motion editing methods (motion (de-)emphasizing, in-place motion replacement, motion sequence shifting) by manipulating attention maps.


![](charts/charts_7_0.png "🔼 Figure 5: Motion (de-)emphasizing. Different weights of 'jump' (↑ or ↓) in 'a man jumps.'")

> The chart visualizes the impact of modifying the weight of the word 'jump' on the height of jumps in generated motion sequences.


![](charts/charts_9_0.png "🔼 Figure 8: t-SNE visualization of different example-based generated results. Different colors imply different driven examples.")

> t-SNE visualization shows that diverse motions generated from the same example motion share similar motion textures, and different examples are well separated.


![](charts/charts_10_0.png "🔼 Figure 12: Action counting error rate comparison. Root trajectory (Traj.) vs. attention map (Ours). “σ” is the smoothing parameter.")

> The chart compares the error rates of action counting using root trajectory and attention map, showing that attention map-based counting is less sensitive to noise.


![](charts/charts_20_0.png "🔼 Figure 14: Additional visualization results for different (de-)emphasizing weights. The self-attention maps show how varying the different weights (e.g., ↓ 0.05, ↓ 0.10, ↑ 0.33, and ↑ 1.00) affect the emphasis on motion.")

> The self-attention maps for different (de-)emphasizing weights show how varying weights affect motion emphasis.


![](charts/charts_21_0.png "🔼 Figure 15: The effect of varying w in classifier-free guidance on generated motions. While changing w influences the general alignment between the text 'a man jumps.' and the generated motion, it does not provide precise control over finer details like jump height and frequency.")

> The chart displays the effect of varying classifier-free guidance weights (w) on the height of generated jumps, showing that while it affects overall alignment, it lacks fine-grained control over jump height and frequency.


![](charts/charts_27_0.png "🔼 Figure 20: Comparison between w/ vs. w/o grounded motion generation settings. The root height and motion visualization of the textual prompt “a person jumps four times”.")

> The chart compares the root height trajectory of a generated motion with and without temporal grounding, showing the improvement in aligning the generated motion with the textual prompt when temporal grounding is used.


![](charts/charts_34_0.png "🔼 Figure 26: Empirical study of attention patterns. We use the example “a person walks stop and then jumps.” (a) Horizontal distance traveled by the person over time, highlighting distinct walking and jumping phases. (b) The vertical height changes of the person, indicating variations during walking and jumping actions. (c) The cross-attention map between timesteps and the described actions. Notice that “walk” and “jump” receive a stronger attention signal corresponding to the walk and jump segments. (d) The self-attention map, which clearly identifies repeated walking and jumping cycles, shows similar patterns in the sub-actions. (e) Visualization of the motion sequences, demonstrating the walking and jumping actions.")

> Figure 26 shows an empirical study of attention mechanisms by visualizing horizontal distance, vertical height, cross-attention, self-attention maps, and motion visualization of a 'person walks, stops, and then jumps' example, highlighting distinct phases and patterns.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<br><table id='16' style='font-size:18px'><tr><td rowspan="2">Ablation</td><td colspan="3">R-Precision↑</td><td rowspan="2">FID↓</td></tr><tr><td>Top 1</td><td>Top 2</td><td>Top 3</td></tr><tr><td>(1)</td><td>0.512</td><td>0.705</td><td>0.792</td><td>0.544</td></tr><tr><td>(2)</td><td>0.509</td><td>0.703</td><td>0.788</td><td>0.550</td></tr><tr><td>MotionCLR</td><td>0.544</td><td>0.732</td><td>0.831</td><td>0.269</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MotionCLR with other state-of-the-art methods on the HumanML3D dataset using various metrics, including R-Precision, FID, and MM-Dist.


{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<table id='0' style='font-size:18px'><tr><td>Rishabh Dabral, Muhammad Hamza Mughal, Vladislav Golyanik, and Christian Theobalt. Mofusion: A framework for denoising-diffusion-based motion synthesis. In CVPR, pages 9760-9770, 2023.</td></tr><tr><td>Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, and Furu Wei. Knowledge neurons in pretrained transformers. In ACL, pages 8493-8502, 2022.</td></tr><tr><td>Wenxun Dai, Ling-Hao Chen, Jingbo Wang, Jinpeng Liu, Bo Dai, and Yansong Tang. Motionlcm: Real-time controllable motion generation via latent consistency model. ECCV, 2024.</td></tr><tr><td>Christian Diller and Angela Dai. Cg-hoi: Contact-guided 3d human-object interaction generation. In CVPR, pages 19888-19901, 2024.</td></tr><tr><td>Markos Diomataris, Nikos Athanasiou, Omid Taheri, Xi Wang, Otmar Hilliges, and Michael J Black. Wandr: Intention-guided human motion generation. In CVPR, pages 927-936, 2024.</td></tr><tr><td>Ke Fan, Junshu Tang, Weijian Cao, Ran Yi, Moran Li, Jingyu Gong, Jiangning Zhang, Yabiao Wang, Chengjie Wang, and Lizhuang Ma. Freemotion: A unified framework for number-free text-to-motion synthesis. ECCV, 2024.</td></tr><tr><td>Bin Feng, Tenglong Ao, Zequn Liu, Wei Ju, Libin Liu, and Ming Zhang. Robust dancer: Long-term 3d dance synthesis using unpaired data. arXiv preprint arXiv:2303.16856, 2023.</td></tr><tr><td>Mor Geva, Roei Schuster, Jonathan Berant, and Omer Levy. Transformer feed-forward layers are key-value memories. In EMNLP, pages 5484-5495, 2021.</td></tr><tr><td>Anindita Ghosh, Rishabh Dabral, Vladislav Golyanik, Christian Theobalt, and Philipp Slusallek. Remos: Reactive 3d motion synthesis for two-person interactions. ECCV, 2023.</td></tr><tr><td>Purvi Goel, Kuan-Chieh Wang, C Karen Liu, and Kayvon Fatahalian. Iterative motion editing with natural language. In ACM SIGGRAPH, pages 1-9, 2024.</td></tr><tr><td>Kehong Gong, Dongze Lian, Heng Chang, Chuan Guo, Zihang Jiang, Xinxin Zuo, Michael Bi Mi, and Xinchao Wang. Tm2d: Bimodality driven 3d dance generation via music-text integration. In ICCV, pages 9942-9952, 2023.</td></tr><tr><td>Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li, and Li Cheng. Generating diverse and natural 3d human motions from text. In CVPR, pages 5152-5161, 2022a.</td></tr><tr><td>Chuan Guo, Xinxin Zuo, Sen Wang, and Li Cheng. Tm2t: Stochastic and tokenized modeling for the reciprocal generation of 3d human motions and texts. In ECCV, pages 580-597, 2022b.</td></tr><tr><td>Chuan Guo, Yuxuan Mu, Muhammad Gohar Javed, Sen Wang, and Li Cheng. Momask: Generative masked modeling of 3d human motions. In CVPR, pages 1900-1910, 2024a.</td></tr><tr><td>Chuan Guo, Yuxuan Mu, Xinxin Zuo, Peng Dai, Youliang Yan, Juwei Lu, and Li Cheng. Generative human motion stylization in latent space. ICLR, 2024b.</td></tr><tr><td>Xinying Guo, Mingyuan Zhang, Haozhe Xie, Chenyang Gu, and Ziwei Liu. Crowdmogen: Zero-shot text-driven collective motion generation. arXiv preprint arXiv:2407.06188, 2024c.</td></tr><tr><td>Bo Han, Hao Peng, Minjing Dong, Yi Ren, Yixuan Shen, and Chang Xu. Amd: Autoregressive motion diffusion. In AAAI, pages 2022-2030, 2024.</td></tr><tr><td>Ligong Han, Song Wen, Qi Chen, Zhixing Zhang, Kunpeng Song, Mengwei Ren, Ruijiang Gao, Yuxiao Chen, Di Liu 0003, Qilong Zhangli, et al. Improving tuning-free real image editing with proximal guidance. WACV, 2023.</td></tr><tr><td>Yaru Hao, Li Dong, Furu Wei, and Ke Xu. Self-attention attribution: Interpreting information interactions inside transformer. In AAAI, volume 35, pages 12963-12971, 2021.</td></tr><tr><td>Felix G Harvey, Mike Yurick, Derek Nowrouzezahrai, and Christopher Pal. Robust motion in- betweening. ACM TOG, 39(4):60-1, 2020.</td></tr><tr><td>Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, and Daniel Cohen-Or. Prompt- to-prompt image editing with cross attention control. ICLR, 2023.</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MotionCLR with other state-of-the-art methods on the HumanML3D dataset, evaluating motion quality, diversity, and text-motion matching.


{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<table id='0' style='font-size:18px'><tr><td>Yonatan Shafir, Guy Tevet, Roy Kapon, and Amit H Bermano. Human motion diffusion as a generative prior. In ICLR, 2024.</td></tr><tr><td>Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. In ICLR, 2021.</td></tr><tr><td>Xiangjun Tang, He Wang, Bo Hu, Xu Gong, Ruifan Yi, Qilong Kou, and Xiaogang Jin. Real-time controllable motion transition for characters. ACM TOG, 41(4):1-10, 2022.</td></tr><tr><td>Chen Tessler, Yunrong Guo, Ofir Nabati, Gal Chechik, and Xue Bin Peng. Maskedmimic: Unified physics-based character control through masked motion inpainting. ACM SIGGRAPH ASIA, 2024.</td></tr><tr><td>Guy Tevet, Brian Gordon, Amir Hertz, Amit H Bermano, and Daniel Cohen-Or. Motionclip: Exposing human motion generation to clip space. In ECCV, pages 358-374, 2022a.</td></tr><tr><td>Guy Tevet, Sigal Raab, Brian Gordon, Yonatan Shafir, Daniel Cohen-Or, and Amit H Bermano. Human motion diffusion model. In ICLR, 2022b.</td></tr><tr><td>Narek Tumanyan, Michal Geyer, Shai Bagon, and Tali Dekel. Plug-and-play diffusion features for text-driven image-to-image translation. In CVPR, pages 1921-1930, 2023.</td></tr><tr><td>Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. NeurIPS, 2017.</td></tr><tr><td>Weilin Wan, Zhiyang Dou, Taku Komura, Wenping Wang, Dinesh Jayaraman, and Lingjie Liu. Tlcontrol: Trajectory and language control for human motion synthesis. ECCV, 2024.</td></tr><tr><td>Zan Wang, Yixin Chen, Tengyu Liu, Yixin Zhu, Wei Liang, and Siyuan Huang. Humanise: Language- conditioned human motion generation in 3d scenes. NeurIPS, pages 14959-14971, 2022.</td></tr><tr><td>Zan Wang, Yixin Chen, Baoxiong Jia, Puhao Li, Jinlu Zhang, Jingze Zhang, Tengyu Liu, Yixin Zhu, Wei Liang, and Siyuan Huang. Move as you say interact as you can: Language-guided human motion generation with scene affordance. In CVPR, pages 433-444, 2024.</td></tr><tr><td>Qianyang Wu, Ye Shi, Xiaoshui Huang, Jingyi Yu, Lan Xu, and Jingya Wang. Thor: Text to human-object interaction diffusion via relation intervention. arXiv preprint arXiv:2403.11208, 2024.</td></tr><tr><td>Zeqi Xiao, Tai Wang, Jingbo Wang, Jinkun Cao, Wenwei Zhang, Bo Dai, Dahua Lin, and Jiangmiao Pang. Unified human-scene interaction via prompted chain-of-contacts. In ICLR, 2024.</td></tr><tr><td>Yiming Xie, Varun Jampani, Lei Zhong, Deqing Sun, and Huaizu Jiang. Omnicontrol: Control any joint at any time for human motion generation. In ICLR, 2024a.</td></tr><tr><td>Zhenyu Xie, Yang Wu, Xuehao Gao, Zhongqian Sun, Wei Yang, and Xiaodan Liang. Towards detailed text-to-motion synthesis via basic-to-advanced hierarchical diffusion model. In AAAI, pages 6252-6260, 2024b.</td></tr><tr><td>Kelvin Xu, Jimmy Ba, Ryan Kiros, Kyunghyun Cho, Aaron Courville, Ruslan Salakhudinov, Rich Zemel, and Yoshua Bengio. Show, attend and tell: Neural image caption generation with visual attention. In ICML, pages 2048-2057. PMLR, 2015.</td></tr><tr><td>Sirui Xu, Zhengyuan Li, Yu-Xiong Wang, and Liang- Yan Gui. Interdiff: Generating 3d human-object interactions with physics-informed diffusion. In ICCV, pages 14928-14940, 2023a.</td></tr><tr><td>Sirui Xu, Yu-Xiong Wang, and Liangyan Gui. Stochastic multi-person 3d motion forecasting. In ICLR, 2023b.</td></tr><tr><td>Sirui Xu, Ziyin Wang, Yu-Xiong Wang, and Liang-Yan Gui. Interdreamer: Zero-shot text to 3d dynamic human-object interaction. arXiv preprint arXiv:2403.19652, 2024.</td></tr><tr><td>Heyuan Yao, Zhenhua Song, Baoquan Chen, and Libin Liu. Controlvae: Model-based learning of</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MotionCLR with other state-of-the-art methods for text-driven human motion generation using several metrics on the HumanML3D dataset.


{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<table id='3' style='font-size:18px'><tr><td>w</td><td>I</td><td>1.5</td><td>2</td><td>2.5</td><td>3</td><td>3.5</td></tr><tr><td>FID</td><td>0.801</td><td>0.408</td><td>0.318</td><td>0.217</td><td>0.317</td><td>0.396</td></tr><tr><td>TMR-sim.</td><td>51.987</td><td>52.351</td><td>53.512</td><td>53.956</td><td>54.300</td><td>54.529</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MotionCLR against other state-of-the-art methods on the HumanML3D dataset, using metrics such as R-Precision, FID, and MM-Dist.


{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<table id='2' style='font-size:20px'><tr><td></td><td>FID ↓</td><td>TMR-sim.→</td></tr><tr><td>direct (pseudo GT)</td><td>0.315</td><td>0.543</td></tr><tr><td>unreplaced</td><td>0.325</td><td>0.567</td></tr><tr><td>unreplaced (unpaired T-M)</td><td>0.925</td><td>0.490</td></tr><tr><td>ours replaced</td><td>0.330</td><td>0.535</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MotionCLR against other state-of-the-art methods on the HumanML3D dataset, evaluating metrics such as motion quality, diversity, and text-motion matching.


{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<table id='5' style='font-size:16px'><tr><td>begin</td><td>end</td><td>FID↓</td><td>TMR-sim.↑</td></tr><tr><td>8</td><td>11</td><td>0.339</td><td>0.472</td></tr><tr><td>5</td><td>14</td><td>0.325</td><td>0.498</td></tr><tr><td>1</td><td>18</td><td>0.330</td><td>0.535</td></tr></table>{{< /table-caption >}}

> Table 1 compares the performance of MotionCLR with other state-of-the-art methods on the HumanML3D dataset using various metrics such as R-Precision, FID, and MM-Dist.


{{< table-caption caption="🔽 Table 1: Comparison with different methods on the HumanML3D dataset. The '*' notation denotes the DDIM sampling inference design choice and the other is the DPM-solver sampling choice." >}}
<table id='2' style='font-size:20px'><tr><td></td><td>FID ↓</td><td>Div. ↑</td></tr><tr><td>Diff. manipulation</td><td>0.718</td><td>1.502</td></tr><tr><td>MotionCLR manipulation</td><td>0.427</td><td>2.567</td></tr></table>{{< /table-caption >}}

> Table 1 compares MotionCLR's performance against other state-of-the-art methods on the HumanML3D dataset, using metrics such as FID, R-Precision, and Multi-Modality.


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
<img src="paper_images/39.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/40.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/41.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
{{< /gallery >}}