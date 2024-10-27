---
title: "3DGS-Enhancer: Enhancing Unbounded 3D Gaussian Splatting with View-consistent 2D Diffusion Priors"
summary: "3DGS-Enhancer boosts 3D Gaussian splatting's novel view synthesis by integrating view-consistent 2D diffusion priors, dramatically improving quality in sparse-view scenarios."
categories: ["AI Generated"]
tags: ["🔖 24-10-21", "🤗 24-10-23"]
showSummary: true
date: 2024-10-21
draft: false
---

### TL;DR


{{< lead >}}

The paper introduces 3DGS-Enhancer, a novel method to enhance the quality of 3D Gaussian splatting (3DGS) for novel view synthesis.  3DGS is an efficient technique for creating realistic images, but it struggles when there aren't many input views.  3DGS-Enhancer solves this by using video diffusion priors, which are essentially AI models trained to create videos.  By cleverly transforming the view consistency issue into a problem of video consistency, it can restore view-consistent details and integrate them with the original 3DGS model.  The improved results make the 3DGS method far more robust and useful, especially in cases with limited data. Extensive experiments on large datasets show a huge increase in the quality of the generated images compared to existing techniques.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.16266" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
To provide a concise and informative summary of the research paper on 3DGS-Enhancer, highlighting its key contributions, methods, findings, and importance for researchers.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} 3DGS-Enhancer significantly improves the quality of 3D Gaussian splatting (3DGS) representations, especially in challenging scenarios with limited input views. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} It leverages video diffusion priors to address the challenging 3D view consistency problem, reformulating it as a temporal consistency problem within video generation. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} Extensive experiments demonstrate superior reconstruction performance and high-fidelity rendering results compared to state-of-the-art methods. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_1_0.png "🔼 Figure 1: The 3DGS-Enhancer improves 3D Gaussian splatting representations on unbounded scenes with sparse input views.")

> The figure shows a comparison of 3D Gaussian splatting results with and without using the proposed 3DGS-Enhancer method on unbounded scenes with sparse input views, demonstrating the improvement in visual quality.







{{< table-caption caption="🔽 Table 1: A quantitative comparison of few-shot 3D reconstruction. Experiments on DL3DV and LLFF follow the setting of [43]. Experiments on Mip-NeRF 360 follow the setting of [40]." >}}
<br><table id='1' style='font-size:14px'><tr><td></td><td colspan="3">3 views</td><td colspan="3">6 views</td><td colspan="3">9 views</td></tr><tr><td>Method</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td></tr><tr><td colspan="10">DL3DV (130 training scenes, 20 test scenes)</td></tr><tr><td>Mip-NeRF [1]</td><td>10.92</td><td>0.191</td><td>0.618</td><td>11.56</td><td>0.199</td><td>0.608</td><td>12.42</td><td>0.218</td><td>0.600</td></tr><tr><td>RegNeRF [27]</td><td>11.46</td><td>0.214</td><td>0.600</td><td>12.69</td><td>0.236</td><td>0.579</td><td>12.33</td><td>0.219</td><td>0.598</td></tr><tr><td>FreeNeRF [43]</td><td>10.91</td><td>0.211</td><td>0.595</td><td>12.13</td><td>0.230</td><td>0.576</td><td>12.85</td><td>0.241</td><td>0.573</td></tr><tr><td>3DGS [18]</td><td>10.97</td><td>0.248</td><td>0.567</td><td>13.34</td><td>0.332</td><td>0.498</td><td>14.99</td><td>0.403</td><td>0.446</td></tr><tr><td>DNGaussian [19]</td><td>11.10</td><td>0.273</td><td>0.579</td><td>12.67</td><td>0.329</td><td>0.547</td><td>13.44</td><td>0.365</td><td>0.539</td></tr><tr><td>3DGS-Enhancer (ours)</td><td>14.33</td><td>0.424</td><td>0.464</td><td>16.94</td><td>0.565</td><td>0.356</td><td>18.50</td><td>0.630</td><td>0.305</td></tr></table>{{< /table-caption >}}

> Table 1 quantitatively compares the performance of several few-shot 3D reconstruction methods across different numbers of input views on three datasets.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_4_0.png "🔼 Figure 2: An overview of the proposed 3DGS-Enhancer framework for 3DGS representation enhancement. We learn 2D video diffusion priors on a large-scale novel view synthesis dataset to enhance the novel views rendered from the 3DGS model on a novel scene. Then, the enhanced views and input views jointly fine-tune the 3DGS model.")

> The figure illustrates the 3DGS-Enhancer framework, showing how 2D video diffusion priors enhance novel views rendered by a 3DGS model, which are then used to fine-tune the model.


![](figures/figures_6_0.png "🔼 Figure 4: A visual comparison of rendered images on scenes from DL3DV [20] test set with the 3-view setting.")

