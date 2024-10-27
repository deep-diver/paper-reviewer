---
title: "Cross-Lingual Auto Evaluation for Assessing Multilingual LLMs"
summary: "CIA Suite: A novel cross-lingual evaluation framework for multilingual LLMs using English reference answers, achieving human-level accuracy."
categories: ["AI Generated"]
tags: ["🔖 24-10-17", "🤗 24-10-22"]
showSummary: true
date: 2024-10-17
draft: false
---

### TL;DR


{{< lead >}}

This paper tackles the challenge of evaluating multilingual large language models (LLMs), which is particularly difficult for languages other than English.  The researchers introduce the "Cross-Lingual Auto Evaluation (CIA) Suite," a new framework that uses an evaluator LLM called HERCULE and a new test set called RECON.  HERCULE cleverly addresses the lack of reference answers in many languages by using English reference answers to learn how to score responses in other languages.  The RECON test set features human annotations for 500 instructions across six languages.  Experiments show that HERCULE performs very well, matching human judgments more closely than existing commercial models.  The authors also show that their method works surprisingly well even when evaluating languages not included in its training data (zero-shot evaluation). The entire framework (code, data, and models) is made publicly available to encourage further research.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.13394" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
The research paper introduces CIA suite, a novel cross-lingual auto evaluation framework for multilingual LLMs.  It addresses the scarcity of reference answers in low-resource languages by leveraging English reference answers.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} Introduced CIA Suite, a cross-lingual auto evaluation framework for multilingual LLMs. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} HERCULE, a cross-lingual evaluation LLM, outperforms proprietary models and aligns better with human judgments. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The study highlights the effectiveness of reference-based cross-lingual evaluation, even in low-resource scenarios. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_1_0.png "🔼 Figure 1: We present cross-lingual Evaluator LLM, HERCULE, where the Instruction & Response provided to the model are in the target language, while all other fields are in English. The model generates feedback & score in English for a given evaluation example.")

> The figure illustrates the CIA (Cross-Lingual Auto Evaluation) suite architecture, showing how the HERCULE evaluator LLM processes multilingual instructions and responses to generate feedback and scores.





![](charts/charts_6_0.png "🔼 Figure 3: Comparison of LLM score vs True score when the difference between the predictions is =1 and ≥2. We see that LLM Evaluator is more generous and awards higher scores. Refer Sec. §5.3 for detailed results.")

> The chart compares LLM and true scores when the difference between them is 1 and greater than or equal to 2, showing that LLM evaluator tends to give higher scores.





