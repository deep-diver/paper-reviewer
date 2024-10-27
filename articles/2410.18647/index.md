---
title: "Data Scaling Laws in Imitation Learning for Robotic Manipulation"
summary: "Robotic manipulation policies achieve near-human success rates in unseen environments using a novel data-scaling approach, enabling efficient data collection and zero-shot generalization."
categories: ["AI Generated"]
tags: ["🔖 24-10-24", "🤗 24-10-25"]
showSummary: true
date: 2024-10-24
draft: false
---

### TL;DR


{{< lead >}}

This paper explores whether data scaling laws, successful in fields like computer vision and natural language processing, apply to robotic manipulation.  Researchers collected over 40,000 demonstrations across many environments and objects, training policies using imitation learning.  Results show that policy generalization performance scales approximately as a power law with the number of training environments and objects; diversity of data is more important than the sheer quantity.  A proposed efficient data collection strategy was validated, achieving approximately 90% success in novel environments with unseen objects using data gathered by four collectors in a single afternoon. This work suggests that significant progress in generalizable robotic manipulation is achievable through carefully considered data scaling and efficient collection methods.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18647" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This research paper investigates data scaling laws in imitation learning for robotic manipulation, revealing power-law relationships between policy generalization and the number of training environments and objects.  It introduces an efficient data collection strategy enabling the training of policies that generalize well to novel environments and unseen objects.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} Policy generalization in robotic manipulation follows a power-law relationship with the number of training environments and objects. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Diversity of environments and objects is more crucial than the absolute number of demonstrations for achieving good generalization. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} An efficient data collection strategy is proposed and verified, enabling the training of high-performing policies with minimal data collection effort. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: Illustrations of all tasks. We derive the data scaling laws through extensive experiments on Pour Water and Mouse Arrangement, and further validate these findings on additional tasks, including Fold Towels and Unplug Charger.")

> The figure shows four different robotic manipulation tasks: Pour Water, Mouse Arrangement, Fold Towels, and Unplug Charger.





![](charts/charts_6_0.png "🔼 Figure 2: Object generalization. Each curve corresponds to a different fraction of demonstrations used, with normalized scores shown as a function of the number of training objects.")

> The chart displays the relationship between a policy's object generalization performance and the number of training objects used, considering different fractions of available demonstrations.





{{< table-caption caption="🔽 Table 1: Success rate across all tasks. We report the average success rate and standard deviation across 8 unseen environments. The performance in each environment is detailed in Table 12." >}}
<table id='5' style='font-size:14px'><tr><td></td><td>Pour Water</td><td>Mouse Arrangement</td><td>Fold Towels</td><td>Unplug Charger</td></tr><tr><td>Score</td><td>0.922 士 0.075</td><td>0.933 士 0.088</td><td>0.95 士 0.062</td><td>0.887 士 0.14</td></tr><tr><td>Success Rate</td><td>85.0 士 19.4%</td><td>92.5 士 9.7%</td><td>87.5 士 17.1%</td><td>90.0 士 14.1%</td></tr></table>{{< /table-caption >}}

> This table summarizes the success rate and standard deviation of the trained policies across four different manipulation tasks in eight unseen environments.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_16_0.png "🔼 Figure 12: Testing environments. These 8 environments are not included in the training data and are used across all tasks.")

> The figure shows eight unseen testing environments used to evaluate the generalization capabilities of the robotic policies across all four manipulation tasks.


![](figures/figures_16_1.png "🔼 Figure 12: Testing environments. These 8 environments are not included in the training data and are used across all tasks.")

> The figure shows eight unseen testing environments used to evaluate the generalization performance of the trained policies across all four tasks.


![](figures/figures_17_0.png "🔼 Figure 8: Training environments for Pour Water. We sample 12 environments from our collected training data. See Appendix D.1 for task details.")

> The figure shows 12 different environments used for training a robot to pour water.


![](figures/figures_17_1.png "🔼 Figure 8: Training environments for Pour Water. We sample 12 environments from our collected training data. See Appendix D.1 for task details.")

