---
title: "DynamicCity: Large-Scale LiDAR Generation from Dynamic Scenes"
summary: "DynamicCity generates high-quality, large-scale 4D LiDAR scenes from dynamic environments, significantly outperforming existing methods."
categories: ["AI Generated"]
tags: ["🔖 24-10-23", "🤗 24-10-24"]
showSummary: true
date: 2024-10-23
draft: false
---

### TL;DR


{{< lead >}}

DynamicCity is a new method for creating realistic 4D LiDAR (light detection and ranging) data, which is crucial for autonomous driving and robotics.  Existing methods struggle to produce large-scale, dynamic scenes. DynamicCity overcomes this by using a two-stage process. First, a Variational Autoencoder (VAE) learns a compact 4D representation called HexPlane. This representation is then used by a Diffusion Transformer (DiT) to generate the actual LiDAR data. The VAE employs a novel projection module to effectively compress the data into six 2D feature maps, making it efficient for DiT processing.  The DiT is further enhanced by a Padded Rollout Operation that arranges the HexPlane feature maps into a squared format. This improves the model's efficiency and accuracy.  DynamicCity is evaluated on multiple datasets, significantly outperforming existing methods across several metrics, and demonstrating its versatility through various application scenarios. The research is significant because it offers a step change in generating more detailed and comprehensive 4D LiDAR data that is much closer to real-world situations. This capability could substantially improve the development and training of autonomous systems.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18084" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
Summarizing the provided research paper on DynamicCity: Large-Scale LiDAR Generation from Dynamic Scenes.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} DynamicCity generates large-scale, high-quality 4D LiDAR scenes capturing dynamic environments. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} It introduces a novel VAE for compact 4D representation (HexPlane) and a DiT-based diffusion model for generation. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} DynamicCity supports various downstream applications, including trajectory and command-driven generation, inpainting, and layout-conditioned generation. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_1_0.png "🔼 Figure 1: Dynamic LiDAR scene generation from DynamicCity. We introduce a new LiDAR generation model that generates diverse 4D scenes of large spatial scales (80 × 80 × 6.4 meter³) and long sequential modeling (up to 128 frames), enabling a diverse set of downstream applications. For more examples, kindly refer to our Project Page: https://dynamic-city.github.io.")

> Figure 1 illustrates DynamicCity's capability to generate diverse large-scale and long-sequential 4D LiDAR scenes from various driving scenarios.







{{< table-caption caption="🔽 Table 1: Comparisons of 4D Scene Reconstruction. We report the mIoU scores of OccSora (Wang et al., 2024) and our DynamicCity framework on the CarlaSC, Occ3D-Waymo, and Occ3D-nuScenes datasets, respectively, under different resolutions and sequence lengths. Symbol † denotes score reported in the OccSora paper. Other scores are reproduced using the official code." >}}
<br><table id='2' style='font-size:14px'><tr><td>Dataset</td><td>#Classes</td><td>Resolution</td><td>#Frames</td><td>OccSora (Wang et al., 2024)</td><td>Ours (DynamicCity)</td></tr><tr><td rowspan="4">CarlaSC (Wilson et al., 2022)</td><td>10</td><td>128x 128 x8</td><td>4</td><td>41.01%</td><td>79.61% (+38.6%)</td></tr><tr><td>10</td><td>128x 128 x8</td><td>8</td><td>39.91%</td><td>76.18% (+36.3%)</td></tr><tr><td>10</td><td>128x 128 x8</td><td>16</td><td>33.40%</td><td>74.22% (+40.8%)</td></tr><tr><td>10</td><td>128x 128 x8</td><td>32</td><td>28.91%</td><td>59.31% (+30.4%)</td></tr><tr><td>Occ3D-Waymo (Tian et al., 2023)</td><td>9</td><td>200x200x16</td><td>16</td><td>36.38%</td><td>68.18% (+31.8%)</td></tr><tr><td rowspan="4">Occ3D-nuScenes (Tian et al., 2023)</td><td>11</td><td>200x200x 16</td><td>16</td><td>13.70%</td><td>56.93% (+43.2%)</td></tr><tr><td>11</td><td>200x200 x 16</td><td>32</td><td>13.51%</td><td>42.60% (+29.1%)</td></tr><tr><td>17</td><td>200x200x 16</td><td>32</td><td>13.41%</td><td>40.79% (+27.3%)</td></tr><tr><td>17</td><td>200x200x 16</td><td>32</td><td>27.40%†</td><td>40.79% (+13.4%)</td></tr></table>{{< /table-caption >}}

