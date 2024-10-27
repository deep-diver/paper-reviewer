---
title: "Agent-to-Sim: Learning Interactive Behavior Models from Casual Longitudinal Videos"
summary: "Agent-to-Sim (ATS) learns realistic 3D agent behaviors from long-term casual videos, bridging the gap between real-world observations and interactive simulations."
categories: ["AI Generated"]
tags: ["🔖 24-10-21", "🤗 24-10-22"]
showSummary: true
date: 2024-10-21
draft: false
---

### TL;DR


{{< lead >}}

Agent-to-Sim (ATS) is a new framework that allows researchers to create realistic simulations of agents (animals or humans) by using casual videos recorded over a long period (e.g., a month).  Instead of relying on precise, controlled settings and marker-based tracking like previous methods, ATS uses readily available videos captured in everyday environments.  The key is a novel technique that reconstructs the videos into a persistent 4D representation (3D space + time), precisely tracking the agent, the scene, and the camera's movement.  This 4D data is then used to train a generative model that can predict the agent's future actions based on its past behavior and current surroundings (what it 'sees').  This model allows researchers to create interactive simulations where the agent behaves realistically and responds to changes in its environment, opening many possibilities for applications like VR/AR, robot planning, and behavior research.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.16259" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
Agent-to-Sim (ATS) learns interactive 3D agent behavior models from casual, longitudinal videos, enabling real-to-sim transfer for various applications.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} ATS reconstructs persistent spacetime 4D representations from casual videos, overcoming limitations of prior marker-based methods. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} ATS trains generative models of agent behavior that are interactive to both the observer and the 3D scene. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} ATS demonstrates real-to-sim transfer from videos to interactive behavior simulators. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_1_0.png "🔼 Figure 1: Learning agent behavior from longitudinal casual video recordings. We answer the following question: can we simulate the behavior of an agent, by learning from casually-captured videos of the same agent recorded across a long period of time (e.g., a month)? A) We first reconstruct videos in 4D (3D & time), which includes the scene, the trajectory of the agent, and the trajectory of the observer (i.e., camera held by the observer). Such individual 4D reconstructions are registered across time, resulting in a complete and persistent 4D representation. B) Then we learn a model of the agent for interactive behavior generation. The behavior model explicitly reasons about goals, paths, and full body movements conditioned on the agent's ego-perception and past trajectory. Such an agent representation allows generation of novel scenarios through conditioning. For example, conditioned on different observer trajectories, the cat agent chooses to walk to the carpet, stays still while quivering his tail, or hide under the tray stand. Please see videos results in the supplement.")

> The figure illustrates the Agent-to-Sim (ATS) framework, showing how 4D spacetime reconstruction from casual longitudinal videos enables learning and simulation of interactive agent behaviors.







{{< table-caption caption="🔽 Table 1: Evaluation of Camera Registration." >}}
<table id='4' style='font-size:14px'><tr><td>Method</td><td>Rotation Error (°)</td><td>Translation Error (m)</td><td></td><td>Videos</td><td>Length</td><td>Unique Days / Span</td></tr><tr><td>Ours</td><td>6.35</td><td>0.41</td><td>Cat</td><td>23</td><td>25m 39s</td><td>9/37 days</td></tr><tr><td>w/o Neural Localizer</td><td>37.59</td><td>0.83</td><td>Human</td><td>5</td><td>9m 27s</td><td>2/4 days</td></tr><tr><td>w/o Featuremetric BA</td><td>22.47</td><td>1.30</td><td>Dog</td><td>3</td><td>7m 13s</td><td>1/1 day</td></tr><tr><td>Multi-video TotalRecon</td><td>59.19</td><td>0.68</td><td>Bunny</td><td>2</td><td>1m 48s</td><td>1/1 day</td></tr></table>{{< /table-caption >}}

