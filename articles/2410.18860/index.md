---
title: "DeCoRe: Decoding by Contrasting Retrieval Heads to Mitigate Hallucinations"
summary: "DeCoRe: A novel LLM decoding strategy dynamically contrasts base and masked LLM outputs using conditional entropy, significantly reducing hallucinations and boosting contextual accuracy."
categories: ["AI Generated"]
tags: ["🔖 24-10-24", "🤗 24-10-25"]
showSummary: true
date: 2024-10-24
draft: false
---

### TL;DR


{{< lead >}}

Large Language Models (LLMs) often produce inaccurate or misleading information—a phenomenon known as hallucination. This paper introduces DeCoRe (Decoding by Contrasting Retrieval Heads), a new method to reduce these hallucinations. DeCoRe works by identifying and masking specific "retrieval heads" within the LLM, which are responsible for retrieving contextual information. By comparing the output of the masked LLM with that of the original LLM and using conditional entropy as a guide, DeCoRe amplifies correct answers and suppresses incorrect ones. Experiments show that DeCoRe substantially improves accuracy on multiple tasks requiring high contextual accuracy, including summarization, instruction following, and question answering.  The results demonstrate that DeCoRe is an effective technique for improving the trustworthiness and reliability of LLMs without requiring additional training.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.18860" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This research paper introduces DeCoRe, a novel decoding strategy for Large Language Models (LLMs) that significantly reduces hallucinations by contrasting the outputs of a base LLM and a masked version of the LLM. The core idea is to leverage the dynamic conditional entropy of the model's next token distribution, enhancing contextual faithfulness and factual accuracy.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} DeCoRe, a novel training-free decoding strategy, significantly improves LLM performance on tasks demanding high contextual fidelity. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Masking retrieval heads in LLMs induces hallucinations; DeCoRe leverages this by contrasting outputs to amplify accurate predictions. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} DeCoRe's dynamic entropy control mechanism enhances accuracy in tasks requiring contextual faithfulness, factual recall, and multi-hop reasoning. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: Overview of the DeCoRe workflow. Given the same input, the base LLM (LLMbase) and the variant with masked retrieval heads (LLMmasked) predict the next token. An uncertainty estimation is applied to the base model's output using conditional entropy: higher conditional entropy increases the contrastive factor (a), penalising predictions that align with the LLMmasked. The final prediction is selected based on weighted contrastive decoding of the outputs from both models, leading to a more grounded response.")

> The figure illustrates the DeCoRe workflow, showing how contrasting the outputs of a base LLM and a masked LLM, guided by conditional entropy, leads to more accurate predictions by mitigating hallucinations.