> Table 1 compares the 4D scene reconstruction performance of the proposed DynamicCity model against OccSora across different datasets, resolutions, and sequence lengths, showing DynamicCity's superior performance.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_4_0.png "🔼 Figure 2: Pipeline of dynamic LiDAR scene generation. Our DynamicCity framework consists of two key procedures: (a) Encoding HexPlane with an VAE architecture (cf. Sec. 4.1), and (b) 4D Scene Generation with HexPlane DiT (cf. Sec. 4.2).")

> The figure illustrates the two-stage pipeline of DynamicCity for dynamic LiDAR scene generation, including HexPlane encoding with a VAE and HexPlane diffusion with DiT.


![](figures/figures_5_0.png "🔼 Figure 3: VAE for Encoding 4D LIDAR Scenes. We use HexPlane H as the 4D representation. fo and go are convolution-based networks with downsampling and upsampling operations, respectively. h(.) denotes the projection network based on transformer modules.")

> The figure illustrates the VAE architecture used in DynamicCity for encoding 4D LiDAR scenes into compact HexPlane representations.


![](figures/figures_6_0.png "🔼 Figure 2: Pipeline of dynamic LiDAR scene generation. Our DynamicCity framework consists of two key procedures: (a) Encoding HexPlane with an VAE architecture (cf. Sec. 4.1), and (b) 4D Scene Generation with HexPlane DiT (cf. Sec. 4.2).")

> The figure illustrates the two-stage pipeline of DynamicCity for dynamic LiDAR scene generation, showing the VAE for HexPlane encoding and the DiT for HexPlane-based 4D scene generation.


![](figures/figures_6_1.png "🔼 Figure 5: Condition Injection for DiT")

> The figure illustrates how numeric and image conditions are injected into the DiT for conditional generation of HexPlane.


![](figures/figures_8_0.png "🔼 Figure 6: Dynamic Scene Generation Results. We provide unconditional generation scenes from the 1st, 8th, and 16th frames on Occ3D-Waymo (Left) and CarlaSC (Right), respectively. Kindly refer to the Appendix for complete sequential scenes and longer temporal modeling examples.")

> Figure 6 shows example unconditional generation results from DynamicCity on Occ3D-Waymo and CarlaSC datasets, showcasing the model's ability to generate realistic dynamic scenes across different time steps.


![](figures/figures_9_0.png "🔼 Figure 7: Dynamic Scene Generation Applications. We demonstrate the capability of our model on a diverse set of downstream tasks. We show the 1st, 8th, and 16th frames for simplicity. Kindly refer to the Appendix for complete sequential scenes and longer temporal modeling examples.")

> The figure showcases various downstream applications of DynamicCity, including command-driven, layout-conditioned, and trajectory-guided generation, as well as dynamic object inpainting.


![](figures/figures_20_0.png "🔼 Figure 8: Unconditional Dynamic Scene Generation Results. We provide qualitative examples of a total of 16 consectutive frames generated by DynamicCity on the Occ3D-Waymo (Tian et al., 2023) dataset. Best viewed in colors and zoomed-in for additional details.")

> Figure 8 shows 16 consecutive frames of an unconditional dynamic scene generated by DynamicCity on the Occ3D-Waymo dataset, showcasing the model's ability to generate realistic and detailed dynamic scenes.


![](figures/figures_21_0.png "🔼 Figure 8: Unconditional Dynamic Scene Generation Results. We provide qualitative examples of a total of 16 consectutive frames generated by DynamicCity on the Occ3D-Waymo (Tian et al., 2023) dataset. Best viewed in colors and zoomed-in for additional details.")

> Figure 8 shows 16 consecutive frames of an unconditional dynamic scene generated by DynamicCity on the Occ3D-Waymo dataset.


![](figures/figures_22_0.png "🔼 Figure 10: HexPlane-Guided Generation Results. We provide qualitative examples of a total of 64 consectutive frames generated by DynamicCity on the Occ3D-Waymo (Tian et al., 2023) dataset. Best viewed in colors and zoomed-in for additional details.")