> The table evaluates the performance of camera registration using different methods by comparing the rotation and translation errors.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_2_0.png "🔼 Figure 1: Learning agent behavior from longitudinal casual video recordings. We answer the following question: can we simulate the behavior of an agent, by learning from casually-captured videos of the same agent recorded across a long period of time (e.g., a month)? A) We first reconstruct videos in 4D (3D & time), which includes the scene, the trajectory of the agent, and the trajectory of the observer (i.e., camera held by the observer). Such individual 4D reconstructions are registered across time, resulting in a complete and persistent 4D representation. B) Then we learn a model of the agent for interactive behavior generation. The behavior model explicitly reasons about goals, paths, and full body movements conditioned on the agent’s ego-perception and past trajectory. Such an agent representation allows generation of novel scenarios through conditioning. For example, conditioned on different observer trajectories, the cat agent chooses to walk to the carpet, stays still while quivering his tail, or hide under the tray stand. Please see videos results in the supplement.")

> The figure illustrates the Agent-to-Sim (ATS) framework, showing how 4D spacetime reconstruction from casual longitudinal videos enables learning and simulation of interactive agent behaviors.


![](figures/figures_2_1.png "🔼 Figure 1: Learning agent behavior from longitudinal casual video recordings. We answer the following question: can we simulate the behavior of an agent, by learning from casually-captured videos of the same agent recorded across a long period of time (e.g., a month)? A) We first reconstruct videos in 4D (3D & time), which includes the scene, the trajectory of the agent, and the trajectory of the observer (i.e., camera held by the observer). Such individual 4D reconstructions are registered across time, resulting in a complete and persistent 4D representation. B) Then we learn a model of the agent for interactive behavior generation. The behavior model explicitly reasons about goals, paths, and full body movements conditioned on the agent’s ego-perception and past trajectory. Such an agent representation allows generation of novel scenarios through conditioning. For example, conditioned on different observer trajectories, the cat agent chooses to walk to the carpet, stays still while quivering his tail, or hide under the tray stand. Please see videos results in the supplement.")

> The figure illustrates the Agent-to-Sim (ATS) framework, showing the 4D spacetime reconstruction from casual longitudinal videos and the interactive behavior simulator learned from it.


![](figures/figures_2_2.png "🔼 Figure 1: Learning agent behavior from longitudinal casual video recordings. We answer the following question: can we simulate the behavior of an agent, by learning from casually-captured videos of the same agent recorded across a long period of time (e.g., a month)? A) We first reconstruct videos in 4D (3D & time), which includes the scene, the trajectory of the agent, and the trajectory of the observer (i.e., camera held by the observer). Such individual 4D reconstructions are registered across time, resulting in a complete and persistent 4D representation. B) Then we learn a model of the agent for interactive behavior generation. The behavior model explicitly reasons about goals, paths, and full body movements conditioned on the agent's ego-perception and past trajectory. Such an agent representation allows generation of novel scenarios through conditioning. For example, conditioned on different observer trajectories, the cat agent chooses to walk to the carpet, stays still while quivering his tail, or hide under the tray stand. Please see videos results in the supplement.")

> The figure shows the Agent-to-Sim (ATS) framework, illustrating the 4D spacetime reconstruction from longitudinal casual videos and the interactive behavior simulator that learns agent behaviors from this reconstruction.


![](figures/figures_6_0.png "🔼 Figure 2: Pipeline for behavior generation. We encode egocentric information into a perception code w, conditioned on which we generate fully body motion in a hierarchical fashion. We start by generating goals Z, then paths P and finally body poses G. Each node is represented by the gradient of its log distribution, trained with denoising objectives (Eq. 8). Given G, the full body motion of an agent can be computed via blend skinning (Eq. 3).")

> This figure illustrates the hierarchical pipeline used for generating the agent's behavior, which involves encoding egocentric information and generating goals, paths, and body poses sequentially.


![](figures/figures_7_0.png "🔼 Figure 3: Comparison on multi-video scene reconstruction. We show birds-eye-view rendering of the reconstructed scene using the bunny dataset. Compared to TotalRecon that does not register multiple videos, ATS produces higher-quality scene reconstruction. Neural localizer (NL) and featuremetric losses (FBA) are shown important for camera registration. Scene annealing is important for reconstructing a complete scene from partial video captures.")