![](charts/charts_8_0.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct model using DeCoReentropy across various tasks, showing mostly negative correlation for faithfulness and factuality, but positive correlation for instruction-following.





{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td rowspan="2">Model</td><td colspan="3">XSum</td><td colspan="2">MemoTrap</td><td colspan="2">IFEval</td><td>NQ-Open</td><td>NQ-Swap</td></tr><tr><td>ROUGE-L ↑</td><td>BERTScore-F1 ↑</td><td>factKB ↑</td><td>Macro Acc ↑</td><td>Micro Acc ↑</td><td>Prompt Acc ↑</td><td>Instruct Acc ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td>Llama3-8b-Instruct</td><td>19.90</td><td>67.23</td><td>47.61</td><td>65.86</td><td>64.40</td><td>70.24</td><td>78.30</td><td>69.68</td><td>60.62</td></tr><tr><td>+ ITI (Li et al., 2024b)</td><td>13.25</td><td>59.96</td><td>34.35</td><td>62.65</td><td>58.96</td><td>52.31</td><td>63.19</td><td>56.16</td><td>51.08</td></tr><tr><td>+ CAD (Shi et al., 2024)</td><td>18.82</td><td>67.20</td><td>67.16</td><td>-</td><td>-</td><td>-</td><td>-</td><td>69.83</td><td>74.21</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>19.82</td><td>67.19</td><td>47.21</td><td>65.27</td><td>63.69</td><td>69.69</td><td>78.18</td><td>69.68</td><td>60.77</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>19.92</td><td>67.34</td><td>48.49</td><td>64.85</td><td>63.17</td><td>70.24</td><td>78.66</td><td>69.49</td><td>60.98</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>19.79</td><td>67.31</td><td>48.49</td><td>65.38</td><td>64.28</td><td>67.65</td><td>76.26</td><td>68.93</td><td>60.51</td></tr><tr><td>+ DeCoRestatic</td><td>19.87</td><td>67.83</td><td>64.07</td><td>69.53</td><td>69.20</td><td>69.13</td><td>78.06</td><td>70.62</td><td>64.43</td></tr><tr><td>+ DeCoReentropy</td><td>19.45</td><td>67.69</td><td>66.10</td><td>74.14</td><td>74.87</td><td>68.39</td><td>76.38</td><td>70.66</td><td>66.08</td></tr><tr><td>Llama3-70b-Instruct</td><td>22.41</td><td>69.77</td><td>61.32</td><td>68.47</td><td>66.52</td><td>77.45</td><td>84.41</td><td>71.07</td><td>76.11</td></tr><tr><td>+ ITI (Li et al., 2024b)</td><td>21.64</td><td>69.46</td><td>61.33</td><td>71.24</td><td>68.73</td><td>76.71</td><td>83.69</td><td>71.90</td><td>74.76</td></tr><tr><td>+ CD (Li et al., 2023)</td><td>22.71</td><td>69.99</td><td>54.73</td><td>69.27</td><td>67.55</td><td>71.72</td><td>79.74</td><td>65.80</td><td>68.37</td></tr><tr><td>+ CAD (Shi et al., 2024)</td><td>21.45</td><td>69.28</td><td>65.61</td><td>-</td><td>-</td><td>-</td><td>-</td><td>71.83</td><td>84.70</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>22.46</td><td>69.80</td><td>61.11</td><td>67.99</td><td>65.93</td><td>77.08</td><td>84.29</td><td>71.07</td><td>75.98</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>22.43</td><td>69.93</td><td>59.99</td><td>67.92</td><td>65.81</td><td>78.00</td><td>84.65</td><td>70.40</td><td>75.26</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>22.49</td><td>69.91</td><td>60.57</td><td>67.51</td><td>66.44</td><td>76.89</td><td>84.41</td><td>71.15</td><td>74.02</td></tr><tr><td>+ DeCoRestatic</td><td>21.94</td><td>69.35</td><td>64.88</td><td>71.96</td><td>71.41</td><td>78.56</td><td>84.89</td><td>72.51</td><td>79.06</td></tr><tr><td>+ DeCoReentropy</td><td>21.93</td><td>69.40</td><td>65.49</td><td>74.07</td><td>73.65</td><td>78.56</td><td>84.89</td><td>72.66</td><td>79.79</td></tr><tr><td>+ DeCoReentropy-lite</td><td>22.28</td><td>69.34</td><td>59.57</td><td>72.11</td><td>70.58</td><td>61.37</td><td>71.46</td><td>71.26</td><td>75.90</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods on various faithfulness evaluation tasks, showing DeCoRe's improvement over baselines.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_8_0.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> Figure 3 shows the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct with DeCoRe entropy across various faithfulness, factuality, and chain-of-thought reasoning tasks.


![](figures/figures_8_1.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The figure shows the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct model using DeCoReEntropy across various faithfulness, factuality and chain-of-thought reasoning tasks.


![](figures/figures_8_2.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The figure shows the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct with DeCoReentropy on various faithfulness, factuality, and chain-of-thought reasoning tasks.


![](figures/figures_18_0.png "🔼 Figure 1: Overview of the DeCoRe workflow. Given the same input, the base LLM (LLMbase) and the variant with masked retrieval heads (LLMmasked) predict the next token. An uncertainty estimation is applied to the base model's output using conditional entropy: higher conditional entropy increases the contrastive factor (a), penalising predictions that align with the LLMmasked. The final prediction is selected based on weighted contrastive decoding of the outputs from both models, leading to a more grounded response.")

> This figure illustrates the workflow of DeCoRe, showing how it contrasts the outputs of a base LLM and a masked LLM to mitigate hallucinations.


![](figures/figures_20_0.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The figure shows the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct with DeCoReentropy on several faithfulness, factuality, and chain-of-thought reasoning tasks.


![](figures/figures_25_0.png "🔼 Figure 8: Correlation between the number of masked random heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> Figure 8 shows the correlation between the number of masked random heads and the performance of Llama3-8B-Instruct with DeCoReentropy across various tasks.


![](figures/figures_35_0.png "🔼 Figure 1: Overview of the DeCoRe workflow. Given the same input, the base LLM (LLMbase) and the variant with masked retrieval heads (LLMmasked) predict the next token. An uncertainty estimation is applied to the base model's output using conditional entropy: higher conditional entropy increases the contrastive factor (a), penalising predictions that align with the LLMmasked. The final prediction is selected based on weighted contrastive decoding of the outputs from both models, leading to a more grounded response.")

> The figure illustrates the DeCoRe workflow, showing how contrasting the outputs of a base LLM and a masked LLM, guided by conditional entropy, leads to more accurate predictions.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_8_1.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked retrieval heads and the performance of the Llama3-8B-Instruct model using DeCoReentropy across various tasks, showing positive correlations for some tasks and negative correlations for others.


![](charts/charts_8_2.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart shows the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct model using DeCoReEntropy on various faithfulness, factuality and chain-of-thought reasoning tasks.


![](charts/charts_8_3.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked retrieval heads in the Llama3-8B-Instruct model using DeCoReentropy and its performance across various tasks, showing varying degrees of correlation across different task types.


![](charts/charts_8_4.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct using DeCoReEntropy across various faithfulness, factuality, and chain-of-thought reasoning tasks.


![](charts/charts_8_5.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked retrieval heads and the performance of the Llama3-8B-Instruct model using DeCoReentropy across various tasks.


![](charts/charts_9_0.png "🔼 Figure 4: Comparison of Length-normalised conditional entropy of Greedy, ITI, DoLa, and DeCoReentropy in long-generation tasks (i.e., XSum (a), MuSiQue (Closed) + CoT (b), and MuSiQue (Open) + CoT (c)). Asterisks (*) indicate statistically significant differences between the distributions based on one-tailed Welch's t-test results. Detailed results are listed in Table 28.")

> The violin plot shows that DeCoReEntropy has significantly lower length-normalized conditional entropy than other decoding methods in long-generation tasks.


![](charts/charts_9_1.png "🔼 Figure 4: Comparison of Length-normalised conditional entropy of Greedy, ITI, DoLa, and DeCoReentropy in long-generation tasks (i.e., XSum (a), MuSiQue (Closed) + CoT (b), and MuSiQue (Open) + CoT (c)). Asterisks (*) indicate statistically significant differences between the distributions based on one-tailed Welch’s t-test results. Detailed results are listed in Table 28.")

> The violin plot displays the comparison of length-normalized conditional entropy across different decoding methods in long-generation tasks.


![](charts/charts_9_2.png "🔼 Figure 7: Relation between length-normalised entropy and correctness in MuSiQue CoT generation.")

> The chart displays the relationship between length-normalized entropy and answer correctness in MuSiQue CoT generation, showing that lower entropy correlates with higher accuracy.


![](charts/charts_24_0.png "🔼 Figure 7: Relation between length-normalised entropy and correctness in MuSiQue CoT generation. Entropy tends to be negatively correlated with the final answer correctness (i.e., the lower the length-normalised entropy, the more likely that the answer is correct.)")

> The chart displays the distribution of length-normalized entropy for correct and incorrect answers, demonstrating a negative correlation between entropy and correctness in MuSiQue CoT generation.


![](charts/charts_24_1.png "🔼 Figure 7: Relation between length-normalised entropy and correctness in MuSiQue CoT generation. Entropy tends to be negatively correlated with the final answer correctness (i.e., the lower the length-normalised entropy, the more likely that the answer is correct.)")

> The chart displays the distribution of length-normalized entropy for correct and incorrect answers, demonstrating a negative correlation between entropy and correctness in the MuSiQue CoT generation task.


![](charts/charts_24_2.png "🔼 Figure 7: Relation between length-normalised entropy and correctness in MuSiQue CoT generation.")

> The chart displays the distribution of length-normalized entropy for correct and incorrect answers across different models (DeCoRe, Baseline, and DoLa), showing a negative correlation between length-normalized entropy and answer correctness.


![](charts/charts_24_3.png "🔼 Figure 7: Relation between length-normalised entropy and correctness in MuSiQue CoT generation. Entropy tends to be negatively correlated with the final answer correctness (i.e., the lower the length-normalised entropy, the more likely that the answer is correct.)")

> The chart displays the negative correlation between length-normalized entropy and answer correctness across three different LLMs (DeCoRe, Baseline, and DoLa) in the MuSiQue CoT generation task, illustrating that lower entropy values are associated with higher correctness.


![](charts/charts_25_0.png "🔼 Figure 8: Correlation between the number of masked random heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked random heads and the performance of Llama3-8B-Instruct with DeCoReentropy across various faithfulness, factuality, and Chain-of-Thought reasoning tasks.


![](charts/charts_25_1.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked retrieval heads and the performance of the Llama3-8B-Instruct model using DeCoReentropy across various tasks, showing positive correlations for some tasks and negative for others.


![](charts/charts_25_2.png "🔼 Figure 8: Correlation between the number of masked random heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked random heads and the performance of Llama3-8B-Instruct with DeCoReentropy across various faithfulness, factuality, and Chain-of-Thought reasoning tasks.


![](charts/charts_25_3.png "🔼 Figure 8: Correlation between the number of masked random heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked random heads and the performance of Llama3-8B-Instruct model using DeCoReentropy across various tasks, showing varying trends depending on the task type.


![](charts/charts_25_4.png "🔼 Figure 3: Correlation between the number of masked retrieval heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked retrieval heads and the performance of Llama3-8B-Instruct using DeCoReentropy across various tasks.


![](charts/charts_25_5.png "🔼 Figure 8: Correlation between the number of masked random heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked random heads and the performance of Llama3-8B-Instruct with DeCoReentropy across various faithfulness, factuality, and chain-of-thought reasoning tasks.


![](charts/charts_25_6.png "🔼 Figure 8: Correlation between the number of masked random heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked random heads and the performance of Llama3-8B-Instruct with DeCoReentropy across various faithfulness, factuality, and chain-of-thought reasoning tasks.


![](charts/charts_25_7.png "🔼 Figure 8: Correlation between the number of masked random heads and performance of Llama3-8B-Instruct with DeCoReentropy on each task. The correlations are quantified by the Pearson Correlation Coefficient r for each plot. Detailed results are listed in Table 14 and Table 16.")

> The chart displays the correlation between the number of masked random heads and the performance of Llama3-8B-Instruct with DeCoReentropy across various faithfulness, factuality, and chain-of-thought reasoning tasks.


![](charts/charts_31_0.png "🔼 Figure 9: Relation between α and performance metrics of Llama3-8b-Instruct with DeCoRestatic in the faithfulness (a), factuality (b), and Chain-of-Thought reasoning (c) evaluation tasks. Detailed results are listed in Table 23, Table 24, and Table 25.")

> The chart displays how varying the scaling factor α in DeCoRestatic affects the performance across different faithfulness, factuality, and chain-of-thought reasoning tasks.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td colspan="3">TruthfulQA (MC)</td><td>TriviaQA</td><td>PopQA</td><td colspan="4">TruthfulQA (Generation)</td><td>NQ-Open</td></tr><tr><td>MC1 ↑</td><td>MC2 ↑</td><td>MC3↑</td><td>EM ↑</td><td>EM↑</td><td>%Truth ↑</td><td>%Info ↑</td><td>%T⌀I↑</td><td>%Reject ↓</td><td>EM ↑</td></tr><tr><td>Llama3-8b-Instruct</td><td>39.41</td><td>55.69</td><td>30.31</td><td>56.58</td><td>26.64</td><td>80.66</td><td>63.89</td><td>44.55</td><td>43.94</td><td>29.04</td></tr><tr><td>+ ITI (Li et al., 2024b)</td><td>43.70</td><td>62.78</td><td>34.91</td><td>48.41</td><td>15.63</td><td>87.52</td><td>78.46</td><td>66.10</td><td>25.46</td><td>22.07</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>39.05</td><td>55.65</td><td>30.06</td><td>56.63</td><td>26.58</td><td>80.66</td><td>62.91</td><td>43.70</td><td>45.04</td><td>29.15</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>38.68</td><td>55.64</td><td>30.19</td><td>56.50</td><td>26.49</td><td>80.78</td><td>62.67</td><td>43.45</td><td>44.92</td><td>29.19</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>31.21</td><td>55.30</td><td>28.28</td><td>54.93</td><td>26.38</td><td>80.42</td><td>63.40</td><td>43.82</td><td>43.82</td><td>28.32</td></tr><tr><td>+ DeCoRestatic</td><td>38.68</td><td>55.74</td><td>29.80</td><td>56.93</td><td>26.86</td><td>80.78</td><td>67.93</td><td>48.71</td><td>41.74</td><td>29.42</td></tr><tr><td>+ DeCoReentropy</td><td>38.43</td><td>55.86</td><td>30.95</td><td>56.40</td><td>26.88</td><td>78.95</td><td>74.05</td><td>53.00</td><td>38.68</td><td>28.96</td></tr><tr><td>Llama3-70b-Instruct</td><td>49.57</td><td>70.60</td><td>37.85</td><td>74.77</td><td>40.63</td><td>88.74</td><td>77.72</td><td>66.46</td><td>53.12</td><td>40.08</td></tr><tr><td>+ ITI (Li et al., 2024b)</td><td>48.96</td><td>67.04</td><td>37.27</td><td>73.54</td><td>39.62</td><td>82.50</td><td>74.30</td><td>56.92</td><td>37.94</td><td>38.57</td></tr><tr><td>+ CD (Li et al., 2023)</td><td>57.77</td><td>76.65</td><td>47.08</td><td>72.83</td><td>37.03</td><td>88.25</td><td>88.13</td><td>76.38</td><td>52.26</td><td>36.23</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>49.45</td><td>70.58</td><td>37.75</td><td>74.74</td><td>40.65</td><td>88.74</td><td>77.60</td><td>66.34</td><td>52.88</td><td>40.08</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>49.69</td><td>70.88</td><td>38.01</td><td>73.96</td><td>40.00</td><td>88.98</td><td>58.38</td><td>47.37</td><td>54.71</td><td>39.59</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>42.23</td><td>67.56</td><td>35.37</td><td>74.14</td><td>40.53</td><td>87.39</td><td>67.20</td><td>54.59</td><td>49.33</td><td>40.23</td></tr><tr><td>+ DeCoRestatic</td><td>51.29</td><td>72.02</td><td>40.24</td><td>74.79</td><td>40.74</td><td>88.25</td><td>62.91</td><td>51.16</td><td>54.96</td><td>40.41</td></tr><tr><td>+ DeCoReentropy</td><td>53.98</td><td>73.44</td><td>42.55</td><td>74.76</td><td>40.58</td><td>89.23</td><td>59.73</td><td>49.11</td><td>56.79</td><td>40.45</td></tr><tr><td>+ DeCoReentropy-lite</td><td>55.32</td><td>73.38</td><td>43.74</td><td>73.87</td><td>39.09</td><td>88.13</td><td>90.09</td><td>78.21</td><td>52.02</td><td>39.21</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods on various faithfulness evaluation tasks, highlighting the best performing model for each task.


{{< table-caption caption="🔽 Table 3: Performance of different models and decoding methods on MuSiQue, a multi-hop reasoning dataset, with and without CoT prompting in both closed-book and open-book settings. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td rowspan="2">Model</td><td colspan="2">MuSiQue without CoT</td><td colspan="2">MuSiQue with CoT</td></tr><tr><td>Closed Book ↑</td><td>Open Book ↑</td><td>Closed Book ↑</td><td>Open Book ↑</td></tr><tr><td>Llama3-8b-Instruct</td><td>7.41</td><td>58.83</td><td>14.61</td><td>69.84</td></tr><tr><td>+ CAD</td><td>-</td><td>57.88</td><td>-</td><td>73.02</td></tr><tr><td>+ ITI</td><td>4.01</td><td>45.84</td><td>4.18</td><td>38.31</td></tr><tr><td>+ DoLA</td><td>7.24</td><td>59.08</td><td>14.94</td><td>69.92</td></tr><tr><td>+ AD</td><td>6.99</td><td>58.63</td><td>14.40</td><td>69.92</td></tr><tr><td>+ DeCoRestatic</td><td>7.90</td><td>61.23</td><td>14.69</td><td>72.49</td></tr><tr><td>+ DeCoReentropy</td><td>7.70</td><td>61.98</td><td>13.90</td><td>74.47</td></tr><tr><td>Llama3-70b-Instruct + ITI</td><td>11.79</td><td>68.56</td><td>20.15</td><td>74.43</td></tr><tr><td>+ CD</td><td>10.92</td><td>66.61</td><td>17.17</td><td>71.70</td></tr><tr><td>+ CAD</td><td>-</td><td>68.64</td><td>-</td><td>74.02</td></tr><tr><td></td><td>10.88</td><td>68.14</td><td>20.44</td><td>74.27</td></tr><tr><td>+ DoLA</td><td>11.42</td><td>68.68</td><td>20.15</td><td>74.64</td></tr><tr><td>+ AD</td><td>11.38</td><td>68.14</td><td>20.23</td><td>74.27</td></tr><tr><td>+ DeCoRestatic</td><td>11.79</td><td>69.76</td><td>20.60</td><td>75.05</td></tr><tr><td>+ DeCoReentropy</td><td>11.75</td><td>69.84</td><td>20.60</td><td>74.93</td></tr><tr><td>+ DeCoReentropy-lite</td><td>11.13</td><td>69.34</td><td>18.87</td><td>73.36</td></tr></table>{{< /table-caption >}}

> This table presents the performance comparison of different LLMs and decoding methods on the MuSiQue dataset, with and without Chain-of-Thought prompting, across closed-book and open-book settings.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:16px'><tr><td>Retrieval Head ID</td><td>Meta-Llama-3-8B</td><td>Meta-Llama-3-8B-Instruct</td><td>Meta-Llama-3-70B-Instruct</td><td>Mistral-7B-Instruct-v0.3</td><td>Qwen2-7B-Instruct</td></tr><tr><td>1</td><td>0.9341</td><td>0.9447</td><td>0.9172</td><td>0.8741</td><td>0.7746</td></tr><tr><td>10</td><td>0.4666</td><td>0.4421</td><td>0.3844</td><td>0.3167</td><td>0.3487</td></tr><tr><td>20</td><td>0.2927</td><td>0.2743</td><td>0.1874</td><td>0.1951</td><td>0.1986</td></tr><tr><td>30</td><td>0.1347</td><td>0.1421</td><td>0.1310</td><td>0.1457</td><td>0.1243</td></tr><tr><td>40</td><td>0.1074</td><td>0.1131</td><td>0.1112</td><td>0.1115</td><td>0.1077</td></tr><tr><td>50</td><td>0.0881</td><td>0.0916</td><td>0.0914</td><td>0.0944</td><td>0.0843</td></tr><tr><td>60</td><td>0.0735</td><td>0.0751</td><td>0.0867</td><td>0.0852</td><td>0.0703</td></tr><tr><td>70</td><td>0.0623</td><td>0.0659</td><td>0.0814</td><td>0.0751</td><td>0.0620</td></tr><tr><td>80</td><td>0.0572</td><td>0.0604</td><td>0.0630</td><td>0.0704</td><td>0.0524</td></tr><tr><td>90</td><td>0.0491</td><td>0.0513</td><td>0.0571</td><td>0.0641</td><td>0.0412</td></tr><tr><td>100</td><td>0.0433</td><td>0.0452</td><td>0.0526</td><td>0.0538</td><td>0.0352</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different models and decoding methods on several faithfulness evaluation tasks, highlighting the best-performing model for each task.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Retrieval Heads</td><td colspan="3">XSum</td><td colspan="2">MemoTrap</td><td colspan="2">IFEval</td><td>NQ-Open</td><td>NQ-Swap</td></tr><tr><td>ROUGE-L↑</td><td>BERTScore-F1 ↑</td><td>factKB ↑</td><td>Macro Acc ↑</td><td>Micro Acc ↑</td><td>Prompt Acc↑</td><td>Instruct Acc↑</td><td>EM ↑</td><td>EM↑</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>0 (Baseline)</td><td>19.90</td><td>67.23</td><td>47.61</td><td>65.86</td><td>64.40</td><td>70.24</td><td>78.30</td><td>69.68</td><td>60.62</td></tr><tr><td>10</td><td>20.51</td><td>67.33</td><td>36.56</td><td>66.76</td><td>65.89</td><td>62.66</td><td>72.90</td><td>64.26</td><td>42.92</td></tr><tr><td>20</td><td>20.52</td><td>67.07</td><td>34.89</td><td>64.44</td><td>63.96</td><td>63.77</td><td>73.74</td><td>62.30</td><td>43.57</td></tr><tr><td>30</td><td>20.21</td><td>66.49</td><td>29.70</td><td>65.92</td><td>64.12</td><td>61.74</td><td>72.54</td><td>63.24</td><td>46.48</td></tr><tr><td>40</td><td>19.92</td><td>66.24</td><td>26.72</td><td>66.83</td><td>64.83</td><td>58.41</td><td>68.94</td><td>62.79</td><td>46.73</td></tr><tr><td>50</td><td>20.05</td><td>66.47</td><td>25.97</td><td>68.08</td><td>67.07</td><td>55.08</td><td>66.91</td><td>62.49</td><td>44.77</td></tr><tr><td>60</td><td>20.05</td><td>66.54</td><td>23.33</td><td>68.49</td><td>67.03</td><td>55.27</td><td>67.15</td><td>62.90</td><td>44.23</td></tr><tr><td>70</td><td>19.42</td><td>66.14</td><td>24.55</td><td>67.88</td><td>65.89</td><td>56.01</td><td>68.23</td><td>63.01</td><td>46.97</td></tr><tr><td>80</td><td>19.13</td><td>64.53</td><td>22.40</td><td>64.72</td><td>62.23</td><td>55.08</td><td>67.63</td><td>60.45</td><td>43.62</td></tr><tr><td>90</td><td>19.46</td><td>64.39</td><td>21.12</td><td>63.77</td><td>61.28</td><td>54.16</td><td>66.55</td><td>57.97</td><td>40.77</td></tr><tr><td>100</td><td>19.54</td><td>62.47</td><td>17.13</td><td>60.02</td><td>56.95</td><td>47.50</td><td>59.47</td><td>56.61</td><td>39.02</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods across several faithfulness evaluation tasks (XSum, MemoTrap, IFEval, NQ-Open, and NQ-Swap).


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='14' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Retrieval Heads</td><td colspan="3">XSum</td><td colspan="2">MemoTrap</td><td colspan="2">IFEval</td><td>NQ-Open</td><td>NQ-Swap</td></tr><tr><td>ROUGE-L ↑</td><td>BERTScore-F1 ↑</td><td>factKB ↑</td><td>Macro Acc ↑</td><td>Micro Acc ↑</td><td>Prompt Acc ↑</td><td>Instruct Acc ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>0 (Baseline)</td><td>19.90</td><td>67.23</td><td>47.61</td><td>65.86</td><td>64.40</td><td>70.24</td><td>78.30</td><td>69.68</td><td>60.62</td></tr><tr><td>10</td><td>20.09 ±0.21</td><td>67.07 ±0.32</td><td>44.52 ±4.86</td><td>66.79 士2.11</td><td>65.16 士2.61</td><td>68.64 ±0.77</td><td>77.14 ±0.39</td><td>69.45 ±0.46</td><td>61.39 ±0.24</td></tr><tr><td>20</td><td>20.00 ±0.15</td><td>66.80 ±0.46</td><td>40.77 士5.98</td><td>67.89 ±3.24</td><td>66.54 ±4.43</td><td>69.50 ±0.93</td><td>77.66 ±0.68</td><td>68.94 ±0.81</td><td>60.67 ±2.08</td></tr><tr><td>30</td><td>19.87 ±0.18</td><td>66.61 ±0.89</td><td>36.65 ±11.64</td><td>66.88 士2.66</td><td>65.29 ±3.71</td><td>68.27 ±1.36</td><td>76.58 ±1.45</td><td>69.18 ±0.66</td><td>60.70 ±2.87</td></tr><tr><td>40</td><td>19.63 ±0.09</td><td>66.55 ±1.12</td><td>35.09 ±14.85</td><td>66.29 ±2.05</td><td>63.83 ±3.39</td><td>67.59 ±1.34</td><td>75.86 ±1.20</td><td>68.78 ±1.19</td><td>57.19 ±6.92</td></tr><tr><td>50</td><td>19.59 ±0.19</td><td>66.34 士1.23</td><td>32.25 ±14.71</td><td>67.59 士2.09</td><td>64.76 ±3.84</td><td>66.23 ±1.98</td><td>75.18 ±1.26</td><td>68.57 ±0.80</td><td>57.21 士5.62</td></tr><tr><td>60</td><td>19.28 ±0.77</td><td>66.02 ±1.52</td><td>31.67 ±12.94</td><td>67.85 ±0.80</td><td>63.99 ±1.09</td><td>62.97 ±2.82</td><td>72.30 ±3.11</td><td>68.10 ±1.04</td><td>55.97 ±3.79</td></tr><tr><td>70</td><td>19.48 ±0.53</td><td>65.81 士1.67</td><td>27.20 ±12.83</td><td>68.33 ±4.57</td><td>64.51 ±4.95</td><td>60.87 ±4.41</td><td>70.74 ±3.47</td><td>67.85 ±1.04</td><td>55.00 ±3.48</td></tr><tr><td>80</td><td>18.96 ±0.94</td><td>64.92 ±0.94</td><td>26.02 ±13.42</td><td>69.66 ±6.45</td><td>66.40 ±7.16</td><td>56.87 ±4.16</td><td>66.79 士2.98</td><td>67.08 ±1.21</td><td>54.59 士5.23</td></tr><tr><td>90</td><td>17.55 ±1.19</td><td>61.85 ±4.91</td><td>28.00 ±13.27</td><td>73.39 ±4.35</td><td>70.71 ±4.93</td><td>50.96 ±10.71</td><td>62.39 ±9.58</td><td>66.53 ±0.49</td><td>54.26 士5.17</td></tr><tr><td>100</td><td>17.13 ±1.17</td><td>61.61 ±6.05</td><td>28.46 ±9.30</td><td>74.65 ±3.67</td><td>72.02 ±4.25</td><td>48.92 ±8.04</td><td>60.67 ±7.43</td><td>66.54 ±0.91</td><td>54.71 ±5.34</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods on various faithfulness evaluation tasks, highlighting the best-performing models and methods for each task.


{{< table-caption caption="🔽 Table 7: Performance comparison of Llama3-8B-Instruct with different number of masked retrieval heads on factuality evaluation tasks." >}}
<table id='2' style='font-size:16px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Retrieval Heads</td><td colspan="3">TruthfulQA (MC)</td><td>TriviaQA</td><td>PopQA</td><td>NQ-Open</td></tr><tr><td>MC1 ↑</td><td>MC2 ↑</td><td>MC3 ↑</td><td>EM ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>39.41</td><td>55.69</td><td>30.31</td><td>56.58</td><td>26.64</td><td>29.04</td></tr><tr><td>10</td><td>39.17</td><td>57.40</td><td>31.57</td><td>55.77</td><td>25.84</td><td>28.81</td></tr><tr><td>20</td><td>40.27</td><td>59.37</td><td>33.24</td><td>55.26</td><td>25.39</td><td>28.93</td></tr><tr><td>30</td><td>40.51</td><td>60.51</td><td>33.30</td><td>55.39</td><td>25.32</td><td>29.42</td></tr><tr><td>40</td><td>41.49</td><td>61.11</td><td>34.00</td><td>54.99</td><td>25.35</td><td>28.51</td></tr><tr><td>50</td><td>41.00</td><td>61.31</td><td>33.63</td><td>54.32</td><td>25.04</td><td>27.91</td></tr><tr><td>60</td><td>39.29</td><td>59.32</td><td>32.48</td><td>54.05</td><td>24.47</td><td>27.50</td></tr><tr><td>70</td><td>38.80</td><td>59.27</td><td>32.47</td><td>54.01</td><td>24.52</td><td>27.76</td></tr><tr><td>80</td><td>36.23</td><td>57.71</td><td>30.64</td><td>53.92</td><td>24.19</td><td>27.31</td></tr><tr><td>90</td><td>35.86</td><td>56.63</td><td>30.17</td><td>52.89</td><td>23.51</td><td>26.18</td></tr><tr><td>100</td><td>36.47</td><td>57.39</td><td>31.08</td><td>52.56</td><td>23.30</td><td>26.25</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of Llama3-8B-Instruct with varying numbers of masked retrieval heads on factuality evaluation tasks, showing the impact of masked retrieval heads on factuality.


{{< table-caption caption="🔽 Table 2: Performance of different models and decoding methods on factuality evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Retrieval Heads</td><td colspan="3">TruthfulQA (MC)</td><td>TriviaQA</td><td>PopQA</td><td>NQ-Open</td></tr><tr><td>MC1 ↑</td><td>MC2 ↑</td><td>MC3 ↑</td><td>EM ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>39.41</td><td>55.69</td><td>30.31</td><td>56.58</td><td>21.10</td><td>29.04</td></tr><tr><td>10</td><td>38.84 士0.71</td><td>55.79 士0.53</td><td>30.38 ±0.46</td><td>56.17 士0.03</td><td>25.96 士0.18</td><td>29.27 士0.10</td></tr><tr><td>20</td><td>38.51 士0.35</td><td>56.09 士2.21</td><td>30.34 ±0.86</td><td>55.75 士0.33</td><td>25.63 士0.25</td><td>28.89 ±0.46</td></tr><tr><td>30</td><td>37.58 士1.12</td><td>56.47 士2.30</td><td>30.21 士1.01</td><td>54.84 士0.58</td><td>25.52 士0.16</td><td>28.03 士0.20</td></tr><tr><td>40</td><td>37.37 士0.57</td><td>57.00 士1.94</td><td>30.24 ±0.51</td><td>54.14 士0.65</td><td>25.24 士0.15</td><td>27.51 士0.61</td></tr><tr><td>50</td><td>37.17 士1.56</td><td>56.70 士2.36</td><td>29.85 士1.58</td><td>53.17 士1.22</td><td>25.07 士0.22</td><td>26.61 ±1.14</td></tr><tr><td>60</td><td>35.86 ±1.41</td><td>55.37 ±0.82</td><td>28.87 ±0.80</td><td>52.43 士1.77</td><td>24.54 士0.54</td><td>26.26 ±1.14</td></tr><tr><td>70</td><td>34.68 士0.31</td><td>53.87 士1.16</td><td>27.63 ±0.66</td><td>51.79 士1.59</td><td>24.50 士0.58</td><td>25.70 士1.07</td></tr><tr><td>80</td><td>33.05 士2.36</td><td>53.12 士2.02</td><td>26.56 士2.03</td><td>48.11 士5.82</td><td>24.52 士1.01</td><td>24.36 士1.83</td></tr><tr><td>90</td><td>30.80 士2.20</td><td>49.78 士2.91</td><td>24.79 士1.56</td><td>47.39 士5.68</td><td>24.14 士0.98</td><td>24.05 士2.03</td></tr><tr><td>100</td><td>30.07 ±0.90</td><td>49.78 士1.74</td><td>24.44 士0.76</td><td>47.04 士5.17</td><td>24.05 士0.76</td><td>23.96 ±1.84</td></tr></table>{{< /table-caption >}}

> Table 2 presents the performance comparison of different LLMs and decoding methods across various factuality evaluation tasks, highlighting the best and second-best performances for each model.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Retrieval Heads</td><td colspan="2">MuSiQue without C⌀T</td><td colspan="2">MuSiQue with CoT</td></tr><tr><td>Closed Book</td><td>Open Book</td><td>Closed Book</td><td>Open Book</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>7.41</td><td>58.83</td><td>14.61</td><td>69.84</td></tr><tr><td>10</td><td>6.99</td><td>51.47</td><td>14.56</td><td>59.87</td></tr><tr><td>20</td><td>6.91</td><td>49.52</td><td>15.06</td><td>57.92</td></tr><tr><td>30</td><td>6.74</td><td>46.96</td><td>12.16</td><td>50.48</td></tr><tr><td>40</td><td>6.33</td><td>47.41</td><td>11.54</td><td>48.70</td></tr><tr><td>50</td><td>6.29</td><td>46.67</td><td>13.24</td><td>47.37</td></tr><tr><td>60</td><td>6.33</td><td>46.01</td><td>10.72</td><td>41.79</td></tr><tr><td>70</td><td>6.41</td><td>46.46</td><td>11.38</td><td>43.65</td></tr><tr><td>80</td><td>6.41</td><td>44.81</td><td>8.98</td><td>32.19</td></tr><tr><td>90</td><td>5.54</td><td>41.25</td><td>7.24</td><td>27.06</td></tr><tr><td>100</td><td>5.63</td><td>38.85</td><td>7.32</td><td>23.34</td></tr></table>{{< /table-caption >}}

> The table presents the performance of various LLMs and decoding methods on several faithfulness evaluation tasks, highlighting the best performing model for each task and model size.


{{< table-caption caption="🔽 Table 10: Performance comparison of Llama3-8B-Instruct with different numbers of masked random heads on MuSiQue, a multi-hop reasoning dataset, with and without CoT prompting in both closed-book and open-book settings." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Random Heads</td><td colspan="2">MuSiQue without CoT</td><td colspan="2">MuSiQue with CoT</td></tr><tr><td>Closed Book</td><td>Open Book</td><td>Closed Book</td><td>Open Book</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>7.41</td><td>58.83</td><td>14.61</td><td>69.84</td></tr><tr><td>10</td><td>7.09 士0.24</td><td>59.25 士0.53</td><td>14.63 ±0.35</td><td>69.70 ±1.81</td></tr><tr><td>20</td><td>7.17 士0.10</td><td>58.67 ±0.68</td><td>14.44 ±0.68</td><td>67.94 ±0.81</td></tr><tr><td>30</td><td>6.90 士0.19</td><td>57.23 ±1.32</td><td>14.09 士1.30</td><td>67.19 士2.42</td></tr><tr><td>40</td><td>6.61 ±0.02</td><td>55.83 士2.82</td><td>13.57 士1.09</td><td>64.27 士4.28</td></tr><tr><td>50</td><td>6.08 ±0.41</td><td>55.65 士3.12</td><td>12.84 ±1.10</td><td>64.87 士2.34</td></tr><tr><td>60</td><td>5.76 士0.77</td><td>54.64 士3.36</td><td>12.49 士1.06</td><td>63.65 士2.38</td></tr><tr><td>70</td><td>5.43 ±0.80</td><td>53.28 士3.66</td><td>11.20 ±1.34</td><td>61.40 士3.96</td></tr><tr><td>80</td><td>5.27 士0.77</td><td>52.19 士2.95</td><td>10.22 ±0.49</td><td>55.98 士3.28</td></tr><tr><td>90</td><td>5.46 ±0.72</td><td>49.25 ±4.41</td><td>8.14 士1.92</td><td>46.59 士8.97</td></tr><tr><td>100</td><td>5.25 士0.46</td><td>48.34 士5.71</td><td>7.43 士2.04</td><td>44.79 士9.19</td></tr></table>{{< /table-caption >}}

> This table presents the performance comparison of Llama3-8B-Instruct model on MuSiQue with different numbers of masked random heads, both with and without CoT prompting in closed-book and open-book settings.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='5' style='font-size:14px'><tr><td>Model</td><td>%Reject ↓</td><td>%T n R ↑</td><td>%I n R</td><td>%T nIn R↑</td></tr><tr><td>Llama3-8b-Instruct</td><td>43.94</td><td>65.50</td><td>94.54</td><td>60.04</td></tr><tr><td>+ ITI (Li et al., 2024b)</td><td>25.46</td><td>83.25</td><td>96.06</td><td>79.47</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>45.04</td><td>64.81</td><td>94.65</td><td>59.69</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>44.92</td><td>65.11</td><td>93.78</td><td>58.89</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>43.82</td><td>65.14</td><td>94.55</td><td>59.69</td></tr><tr><td>+ DeCoRe static (Ours)</td><td>41.74</td><td>67.02</td><td>95.38</td><td>62.39</td></tr><tr><td>+ DeCoRe entropy (Ours)</td><td>38.68</td><td>65.87</td><td>95.61</td><td>61.48</td></tr><tr><td>Llama3-70b-Instruct</td><td>53.12</td><td>76.50</td><td>97.91</td><td>74.41</td></tr><tr><td>+ CD (Li et al., 2023)</td><td>52.26</td><td>75.64</td><td>97.69</td><td>73.33</td></tr><tr><td>+ ITI (Li et al., 2024b)</td><td>37.94</td><td>71.79</td><td>98.82</td><td>70.81</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>52.88</td><td>76.62</td><td>97.92</td><td>74.55</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>54.71</td><td>76.22</td><td>97.30</td><td>73.51</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>49.33</td><td>75.36</td><td>98.31</td><td>73.67</td></tr><tr><td>+ DeCoRe static (Ours)</td><td>54.96</td><td>74.46</td><td>97.01</td><td>71.47</td></tr><tr><td>+ DeCoRe entropy (Ours)</td><td>56.79</td><td>75.35</td><td>96.32</td><td>71.67</td></tr><tr><td>+ DeCoRe entropy-small amateur (Ours)</td><td>52.02</td><td>75.77</td><td>97.70</td><td>73.47</td></tr></table>{{< /table-caption >}}

> The table presents a comparison of different LLMs and decoding methods on several faithfulness evaluation tasks, highlighting the best-performing models for each task.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='15' style='font-size:16px'><tr><td rowspan="2"></td><td rowspan="2">MuSiQue (Closed)</td><td rowspan="2">MuSiQue (Open)</td><td rowspan="2">Model</td><td colspan="2">T-test</td><td colspan="2">U-test</td></tr><tr><td>Statistics</td><td>p-value</td><td>Statistics</td><td>p-value</td></tr><tr><td>Correct</td><td>31.74</td><td>27.99</td><td>Baseline</td><td>11.75</td><td>2.57 x 10-31</td><td>4.31 x 105</td><td>8.36 x 10-26</td></tr><tr><td>Incorrect</td><td>43.91</td><td>33.32</td><td>DoLa</td><td>12.52</td><td>3.51 x 10-35</td><td>4.28 x 105</td><td>3.66 x 10-28</td></tr><tr><td></td><td></td><td></td><td>DeCoRe entropy</td><td>11.01</td><td>7.43 x 10-28</td><td>4.05 X 105</td><td>3.43 X 10-24</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different models and decoding methods on several faithfulness evaluation tasks, highlighting the best performing model for each task and model size.


{{< table-caption caption="🔽 Table 15: Ablation study of DeCoRe entropy on faithfulness hallucination tasks with varying numbers of masked random heads." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Random Heads</td><td colspan="3">XSum</td><td colspan="2">MemoTrap</td><td colspan="2">IFEval</td><td>NQ-Open</td><td>NQ-Swap</td></tr><tr><td>ROUGE-L ↑</td><td>BERTScore-F1 ↑</td><td>factKB ↑</td><td>Macro Acc ↑</td><td>Micro Acc ↑</td><td>Prompt Acc ↑</td><td>Instruct Acc ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>0 (Baseline)</td><td>19.90</td><td>67.23</td><td>47.61</td><td>65.86</td><td>64.40</td><td>70.24</td><td>78.30</td><td>69.68</td><td>60.62</td></tr><tr><td>10</td><td>20.02 ±0.12</td><td>67.43 ±0.31</td><td>51.39 士5.67</td><td>69.38 ±2.70</td><td>68.08 ±2.75</td><td>68.52 ±0.75</td><td>76.82 ±0.82</td><td>69.27 ±0.24</td><td>59.65 ±0.47</td></tr><tr><td>20</td><td>20.09 ±0.26</td><td>67.64 ±0.37</td><td>54.13 士5.85</td><td>68.22 ±4.61</td><td>66.68 士5.76</td><td>±1.49 65.31</td><td>74.46 ±0.95</td><td>69.30 ±0.66</td><td>59.49 ±1.93</td></tr><tr><td>30</td><td>20.06 ±0.11</td><td>67.78 ±0.53</td><td>56.00 ±7.34</td><td>69.29 ±3.91</td><td>68.77 ±4.88</td><td>64.76 ±1.87</td><td>74.26 ±1.63</td><td>69.11 ±0.49</td><td>58.91 ±2.61</td></tr><tr><td>40</td><td>20.07 ±0.23</td><td>67.76 ±0.54</td><td>56.78 ±9.68</td><td>71.09 ±0.71</td><td>70.72 ±1.56</td><td>64.94 ±1.34</td><td>74.38 ±1.39</td><td>69.23 ±0.60</td><td>61.23 ±5.48</td></tr><tr><td>50</td><td>20.08 ±0.36</td><td>67.89 ±0.50</td><td>57.37 ±8.45</td><td>69.69 ±2.14</td><td>69.07 ±3.18</td><td>64.08 ±1.99</td><td>73.78 ±1.80</td><td>69.13 ±0.53</td><td>61.33 ±4.92</td></tr><tr><td>60</td><td>20.09 ±0.47</td><td>67.99 ±0.61</td><td>57.87 ±6.37</td><td>70.52 ±1.89</td><td>70.17 ±1.18</td><td>60.51 士2.63</td><td>70.78 士1.92</td><td>69.23 ±0.56</td><td>62.23 ±2.77</td></tr><tr><td>70</td><td>19.83 ±0.47</td><td>67.96 ±0.54</td><td>60.16 ±6.49</td><td>70.96 ±2.19</td><td>70.76 ±1.90</td><td>60.14 ±0.21</td><td>70.90 ±0.42</td><td>69.19 ±0.33</td><td>62.03 ±3.23</td></tr><tr><td>80</td><td>19.71 ±0.44</td><td>67.85 ±0.49</td><td>60.00 ±5.13</td><td>69.47 ±1.68</td><td>68.94 ±0.94</td><td>58.96 ±1.44</td><td>69.46 ±1.23</td><td>68.76 ±0.36</td><td>60.89 ±5.05</td></tr><tr><td>90</td><td>19.75 ±0.34</td><td>67.78 ±0.52</td><td>59.04 ±4.80</td><td>66.91 ±2.68</td><td>66.63 ±3.58</td><td>59.64 士1.20</td><td>69.94 ±0.45</td><td>68.59 ±0.59</td><td>59.62 士5.86</td></tr><tr><td>100</td><td>19.68 ±0.45</td><td>67.82 ±0.50</td><td>59.03 ±3.41</td><td>67.27 士2.01</td><td>66.76 ±2.80</td><td>59.02 ±1.23</td><td>69.62 ±1.08</td><td>68.15 ±0.76</td><td>59.27 ±5.37</td></tr></table>{{< /table-caption >}}

> This table presents the results of an ablation study on the DeCoRe entropy method, varying the number of masked random heads on faithfulness evaluation tasks.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Retrieval Heads</td><td colspan="3">TruthfulQA (MC)</td><td>TriviaQA</td><td>PopQA</td><td>NQ-Open</td></tr><tr><td>MC1 ↑</td><td>MC2 ↑</td><td>MC3↑</td><td>EM ↑</td><td>EM↑</td><td>EM ↑</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>39.41</td><td>55.69</td><td>30.31</td><td>56.58</td><td>26.64</td><td>29.04</td></tr><tr><td>10</td><td>37.45</td><td>53.76</td><td>28.48</td><td>56.40</td><td>26.88</td><td>28.96</td></tr><tr><td>20</td><td>36.96</td><td>54.46</td><td>28.95</td><td>56.18</td><td>26.74</td><td>28.55</td></tr><tr><td>30</td><td>37.58</td><td>53.76</td><td>29.38</td><td>55.14</td><td>26.28</td><td>27.42</td></tr><tr><td>40</td><td>36.23</td><td>53.62</td><td>29.34</td><td>54.73</td><td>25.97</td><td>27.91</td></tr><tr><td>50</td><td>37.70</td><td>54.66</td><td>29.82</td><td>53.99</td><td>25.55</td><td>27.27</td></tr><tr><td>60</td><td>37.21</td><td>54.50</td><td>30.21</td><td>53.72</td><td>25.39</td><td>27.01</td></tr><tr><td>70</td><td>36.96</td><td>55.05</td><td>30.35</td><td>52.84</td><td>24.99</td><td>26.44</td></tr><tr><td>80</td><td>38.43</td><td>55.86</td><td>30.95</td><td>52.19</td><td>24.76</td><td>26.44</td></tr><tr><td>90</td><td>37.70</td><td>55.32</td><td>30.30</td><td>52.29</td><td>24.85</td><td>26.70</td></tr><tr><td>100</td><td>36.60</td><td>54.10</td><td>29.61</td><td>52.21</td><td>25.09</td><td>26.55</td></tr><tr><td rowspan="11">Llama3-70B-Instruct</td><td>Baseline</td><td>49.57</td><td>70.60</td><td>37.85</td><td>74.77</td><td>40.63</td><td>40.08</td></tr><tr><td>10</td><td>49.94</td><td>70.66</td><td>38.11</td><td>74.75</td><td>40.58</td><td>40.30</td></tr><tr><td>20</td><td>50.31</td><td>70.93</td><td>38.35</td><td>74.67</td><td>40.46</td><td>40.23</td></tr><tr><td>30</td><td>50.43</td><td>71.76</td><td>39.65</td><td>74.57</td><td>40.51</td><td>40.11</td></tr><tr><td>40</td><td>50.80</td><td>71.54</td><td>39.33</td><td>74.58</td><td>40.49</td><td>40.08</td></tr><tr><td>50</td><td>52.14</td><td>72.17</td><td>40.36</td><td>74.72</td><td>40.44</td><td>40.15</td></tr><tr><td>60</td><td>52.88</td><td>72.45</td><td>41.64</td><td>74.51</td><td>40.30</td><td>40.26</td></tr><tr><td>70</td><td>53.98</td><td>73.44</td><td>42.55</td><td>74.61</td><td>40.38</td><td>40.45</td></tr><tr><td>80</td><td>53.61</td><td>72.98</td><td>41.79</td><td>74.65</td><td>40.49</td><td>40.30</td></tr><tr><td>90</td><td>52.88</td><td>72.61</td><td>41.71</td><td>74.60</td><td>40.58</td><td>40.38</td></tr><tr><td>100</td><td>54.10</td><td>72.96</td><td>42.86</td><td>74.64</td><td>40.49</td><td>40.45</td></tr></table>{{< /table-caption >}}

> The table presents a comparison of different LLMs and decoding methods on various faithfulness evaluation tasks, highlighting the best-performing model for each task and model.


{{< table-caption caption="🔽 Table 7: Performance comparison of Llama3-8B-Instruct with different number of masked retrieval heads on factuality evaluation tasks." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Random Heads</td><td colspan="3">TruthfulQA (MC)</td><td>TriviaQA</td><td>PopQA</td><td>NQ-Open</td></tr><tr><td>MC1 ↑</td><td>MC2 ↑</td><td>MC3↑</td><td>EM ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>39.41</td><td>55.69</td><td>30.31</td><td>56.58</td><td>26.64</td><td>29.04</td></tr><tr><td>10</td><td>38.92 ±0.53</td><td>56.15 ±0.78</td><td>30.22 ±0.28</td><td>55.38 ±0.45</td><td>25.96 ±0.18</td><td>28.70 ±0.57</td></tr><tr><td>20</td><td>39.25 ±0.62</td><td>56.55 士2.07</td><td>30.93 ±0.85</td><td>54.68 ±0.68</td><td>25.63 ±0.25</td><td>28.02 ±0.53</td></tr><tr><td>30</td><td>39.41 ±1.28</td><td>56.43 士2.33</td><td>31.10 ±1.26</td><td>54.15 ±0.73</td><td>25.52 ±0.16</td><td>27.86 ±0.32</td></tr><tr><td>40</td><td>38.84 ±0.75</td><td>55.32 ±1.85</td><td>30.39 ±1.03</td><td>53.58 ±0.59</td><td>25.27 ±0.17</td><td>27.16 ±0.33</td></tr><tr><td>50</td><td>38.76 ±0.35</td><td>54.97 ±1.43</td><td>30.37 ±1.05</td><td>53.38 ±0.80</td><td>25.07 ±0.22</td><td>27.16 ±0.31</td></tr><tr><td>60</td><td>38.31 ±0.65</td><td>54.45 ±0.82</td><td>29.89 ±0.92</td><td>53.04 ±0.72</td><td>24.54 ±0.54</td><td>27.12 ±0.26</td></tr><tr><td>70</td><td>38.68 ±0.92</td><td>55.31 ±0.98</td><td>30.74 ±1.26</td><td>52.79 ±0.60</td><td>24.50 ±0.58</td><td>26.78 ±0.13</td></tr><tr><td>80</td><td>37.58 ±0.65</td><td>55.19 ±1.65</td><td>30.05 ±0.45</td><td>52.52 ±0.84</td><td>24.52 ±1.01</td><td>26.87 ±0.21</td></tr><tr><td>90</td><td>38.39 士2.22</td><td>56.48 ±3.06</td><td>30.82 士2.20</td><td>52.13 ±0.28</td><td>24.14 ±0.98</td><td>26.74 ±0.33</td></tr><tr><td>100</td><td>38.23 士2.70</td><td>56.66 士3.77</td><td>31.03 士2.72</td><td>51.60 ±0.35</td><td>24.05 ±0.76</td><td>26.43 ±0.51</td></tr></table>{{< /table-caption >}}

> The table shows the performance comparison of Llama3-8B-Instruct model with different numbers of masked retrieval heads on various factuality evaluation tasks, including TruthfulQA, TriviaQA, PopQA, and NQ-Open.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:16px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Retrieval Heads</td><td colspan="2">MuSiQue without CoT</td><td colspan="2">MuSiQue with C⌀T</td></tr><tr><td>Closed Book</td><td>Open Book</td><td>Closed Book</td><td>Open Book</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>7.41</td><td>58.83</td><td>14.61</td><td>69.84</td></tr><tr><td>10</td><td>7.61</td><td>61.98</td><td>13.90</td><td>74.47</td></tr><tr><td>20</td><td>7.70</td><td>61.81</td><td>13.82</td><td>72.20</td></tr><tr><td>30</td><td>7.70</td><td>61.44</td><td>13.61</td><td>71.70</td></tr><tr><td>40</td><td>7.03</td><td>61.32</td><td>13.03</td><td>72.16</td></tr><tr><td>50</td><td>7.12</td><td>61.32</td><td>12.78</td><td>71.62</td></tr><tr><td>60</td><td>6.50</td><td>60.36</td><td>13.03</td><td>72.11</td></tr><tr><td>70</td><td>6.21</td><td>59.21</td><td>12.83</td><td>71.66</td></tr><tr><td>80</td><td>5.75</td><td>58.05</td><td>12.29</td><td>71.74</td></tr><tr><td>90</td><td>6.04</td><td>59.54</td><td>12.49</td><td>70.87</td></tr><tr><td>100</td><td>6.45</td><td>59.78</td><td>11.96</td><td>71.00</td></tr><tr><td rowspan="11">Llama3-70B-Instruct</td><td>Baseline</td><td>11.79</td><td>68.56</td><td>20.15</td><td>74.43</td></tr><tr><td>10</td><td>11.75</td><td>69.22</td><td>20.60</td><td>74.76</td></tr><tr><td>20</td><td>11.67</td><td>69.05</td><td>20.02</td><td>74.56</td></tr><tr><td>30</td><td>11.50</td><td>68.97</td><td>20.31</td><td>74.43</td></tr><tr><td>40</td><td>11.63</td><td>69.05</td><td>20.23</td><td>74.22</td></tr><tr><td>50</td><td>11.34</td><td>69.38</td><td>20.02</td><td>73.60</td></tr><tr><td>60</td><td>11.34</td><td>68.68</td><td>19.69</td><td>73.85</td></tr><tr><td>70</td><td>11.34</td><td>69.38</td><td>19.40</td><td>74.06</td></tr><tr><td>80</td><td>11.25</td><td>69.67</td><td>19.28</td><td>74.18</td></tr><tr><td>90</td><td>11.38</td><td>69.51</td><td>19.53</td><td>74.47</td></tr><tr><td>100</td><td>11.25</td><td>69.84</td><td>19.69</td><td>74.93</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods on faithfulness evaluation tasks, highlighting the best-performing model and method for each task.


{{< table-caption caption="🔽 Table 19: Performance comparison across different numbers of masked random heads on MuSiQue, a multi-hop reasoning dataset, with and without CoT prompting in both closed-book and open-book settings." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">Masked Random Heads</td><td colspan="2">MuSiQue without CoT</td><td colspan="2">MuSiQue with CoT</td></tr><tr><td>Closed Book</td><td>Open Book</td><td>Closed Book</td><td>Open Book</td></tr><tr><td rowspan="11">Llama3-8B-Instruct</td><td>Baseline</td><td>7.41</td><td>58.83</td><td>14.61</td><td>69.84</td></tr><tr><td>10</td><td>6.63 士0.17</td><td>59.21 士0.91</td><td>13.57 士0.91</td><td>69.40 士1.09</td></tr><tr><td>20</td><td>6.87 ±0.14</td><td>59.72 ±0.70</td><td>13.07 ±0.90</td><td>70.18 ±0.44</td></tr><tr><td>30</td><td>6.65 ±0.44</td><td>59.95 ±0.77</td><td>12.61 ±0.91</td><td>70.43 ±1.47</td></tr><tr><td>40</td><td>6.22 ±0.42</td><td>60.52 ±1.69</td><td>12.29 ±0.40</td><td>70.28 士2.53</td></tr><tr><td>50</td><td>6.50 ±0.26</td><td>60.60 ±1.46</td><td>12.26 ±0.15</td><td>69.41 ±1.44</td></tr><tr><td>60</td><td>6.36 ±0.31</td><td>60.31 ±1.49</td><td>11.81 ±0.58</td><td>68.89 士0.95</td></tr><tr><td>70</td><td>6.32 ±0.06</td><td>61.03 ±0.97</td><td>12.05 士1.06</td><td>69.78 士1.56</td></tr><tr><td>80</td><td>6.45 ±0.54</td><td>61.32 ±0.50</td><td>11.64 士0.66</td><td>70.05 ±1.08</td></tr><tr><td>90</td><td>6.55 ±0.46</td><td>61.45 士1.38</td><td>11.65 士0.57</td><td>70.20 士2.17</td></tr><tr><td>100</td><td>6.34 ±0.27</td><td>61.76 ±0.90</td><td>11.72 士0.27</td><td>70.29 士2.36</td></tr></table>{{< /table-caption >}}

> This table presents the performance comparison of Llama3-8B-Instruct with different numbers of masked random heads on MuSiQue, a multi-hop reasoning task, with and without CoT prompting in both closed-book and open-book settings.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td rowspan="2">Model</td><td colspan="3">XSum</td><td colspan="2">MemoTrap</td><td colspan="2">IFEval</td><td>NQ-Open</td><td>NQ-Swap</td></tr><tr><td>ROUGE-L ↑</td><td>BERTScore-F1 ↑</td><td>factKB ↑</td><td>Macro Acc ↑</td><td>Micro Acc ↑</td><td>Prompt Acc ↑</td><td>Instruct Acc ↑</td><td>EM↑</td><td>EM↑</td></tr><tr><td>Mistral-7B-Instruct-v0.3</td><td>16.53</td><td>65.30</td><td>65.53</td><td>76.63</td><td>75.11</td><td>51.02</td><td>60.91</td><td>66.86</td><td>65.17</td></tr><tr><td>+ CAD (Shi et al., 2024)</td><td>14.71</td><td>63.55</td><td>69.90</td><td>-</td><td>-</td><td>-</td><td>-</td><td>65.54</td><td>76.11</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>16.45</td><td>65.24</td><td>65.51</td><td>76.33</td><td>74.75</td><td>49.54</td><td>60.19</td><td>67.01</td><td>65.32</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>16.44</td><td>65.23</td><td>65.70</td><td>76.47</td><td>74.91</td><td>49.72</td><td>60.19</td><td>66.97</td><td>65.21</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>16.58</td><td>65.36</td><td>65.25</td><td>76.80</td><td>75.35</td><td>51.76</td><td>62.35</td><td>66.70</td><td>63.99</td></tr><tr><td>+ DeCoRe static (Ours)</td><td>15.57</td><td>64.20</td><td>71.75</td><td>77.01</td><td>76.49</td><td>51.94</td><td>62.47</td><td>68.02</td><td>68.08</td></tr><tr><td>+ DeCoRe entropy (Ours)</td><td>15.15</td><td>63.80</td><td>70.73</td><td>77.54</td><td>76.96</td><td>51.20</td><td>61.27</td><td>68.48</td><td>68.61</td></tr><tr><td>Qwen2-7B-Instruct</td><td>20.00</td><td>67.70</td><td>68.66</td><td>82.13</td><td>80.54</td><td>52.31</td><td>62.35</td><td>68.81</td><td>72.90</td></tr><tr><td>+ CAD (Shi et al., 2024)</td><td>17.06</td><td>65.08</td><td>71.98</td><td></td><td></td><td></td><td></td><td>69.30</td><td>78.05</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>19.57</td><td>67.47</td><td>65.05</td><td>82.76</td><td>81.76</td><td>54.16</td><td>65.35</td><td>68.32</td><td>72.88</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>18.69</td><td>66.60</td><td>55.71</td><td>56.61</td><td>55.89</td><td>47.32</td><td>59.59</td><td>65.76</td><td>70.48</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>19.58</td><td>67.66</td><td>66.42</td><td>81.37</td><td>80.03</td><td>51.76</td><td>62.35</td><td>68.14</td><td>72.29</td></tr><tr><td>+ DeCoRe static (Ours)</td><td>18.78</td><td>66.82</td><td>75.21</td><td>82.50</td><td>81.02</td><td>58.04</td><td>67.51</td><td>70.13</td><td>75.64</td></tr><tr><td>+ DeCoRe entropy (Ours)</td><td>17.09</td><td>64.79</td><td>76.90</td><td>83.80</td><td>82.04</td><td>54.90</td><td>64.03</td><td>70.58</td><td>75.31</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods on multiple faithfulness evaluation tasks, highlighting the best-performing models and methods for each task.


{{< table-caption caption="🔽 Table 2: Performance of different models and decoding methods on factuality evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td rowspan="2">Model</td><td colspan="3">TruthfulQA (MC)</td><td>TriviaQA</td><td>PopQA</td><td colspan="4">TruthfulQA (Generation)</td><td>NQ-Open</td></tr><tr><td>MC1 ↑</td><td>MC2↑</td><td>MC3↑</td><td>EM↑</td><td>EM ↑</td><td>%Truth ↑</td><td>%Info ↑</td><td>%TnI↑</td><td>%Reject ↓</td><td>EM↑</td></tr><tr><td>Mistral-7B-Instruct-v0.3</td><td>50.31</td><td>65.62</td><td>38.29</td><td>59.99</td><td>26.65</td><td>80.54</td><td>97.06</td><td>77.60</td><td>26.07</td><td>31.49</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>50.18</td><td>65.64</td><td>38.17</td><td>60.06</td><td>26.68</td><td>80.29</td><td>97.31</td><td>77.60</td><td>25.70</td><td>31.53</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>50.18</td><td>65.61</td><td>38.18</td><td>60.03</td><td>26.68</td><td>80.54</td><td>97.06</td><td>77.60</td><td>25.70</td><td>31.53</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>43.82</td><td>64.44</td><td>35.67</td><td>59.92</td><td>26.66</td><td>80.29</td><td>97.18</td><td>77.48</td><td>25.70</td><td>30.55</td></tr><tr><td>+ DeCoRe static (Ours)</td><td>53.49</td><td>67.13</td><td>39.48</td><td>60.09</td><td>27.02</td><td>77.85</td><td>97.43</td><td>75.40</td><td>20.81</td><td>31.38</td></tr><tr><td>+ DeCoRe entropy (Ours)</td><td>54.84</td><td>69.08</td><td>41.82</td><td>59.64</td><td>27.11</td><td>76.99</td><td>97.80</td><td>74.79</td><td>15.91</td><td>31.45</td></tr><tr><td>Qwen2-7B-Instruct</td><td>29.99</td><td>48.08</td><td>24.22</td><td>42.77</td><td>17.55</td><td>80.78</td><td>67.93</td><td>48.71</td><td>37.33</td><td>25.91</td></tr><tr><td>+ DoLA (low) (Chuang et al., 2023)</td><td>30.11</td><td>49.11</td><td>25.09</td><td>40.57</td><td>15.85</td><td>84.58</td><td>65.36</td><td>50.06</td><td>41.74</td><td>23.84</td></tr><tr><td>+ DoLA (high) (Chuang et al., 2023)</td><td>20.44</td><td>47.09</td><td>22.76</td><td>37.82</td><td>13.84</td><td>83.97</td><td>61.57</td><td>45.53</td><td>45.17</td><td>21.36</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>30.85</td><td>49.71</td><td>25.33</td><td>42.13</td><td>18.19</td><td>78.09</td><td>79.68</td><td>57.83</td><td>26.31</td><td>24.41</td></tr><tr><td>+ DeCoRe static (Ours)</td><td>31.09</td><td>48.23</td><td>25.20</td><td>42.50</td><td>17.71</td><td>79.31</td><td>69.28</td><td>48.59</td><td>37.33</td><td>26.06</td></tr><tr><td>+ DeCoRe entropy (Ours)</td><td>34.52</td><td>51.79</td><td>27.30</td><td>41.30</td><td>17.15</td><td>76.87</td><td>76.74</td><td>53.61</td><td>26.81</td><td>25.05</td></tr></table>{{< /table-caption >}}

> Table 2 presents the performance comparison of different LLMs and decoding methods on various factuality evaluation tasks, highlighting the best-performing models and methods for each task.


{{< table-caption caption="🔽 Table 22: Performance comparison of other model families (i.e., Mistral-7B-Instruct-v0.3 and Qwen2-7B-Instruct) with different decoding strategies on MuSiQue, a multi-hop reasoning task. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td colspan="2">MuSiQue without CoT</td><td colspan="2">MuSiQue with CoT</td></tr><tr><td>Closed Book</td><td>Open Book</td><td>Closed Book</td><td>Open Book</td></tr><tr><td>Mistral-7B-Instruct-v0.3</td><td>7.61</td><td>58.01</td><td>11.17</td><td>59.70</td></tr><tr><td>+ CAD (Shi et al., 2024)</td><td>-</td><td>50.10</td><td>-</td><td>63.55</td></tr><tr><td>+ DoLA (low)</td><td>7.53</td><td>58.21</td><td>10.92</td><td>59.79</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>7.53</td><td>59.00</td><td>11.34</td><td>61.69</td></tr><tr><td>+ DeCoRe static</td><td>7.86</td><td>59.33</td><td>12.04</td><td>63.92</td></tr><tr><td>+ DeCoRe entropy</td><td>7.57</td><td>62.72</td><td>11.21</td><td>65.12</td></tr><tr><td>Qwen2-7B-Instruct</td><td>6.54</td><td>63.01</td><td>8.23</td><td>60.57</td></tr><tr><td>+ CAD (Shi et al., 2024)</td><td>-</td><td>64.58</td><td>-</td><td>66.41</td></tr><tr><td>+ DoLA (low)</td><td>7.03</td><td>65.45</td><td>7.70</td><td>64.54</td></tr><tr><td>+ AD (Chen et al., 2024)</td><td>5.71</td><td>65.29</td><td>8.44</td><td>65.70</td></tr><tr><td>+ DeCoRe static</td><td>6.70</td><td>63.34</td><td>8.36</td><td>66.78</td></tr><tr><td>+ DeCoRe entropy</td><td>6.16</td><td>66.49</td><td>8.23</td><td>67.98</td></tr></table>{{< /table-caption >}}

> This table presents the performance comparison of different models and decoding strategies on the MuSiQue multi-hop reasoning dataset, showing the impact of different decoding methods on the accuracy of different models in this task.


{{< table-caption caption="🔽 Table 23: Performance of Llama3-8b-Instruct with DeCoRestatic on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='5' style='font-size:16px'><tr><td rowspan="2">a</td><td colspan="3">XSum</td><td colspan="2">MemoTrap</td><td colspan="2">IFEval</td><td>NQ-Open</td><td>NQ-Swap</td></tr><tr><td>ROUGE-L ↑</td><td>BERTScore-F1 ↑</td><td>factKB ↑</td><td>Macro Acc ↑</td><td>Micro Acc ↑</td><td>Instruct Acc ↑</td><td>Prompt Acc ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td>-0.5</td><td>20.16</td><td>66.42</td><td>28.17</td><td>63.52</td><td>60.65</td><td>76.98</td><td>68.58</td><td>68.17</td><td>55.75</td></tr><tr><td>0.0</td><td>19.90</td><td>67.23</td><td>47.61</td><td>65.86</td><td>64.40</td><td>70.24</td><td>78.30</td><td>69.68</td><td>60.62</td></tr><tr><td>0.5</td><td>19.87</td><td>67.83</td><td>64.07</td><td>69.53</td><td>69.20</td><td>69.13</td><td>78.06</td><td>70.62</td><td>64.43</td></tr><tr><td>1.0</td><td>19.41</td><td>67.83</td><td>67.46</td><td>69.71</td><td>70.22</td><td>73.74</td><td>63.59</td><td>70.73</td><td>64.88</td></tr><tr><td>2.0</td><td>18.38</td><td>67.19</td><td>64.02</td><td>71.28</td><td>71.84</td><td>70.74</td><td>59.70</td><td>69.64</td><td>63.02</td></tr><tr><td>4.0</td><td>16.65</td><td>65.26</td><td>52.61</td><td>70.77</td><td>71.09</td><td>51.56</td><td>37.52</td><td>62.86</td><td>54.83</td></tr><tr><td>8.0</td><td>13.05</td><td>55.65</td><td>31.34</td><td>70.68</td><td>70.97</td><td>35.01</td><td>20.70</td><td>43.24</td><td>39.97</td></tr></table>{{< /table-caption >}}

> The table shows the performance of Llama3-8b-Instruct model with DeCoRestatic decoding method on faithfulness evaluation tasks using different values of hyperparameter alpha.


{{< table-caption caption="🔽 Table 24: Performance of Llama3-8b-Instruct with DeCoRestatic on factuality evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td rowspan="2">a</td><td colspan="3">TruthfulQA (MC)</td><td>TriviaQA</td><td>PopQA</td><td>NQ-Open</td></tr><tr><td>MC1 ↑</td><td>MC2 ↑</td><td>MC3 ↑</td><td>EM ↑</td><td>EM ↑</td><td>EM ↑</td></tr><tr><td>-0.5</td><td>38.31</td><td>57.05</td><td>31.48</td><td>56.00</td><td>26.09</td><td>28.93</td></tr><tr><td>0.0</td><td>39.41</td><td>55.69</td><td>30.31</td><td>56.58</td><td>26.64</td><td>29.04</td></tr><tr><td>0.5</td><td>38.68</td><td>55.74</td><td>29.80</td><td>56.93</td><td>26.86</td><td>29.42</td></tr><tr><td>1.0</td><td>38.07</td><td>55.86</td><td>29.81</td><td>56.78</td><td>26.87</td><td>28.93</td></tr><tr><td>2.0</td><td>36.84</td><td>56.13</td><td>30.08</td><td>56.47</td><td>26.60</td><td>28.59</td></tr><tr><td>4.0</td><td>37.45</td><td>57.62</td><td>31.43</td><td>53.92</td><td>24.55</td><td>28.14</td></tr><tr><td>8.0</td><td>37.70</td><td>58.37</td><td>31.82</td><td>43.67</td><td>18.66</td><td>23.47</td></tr></table>{{< /table-caption >}}

> The table presents the performance of Llama3-8b-Instruct with DeCoRestatic on factuality evaluation tasks with varying scaling factor (α).


{{< table-caption caption="🔽 Table 1. Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">a</td><td colspan="2">MuSiQue without CoT</td><td colspan="2">MuSiQue with CoT</td></tr><tr><td>Closed Book ↑</td><td>Open Book ↑</td><td>Closed Book ↑</td><td>Open Book ↑</td></tr><tr><td>-0.5</td><td>6.95</td><td>55.94</td><td>14.56</td><td>66.32</td></tr><tr><td>0.0</td><td>11.79</td><td>68.56</td><td>20.15</td><td>74.43</td></tr><tr><td>0.5</td><td>11.79</td><td>69.76</td><td>20.60</td><td>75.05</td></tr><tr><td>1.0</td><td>8.27</td><td>62.27</td><td>14.19</td><td>72.07</td></tr><tr><td>2.0</td><td>7.12</td><td>60.57</td><td>11.67</td><td>70.09</td></tr><tr><td>4.0</td><td>4.18</td><td>52.92</td><td>7.36</td><td>58.46</td></tr><tr><td>8.0</td><td>2.52</td><td>33.88</td><td>5.01</td><td>31.36</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods on various faithfulness evaluation tasks, highlighting the best-performing method for each model.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:14px'><tr><td>Task</td><td>Metric</td><td># of shots</td><td>Prompt Template</td></tr><tr><td colspan="4">Faithfulness Hallucination</td></tr><tr><td>XSum</td><td>ROUGE-L BERTScore factKB</td><td>0</td><td>Generate a summary comprising of 1 sentence for the given article. \n\n Article: " + {{document}}\n\nSummary:</td></tr><tr><td>MemoTrap</td><td>Macro Accuracy Micro Accuracy</td><td>0</td><td>{{question}}</td></tr><tr><td>IFEval</td><td>Instruction-level Strict Accuracy Prompt-level Strict Accuracy</td><td>0</td><td>{{question}}</td></tr><tr><td>Open Book NQ-Open</td><td>EM</td><td>1</td><td>Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant). Provide the answer in 5 words or less without any explanation. \n\n {{in-context learning demonstrations}}\n\n Document [{{document_index}}] {{document}}\n Question: {{question}}\n Answer:</td></tr><tr><td>NQ-Swap</td><td>EM</td><td>4</td><td>Answer the following question based on the provided context:\n\n {{in-context learning demonstrations}}\n\n Context: {{context}}\n Question: {{question}} \n Answer:</td></tr><tr><td colspan="4">Factuality Hallucination</td></tr><tr><td>Closed-Book NQ-Open</td><td>EM</td><td>8</td><td>Write a high-quality answer for the given question. Provide the answer in 5 words or less without any explanation. \n\n {{in-context learning demonstrations}}\n\n Question: {{question}}\n Answer:</td></tr><tr><td>TriviaQA</td><td>EM</td><td>8</td><td>Answer the given question.\n\n {{in-context learning demonstrations}}\n\n Question: {{question}} In Answer:</td></tr><tr><td>PopQA</td><td>EM</td><td>8</td><td>Answer the given question. \n\n {{in-context learning demonstrations}}\n\n Question: {{question}}\n Answer:</td></tr><tr><td>TruthfulQA</td><td>MC1 MC2 MC3 GPT-Judge GPT-Info</td><td>6</td><td>Interpret each question literally, and as a question about the real world; carefully research each answer, without falling prey to any common myths; and reply "I have no comment" unless you are completely certain of the answer. \n\n {{in-context learning demonstrations}}\n\n Q: {{question}}\n A:</td></tr><tr><td colspan="4">Reasoning</td></tr><tr><td>MuSiQue Direct</td><td>EM</td><td>17</td><td>Answer the following question. \n\n {{in-context learning demonstrations}}\n\n Q: {{question}}\n Answer:</td></tr><tr><td>MuSiQue CoT</td><td>EM</td><td>17</td><td>Answer the following question by reasoning step-by-step.\n\n {{in-context learning demonstrations}}\n\n Q: {{question}}\n Answer:</td></tr></table>{{< /table-caption >}}

> The table presents the performance comparison of different LLMs and decoding methods on multiple faithfulness evaluation tasks, highlighting the best-performing model for each task and base model.


{{< table-caption caption="🔽 Table 1: Performance of different models and decoding methods on faithfulness evaluation tasks. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='2' style='font-size:16px'><tr><td>Question</td><td>Answer</td><td>Reason of Removal</td></tr><tr><td>What genre is the record label of the performer of So Long, See You Tomorrow associated with?</td><td>The performer of So Long, See You Tomorrow is Bombay Bicycle Club. The record label of Bombay Bicy- cle Club is Island Records. The genre of Island Records is jazz. So the answer is: jazz.</td><td>A record label does not have only one specific genre, as confirmed by a Wikipedia search of Is- land Records.</td></tr><tr><td>What is the genre of the record label of the band that performed on the Crush Tour?</td><td>The Crush Tour is performed by the band Bon Jovi. The record label of Bon Jovi is Island Records. The genre of Island Records is jazz. So the answer is: jazz.</td><td>A record label does not have only one specific genre, as confirmed by a Wikipedia search of Is- land Records.</td></tr><tr><td>Where is the crying stone found in the coun- try in which Raphael Tuju holds citizenship?</td><td>Raphael Tuju is a citizen of Kenya. The crying stone in Kenya is found along the highway towards Kisumu. So the answer is: along the highway towards Kisumu.</td><td>The second passage al- ready contains the an- swer as standalone evi- dence. It does not high- light the multi-hop rea- soning.</td></tr></table>{{< /table-caption >}}

> The table presents the performance of different LLMs and decoding methods on various faithfulness evaluation tasks, highlighting the best-performing model and method for each task.


{{< table-caption caption="🔽 Table 3: Performance of different models and decoding methods on MuSiQue, a multi-hop reasoning dataset, with and without CoT prompting in both closed-book and open-book settings. For each base model, the best performance is indicated in bold, and the second-best is underlined." >}}
<table id='4' style='font-size:14px'><tr><td rowspan="2">Model</td><td rowspan="2">XSum</td><td colspan="2">MuSiQue with CoT</td></tr><tr><td>Closed</td><td>Open</td></tr><tr><td>Llama3-8b-Instruct</td><td>0.41 ±0.12</td><td>0.30 士0.10</td><td>0.43 士0.20</td></tr><tr><td>+ ITI</td><td>0.65 ±0.21</td><td>0.46 士0.18</td><td>0.72 士0.28</td></tr><tr><td>+ DoLa</td><td>0.41 ±0.12</td><td>0.30 ±0.10</td><td>0.43 ±0.20</td></tr><tr><td>+ DeCoRe entropy</td><td>0.38 士0.11</td><td>0.29 士0.10</td><td>0.41 士0.20</td></tr></table>{{< /table-caption >}}

> This table presents the performance comparison of different models and decoding methods on the MuSiQue dataset, a multi-hop reasoning task, with and without Chain-of-Thought (CoT) prompting in both closed-book and open-book settings.


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
{{< /gallery >}}