> Figure 10 shows 64 consecutive frames generated by DynamicCity, demonstrating the model's ability to generate long, temporally consistent sequences of 4D LiDAR data conditioned on HexPlane.


![](figures/figures_23_0.png "🔼 Figure 1: Dynamic LiDAR scene generation from DynamicCity. We introduce a new LiDAR generation model that generates diverse 4D scenes of large spatial scales (80 × 80 × 6.4 meter³) and long sequential modeling (up to 128 frames), enabling a diverse set of downstream applications. For more examples, kindly refer to our Project Page: https://dynamic-city.github.io.")

> Figure 1 shows example LiDAR scene generation results from the DynamicCity model, highlighting its ability to generate diverse and large-scale 4D scenes.


![](figures/figures_24_0.png "🔼 Figure 12: Command-Guided Scene Generation Results. We provide qualitative examples of a total of 16 consectutive frames generated under the command RIGHT by DynamicCity on the CarlaSC (Wilson et al., 2022) dataset. Best viewed in colors and zoomed-in for additional details.")

> This figure shows qualitative examples of 16 consecutive frames generated by DynamicCity under the command RIGHT, demonstrating the model's ability to control the ego vehicle's motion and the scene's relative motion based on movement trends.


![](figures/figures_25_0.png "🔼 Figure 8: Unconditional Dynamic Scene Generation Results. We provide qualitative examples of a total of 16 consectutive frames generated by DynamicCity on the Occ3D-Waymo (Tian et al., 2023) dataset. Best viewed in colors and zoomed-in for additional details.")

> Figure 8 shows 16 consecutive frames of an unconditonally generated dynamic LiDAR scene from the Occ3D-Waymo dataset showcasing the model's ability to generate realistic and detailed dynamic scenes.


![](figures/figures_26_0.png "🔼 Figure 14: Dynamic Inpainting Results. We provide qualitative examples of a total of 16 consecutive frames generated by DynamicCity on the CarlaSC (Wilson et al., 2022) dataset. Best viewed in colors and zoomed-in for additional details.")

> Figure 14 shows the results of dynamic inpainting on 16 consecutive frames from the CarlaSC dataset, demonstrating the model's ability to seamlessly regenerate masked regions while maintaining consistency with the surrounding scene.


![](figures/figures_27_0.png "🔼 Figure 6: Dynamic Scene Generation Results. We provide unconditional generation scenes from the 1st, 8th, and 16th frames on Occ3D-Waymo (Left) and CarlaSC (Right), respectively. Kindly refer to the Appendix for complete sequential scenes and longer temporal modeling examples.")

> Figure 6 shows the unconditional generation results of DynamicCity on Occ3D-Waymo and CarlaSC datasets, illustrating the model's ability to generate realistic and detailed dynamic scenes.


</details>




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Comparisons of 4D Scene Generation. We report the Inception Score (IS), Fréchet Inception Distance (FID), Kernel Inception Distance (KID), and the Precision (P) and Recall (R) rates of SemCity (Lee et al., 2024), OccSora (Wang et al., 2024), and our DynamicCity framework on the CarlaSC and Occ3D-Waymo datasets, respectively, in both the 2D and 3D spaces." >}}
<br><table id='4' style='font-size:14px'><tr><td rowspan="2">Dataset</td><td rowspan="2">Method</td><td rowspan="2">#Frames</td><td colspan="5">Metric2D</td><td colspan="5">Metric⌀D</td></tr><tr><td>IS ↑</td><td>FID⌀ ↓</td><td>KID2D ↓</td><td>P↑</td><td>R↑</td><td>IS ↑</td><td>FID- ↓</td><td>KID3D↓</td><td>P↑</td><td>R⌀ ↑</td></tr><tr><td rowspan="2">CarlaSC (Wilson et al., 2022)</td><td rowspan="2">OccSora Ours</td><td rowspan="2">16</td><td>2.492</td><td>25.08</td><td>0.013</td><td>0.115</td><td>0.008</td><td>2.257</td><td>1559</td><td>52.72</td><td>0.380</td><td>0.151</td></tr><tr><td>2.498</td><td>10.95</td><td>0.002</td><td>0.238</td><td>0.066</td><td>2.331</td><td>354.2</td><td>19.10</td><td>0.460</td><td>0.170</td></tr><tr><td rowspan="2">Occ3D-Waymo (Tian et al., 2023)</td><td rowspan="2">OccSora Ours</td><td rowspan="2">16</td><td>1.926</td><td>82.43</td><td>0.094</td><td>0.227</td><td>0.014</td><td>3.129</td><td>3140</td><td>12.20</td><td>0.384</td><td>0.001</td></tr><tr><td>1.945</td><td>7.138</td><td>0.003</td><td>0.617</td><td>0.096</td><td>3.206</td><td>1806</td><td>77.71</td><td>0.494</td><td>0.026</td></tr></table>{{< /table-caption >}}