> Figure 3 shows a comparison of multi-video scene reconstruction results using different methods, highlighting the impact of neural localization, featuremetric losses, and scene annealing on reconstruction quality.


![](figures/figures_9_0.png "🔼 Figure 4: Analysis of conditioning signals. We show results of removing one conditioning signal at a time. Removing observer conditioning and past trajectory conditioning makes the sampled goals more spread out (e.g., regions both in front of the agent and behind the agent); removing the environment conditioning introduces infeasible goals that penetrate the ground and the walls.")

> Figure 4 shows an ablation study on the effect of conditioning signals for goal generation, demonstrating that all three signals (user, past trajectory, and environment) contribute to generating realistic goals.


![](figures/figures_10_0.png "🔼 Figure 5: Results of 4D reconstruction. Top: reference images and renderings. Background color represents correspondence. Colored blobs on the cat represent B = 25 bones (e.g., head is represented by the yellow blob). The magenta colored lines represents reconstructed trajectories of each blob in the world space. Bottom: Bird’s eye view of the reconstructed scene and agent trajectories, registered to the same scene coordinate. Each colored line represents a unique video sequence where boxes and spheres indicate the starting and the end location.")

> The figure shows the results of a 4D reconstruction of an agent (cat) and its environment from multiple video sequences, displaying both individual frames and a bird's-eye view of the registered trajectories.


![](figures/figures_18_0.png "🔼 Figure 6: Qualitative comparison with TotalRecon (Song et al., 2023) on 4D reconstruction. Top: reconstruction of the agent at at specific frame. Total-recon produces shapes with missing limbs and bone transformations that are misaligned with the shape, while our method produces complete shapes and good alignment. Bottom: reconstruction of the environment. TotalRecon produces distorted and incomplete geometry (due to lack of observations from a single video), while our method produces an accurate and complete environment reconstruction.")

> Figure 6 shows a qualitative comparison of 4D reconstruction results between the proposed method and TotalRecon, highlighting the superior quality of shape, alignment, and completeness achieved by the proposed method.


![](figures/figures_18_1.png "🔼 Figure 7: Qualitative comparison on 4D reconstruction (Tab. 3). We compare with TotalRecon on 4D reconstruction quality. We show novel views rendered with a held-out camera that looks from the opposite side. ATS is able to leverage multiple videos captured at different times to reconstruct the wall (blue box) and the tripod stand (red box) even they are not visible in the input views. Multi-video TotalRecon produces blurry RGB and depth due to bad camera registration. The original TotalRecon takes a single video as input and therefore fails to reconstruct the regions (the tripod and the wall) that are not visible in the input video.")

> Figure 7 shows a qualitative comparison of 4D reconstruction results between ATS and TotalRecon, highlighting ATS's ability to leverage multiple videos for improved reconstruction of scene details even when those details are not visible in any single video.


![](figures/figures_19_0.png "🔼 Figure 8: Visual ablation on scene awareness. We demonstrate the effect of the scene code \(\boldsymbol{\omega}_s\) through goal-conditioned path generation (bird’s-eye-view, blue sphere goal; gradient color generated path; gray blocks locations that have been visited in the training data). Conditioned on scene, the generated path abide by the scene geometry, while removing the scene code, the generated paths go through the wall in between two empty spaces.")

> Figure 8 shows the impact of scene awareness on path generation, demonstrating that incorporating scene information prevents the generated path from going through walls.


![](figures/figures_19_1.png "🔼 Figure 9: Given the 3D trajectories of the agent and the user accumulated over time (top), one could compute their preference represented by 3D heatmaps (bottom). Note the high agent preference over table and sofa.")

> Figure 9 shows agent and user's preference over the environment represented by 3D heatmaps generated from their accumulated trajectories.


