---
title: "Stable Consistency Tuning: Understanding and Improving Consistency Models"
summary: "Stable Consistency Tuning (SCT) boosts image generation speed and quality in consistency models, reaching new state-of-the-art performance."
categories: ["AI Generated"]
tags: ["🔖 24-10-24", "🤗 24-10-25"]
showSummary: true
date: 2024-10-24
draft: false
---

### TL;DR


{{< lead >}}

This paper introduces Stable Consistency Tuning (SCT), a novel technique to enhance consistency models, a type of AI model for generating images.  Consistency models are faster than other leading methods, but existing training methods suffer from high variance and instability.  SCT addresses this by using variance reduction methods (leveraging the score identity) and a refined training schedule.  The authors frame the training process as a Markov Decision Process (MDP) and value estimation, providing a theoretical foundation for understanding the model's behavior. Experiments on standard datasets (CIFAR-10 and ImageNet-64) demonstrate that SCT outperforms current state-of-the-art methods, achieving faster convergence and improved image quality.  The results show significant improvements in FID (Frechet Inception Distance) scores, a common metric for evaluating generated image quality.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18958" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
Stable Consistency Tuning (SCT) significantly improves the speed and quality of generating images with consistency models, achieving state-of-the-art results on benchmark datasets.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} SCT, a new method, improves consistency model training by reducing variance and discretization errors. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} SCT achieves state-of-the-art results on ImageNet-64 and CIFAR-10 benchmarks. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The research offers a novel framework for understanding consistency models through the lens of Markov Decision Processes. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: Stable consistency tuning (SCT) with variance reduced training target. SCT provides a unifying perspective to understand different training strategies of consistency models.")

> The figure illustrates Stable Consistency Tuning (SCT) as a unifying framework for understanding different training strategies of consistency models, including consistency distillation (CD) and consistency training (CT), by showing how they solve the ODE through approximating the expectation of the score function.





![](charts/charts_8_0.png "🔼 Figure 3: FID vs Training iterations. SCT has faster convergence speed and better performance upper bound than ECT.")

> The chart compares the FID scores of ECT and SCT models over training iterations for both 1-step and 2-step generation, showing SCT's superior convergence speed and performance.





{{< table-caption caption="🔽 Table 2: Comparing the quality of samples on CIFAR-10." >}}
<table id='2' style='font-size:16px'><tr><td>Fu-Yun Wang</td><td>Zhengyang Geng</td><td>Hongsheng Li</td></tr><tr><td>MMLab, CUHK</td><td>Carnegie Mellon University</td><td>MMLab, CUHK</td></tr><tr><td>Hong Kong SAR</td><td>Pittsburgh, USA</td><td>Hong Kong SAR</td></tr><tr><td>fywang@link . cuhk · edu . hk</td><td>zhengyanggeng@gmail · com</td><td>hsli@ee · cuhk · edu. hk</td></tr></table>{{< /table-caption >}}

> Table 2 compares the FID scores of various methods for generating samples on the CIFAR-10 dataset.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_5_0.png "🔼 Figure 2: Phasing the ODE path along the time axis for consistency training. We visualize both training and inference techniques in discrete form for easier understanding.")

> Figure 2 illustrates the difference between one-step inference and edge-skipping multistep inference in consistency models by visualizing the ODE solving process and bootstrapping prediction.


![](figures/figures_18_0.png "🔼 Figure 1: Stable consistency tuning (SCT) with variance reduced training target. SCT provides a unifying perspective to understand different training strategies of consistency models.")

> The figure illustrates stable consistency tuning (SCT) by showing how it reduces variance in the training target compared to other consistency training methods, unifying different training strategies under a single framework.


![](figures/figures_19_0.png "🔼 Figure 1: Stable consistency tuning (SCT) with variance reduced training target. SCT provides a unifying perspective to understand different training strategies of consistency models.")

> The figure illustrates the Stable Consistency Tuning (SCT) framework, highlighting how it unifies and improves different training strategies for consistency models by incorporating variance-reduced learning.


![](figures/figures_20_0.png "🔼 Figure 1: Stable consistency tuning (SCT) with variance reduced training target. SCT provides a unifying perspective to understand different training strategies of consistency models.")

> The figure illustrates Stable Consistency Tuning (SCT) and how it unifies different training strategies of consistency models by variance reduction.


![](figures/figures_21_0.png "🔼 Figure 1: Stable consistency tuning (SCT) with variance reduced training target. SCT provides a unifying perspective to understand different training strategies of consistency models.")

> The figure illustrates Stable Consistency Tuning (SCT) by comparing different training strategies of consistency models and highlighting how SCT reduces training variance.


![](figures/figures_22_0.png "🔼 Figure 1: Stable consistency tuning (SCT) with variance reduced training target. SCT provides a unifying perspective to understand different training strategies of consistency models.")

> The figure illustrates Stable Consistency Tuning (SCT) which incorporates variance-reduced learning using the score identity, providing a unifying perspective to understand different training strategies of consistency models.


![](figures/figures_23_0.png "🔼 Figure 1: Stable consistency tuning (SCT) with variance reduced training target. SCT provides a unifying perspective to understand different training strategies of consistency models.")

> The figure illustrates Stable Consistency Tuning (SCT) and how it unifies and improves upon different training strategies of consistency models by reducing variance and providing a novel understanding of the training process.


![](figures/figures_24_0.png "🔼 Figure 13: 1-step samples from class-conditional SCT trained on ImageNet-64 (FID 2.23). Each row corresponds to a different class.")

> The figure shows 1-step samples generated by class-conditional Stable Consistency Tuning (SCT) on ImageNet-64, achieving a Fréchet Inception Distance (FID) score of 2.23.


![](figures/figures_25_0.png "🔼 Figure 13: 1-step samples from class-conditional SCT trained on ImageNet-64 (FID 2.23). Each row corresponds to a different class.")

> The figure displays 1-step samples generated from a class-conditional Stable Consistency Tuning (SCT) model trained on the ImageNet-64 dataset, achieving a Fréchet Inception Distance (FID) score of 2.23.


![](figures/figures_26_0.png "🔼 Figure 13: 1-step samples from class-conditional SCT trained on ImageNet-64 (FID 2.23). Each row corresponds to a different class.")

> The figure displays 1-step samples generated by class-conditional Stable Consistency Tuning (SCT) on ImageNet-64, achieving a Fréchet Inception Distance (FID) score of 2.23.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_9_0.png "🔼 Figure 4: The effectiveness of variance reduced training target.")

> The chart compares the 1-step and 2-step FID scores for different training methods, demonstrating the effectiveness of variance reduction techniques.


![](charts/charts_9_1.png "🔼 Figure 5: The effectiveness of edge-skipping multi-step sampling.")

> The chart displays the FID scores for different eta values (η) during the training process of a multistep sampling method, showing how different eta values affect the performance.


![](charts/charts_9_2.png "🔼 Figure 6: The effectiveness of classifier-free guidance on consistency models.")

> The chart displays the impact of classifier-free guidance (CFG) strength on 1-step and 2-step FID scores for consistency models, showing performance variation at different CFG strengths and iteration numbers.


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
{{< /gallery >}}