{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<table id='0' style='font-size:16px'><tr><td>Model</td><td>Type</td><td>bn</td><td>de</td><td>fr</td><td>hi</td><td>te</td><td>ur</td><td>avg.</td></tr><tr><td>GPT-40</td><td>Zero-Shot</td><td>0.64</td><td>0.66</td><td>0.65</td><td>0.64</td><td>0.61</td><td>0.64</td><td>0.64</td></tr><tr><td>GEMINI-1.5-PRO</td><td>Zero-Shot</td><td>0.54</td><td>0.58</td><td>0.59</td><td>0.57</td><td>0.53</td><td>0.57</td><td>0.56</td></tr><tr><td>8 LLAMA-3.1-405B-I</td><td>Zero-Shot</td><td>0.60</td><td>0.66</td><td>0.66</td><td>0.62</td><td>0.51</td><td>0.65</td><td>0.62</td></tr><tr><td>8 LLAMA-3.2 3B</td><td>FFT</td><td>0.68</td><td>0.72</td><td>0.71</td><td>0.71</td><td>0.70</td><td>0.72</td><td>0.71</td></tr><tr><td>GEMMA 7B</td><td>FFT</td><td>0.47</td><td>0.39</td><td>0.36</td><td>0.43</td><td>0.33</td><td>0.38</td><td>0.39</td></tr><tr><td> AYA23 8B</td><td>FFT</td><td>0.70</td><td>0.72</td><td>0.73</td><td>0.72</td><td>0.65</td><td>0.71</td><td>0.70</td></tr><tr><td>HERCULE 8B</td><td>FFT</td><td>0.74</td><td>0.75</td><td>0.75</td><td>0.74</td><td>0.69</td><td>0.74</td><td>0.73</td></tr><tr><td>HERCULE 8B</td><td>LoRA</td><td>0.72</td><td>0.74</td><td>0.72</td><td>0.72</td><td>0.70</td><td>0.70</td><td>0.72</td></tr></table>{{< /table-caption >}}

> Table 1 presents the  linear weighted Cohen's Kappa scores for various LLMs (both zero-shot and fine-tuned) on the RECON test set, indicating the correlation between model predictions and human judgments.



### More visual insights




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Pearson correlation (ρ) between human annotator scores and Evaluator LLM scores on a sample of 100 prompt-response pairs. A higher value indicates stronger alignment with human judgments. See Sec. §5.2 for detailed results." >}}
<table id='2' style='font-size:16px'><tr><td>Model</td><td>bn</td><td>hi</td><td>te</td><td>ur</td></tr><tr><td>GPT-40</td><td>0.37</td><td>0.61</td><td>0.62</td><td>0.67</td></tr><tr><td>GEMINI-PRO</td><td>0.31</td><td>0.51</td><td>0.61</td><td>0.62</td></tr><tr><td>8 LLAMA 405B-I</td><td>0.38</td><td>0.59</td><td>0.67</td><td>0.72</td></tr><tr><td>HERCULE 8B</td><td>0.42</td><td>0.53</td><td>0.74</td><td>0.78</td></tr><tr><td>IAA</td><td>0.38</td><td>0.38</td><td>0.44</td><td>0.46</td></tr></table>{{< /table-caption >}}

> Table 2 presents the Pearson correlation between human annotator scores and Evaluator LLM scores, indicating the level of agreement between human and LLM evaluations.


{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<table id='0' style='font-size:16px'><tr><td></td><td>bn</td><td>de</td><td>fr</td><td>hi</td><td>te</td><td>ur</td><td>Avg.</td></tr><tr><td></td><td>0.64</td><td>0.66</td><td>0.65</td><td>0.64</td><td>0.61</td><td>0.64</td><td>0.64</td></tr><tr><td></td><td>0.61</td><td>0.69</td><td>0.71</td><td>0.08</td><td>0.50</td><td>0.39</td><td>0.50</td></tr><tr><td>bn</td><td>0.74</td><td>0.76</td><td>0.74</td><td>0.74</td><td>0.57</td><td>0.72</td><td>0.71</td></tr><tr><td>de</td><td>0.64</td><td>0.75</td><td>0.72</td><td>0.70</td><td>0.62</td><td>0.69</td><td>0.69</td></tr><tr><td>fr</td><td>0.62</td><td>0.75</td><td>0.75</td><td>0.69</td><td>0.60</td><td>0.68</td><td>0.68</td></tr><tr><td>hi</td><td>0.62</td><td>0.76</td><td>0.77</td><td>0.74</td><td>0.56</td><td>0.69</td><td>0.69</td></tr><tr><td>te</td><td>0.65</td><td>0.71</td><td>0.72</td><td>0.72</td><td>0.69</td><td>0.72</td><td>0.70</td></tr><tr><td>ur</td><td>0.64</td><td>0.76</td><td>0.77</td><td>0.73</td><td>0.59</td><td>0.74</td><td>0.70</td></tr><tr><td></td><td>0.74</td><td>0.75</td><td>0.75</td><td>0.74</td><td>0.69</td><td>0.74</td><td>0.73</td></tr></table>{{< /table-caption >}}

> Table 1 presents the linear weighted Cohen's Kappa scores evaluating the agreement between ground truth scores and model predictions for various models on the RECON test set, differentiating between zero-shot and fine-tuned model evaluations.


{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<table id='9' style='font-size:16px'><tr><td>Model</td><td>bn</td><td>hi</td><td>te</td><td>avg.</td></tr><tr><td>GEMMA-2B</td><td>0.64</td><td>0.62</td><td>0.60</td><td>0.62</td></tr><tr><td>S S ARVAM-2B</td><td>0.58</td><td>0.56</td><td>0.58</td><td>0.57</td></tr><tr><td>GEMMA-2B-IT</td><td>0.64</td><td>0.67</td><td>0.61</td><td>0.64</td></tr><tr><td>8 LLAMA 3.2 3B</td><td>0.68</td><td>0.71</td><td>0.70</td><td>0.70</td></tr></table>{{< /table-caption >}}

> Table 1 shows the performance of different LLMs (both zero-shot and fine-tuned) on the RECON benchmark, measured by the Linear Weighted Cohen's Kappa score.


{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<table id='0' style='font-size:16px'><tr><td>Model</td><td>bn</td><td>de</td><td>fr</td><td>hi</td><td>te</td><td>ur</td><td>avg.</td></tr><tr><td>Single</td><td>0.74</td><td>0.75</td><td>0.75</td><td>0.74</td><td>0.69</td><td>0.74</td><td>0.73</td></tr><tr><td>Joint</td><td>0.70</td><td>0.70</td><td>0.70</td><td>0.69</td><td>0.68</td><td>0.67</td><td>0.69</td></tr><tr><td>Linear</td><td>0.71</td><td>0.75</td><td>0.77</td><td>0.73</td><td>0.64</td><td>0.73</td><td>0.72</td></tr><tr><td>TIES</td><td>0.68</td><td>0.74</td><td>0.77</td><td>0.76</td><td>0.64</td><td>0.72</td><td>0.72</td></tr></table>{{< /table-caption >}}

> Table 1 shows the Linear Weighted Cohen's Kappa scores of various LLMs on the RECON benchmark, comparing zero-shot and fine-tuned models.


{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<br><table id='14' style='font-size:14px'><tr><td></td><td colspan="2"></td><td colspan="2"></td><td colspan="2">8</td><td colspan="2"></td></tr><tr><td></td><td>T</td><td>Ps</td><td>T</td><td>Ps</td><td>T</td><td>Ps</td><td>T</td><td>Ps</td></tr><tr><td>bn</td><td>0.28</td><td>0.35</td><td>0.22</td><td>0.28</td><td>0.33</td><td>0.40</td><td>0.35</td><td>0.43</td></tr><tr><td>hi</td><td>0.43</td><td>0.52</td><td>0.38</td><td>0.47</td><td>0.40</td><td>0.48</td><td>0.36</td><td>0.43</td></tr><tr><td>te</td><td>0.50</td><td>0.62</td><td>0.51</td><td>0.63</td><td>0.57</td><td>0.67</td><td>0.61</td><td>0.75</td></tr><tr><td>ur</td><td>0.54</td><td>0.66</td><td>0.53</td><td>0.64</td><td>0.57</td><td>0.70</td><td>0.65</td><td>0.77</td></tr></table>{{< /table-caption >}}

> Table 1 presents the performance of various LLMs (both zero-shot and fine-tuned) on the RECON benchmark, measured by the linear weighted Cohen's Kappa score.


{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<table id='2' style='font-size:14px'><tr><td>Reference</td><td>Model Prediction - Translated</td></tr><tr><td>Anna - Ben - Carl - Dave - Eve - Frank</td><td>Anna - Ben - Frank - Dave - Eve - Carl</td></tr></table>{{< /table-caption >}}

> Table 1 presents the Cohen's Kappa scores evaluating the correlation between ground truth scores and model predictions for various models on the RECON test set, categorized by zero-shot and fine-tuned settings.


{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<table id='2' style='font-size:14px'><tr><td>Reference</td><td>Model Prediction</td></tr><tr><td>Anna - Ben - Carl - Dave - Eve - Frank</td><td>Anna - Ben - Frank - Dave - Eve - Carl</td></tr></table>{{< /table-caption >}}

> Table 1 presents the performance of various LLMs, both zero-shot and fine-tuned, on the RECON test set using a linear weighted Cohen's Kappa score.


{{< table-caption caption="🔽 Table 1: Evaluation results of all models on the RECON test set. We report the Linear Weighted Cohen's Kappa (κ) score between the ground truth scores and the model predictions. Higher the value, better is the correlation. The upper half of the table presents zero-shot evaluations, while the lower half shows the results of fine-tuned models. Refer to Sec. §5.1 for detailed results." >}}
<table id='2' style='font-size:14px'><tr><td>Reference</td><td>Model Prediction - Translated</td></tr><tr><td>Anna - Ben - Carl - Dave - Eve - Frank</td><td>Anna - Ben - Frank - Dave - Eve - Carl</td></tr></table>{{< /table-caption >}}

> Table 1 presents the linear weighted Cohen's Kappa scores of various LLMs on the RECON test set, comparing zero-shot and fine-tuned model performances.


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
{{< /gallery >}}