> Table 2 compares the performance of three different methods (SemCity, OccSora, and DynamicCity) on 4D scene generation using Inception Score, Fréchet Inception Distance, Kernel Inception Distance, Precision, and Recall in both 2D and 3D spaces.


{{< table-caption caption="🔽 Table 3: Ablation Study on VAE Network Structures. We report the mIoU scores, training time (second-per-iteration), and training-time memory consumption (VRAM) of different Encoder and Decoder configurations on CarlaSC and Occ3D-Waymo, respectively. Note that 'ESS' denotes 'Expansion & Squeeze'. The best and second-best values are in bold and underlined." >}}
<br><table id='2' style='font-size:16px'><tr><td rowspan="2">Encoder</td><td rowspan="2">Decoder</td><td colspan="3">CarlaSC</td><td colspan="3">Occ3D-Waymo</td></tr><tr><td>mIoU↑</td><td>Time (s)↓</td><td>VRAM (G)↓</td><td>mIoU↑</td><td>Time (s)↓</td><td>VRAM (G)↓</td></tr><tr><td rowspan="2">Average Pooling Average Pooling</td><td>Query</td><td>60.97%</td><td>0.236</td><td>12.46</td><td>49.37%</td><td>1.563</td><td>69.66</td></tr><tr><td>ESS</td><td>68.02%</td><td>0.143</td><td>4.27</td><td>55.72%</td><td>0.758</td><td>20.31</td></tr><tr><td rowspan="2">Projection Projection</td><td>Query</td><td>68.73%</td><td>0.292</td><td>13.59</td><td>61.93%</td><td>2.128</td><td>73.15</td></tr><tr><td>ESS</td><td>74.22%</td><td>0.205</td><td>5.92</td><td>62.57%</td><td>1.316</td><td>25.92</td></tr></table>{{< /table-caption >}}

> The table presents an ablation study comparing different VAE network structures (encoders and decoders, with and without the proposed Expansion & Squeeze Strategy) across two datasets, measuring mIoU scores, training time, and VRAM usage.


{{< table-caption caption="🔽 Table 4: Ablation Study on HexPlane Downsampling (D.S.) Rates. We report the compression ratios (C.R.), mIoU scores, training speed (seconds per iteration), and training-time memory consumption on CarlaSC and Occ3D-Waymo. The best and second-best values are in bold and underlined." >}}
<br><table id='4' style='font-size:14px'><tr><td colspan="4">D.S. Rates</td><td colspan="4">CarlaSC</td><td colspan="4">Occ3D-Waymo</td></tr><tr><td>dT</td><td>dx</td><td>dy</td><td>dz</td><td>C.R.↑</td><td>mIoU↑</td><td>Time (s)↓</td><td>VRAM (G)↓</td><td>C.R.↑</td><td>mIoU↑</td><td>Time (s)↓</td><td>VRAM (G)↓</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>5.78%</td><td>84.67%</td><td>1.149</td><td>21.63</td><td colspan="3">Out-of-Memory</td><td>>80</td></tr><tr><td>1</td><td>2</td><td>2</td><td>1</td><td>17.96%</td><td>76.05%</td><td>0.289</td><td>8.49</td><td>38.42%</td><td>63.30%</td><td>1.852</td><td>32.82</td></tr><tr><td>2</td><td>2</td><td>2</td><td>2</td><td>23.14%</td><td>74.22%</td><td>0.205</td><td>5.92</td><td>48.25%</td><td>62.37%</td><td>0.935</td><td>24.9</td></tr><tr><td>2</td><td>4</td><td>4</td><td>2</td><td>71.86%</td><td>65.15%</td><td>0.199</td><td>4.00</td><td>153.69%</td><td>58.13%</td><td>0.877</td><td>22.30</td></tr></table>{{< /table-caption >}}