> The figure shows 12 different training environments used for the Pour Water task in the robotic manipulation experiment.


![](figures/figures_17_2.png "🔼 Figure 12: Testing environments. These 8 environments are not included in the training data and are used across all tasks.")

> The figure shows eight unseen testing environments used to evaluate the generalization performance of the robotic manipulation policies.


![](figures/figures_18_0.png "🔼 Figure 13: Objects for Pour Water. All of our experiments include a total of 64 training bottles and mugs, as well as 16 unseen testing bottles and mugs.")

> The figure shows the 64 training and 16 testing objects used in the Pour Water task of the robotic manipulation experiment.


![](figures/figures_19_0.png "🔼 Figure 14: Objects for Mouse Arrangement. All of our experiments include a total of 64 training mice and mouse pads, as well as 16 unseen testing mice and mouse pads.")

> The figure shows the 64 training and 16 testing mouse and mousepad pairs used in the experiments.


![](figures/figures_20_0.png "🔼 Figure 15: Objects for Fold Towels. All of our experiments include a total of 32 training towels, as well as 16 unseen testing towels.")

> The figure shows the 32 training towels and 16 unseen testing towels used in the Fold Towels task.


![](figures/figures_21_0.png "🔼 Figure 16: Objects for Unplug Charger. All of our experiments include a total of 32 training chargers and power strips, as well as 16 unseen testing chargers and power strips.")

> The figure shows the 32 training objects and 16 testing objects used for the Unplug Charger task in the experiment.


![](figures/figures_29_0.png "🔼 Figure 18: UMI hand-held grippers. We do not install side mirrors on the grippers.")

> The figure shows four UMI hand-held grippers used in the data collection process of the paper.


![](figures/figures_29_1.png "🔼 Figure 19: Deployment hardware setup.")

> The figure shows the hardware setup used for the robotic manipulation experiments, including the robot arm, gripper, camera, and power supply.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_6_1.png "🔼 Figure 2: Object generalization. Each curve corresponds to a different fraction of demonstrations used, with normalized scores shown as a function of the number of training objects.")

> The chart displays how a policy's ability to generalize to unseen objects changes as the number of training objects and the fraction of demonstrations used increases.


![](charts/charts_7_0.png "🔼 Figure 4: Generlization across environments and objects. Each curve corresponds to a different fraction of demonstrations used, with normalized scores shown as a function of the number of training environment-object pairs.")

> The chart displays the relationship between a policy's generalization ability and the number of training environment-object pairs, considering different fractions of used demonstrations.


![](charts/charts_7_1.png "🔼 Figure 5: Power-law relationship. Dashed lines represent power-law fits, with the equations provided in the legend. All axes are shown on a logarithmic scale. The correlation coefficient r indicates a power-law relationship between the policy generalization ability and the number of objects, environments, and environment-object pairs. See Appendix G.1 for data scaling laws on MSE.")

> The chart displays the power-law relationships between the policy's generalization ability and the number of training objects, environments, and environment-object pairs, showing how generalization scales approximately as a power law with the number of training instances across different data dimensions.


![](charts/charts_8_0.png "🔼 Figure 6: Multiple objects per environment. Brighter colors indicate higher normalized scores.")

> The heatmap visualizes how the policy's normalized scores vary depending on the number of environments and the number of objects per environment.


![](charts/charts_9_0.png "🔼 Figure 7: Number of demonstrations. Left: In the setting where we collect the maximum number of demonstrations, we examine whether the policy's performance follows a power-law relationship with the total number of demonstrations. The correlation coefficients for Pour Water and Mouse Arrangement are -0.62 and -0.79, respectively, suggesting only a weak power-law relationship. Right: For varying environment-object pairs, the policy performance increases with the total number of demonstrations at first, and then reaches saturation.")

> The chart displays the relationship between the number of demonstrations and the policy's performance for object and environment generalization, showing saturation after a certain number of demonstrations.