> Figure 4 presents a visual comparison of novel view synthesis results from various methods on scenes from the DL3DV test set using only three input views.


![](figures/figures_9_0.png "🔼 Figure 3: The red circle indicates the area with high confidence, meaning the generated videos can contribute more information. Conversely, the green quadrilateral highlights the area with low confidence, suggesting that the generated video should not tend to optimize this area.")

> The figure shows a comparison of rendered images, confidence map, and ground truth, highlighting areas of high and low confidence in the generated video.


![](figures/figures_9_1.png "🔼 Figure 1: The 3DGS-Enhancer improves 3D Gaussian splatting representations on unbounded scenes with sparse input views.")

> The figure shows a visual comparison of 3D Gaussian splatting (3DGS) and 3DGS enhanced by the proposed method (3DGS-Enhancer) on unbounded scenes with sparse input views, demonstrating improved quality and reduced artifacts in the enhanced results.


![](figures/figures_9_2.png "🔼 Figure 3: The red circle indicates the area with high confidence, meaning the generated videos can contribute more information. Conversely, the green quadrilateral highlights the area with low confidence, suggesting that the generated video should not tend to optimize this area.")

> The figure shows a comparison of rendered images, confidence map, and ground truth, highlighting areas of high and low confidence for generated video frames.


![](figures/figures_9_3.png "🔼 Figure 3: The red circle indicates the area with high confidence, meaning the generated videos can contribute more information. Conversely, the green quadrilateral highlights the area with low confidence, suggesting that the generated video should not tend to optimize this area.")

> The figure shows a comparison of rendered images, a confidence map, and ground truth, highlighting areas of high and low confidence in the generated images.


![](figures/figures_9_4.png "🔼 Figure 1: The 3DGS-Enhancer improves 3D Gaussian splatting representations on unbounded scenes with sparse input views.")

> The figure shows a comparison of 3D Gaussian splatting (3DGS) renderings with and without the proposed 3DGS-Enhancer on unbounded scenes using sparse input views.


![](figures/figures_10_0.png "🔼 Figure 6: An ablation study of the video diffusion model components in our 3DGS-Enhancer framework.")

> The figure shows an ablation study comparing the input, video diffusion model output, spatial-temporal decoder output, and ground truth for a sample image, demonstrating the effectiveness of each component in improving image quality.


![](figures/figures_15_0.png "🔼 Figure 7: The fitting trajectories under different number of input views.")

> This figure shows the fitting trajectories of cameras under different numbers of input views, illustrating how the trajectory fitting algorithm adapts to varying input conditions.


![](figures/figures_16_0.png "🔼 Figure 3: The red circle indicates the area with high confidence, meaning the generated videos can contribute more information. Conversely, the green quadrilateral highlights the area with low confidence, suggesting that the generated video should not tend to optimize this area.")

> Figure 3 shows a comparison of rendered images, a confidence map, and ground truth, highlighting areas of high and low confidence for generated video frames in the context of novel view synthesis.


![](figures/figures_16_1.png "🔼 Figure 1: The 3DGS-Enhancer improves 3D Gaussian splatting representations on unbounded scenes with sparse input views.")

> The figure shows a comparison of 3D Gaussian splatting (3DGS) renderings with and without the proposed 3DGS-Enhancer, demonstrating improved quality with sparse input views.


![](figures/figures_16_2.png "🔼 Figure 3: The red circle indicates the area with high confidence, meaning the generated videos can contribute more information. Conversely, the green quadrilateral highlights the area with low confidence, suggesting that the generated video should not tend to optimize this area.")

> The figure shows a comparison of rendered images, a confidence map, and ground truth images, highlighting areas of high and low confidence in the generated video.


![](figures/figures_16_3.png "🔼 Figure 3: The red circle indicates the area with high confidence, meaning the generated videos can contribute more information. Conversely, the green quadrilateral highlights the area with low confidence, suggesting that the generated video should not tend to optimize this area.")

> The figure shows a comparison of rendered images, a confidence map, and a ground truth image, highlighting areas of high and low confidence in the generated images.


![](figures/figures_16_4.png "🔼 Figure 8: The low and high quality image pairs created in our 3DGS Enhancement dataset.")

> The figure shows example pairs of low-quality and high-quality images from the 3DGS Enhancement dataset, illustrating the types of artifacts the model is designed to correct.


