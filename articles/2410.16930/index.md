---
title: "Math Neurosurgery: Isolating Language Models' Math Reasoning Abilities Using Only Forward Passes"
summary: "Math Neurosurgery precisely isolates math reasoning in LLMs using only forward passes, boosting performance without harming other skills."
categories: ["AI Generated"]
tags: ["🔖 24-10-22", "🤗 24-10-23"]
showSummary: true
date: 2024-10-22
draft: false
---

### TL;DR


{{< lead >}}

This paper introduces 'Math Neurosurgery' (MathNeuro), a new technique to precisely target and modify the parts of large language models (LLMs) that handle mathematical reasoning.  Unlike previous methods, MathNeuro uses only the model's forward pass (how the model processes information), making it computationally efficient and applicable to massive models.  The method identifies parameters vital for math by comparing their importance for math problems versus other tasks.  Experiments showed that removing these math-specific parameters eliminates the model's ability to solve math problems, while scaling up these parameters surprisingly improves its math performance by 4-17% on a standard math benchmark (GSM8K). Importantly, these manipulations don't negatively impact the model's performance on non-math tasks.  This research opens avenues for targeted LLM improvement in math and potentially other specific skill areas.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.16930" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
Math Neurosurgery (MathNeuro) is a novel method that precisely isolates and manipulates parameters responsible for mathematical reasoning in LLMs, enhancing performance without affecting other skills.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} MathNeuro effectively isolates math-specific parameters in LLMs. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Pruning these parameters removes math abilities without affecting other skills. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} Scaling these parameters improves math performance significantly. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_3_0.png "🔼 Figure 1: Overview of MathNeuro. First, we sum weights times activations separately over N samples for math and non-math inputs, finding the top-K parameters for each input type. Next, we find math-specific parameters by removing parameters that are important for non-math inputs.")

> The figure illustrates the MathNeuro process, showing how it identifies math-specific parameters by comparing top parameters for math and non-math inputs and removing those common to both.