![](charts/charts_27_0.png "🔼 Figure 17: Comparison between normalized score and MSE. Left: In the object generalization experiment, the inverse correlation between MSE and normalized score is weak. Right: In the generalization experiment across both environments and objects, the inverse correlation between MSE and normalized score is very strong. Correlation coefficients (Pearson's r and Spearman's ρ) are shown in the bottom right.")

> The chart compares two evaluation metrics, normalized score and MSE, for evaluating the generalization performance of robot policies in object generalization and generalization across both environments and objects, revealing the strength of correlation between them.


![](charts/charts_30_0.png "🔼 Figure 20: Data scaling laws on MSE. Dashed lines represent power-law fits, with the equations provided in the legend. All axes are shown on a logarithmic scale.")

> The chart shows the relationship between the mean squared error (MSE) and the number of training objects, environments, and environment-object pairs.


![](charts/charts_31_0.png "🔼 Figure 21: Object generalization. Each curve corresponds to a different total numbers of demonstrations used, with normalized scores shown as a function of the number of training objects.")

> The chart displays the normalized scores of object generalization for Pour Water and Mouse Arrangement tasks, showing how performance varies with different numbers of training objects and data usage.


![](charts/charts_31_1.png "🔼 Figure 21: Object generalization. Each curve corresponds to a different total numbers of demonstrations used, with normalized scores shown as a function of the number of training objects.")

> The chart displays the object generalization performance of the policies trained with varying amounts of data (2x, 4x, 8x, 16x, and 32x demonstrations) in relation to the number of training objects.


![](charts/charts_31_2.png "🔼 Figure 23: Generalization across environments and objects. Each curve corresponds to a different total numbers of demonstrations used, with normalized scores shown as a function of the number of training environment-object pairs.")

> The chart displays how the policy's generalization ability across environments and objects improves with increasing number of training environment-object pairs while keeping the total number of demonstrations relatively constant.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Model related experiments on Pour Water. The entries marked in gray are the same, which specify the default settings: the visual encoder is a fully fine-tuned ViT-L/14 model pre-trained with DINOv2, while the action diffusion model employs a base-size 1D CNN U-Net." >}}
<table id='1' style='font-size:14px'><tr><td>Case</td><td>Score</td><td></td><td></td></tr><tr><td>DINOv2 ViT-L/14</td><td>0.90</td><td>Case</td><td>Score</td></tr><tr><td>LfS ViT-L/14</td><td>0.03</td><td>DINOv2 ViT-S/14</td><td>0.66</td></tr><tr><td>frozen DINOv2</td><td>0.00</td><td>DINOv2 ViT-B/14</td><td>0.81</td></tr><tr><td>LoRA DINOv2</td><td>0.72</td><td>DINOv2 ViT-L/14</td><td>0.90</td></tr></table>{{< /table-caption >}}

> The table shows the results of model-related experiments on the Pour Water task, comparing different training strategies, visual encoder sizes, and action diffusion model sizes.


{{< table-caption caption="🔽 Table 2: Model related experiments on Pour Water. The entries marked in gray are the same, which specify the default settings: the visual encoder is a fully fine-tuned ViT-L/14 model pre-trained with DINOv2, while the action diffusion model employs a base-size 1D CNN U-Net." >}}
<br><table id='2' style='font-size:14px'><tr><td>Case</td><td>Score</td></tr><tr><td>small U-Net</td><td>0.88</td></tr><tr><td>base U-Net</td><td>0.90</td></tr><tr><td>large U-Net</td><td>0.83</td></tr></table>{{< /table-caption >}}

> The table presents the results of experiments on the Pour Water task, comparing the performance of different model sizes and training strategies for the visual encoder and action diffusion model.