![](figures/figures_20_0.png "🔼 Figure 11: Generalization ability of the behavior model. Thanks to the ego-centric encoding design (Eq. 12), a specific behavior can be learned and generalized to novel situations even it was seen once. Although there's only one data point where the cat jumps off the dining table, our method can generate diverse motion of cat jumping off the table while landing at different locations (to the left, middle, and right of the table) as shown in the visual.")

> The figure shows the generalization ability of the behavior model to generate diverse motions of a cat jumping off a table and landing at different locations, even with limited training data.


![](figures/figures_20_1.png "🔼 Figure 1: Learning agent behavior from longitudinal casual video recordings. We answer the following question: can we simulate the behavior of an agent, by learning from casually-captured videos of the same agent recorded across a long period of time (e.g., a month)? A) We first reconstruct videos in 4D (3D & time), which includes the scene, the trajectory of the agent, and the trajectory of the observer (i.e., camera held by the observer). Such individual 4D reconstructions are registered across time, resulting in a complete and persistent 4D representation. B) Then we learn a model of the agent for interactive behavior generation. The behavior model explicitly reasons about goals, paths, and full body movements conditioned on the agent's ego-perception and past trajectory. Such an agent representation allows generation of novel scenarios through conditioning. For example, conditioned on different observer trajectories, the cat agent chooses to walk to the carpet, stays still while quivering his tail, or hide under the tray stand. Please see videos results in the supplement.")

> The figure illustrates the Agent-to-Sim (ATS) framework, showing how it reconstructs casual videos into a 4D representation and then uses that to train a generative model for simulating interactive agent behavior.


![](figures/figures_21_0.png "🔼 Figure 1: Learning agent behavior from longitudinal casual video recordings. We answer the following question: can we simulate the behavior of an agent, by learning from casually-captured videos of the same agent recorded across a long period of time (e.g., a month)? A) We first reconstruct videos in 4D (3D & time), which includes the scene, the trajectory of the agent, and the trajectory of the observer (i.e., camera held by the observer). Such individual 4D reconstructions are registered across time, resulting in a complete and persistent 4D representation. B) Then we learn a model of the agent for interactive behavior generation. The behavior model explicitly reasons about goals, paths, and full body movements conditioned on the agent's ego-perception and past trajectory. Such an agent representation allows generation of novel scenarios through conditioning. For example, conditioned on different observer trajectories, the cat agent chooses to walk to the carpet, stays still while quivering his tail, or hide under the tray stand. Please see videos results in the supplement.")

> The figure illustrates the Agent-to-Sim (ATS) framework, showing the 4D spacetime reconstruction from longitudinal casual videos and the interactive behavior simulator.


![](figures/figures_21_1.png "🔼 Figure 13: Robustness to layout changes. We find our camera localization to be robust to layout changes, e.g., the cushion and the large boxes (left) and the box (right). However, it fails to reconstruct layout changes, especially when they are only observed in a few views.")

> The figure shows the robustness of the camera localization method to changes in the environment layout, highlighting its limitations when dealing with changes only observed in a few views.


</details>




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 3: Evaluation of 4D Reconstruction. SV: Single-video. MV: Multi-video." >}}
<table id='1' style='font-size:16px'><tr><td>Method</td><td>DepthAcc (all)</td><td>DepthAcc (fg)</td><td>DepthAcc (bg)</td><td>LPIPS (all)</td><td>LPIPS (fg)</td><td>LPIPS (bg)</td></tr><tr><td>Ours</td><td>0.708</td><td>0.695</td><td>0.703</td><td>0.613</td><td>0.609</td><td>0.613</td></tr><tr><td>SV TotalRecon</td><td>0.533</td><td>0.685</td><td>0.518</td><td>0.641</td><td>0.619</td><td>0.641</td></tr><tr><td>MV TotalRecon</td><td>0.099</td><td>0.647</td><td>0.053</td><td>0.634</td><td>0.666</td><td>0.633</td></tr></table>{{< /table-caption >}}

