---
title: "LOGO -- Long cOntext aliGnment via efficient preference Optimization"
summary: "LOGO: a novel training strategy enhances long-context models' generation by efficiently optimizing preferences, achieving performance comparable to GPT-4 with limited data."
categories: ["AI Generated"]
tags: ["🔖 24-10-24", "🤗 24-10-25"]
showSummary: true
date: 2024-10-24
draft: false
---

### TL;DR


{{< lead >}}

Long-context models (LCMs) show promise but often produce misaligned outputs.  Existing solutions to improve LCMs focus on increasing data size, which is expensive and inefficient. This paper introduces LOGO (Long context aliGnment via efficient preference Optimization), a new training strategy that uses preference optimization to better align LCM outputs with human preferences.  Instead of relying on massive datasets, LOGO uses a clever technique to construct training data that overcomes GPU memory limitations.  Experiments show that LOGO significantly improves LCM performance on real-world long-context tasks, bringing open-source models closer to the performance of GPT-4.  It's achieved with only 0.3B training data on a single 8xA800 GPU machine in 16 hours, making it a more efficient and accessible method.  LOGO also maintains the models’ abilities on other tasks.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18533" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
LOGO efficiently aligns long-context models with human preferences, significantly improving generation quality without extensive data or resources.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} LOGO improves long-context model generation by using preference optimization. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} LOGO addresses GPU memory limitations with a reference-free approach and data synthesis. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} LOGO enhances performance on real-world and synthetic tasks while preserving original model capabilities. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_5_0.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> Figure 1 shows the performance comparison of various long-context models (LCMs) on real-world and synthetic tasks, along with their training data sizes.