{{< table-caption caption="🔽 Table 3: A default set of hyper-parameters." >}}
<table id='5' style='font-size:14px'><tr><td>Config</td><td>Value</td></tr><tr><td>Image observation horizon</td><td>3 (Pour Water, Unplug Charger), 2 (other tasks)</td></tr><tr><td>Proprioception observation horizon</td><td>3 (Pour Water, Unplug Charger), 2 (other tasks)</td></tr><tr><td>Action horizon</td><td>16</td></tr><tr><td>Observation resolution</td><td>224x224</td></tr><tr><td>Environment frequency</td><td>5</td></tr><tr><td>Optimizer</td><td>AdamW</td></tr><tr><td>Optimizer momentum</td><td>B1, B2 = 0.95, 0.999</td></tr><tr><td>Learning rate for action diffusion model</td><td>3e-4</td></tr><tr><td>Learning rate for visual encoder</td><td>3e-5</td></tr><tr><td>Learning rate schedule</td><td>cosine decay</td></tr><tr><td>Batch size</td><td>256</td></tr><tr><td>Inference denoising iterations</td><td>16</td></tr><tr><td>Temporal ensemble steps</td><td>8</td></tr><tr><td>Temporal ensemble adaptation rate</td><td>-0.01</td></tr></table>{{< /table-caption >}}

> This table lists the default hyperparameters used in the policy training process, specifying values for image observation horizon, proprioception observation horizon, action horizon, observation resolution, environment frequency, optimizer, optimizer momentum, learning rate for action diffusion model, learning rate for visual encoder, learning rate schedule, batch size, inference denoising iterations, temporal ensemble steps, and temporal ensemble adaptation rate.


{{< table-caption caption="🔽 Table 5: Environment generalization on Pour Water. Normalizing these scores by dividing them by 9 yields the results shown in Fig. 3." >}}
<table id='5' style='font-size:14px'><tr><td>Usage</td><td rowspan="2">3.125%</td><td rowspan="2">6.25%</td><td rowspan="2">12.5%</td><td rowspan="2">25%</td><td rowspan="2">50%</td><td rowspan="2">100%</td></tr><tr><td>#Envs</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1.3</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td>2.85</td><td>3.325</td></tr><tr><td>4</td><td></td><td></td><td></td><td>2.55</td><td>4.3</td><td>4.475</td></tr><tr><td>8</td><td></td><td></td><td>3.925</td><td>6.1</td><td>6.575</td><td>6.2</td></tr><tr><td>16</td><td></td><td>4.15</td><td>6.2</td><td>6.525</td><td>7.85</td><td>8</td></tr><tr><td>32</td><td>3.475</td><td>6.55</td><td>7.2</td><td>8.65</td><td>8.75</td><td>8.6</td></tr></table>{{< /table-caption >}}

> Table 5 shows the results of the environment generalization experiment on the Pour Water task, presenting the normalized scores as a function of the number of training environments and the fraction of demonstrations used.


{{< table-caption caption="🔽 Table 7: Number of demonstrations on Pour Water. Normalizing these scores by dividing them by 9 yields the results shown in Fig. 7." >}}
<table id='9' style='font-size:14px'><tr><td>#Demos</td><td>64</td><td>100</td><td>200</td><td>400</td><td>800</td><td>1600</td><td>3200</td><td>6400</td></tr><tr><td>Score</td><td>4.35</td><td>6.15</td><td>6.875</td><td>7.025</td><td>6.975</td><td>7.2</td><td>7.125</td><td>6.525</td></tr></table>{{< /table-caption >}}

> The table shows the raw test scores before normalization for the Pour Water task, varying the number of demonstrations used for training.


{{< table-caption caption="🔽 Table 9: Environment generalization on Mouse Arrangement. Normalizing these scores by dividing them by 6 yields the results shown in Fig. 3." >}}
<table id='3' style='font-size:14px'><tr><td>Usage</td><td>3.125%</td><td>6.25%</td><td>12.5%</td><td>25%</td><td>50%</td><td>100%</td></tr><tr><td>#Envs 1</td><td></td><td></td><td></td><td></td><td></td><td>1.3</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td>1.975</td><td>2.475</td></tr><tr><td>4</td><td></td><td></td><td></td><td>1.8</td><td>3.3</td><td>3.625</td></tr><tr><td>8</td><td></td><td></td><td>2.075</td><td>2.5</td><td>3.2</td><td>3.6</td></tr><tr><td>16</td><td></td><td>1.525</td><td>3.65</td><td>3.8</td><td>4.375</td><td>4.45</td></tr><tr><td>32</td><td>2.725</td><td>3.325</td><td>3.9</td><td>4.7</td><td>5.125</td><td>5.2</td></tr></table>{{< /table-caption >}}