> Table 4 shows the impact of different downsampling rates on the HexPlane's compression ratio, mIoU score, training speed, and VRAM usage for the VAE model on CarlaSC and Occ3D-Waymo datasets.


{{< table-caption caption="🔽 Table 5: Ablation Study on Organizing HexPlane as Image Tokens. We report the Inception Score (IS), Fréchet Inception Distance (FID), Kernel Inception Distance (KID), and the Precision (P) and Recall (R) rates on CarlaSC. The best values are highlighted in bold." >}}
<br><table id='6' style='font-size:14px'><tr><td rowspan="2">Method</td><td colspan="5">Metric2D</td><td colspan="5">Metric3D</td></tr><tr><td>IS2D ↑</td><td>FID2D ↓</td><td>KID2D ↓</td><td>P↑</td><td>R↑</td><td>IS ⌀ ↑</td><td>FID 3D ↓</td><td>KID3D ↓</td><td>P↑</td><td>R↑</td></tr><tr><td>Direct Unfold</td><td>2.496</td><td>205.0</td><td>0.248</td><td>0.000</td><td>0.000</td><td>2.269</td><td>9110</td><td>723.7</td><td>0.173</td><td>0.043</td></tr><tr><td>Vertical Concatenation</td><td>2.476</td><td>12.79</td><td>0.003</td><td>0.191</td><td>0.042</td><td>2.305</td><td>623.2</td><td>26.67</td><td>0.424</td><td>0.159</td></tr><tr><td>Padded Rollout</td><td>2.498</td><td>10.96</td><td>0.002</td><td>0.238</td><td>0.066</td><td>2.331</td><td>354.2</td><td>19.10</td><td>0.460</td><td>0.170</td></tr></table>{{< /table-caption >}}

> Table 5 presents an ablation study comparing different methods of organizing HexPlanes as image tokens for 4D LiDAR generation, evaluating their performance using Inception Score, Fréchet Inception Distance, Kernel Inception Distance, Precision, and Recall metrics.


{{< table-caption caption="🔽 Table 1: Comparisons of 4D Scene Reconstruction. We report the mIoU scores of OccSora (Wang et al., 2024) and our DynamicCity framework on the CarlaSC, Occ3D-Waymo, and Occ3D-nuScenes datasets, respectively, under different resolutions and sequence lengths. Symbol † denotes score reported in the OccSora paper. Other scores are reproduced using the official code." >}}
<table id='8' style='font-size:16px'><tr><td>Class</td><td>CarlaSC</td><td>Occ3D-Waymo</td><td>Occ3D-nuScenes</td></tr><tr><td>Building</td><td>Building</td><td>Building</td><td>Manmade</td></tr><tr><td>Barrier</td><td>Barrier, Wall, Guardrail</td><td>-</td><td>Barrier</td></tr><tr><td>Other</td><td>Other, Sky, Bridge, Rail track, Static, Dynamic, Water</td><td>General Object</td><td>General Object</td></tr><tr><td>Pedestrian</td><td>Pedestrian</td><td>Pedestrian</td><td>Pedestrian</td></tr><tr><td>Pole</td><td>Pole, Traffic sign, Traffic light</td><td>Sign, Traffic light, Pole, Construction Cone</td><td>Traffic cone</td></tr><tr><td>Road</td><td>Road, Roadlines</td><td>Road</td><td>Drivable surface</td></tr><tr><td>Ground</td><td>Ground, Terrain</td><td>-</td><td>Other flat, Terrain</td></tr><tr><td>Sidewalk</td><td>Sidewalk</td><td>Sidewalk</td><td>Sidewalk</td></tr><tr><td>Vegetation</td><td>Vegetation</td><td>Vegetation, Tree trunk</td><td>Vegetation</td></tr><tr><td>Vehicle</td><td>Vehicle</td><td>Vehicle</td><td>Bus, Car, Construction vehicle, Trailer, Truck</td></tr><tr><td>Bicycle</td><td>-</td><td>Bicyclist, Bicycle, Motorcycle</td><td>Bicycle, Motorcycle</td></tr></table>{{< /table-caption >}}

> Table 1 compares the 4D scene reconstruction performance (mIoU) of DynamicCity against OccSora across three datasets with varying resolutions and sequence lengths.


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
{{< /gallery >}}