![](charts/charts_1_0.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The chart displays the performance of various Long-Context Models (LCMs) across real-world and synthetic long-context tasks, showing retrieval and recall scores, and relating performance to training data size.





{{< table-caption caption="🔽 Table 1: Evaluation results on LongBench benchmark, where † denotes training-free method." >}}
<br><table id='2' style='font-size:14px'><tr><td>Models</td><td>S-Doc QA</td><td>M-Doc QA</td><td>Summ</td><td>Few-shot</td><td>Synthetic</td><td>Avg.</td></tr><tr><td>GPT-3.5-Turbo-16K</td><td>39.8</td><td>38.7</td><td>26.5</td><td>67.1</td><td>37.8</td><td>42.0</td></tr><tr><td>LongChat-v1.5-7B-32k</td><td>28.7</td><td>20.6</td><td>26.7</td><td>60.0</td><td>15.8</td><td>30.4</td></tr><tr><td>LLama-3.1-8B-Instruct-128K</td><td>23.9</td><td>15.8</td><td>28.9</td><td>69.8</td><td>57.5</td><td>39.2</td></tr><tr><td colspan="7">Results on SCMs (scaling x8 context window)</td></tr><tr><td>Llama-3-8B-Instruct-8K</td><td>39.3</td><td>36.2</td><td>24.8</td><td>63.5</td><td>39.9</td><td>40.7</td></tr><tr><td>+ YaRN-64K+</td><td>38.0</td><td>36.6</td><td>27.4</td><td>61.7</td><td>40.9</td><td>40.9</td></tr><tr><td>+ RandPOS-64K</td><td>32.5</td><td>30.5</td><td>26.5</td><td>61.3</td><td>33.4</td><td>36.8</td></tr><tr><td>+ LOGO-64K</td><td>39.8</td><td>36.7</td><td>28.8</td><td>65.4</td><td>49.0</td><td>43.9</td></tr><tr><td>Llama-2-7B-Chat-4K</td><td>24.9</td><td>22.6</td><td>24.7</td><td>60.0</td><td>5.9</td><td>27.6</td></tr><tr><td>+ LOGO-32K</td><td>26.7</td><td>23.3</td><td>26.3</td><td>63.1</td><td>11.1</td><td>30.1</td></tr><tr><td colspan="7">Results on LCMs (long-context alignment)</td></tr><tr><td>Llama-3-8B-Instruct-80K</td><td>43.0</td><td>39.8</td><td>22.2</td><td>64.3</td><td>46.3</td><td>42.3</td></tr><tr><td>+ Instruct Tuning (Full)</td><td>38.8</td><td>35.0</td><td>24.6</td><td>65.9</td><td>44.5</td><td>41.8</td></tr><tr><td>+ Instruct Tuning (Partial)</td><td>39.3</td><td>36.2</td><td>26.8</td><td>63.5</td><td>48.0</td><td>42.8</td></tr><tr><td>+ LOGO-80K</td><td>44.0</td><td>41.2</td><td>28.1</td><td>68.6</td><td>53.0</td><td>47.0</td></tr><tr><td>Llama-2-7B-Instruct-80K</td><td>26.9</td><td>23.8</td><td>21.3</td><td>65.0</td><td>7.9</td><td>29.0</td></tr><tr><td>+ LOGO-80K</td><td>33.6</td><td>28.0</td><td>29.4</td><td>65.1</td><td>24.5</td><td>36.1</td></tr><tr><td>Mistral-Instruct-7B- V0.2-32K</td><td>31.7</td><td>30.6</td><td>16.7</td><td>58.4</td><td>17.9</td><td>31.1</td></tr><tr><td>+ LOGO-32K</td><td>38.3</td><td>37.6</td><td>26.1</td><td>67.0</td><td>31.5</td><td>40.1</td></tr></table>{{< /table-caption >}}

> The table presents the quantitative results of different long-context models on various tasks within the LongBench benchmark, comparing the performance of LOGO with other methods.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_17_0.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The figure shows the performance comparison of various long-context models (LCMs) on real-world and synthetic tasks, highlighting their retrieval and generation capabilities, and the amount of training data used.


![](figures/figures_18_0.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The figure compares the performance of various long-context models (LCMs) on real-world and synthetic tasks, showing their retrieval and generation capabilities in relation to training data size.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_1_1.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The chart compares the performance of various long-context models (LCMs) on real-world and synthetic tasks, showing retrieval and recall scores, and training data size.


![](charts/charts_1_2.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The chart displays the performance of various long-context models (LCMs) on real-world and synthetic tasks, showing their retrieval and recall scores in relation to their training data size.


![](charts/charts_8_0.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The chart displays the performance of various long-context models (LCMs) on real-world tasks, their retrieval and recall scores on a synthetic task, and their training data sizes.


![](charts/charts_8_1.png "🔼 Figure 4: Evaluation results of language modeling task. The solid and dashed curves represent the PPL of the baselines and LOGO, respectively.")

> The chart displays the perplexity (PPL) scores of several large language models (LLMs) with and without LOGO training across various context lengths, illustrating LOGO's impact on language modeling performance.


![](charts/charts_9_0.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The chart compares the performance of various long-context models (LCMs) on real-world and synthetic tasks, showing their retrieval and recall scores, and the amount of training data used.


![](charts/charts_9_1.png "🔼 Figure 6: Ablation study results. (a) Comparison among different settings on the language modeling task (PPL) and real-world tasks (Avg. score on LongBench testing set); (b) Reward difference distribution under different M settings; (c) Training GPU memory consumption of different settings.")

> Figure 6 presents the ablation study results showing the impact of different hyperparameters (M, λ) and context lengths on both the language modeling task and real-world tasks, along with the distribution of reward differences and GPU memory consumption.


![](charts/charts_9_2.png "🔼 Figure 6: Ablation study results. (a) Comparison among different settings on the language modeling task (PPL) and real-world tasks (Avg. score on LongBench testing set); (b) Reward difference distribution under different M settings; (c) Training GPU memory consumption of different settings.")

> Figure 6 presents an ablation study showing the impact of different hyperparameters (M and λ) and context lengths on both language modeling performance and real-world task performance, along with GPU memory usage.


![](charts/charts_10_0.png "🔼 Figure 1: (a) Performance of LCMs on real-world long-context tasks; (b) Retrieval score (long-context understanding ability) and recall score (generation ability) of LCMs on the synthetic retrieval long-context task (multi-value NIAH); (c) Long-context (pre-)training data size for each LCM.")

> The chart displays a comparison of various Long-Context Models (LCMs) across real-world tasks, a synthetic retrieval task, and their respective training data sizes.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 1: Evaluation results on LongBench benchmark, where † denotes training-free method." >}}
<table id='1' style='font-size:18px'><tr><td>Jack W Rae, Anna Potapenko, Siddhant M Jayakumar, and Timothy P Lillicrap. Compressive transformers for long-range sequence modelling. arXiv preprint arXiv:1911.05507, 2019.</td></tr><tr><td>Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. Advances in Neural Information Processing Systems, 36, 2024.</td></tr><tr><td>Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of machine learning research, 21(140):1-67, 2020.</td></tr><tr><td>Mathieu Ravaut, Aixin Sun, Nancy Chen, and Shafiq Joty. On context utilization in summarization with large language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 2764-2781, 2024.</td></tr><tr><td>Dongyu Ru, Lin Qiu, Xiangkun Hu, Tianhang Zhang, Peng Shi, Shuaichen Chang, Jiayang Cheng, Cunxiang Wang, Shichao Sun, Huanyu Li, et al. Ragchecker: A fine-grained framework for diagnosing retrieval-augmented generation. arXiv preprint arXiv:2408.08067, 2024.</td></tr><tr><td>Anian Ruoss, Gregoire Deletang, Tim Genewein, Jordi Grau-Moya, Robert Csordas, Mehdi Ben- nani, Shane Legg, and Joel Veness. Randomized positional encodings boost length generalization of transformers. arXiv preprint arXiv:2305.16843, 2023.</td></tr><tr><td>Amir Saeidi, Shivanshu Verma, Aswin RRV, and Chitta Baral. Triple preference optimiza- tion: Achieving better alignment with less data in a single step optimization. arXiv preprint arXiv:2405.16681, 2024.</td></tr><tr><td>John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.</td></tr><tr><td>Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H Chi, Nathanael Sch�rli, and Denny Zhou. Large language models can be easily distracted by irrelevant context. In International Conference on Machine Learning, pp. 31210-31227. PMLR, 2023.</td></tr><tr><td>Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Niko- lay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open founda- tion and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.</td></tr><tr><td>Szymon Tworkowski, Konrad Staniszewski, Mikotaj Pacek, Yuhuai Wu, Henryk Michalewski, and Piotr Milos. Focused transformer: Contrastive training for context scaling. Advances in Neural Information Processing Systems, 36, 2024.</td></tr><tr><td>Wenhao Wu, Yizhong Wang, Yao Fu, Xiang Yue, Dawei Zhu, and Sujian Li. Long context alignment with short instructions and synthesized positions. arXiv preprint arXiv:2405.03939, 2024a.</td></tr><tr><td>Wenhao Wu, Yizhong Wang, Guangxuan Xiao, Hao Peng, and Yao Fu. Retrieval head mechanisti- cally explains long-context factuality. arXiv preprint arXiv:2404. 15574, 2024b.</td></tr><tr><td>Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang, Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta, Karthik Abinav Sankararaman, Barlas Oguz, et al. Effective long-context scaling of foundation models. arXiv preprint arXiv:2309.16039, 2023.</td></tr><tr><td>Haoran Xu, Amr Sharaf, Yunmo Chen, Weiting Tan, Lingfeng Shen, Benjamin Van Durme, Kenton Murray, and Young Jin Kim. Contrastive preference optimization: Pushing the boundaries of 11m performance in machine translation. arXiv preprint arXiv:2401.08417, 2024.</td></tr><tr><td>An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jialong Tang, Jialin Wang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, Jin Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Junyang Lin, Kai Dang, Keming Lu, Keqin Chen, Kexin Yang, Mei Li, Mingfeng Xue, Na Ni, Pei Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao, Runji Lin, Shijie Wang, Shuai Bai, Sinan Tan, Tianhang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge, Xiaodong Deng, Xiaohuan Zhou, Xingzhang Ren, Xinyu Zhang, Xipin Wei, Xuancheng Ren, Yang Fan, Yang Yao, Yichang Zhang, Yu Wan, Yunfei Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zhihao Fan. Qwen2 technical report. arXiv preprint arXiv:2407.10671, 2024.</td></tr></table>{{< /table-caption >}}

> Table 1 presents the quantitative results of different models on six categories of tasks in the LongBench benchmark, comparing the performance of LOGO with other methods.


{{< table-caption caption="🔽 Table 1: Evaluation results on LongBench benchmark, where † denotes training-free method." >}}
<br><table id='2' style='font-size:16px'><tr><td>Context: context</td></tr><tr><td>What is the slope of the line containing points (2, -3) and (4, 3)? slope = 3 context A slope that goes from low to high is positive. A slope that goes from high to low is negative. A slope that goes straight across is 0. * ** context ...</td></tr><tr><td>Question: is slope of the line containing points (2, -3) and (4, 3)?</td></tr><tr><td>What the Ground Truth: (preference) 3</td></tr><tr><td>Dis-preference Prediction1: (Instruction Unfollowing) Do you want to solve it step by step?</td></tr><tr><td></td></tr><tr><td>Dis-preference Prediction2: (Hallucination) The question can be interpreted as the difference in y-values divided by the difference in X- values. That is, let y1 = -3 and y2 = 3. Then x1 = 2 and x2 = 4. The slope is: = 6</td></tr></table>{{< /table-caption >}}

> Table 1 presents the average scores of different LLMs on six categories of tasks in the LongBench benchmark, comparing the performance of several LLMs with different context scaling and alignment methods.


{{< table-caption caption="🔽 Table 1: Evaluation results on LongBench benchmark, where † denotes training-free method." >}}
<br><table id='5' style='font-size:14px'><tr><td>Context:</td></tr><tr><td>context</td></tr><tr><td>And then there was no more speaking of the old lady, the house with the candle and the woman who was like a candle until, in the last train, they were nearly home. ... context ...</td></tr><tr><td>Question:</td></tr><tr><td>Why does the narrator stop asking his father about the grapes and the grape-vine?</td></tr><tr><td>Ground Truth: (preference)</td></tr><tr><td>Because of the unpleasant encounter with the old lady at the house.</td></tr><tr><td>Dis-preference Prediction1: (Hallucination)</td></tr><tr><td>The narrator stops asking his father about the grapes and the grape-vine because his father is not responding to the questions. The narrator is trying to learn about the grape-vine and its whereabouts but his father is not willing to provide any information...</td></tr><tr><td>Dis-preference Prediction2: (Hallucination)</td></tr><tr><td>Blended learning in action: Because his father� eyes seemed to fill with water and he began to speak in a small voice. At the same time, the narrator himself felt like his heart had been "torn in half.". · ..</td></tr></table>{{< /table-caption >}}

> Table 1 presents the average scores of different language models on six categories of tasks from the LongBench benchmark, comparing the performance of various context scaling and alignment methods.


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
{{< /gallery >}}