> Table 9 shows the results of the environment generalization experiment on the Mouse Arrangement task, where the normalized scores are obtained by dividing the raw scores by 6.


{{< table-caption caption="🔽 Table 6: Generlization across environments and objects on Pour Water. Normalizing these scores by dividing them by 9 yields the results shown in Fig. 4." >}}
<table id='5' style='font-size:14px'><tr><td>Usage</td><td>3.125%</td><td>6.25%</td><td>12.5%</td><td>25%</td><td>50%</td><td>100%</td></tr><tr><td>#Pairs 1</td><td></td><td></td><td></td><td></td><td></td><td>0.75</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td>0.975</td><td>0.875</td></tr><tr><td>4</td><td></td><td></td><td></td><td>1.8</td><td>2.3</td><td>2.325</td></tr><tr><td>8</td><td></td><td></td><td>2.425</td><td>3.725</td><td>3.425</td><td>3.35</td></tr><tr><td>16</td><td></td><td>3.375</td><td>4.925</td><td>4.5</td><td>5.05</td><td>4.75</td></tr><tr><td>32</td><td>4.225</td><td>4.225</td><td>5.075</td><td>5.2</td><td>5.6</td><td>5.525</td></tr></table>{{< /table-caption >}}

> Table 6 presents the normalized scores for Pour Water experiments evaluating generalization across both environments and objects, showing the impact of different fractions of demonstrations.


{{< table-caption caption="🔽 Table 11: Number of demonstrations on Mouse Arrangement. Normalizing these scores by dividing them by 6 yields the results shown in Fig. 7." >}}
<table id='7' style='font-size:14px'><tr><td>#Demos</td><td>64</td><td>100</td><td>200</td><td>400</td><td>800</td><td>1600</td><td>3200</td><td>6400</td></tr><tr><td>Score</td><td>1.725</td><td>3.025</td><td>3.3</td><td>3.775</td><td>3.975</td><td>3.8</td><td>3.875</td><td>3.8</td></tr></table>{{< /table-caption >}}

> Table 11 shows the normalized scores for the Mouse Arrangement task based on varying numbers of demonstrations.


{{< table-caption caption="🔽 Table 12: Success rate across all tasks. For each task, we report the success rate in each evaluation environment." >}}
<table id='3' style='font-size:14px'><tr><td></td><td colspan="8">Environment ID</td><td></td></tr><tr><td>Task</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Mean</td></tr><tr><td>Pour Water</td><td>80%</td><td>40%</td><td>100%</td><td>80%</td><td>100%</td><td>100%</td><td>80%</td><td>100%</td><td>85%</td></tr><tr><td>Mouse Arrangement</td><td>100%</td><td>80%</td><td>100%</td><td>100%</td><td>80%</td><td>80%</td><td>100%</td><td>100%</td><td>92.5%</td></tr><tr><td>Fold Towels</td><td>100%</td><td>100%</td><td>60%</td><td>100%</td><td>100%</td><td>60%</td><td>100%</td><td>80%</td><td>87.5%</td></tr><tr><td>Unplug Charger</td><td>80%</td><td>60%</td><td>100%</td><td>100%</td><td>100%</td><td>80%</td><td>100%</td><td>100%</td><td>90%</td></tr></table>{{< /table-caption >}}

> This table presents the success rates of the policies trained across 32 environment-object pairs for four different manipulation tasks, showing the performance in each of eight unseen evaluation environments.


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
{{< /gallery >}}