> This table shows the quantitative results of 4D reconstruction comparing the proposed method to TotalRecon on several metrics, including depth accuracy and LPIPS.


{{< table-caption caption="🔽 Table 4: End-to-end Evaluation of Interactive Behavior Prediction. We report results of predicting goal, path, orientation, and joint angles, using K = 16 samples across L = 12 trials. The metrics are minimum average displacement error (minADE) with standard deviations (±σ). The lower the better and the best results are in bold." >}}
<table id='3' style='font-size:14px'><tr><td>Method</td><td>Goal (m) ↓</td><td>Path (m) ↓</td><td>Orientation (rad) ↓</td><td>Joint Angles (rad)↓</td></tr><tr><td>Location prior (Ziebart et al., 2009)</td><td>0.663±0.307</td><td>N.A.</td><td>N.A.</td><td>N.A.</td></tr><tr><td>Gaussian (Kendall & Gal, 2017)</td><td>0.942±0.081</td><td>0.440 ±0.002</td><td>1.099 ±0.003</td><td>0.295 士0.001</td></tr><tr><td>ATS (Ours)</td><td>0.448±0.146</td><td>0.234 士0.054</td><td>0.550 士0.112</td><td>0.237 士0.006</td></tr><tr><td>(a) hier→1-stage (Tevet et al., 2022)</td><td>1.322±0.071</td><td>0.575 士0.026</td><td>0.879 士0.041</td><td>0.263 士0.007</td></tr><tr><td>(b) ego→world (Rhinehart & Kitani, 2016)</td><td>1.164±0.043</td><td>0.577 士0.022</td><td>0.873 士0.027</td><td>0.295 士0.006</td></tr><tr><td>(c) w/o observer Wo</td><td>0.647±0.148</td><td>0.327 士0.076</td><td>0.620 士0.092</td><td>±0.006 0.240</td></tr><tr><td>(d) w/o scene Ws</td><td>0.784±0.126</td><td>士0.051 0.340</td><td>士0.081 0.678</td><td>士0.007 0.243</td></tr></table>{{< /table-caption >}}

> Table 4 presents a quantitative evaluation of the interactive behavior prediction model, showing the minimum average displacement error for goal, path, orientation, and joint angle prediction.


{{< table-caption caption="🔽 Table 5: Evaluation of Spatial Control. We evaluate goal-conditioned path generation and path-conditoned full body motion generation respectively." >}}
<table id='5' style='font-size:14px'><tr><td>Method</td><td>Path (m) ↓</td><td>Orientation (rad) ↓</td><td>Joint Angles (rad)↓</td></tr><tr><td>Gaussian (Kendall & Gal, 2017)</td><td>0.206±0.002</td><td>0.370±0.003</td><td>0.232±0.001</td></tr><tr><td>ATS (Ours)</td><td>0.115±0.006</td><td>0.331 ±0.004</td><td>0.213±0.001</td></tr><tr><td>(a) ego→world (Rhinehart & Kitani, 2016)</td><td>0.209±0.002</td><td>0.429±0.006</td><td>0.250±0.002</td></tr><tr><td>(b) control-unet→code</td><td>0.146 士0.005</td><td>士0.004 0.351</td><td>士0.001 0.220</td></tr></table>{{< /table-caption >}}

> Table 5 presents a quantitative evaluation of the model's ability to generate paths and full body motions conditioned on either goals or paths, comparing its performance to existing methods.