</details>




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: A quantitative comparison of methods on the unseen Mip-NeRF360 dataset [2]." >}}
<br><table id='15' style='font-size:14px'><tr><td rowspan="2">Method</td><td colspan="3">6 views</td><td colspan="3">9 views</td></tr><tr><td>PSNR ↑</td><td>SSIM ↑</td><td>LPIPS ↓</td><td>PSNR ↑</td><td>SSIM ↑</td><td>LPIPS ↓</td></tr><tr><td colspan="7">Mip-NeRF360 (all test scenes)</td></tr><tr><td>Mip-NeRF</td><td>13.08</td><td>0.159</td><td>0.637</td><td>13.73</td><td>0.189</td><td>0.628</td></tr><tr><td>RegNeRF</td><td>12.69</td><td>0.175</td><td>0.660</td><td>13.73</td><td>0.193</td><td>0.629</td></tr><tr><td>FreeNeRF</td><td>12.56</td><td>0.182</td><td>0.646</td><td>13.20</td><td>0.198</td><td>0.635</td></tr><tr><td>3DGS</td><td>11.53</td><td>0.144</td><td>0.651</td><td>12.65</td><td>0.187</td><td>0.607</td></tr><tr><td>DNGaussian</td><td>11.81</td><td>0.208</td><td>0.689</td><td>12.51</td><td>0.228</td><td>0.683</td></tr><tr><td>3DGS-Enhancer (ours)</td><td>13.96</td><td>0.260</td><td>0.570</td><td>16.22</td><td>0.399</td><td>0.454</td></tr></table>{{< /table-caption >}}

> Table 2 quantitatively compares different methods' performance on the unseen Mip-NeRF360 dataset using PSNR, SSIM, and LPIPS metrics for 6 and 9 input views.


{{< table-caption caption="🔽 Table 1: A quantitative comparison of few-shot 3D reconstruction. Experiments on DL3DV and LLFF follow the setting of [43]. Experiments on Mip-NeRF 360 follow the setting of [40]." >}}
<br><table id='1' style='font-size:14px'><tr><td>Video diffusion</td><td>Real image</td><td>Image confidence</td><td>Pixel confidence</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td></tr><tr><td></td><td></td><td>-</td><td>-</td><td>14.33</td><td>0.476</td><td>0.422</td></tr><tr><td></td><td></td><td>-</td><td>-</td><td>17.01</td><td>0.553</td><td>0.361</td></tr><tr><td></td><td></td><td></td><td></td><td>17.29</td><td>0.570</td><td>0.354</td></tr><tr><td></td><td></td><td></td><td></td><td>17.16 17.34</td><td>0.564 0.574</td><td>0.351 0.351</td></tr></table>{{< /table-caption >}}

> Table 1 quantitatively compares the performance of several few-shot 3D reconstruction methods across different numbers of input views on three datasets.


{{< table-caption caption="🔽 Table 1: A quantitative comparison of few-shot 3D reconstruction. Experiments on DL3DV and LLFF follow the setting of [43]. Experiments on Mip-NeRF 360 follow the setting of [40]." >}}
<br><table id='3' style='font-size:14px'><tr><td>Video diffusion</td><td>STD (temporal layers)</td><td>color correction</td><td>PSNR ↑</td><td>SSIM ↑</td><td>LPIPS ↓</td></tr><tr><td></td><td></td><td>-</td><td>18.11</td><td>0.591</td><td>0.312</td></tr><tr><td></td><td></td><td>-</td><td>18.44</td><td>0.625</td><td>0.306</td></tr><tr><td></td><td></td><td></td><td>18.50</td><td>0.630</td><td>0.305</td></tr></table>{{< /table-caption >}}

> Table 1 quantitatively compares the performance of different few-shot 3D reconstruction methods on the DL3DV and Mip-NeRF 360 datasets, evaluating metrics such as PSNR, SSIM, and LPIPS.


{{< table-caption caption="🔽 Table 1: A quantitative comparison of few-shot 3D reconstruction. Experiments on DL3DV and LLFF follow the setting of [43]. Experiments on Mip-NeRF 360 follow the setting of [40]." >}}
<br><table id='11' style='font-size:20px'><tr><td>Method</td><td>Per-scene training time ↓</td><td>Rendering FPS ↑</td></tr><tr><td>Mip-NeRF</td><td>10.7h</td><td>0.09</td></tr><tr><td>RegNeRF</td><td>2.5h</td><td>0.09</td></tr><tr><td>FreeNeRF</td><td>3.8h</td><td>0.09</td></tr><tr><td>3DGS</td><td>10.5min</td><td>100</td></tr><tr><td>DNGaussian</td><td>3.3min</td><td>100</td></tr><tr><td>3DGS-Enhancer (ours)</td><td>24.5min</td><td>100</td></tr></table>{{< /table-caption >}}

> Table 1 quantitatively compares the performance of several few-shot 3D reconstruction methods across different numbers of input views on three datasets (DL3DV, LLFF, and Mip-NeRF 360), evaluating PSNR, SSIM, and LPIPS scores.


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
{{< /gallery >}}