![](charts/charts_5_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the impact of pruning parameters identified by four different methods (including the authors' method, MathNeuro) on a language model's performance across math and non-math tasks, indicating MathNeuro's superior ability to isolate math-specific parameters.





### More visual insights



<details>
<summary>More on charts
</summary>


![](charts/charts_5_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by four different methods on a Llama 3.2 1B IT model's performance on math and non-math tasks.


![](charts/charts_7_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the impact of pruning parameters identified by four different methods on the math and non-math performance of a Llama 3.2 1B IT language model, indicating MathNeuro's effectiveness in isolating math-specific parameters.


![](charts/charts_7_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning parameters identified as important for math reasoning on both math and non-math task performance for Llama 3.2 1B IT model.


![](charts/charts_7_2.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning parameters, identified by different methods, on math and non-math performance for Llama 3.2 1B IT model.


![](charts/charts_7_3.png "🔼 Figure 6: Consistency of math-specific parameters identified by MathNeuro for Llama 3.2 1B IT when identifying using GSM8K compared to RACE.")

> The chart displays the percentage of consistently identified math-specific parameters across different proportions of top parameters calculated and varying numbers of samples used for comparison, using GSM8K and RACE datasets.


![](charts/charts_7_4.png "🔼 Figure 6: Consistency of math-specific parameters identified by MathNeuro for Llama 3.2 1B IT when identifying using GSM8K compared to RACE.")

> The chart displays the percentage of consistently identified math-specific parameters across different random subsets of data, varying the number of samples and proportion of top parameters considered.


![](charts/charts_8_0.png "🔼 Figure 6: Consistency of math-specific parameters identified by MathNeuro for Llama 3.2 1B IT when identifying using GSM8K compared to RACE.")

> The chart displays the consistency of math-specific parameters identified by MathNeuro across different random subsets of data, showing a high degree of overlap even with a single sample.


![](charts/charts_8_1.png "🔼 Figure 6: Consistency of math-specific parameters identified by MathNeuro for Llama 3.2 1B IT when identifying using GSM8K compared to RACE.")

> The chart displays the percentage of consistently identified math-specific parameters by MathNeuro across different random subsets of data, varying sample sizes, and proportions of top parameters calculated, showing its consistency in identifying parameters related to math reasoning.


![](charts/charts_8_2.png "🔼 Figure 10: Distribution of math-specific parameters identified by MathNeuro for Llama 3.2 1B IT when identifying using GSM8K compared to RACE.")

> The chart displays the distribution of math-specific parameters across different layers of the Llama 3.2 1B IT model when using GSM8K and RACE datasets.


![](charts/charts_8_3.png "🔼 Figure 10: Distribution of math-specific parameters identified by MathNeuro for Llama 3.2 1B IT when identifying using GSM8K compared to RACE.")

> The chart displays the distribution of math-specific parameters across different layers of a Llama 3.2 1B IT language model, showing a relatively even distribution rather than concentration in specific layers.


![](charts/charts_12_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning identified parameters on Llama 3.2 1B IT's performance for math and non-math tasks, showing the trade-off between maintaining non-math accuracy and reducing math accuracy.


![](charts/charts_12_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning parameters identified by different methods on math and non-math performance for Llama 3.2 1B IT.


![](charts/charts_12_2.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the impact of pruning parameters identified by different methods (MathNeuro, Wanda, LAPE, Random) on the GSM8K, RACE, and MMLU performance of Llama 3.2 1B IT model.


![](charts/charts_12_3.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning parameters identified by different methods on math and non-math performance for the Llama 3.2 1B IT language model, showing the trade-off between preserving non-math abilities and eliminating math reasoning abilities.


![](charts/charts_13_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning parameters identified by four different methods (including MathNeuro) on math and non-math performance for the Llama 3.2 1B IT language model.


![](charts/charts_13_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified as important for math on both math and non-math tasks, showing the tradeoff between preserving non-math accuracy and reducing math accuracy.


![](charts/charts_13_2.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the impact of pruning parameters, identified by different methods, on the model's performance in math and non-math tasks.


![](charts/charts_13_3.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the impact of pruning parameters identified by different methods on math and non-math performance for the Llama 3.2 1B IT language model.


![](charts/charts_14_0.png "🔼 Figure 16: Impact of parameter proportion on GSM8K performance for pruning parameters identified by each method for Llama 3.2 1B IT.")

> The chart displays the effect of pruning different proportions of parameters identified by various methods (including MathNeuro) on the GSM8K accuracy for the Llama 3.2 1B IT language model.


![](charts/charts_14_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified as important for math on both math and non-math performance for the Llama 3.2 1B IT model.


![](charts/charts_14_2.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by different methods on Llama 3.2 1B IT's performance on math and non-math tasks, showing that MathNeuro effectively isolates math-specific parameters.


![](charts/charts_15_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning parameters identified as important for math on math and non-math performance for Llama 3.2 1B IT, showing that MathNeuro effectively isolates math-specific parameters.


![](charts/charts_15_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> Figure 2 shows the effects of pruning parameters identified as important for math reasoning on both math and non-math task performance for the Llama 3.2 1B IT model.


![](charts/charts_15_2.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified as important for mathematical reasoning on the math performance (GSM8K) and non-math performance (RACE, MMLU) of the Llama 3.2 1B IT language model.


![](charts/charts_15_3.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by four different methods (including MathNeuro) on Llama 3.2 1B IT's performance across math and non-math tasks, showing MathNeuro's effectiveness in isolating math-specific parameters.


![](charts/charts_15_4.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by different methods on Llama 3.2 1B IT's performance on math and non-math tasks.


![](charts/charts_16_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by different methods (including MathNeuro) on math and non-math performance for the Llama 3.2 1B IT language model.


![](charts/charts_16_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the impact of pruning parameters identified by different methods on GSM8K, MMLU, and RACE accuracy for Llama 3.2 1B IT, showing that MathNeuro effectively isolates math-specific parameters without significantly affecting non-math performance.


![](charts/charts_16_2.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> Figure 2 shows the effect of pruning parameters identified by different methods (MathNeuro, Wanda, LAPE, and Random) on Llama 3.2 1B IT's performance across math (GSM8K) and non-math (MMLU and RACE) tasks.


![](charts/charts_16_3.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by different methods on the model's performance in math and non-math tasks.


![](charts/charts_17_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effect of pruning parameters identified by four different methods on the model's performance in math and non-math tasks.


![](charts/charts_17_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by different methods on math and non-math performance for the Llama 3.2 1B IT model.


![](charts/charts_17_2.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as  Dnon-math.")

> The chart displays the effect of pruning parameters identified as important for math on the model's performance on math and non-math tasks.


![](charts/charts_17_3.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the impact of pruning parameters identified by different methods on math and non-math performance for the Llama 3.2 1B IT language model, showing that MathNeuro effectively isolates math-specific parameters.


![](charts/charts_18_0.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified as important for math reasoning on the model's performance on math and non-math tasks for Llama 3.2 1B IT, showing the tradeoff between reduced math accuracy and preserved non-math accuracy.


![](charts/charts_18_1.png "🔼 Figure 2: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT based on calculating the top 15% of parameters. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified as important for math on both math and non-math task performance for the Llama 3.2 1B IT model.


![](charts/charts_18_2.png "🔼 Figure 4: Effect of pruning identified parameters on math and non-math performance for Llama 3.2 1B IT for calculating the top 10% of parameters based on one sample. Ideal methods should fall in the top left of the plot. MMLU and RACE denote that a point was calculated using MMLU or RACE, respectively, as Dnon-math.")

> The chart displays the effects of pruning parameters identified by four different methods (including MathNeuro) on Llama 3.2 1B IT's performance on math and non-math tasks, using a single sample for parameter importance calculation.


![](charts/charts_19_0.png "🔼 Figure 29: Impact of MathNeuro scale factor on GSM8K performance for Llama 3.2 1B.")

> The chart displays the effect of different scaling factors applied to math-specific parameters identified by MathNeuro on the GSM8K CoT accuracy for Llama 3.2 1B model.


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