{{< table-caption caption="🔽 Table 6: Table of Notation." >}}
<table id='1' style='font-size:14px'><tr><td>Symbol</td><td>Description</td></tr><tr><td colspan="2">Global Notations</td></tr><tr><td>B</td><td>The number of bones of an agent. By defatult B = 25.</td></tr><tr><td>M</td><td>The number of videos.</td></tr><tr><td>Ni</td><td>The number of image frames extracted from video i.</td></tr><tr><td>Ii</td><td>The sequence of color images {I1, · · · , INi} extracted from video i.</td></tr><tr><td>⌀i</td><td>The sequence of DINOv2 feature images {⌀1, . . . , �Ni} extracted from video i.</td></tr><tr><td>Ti</td><td>The length of video i.</td></tr><tr><td>T*</td><td>The time horizon of behavior diffusion. By default T* = 5.6s.</td></tr><tr><td>T'</td><td>The time horizon of past conditioning. By default T' = 0.8s</td></tr><tr><td>Z E R3</td><td>Goal of the agent, defined as the location at the end of T*</td></tr><tr><td>P E R3xT*</td><td>Path of the agent, defined as the root body trajectory over T*</td></tr><tr><td>G E R6bxt*</td><td>Pose of the agent, defined as the 6DoF rigid motion of bones over T*</td></tr><tr><td>Ws E R64</td><td>Scene code, representing the scene perceived by the agent.</td></tr><tr><td>Wo E R64</td><td>Observer code, representing the observer perceived by the agent.</td></tr><tr><td>Wp E R64</td><td>Past code, representing the history of events happened to the agent.</td></tr><tr><td colspan="2">Learnable Parameters of 4D Reconstruction</td></tr><tr><td>T</td><td>Canonical NeRFs, including a scene MLP and an agent MLP.</td></tr><tr><td>Bi E R128</td><td>Per-video code that allows NeRFs to represent variations across videos.</td></tr><tr><td>D</td><td>Time-varying parameters, including {E, G, W}.</td></tr><tr><td>Et E SE(3)</td><td>The camera pose that transforms the scene to the camera coordinates at t.</td></tr><tr><td>Go E SE(3)</td><td>The camera pose that transforms the canonical agent to the camera coordinates at t.</td></tr><tr><td>Git E SE(3)</td><td>The transformation that moves bone b from its rest state to time t state.</td></tr><tr><td>W ERB</td><td>Skinning weights of a point, defined as the probability of belonging to bones.</td></tr><tr><td>f⌀</td><td>PoseNet that takes a DINOv2 feature image as input and produces camera pose.</td></tr><tr><td colspan="2">Learnable Parameters of Behavior Generation</td></tr><tr><td>MLP Oz</td><td>Goal MLP that represent the score function of goal distributions.</td></tr><tr><td>ControlUNet⌀p</td><td>Path UNet that represents the score function of path distributions.</td></tr><tr><td>ControlUNet⌀G</td><td>Pose UNet that represents the score function of pose distributions.</td></tr><tr><td>ResNet3D U⌀</td><td>Scene perception network that produces Ws from 3D feature grids ⌀.</td></tr><tr><td>MLP⌀。</td><td>Observer MLP that produces Wo from observer's past trajectory in T'.</td></tr><tr><td>MLP Up</td><td>Past MLP that produces Wp from agent's past trajectory in T'</td></tr></table>{{< /table-caption >}}

> This table lists the notations and descriptions of symbols used throughout the paper.


{{< table-caption caption="🔽 Table 7: Summary of inputs and outputs at different stages of the method." >}}
<table id='3' style='font-size:14px'><tr><td>Stage</td><td>Description</td></tr><tr><td>Overall</td><td>Input: A walk-through video of the scene and videos with agent interactions. Output: An interactive behavior generator of the agent.</td></tr><tr><td>Localizer Training</td><td>Input: 3D reconstruction of the environment and the agent. Output: Neural localizer f⌀.</td></tr><tr><td>Neural Localization</td><td>Input: Neural localizer f⌀ and the agent interaction videos. Output: Camera poses for each video frame.</td></tr><tr><td>4D Reconstruction</td><td>Input: A collection of videos and their corresponding camera poses. Output: Scene feature volume 重, motion of the agent G and observer 8.</td></tr><tr><td>Behavior Learning</td><td>Input: Scene feature volume 重, motion of the agent G and observer E. Output: An interactive behavior generator of the agent.</td></tr></table>{{< /table-caption >}}

> This table summarizes the inputs and outputs at each stage of the proposed method for learning interactive behavior models from casual longitudinal videos.


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