---
title: "Teaching Models to Balance Resisting and Accepting Persuasion"
summary: "LLMs can now better resist manipulation while also learning from helpful advice, thanks to a new training method that balances resisting misinformation with accepting helpful persuasion!"
categories: ["AI Generated"]
tags: ["🔖 24-10-18", "🤗 24-10-21"]
showSummary: true
date: 2024-10-18
draft: false
---

### TL;DR


{{< lead >}}

Large language models (LLMs) are susceptible to manipulation.  This paper introduces Persuasion-Balanced Training (PBT), a novel method that trains LLMs to both resist harmful persuasion and accept helpful persuasion.  PBT uses multi-agent recursive dialogue trees to create training data, teaching models to assess when persuasion is beneficial or harmful.  Results show PBT improves resistance to misinformation and resilience to challenges, leading to better overall performance than models focused solely on resisting or accepting persuasion.  Crucially, PBT enhances collaboration in multi-agent settings by reducing the impact of the order in which models present arguments. The study also found that model decisions are primarily driven by the plausibility of the alternative answer, rather than its perceived confidence.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.14596" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This research paper explores how large language models (LLMs) can be made more resilient to manipulation while also being more receptive to helpful suggestions.  It introduces a novel training method to improve the balance between resisting misinformation and accepting beneficial persuasion.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} A novel training method, Persuasion-Balanced Training (PBT), improves LLMs' ability to both resist misinformation and accept helpful suggestions. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} PBT models are more stable and less prone to order effects in multi-agent dialogues compared to models trained to only resist or only accept persuasion. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The model's decision to accept or reject persuasion is primarily driven by the plausibility of the alternative answer, not confidence levels. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_4_0.png "🔼 Figure 1: Resisting negative persuasion and accepting positive persuasion are both needed for productive dialogues. However, only optimizing one or the other can lead to overcorrection. We argue that the two must be balanced, i.e. the agent should resist and accept persuasion when appropriate.")

> The figure illustrates the importance of balancing resisting negative persuasion with accepting positive persuasion in large language models for productive dialogues.





![](charts/charts_7_0.png "🔼 Figure 3: Accuracy of a team after discussion. A strong model (Llama 3.1 70B) paired with a weaker model (Llama 3.1 8B) leads to order dependence. Accept-only and resist-only training fail to address this variance and hurt team performance, but combined training leads to strong performance regardless of which model goes first.")

> The chart displays the impact of different training methods (base, accept-only, resist-only, and PBT) on the performance of multi-agent teams composed of a strong and a weak model, showing how the order of speakers affects the outcome and how PBT training mitigates this effect.





{{< table-caption caption="🔽 Table 1: Rate at which models adopt misinformation across different datasets (lower is better). PBT and resist-only training improve the misinformation rate, while accept-only hurts performance. Other models in Table 5." >}}
<table id='0' style='font-size:20px'><tr><td>model</td><td>NQ1</td><td>NQ2</td><td>Boolq</td><td>TruthfulQA</td><td>Avg.</td></tr><tr><td>Llama-3.1-70B</td><td>75.95± 0.29</td><td>56.88± 0.42</td><td>71.99± 0.60</td><td>38.47± 2.32</td><td>60.82± 0.82</td></tr><tr><td>+ accept</td><td>79.28± 9.98</td><td>85.68± 7.52</td><td>90.51± 4.32</td><td>87.62± 5.93</td><td>85.78± 2.09</td></tr><tr><td>+ resist</td><td>22.45± 37.12</td><td>9.16± 14.82</td><td>26.53± 5.54</td><td>2.41± 2.51</td><td>15.13± 13.55</td></tr><tr><td>+ PBT</td><td>9.63± 3.74</td><td>16.13± 4.10</td><td>37.45± 13.71</td><td>27.54± 8.13</td><td>22.69± 4.02</td></tr></table>{{< /table-caption >}}

> Table 1 presents the rate at which different language models adopt misinformation across various datasets, comparing the performance of models trained with persuasion-balanced training (PBT), resist-only training, accept-only training, and no training.



### More visual insights




<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Flipflopping evaluation using Laban et al. (2023)'s 'Are you sure?' prompt. PBT leads to less flipflopping. Full results in Appendix A." >}}
<table id='2' style='font-size:14px'><tr><td>Model</td><td>Before</td><td>After</td><td>Diff.</td></tr><tr><td>Llama-3.1-70B</td><td>73.10± 0.00</td><td>40.10± 0.00</td><td>-33.00</td></tr><tr><td>+ accept</td><td>65.20± 3.25</td><td>55.70± 5.95</td><td>-9.50</td></tr><tr><td>+ resist</td><td>43.87± 27.80</td><td>43.47± 26.70</td><td>-0.40</td></tr><tr><td>+ PBT</td><td>73.17± 2.53</td><td>73.40± 2.52</td><td>0.23</td></tr></table>{{< /table-caption >}}

> Table 2 shows the accuracy of different models using the “Are you sure?” prompt from Laban et al. (2023), measuring the rate at which models flip their answers when challenged.


{{< table-caption caption="🔽 Table 3: Accuracy on balanced persuasion data, where half of the examples involve flipping a correct answer to an incorrect one (+ → -) and the other half involve flipping an incorrect answer to a correct one (- → +). Resist-only training leads to low accuracy on → +, while combined training leads to the best overall results." >}}
<br><table id='8' style='font-size:14px'><tr><td>Model</td><td>+ → -</td><td>- → +</td><td>Overall</td></tr><tr><td>Mistral-7B</td><td>25.28± 0.00</td><td>65.60± 0.00</td><td>45.44± 0.00</td></tr><tr><td>+ accept</td><td>20.88± 0.86</td><td>62.57± 3.65</td><td>41.72± 1.44</td></tr><tr><td>+ resist</td><td>64.69± 10.18</td><td>22.40± 4.73</td><td>43.55± 7.40</td></tr><tr><td>+ PBT</td><td>53.00± 1.99</td><td>59.23± 6.29</td><td>56.11± 4.14</td></tr><tr><td>Llama-3.1-8B</td><td>27.11± 0.00</td><td>59.23± 0.00</td><td>43.17± 0.00</td></tr><tr><td>+ accept</td><td>27.64± 5.87</td><td>57.40± 10.32</td><td>42.52± 7.54</td></tr><tr><td>+ resist</td><td>54.67± 6.98</td><td>19.44± 0.73</td><td>37.05±3.68</td></tr><tr><td>+ PBT</td><td>61.73± 6.13</td><td>60.21± 0.47</td><td>60.97± 3.30</td></tr><tr><td>Llama-3.1-70B</td><td>54.52± 1.52</td><td>61.50± 1.37</td><td>58.01±0.17</td></tr><tr><td>+ accept</td><td>41.69± 10.05</td><td>66.21± 6.46</td><td>53.95± 8.00</td></tr><tr><td>+ resist</td><td>50.72± 16.53</td><td>13.67± 6.17</td><td>32.19± 11.31</td></tr><tr><td>+ PBT</td><td>80.41±3.36</td><td>68.72±3.50</td><td>74.56± 2.73</td></tr></table>{{< /table-caption >}}

> Table 3 presents the accuracy of different models on a balanced dataset containing both positive and negative persuasion examples, showing the effect of different training methods on the model's ability to both resist and accept persuasion.


{{< table-caption caption="🔽 Table 1: Rate at which models adopt misinformation across different datasets (lower is better). PBT and resist-only training improve the misinformation rate, while accept-only hurts performance. Other models in Table 5." >}}
<br><table id='4' style='font-size:14px'><tr><td>Ans. H</td><td>log Porig.</td><td>log Palt.</td><td>Conf.orig.</td><td>Conf.alt.</td><td>Acc.</td></tr><tr><td>-0.64</td><td>0.36*</td><td>-0.36*</td><td>-0.23</td><td>0.06</td><td>0.15</td></tr></table>{{< /table-caption >}}

> Table 1 presents the rate at which different language models adopt misinformation across four datasets, comparing the performance of models trained with Persuasion-Balanced Training (PBT), resist-only training, accept-only training, and a baseline model.


{{< table-caption caption="🔽 Table 1: Rate at which models adopt misinformation across different datasets (lower is better). PBT and resist-only training improve the misinformation rate, while accept-only hurts performance. Other models in Table 5." >}}
<br><table id='8' style='font-size:14px'><tr><td>Agent 2: I apologize for my earlier response being partially correct but also partially outdated. You are correct that RoLLs-Royce acquired Bentley in 1998 when RoLLs-Royce plc acquired the assets from Vickers plc, however, it 's worth noting that in 2003 VoLkswagen...</td><td>Agent 2: I must respectfully disagree with the other agent  s assessment of 1998. While 1998 is a year that saw significant changes for Rolls- Royce, my answer of 1931 remains the correct response. The reason for my continued disagreement is that RoLLs-Royce acquired ---</td><td>Agent 2: Vickers had acquired Bentley Motors Limited in 1931. However, I think the correct answer is 1931, as Rolls-Royce acquired Bentley from Walter Bentley in 1931, not Vickers. Therefore, my answer is 1931. I 'm just more confident in my answer...</td></tr></table>{{< /table-caption >}}

> Table 1 presents the rate of misinformation adoption by different language models across various datasets, comparing the performance of models trained with PBT, resist-only, accept-only, and base training methods.


{{< table-caption caption="🔽 Table 1: Rate at which models adopt misinformation across different datasets (lower is better). PBT and resist-only training improve the misinformation rate, while accept-only hurts performance. Other models in Table 5." >}}
<table id='0' style='font-size:20px'><tr><td>Model</td><td>NQ1</td><td>NQ2</td><td>Boolq</td><td>TruthfulQA</td><td>Avg.</td></tr><tr><td>Mistral 7B v0.2</td><td>51.08± 2.54</td><td>51.98± 1.65</td><td>41.75± 2.38</td><td>31.12± 2.09</td><td>43.98± 0.34</td></tr><tr><td>+ accept</td><td>58.85± 13.25</td><td>89.68± 5.51</td><td>62.73± 20.30</td><td>62.86± 11.24</td><td>68.53± 5.29</td></tr><tr><td>+ resist</td><td>14.67 + 12.69</td><td>16.97 + 19.95</td><td>22.09± 23.40</td><td>14.56± 8.68</td><td>17.07 土 5.80</td></tr><tr><td>+ PBT</td><td>24.37± 12.35</td><td>49.01± 6.73</td><td>38.60± 7.34</td><td>55.22± 4.90</td><td>41.80± 2.76</td></tr><tr><td>Llama 3.1 8B</td><td>73.72± 1.58</td><td>46.14± 1.81</td><td>64.77± 1.68</td><td>32.79± 2.32</td><td>54.36± 0.28</td></tr><tr><td>+ accept</td><td>43.34± 44.00</td><td>55.14± 49.92</td><td>83.96± 17.25</td><td>47.57± 46.41</td><td>57.50± 12.96</td></tr><tr><td>+ resist</td><td>18.09± 12.61</td><td>17.74± 13.82</td><td>56.06± 19.00</td><td>27.67 土 3.70</td><td>29.89± 5.51</td></tr><tr><td>+ PBT</td><td>32.66± 15.48</td><td>30.23± 15.99</td><td>45.70± 22.52</td><td>44.83± 13.11</td><td>38.36± 3.49</td></tr><tr><td>Llama 3.1 70B</td><td>75.95± 0.29</td><td>56.88± 0.42</td><td>71.99± 0.60</td><td>38.47 + 2.32</td><td>60.82± 0.82</td></tr><tr><td>+ accept</td><td>79.28± 9.98</td><td>85.68± 7.52</td><td>90.51± 4.32</td><td>87.62± 5.93</td><td>85.78± 2.09</td></tr><tr><td>+ resist</td><td>22.45± 37.12</td><td>9.16± 14.82</td><td>26.53± 5.54</td><td>2.41± 2.51</td><td>15.13± 13.55</td></tr><tr><td>+ PBT</td><td>9.63± 3.74</td><td>16.13± 4.10</td><td>37.45± 13.71</td><td>27.54± 8.13</td><td>22.69± 4.02</td></tr></table>{{< /table-caption >}}

> Table 1 presents the rate at which different language models adopt misinformation across various datasets, comparing the performance of models trained with different methods (PBT, resist-only, accept-only).


{{< table-caption caption="🔽 Table 2: Flipflopping evaluation using Laban et al. (2023)'s “Are you sure?” prompt. PBT leads to less flipflopping. Full results in Appendix A." >}}
<table id='2' style='font-size:18px'><tr><td>Model</td><td>Before</td><td>After</td><td>Diff.</td></tr><tr><td>Mistral 7B</td><td>53.53± 0.06</td><td>31.87± 0.06</td><td>-21.67</td></tr><tr><td>+ accept</td><td>53.67± 0.38</td><td>34. 70± 0.82</td><td>-18.97</td></tr><tr><td>+ resist</td><td>38.63± 16.18</td><td>37.80± 14.75</td><td>-0.83</td></tr><tr><td>+ PBT</td><td>50.03± 6.64</td><td>47.40± 8.51</td><td>-2.63</td></tr><tr><td>Llama 3.1 8B</td><td>61.60± 0.00</td><td>34.40± 0.00</td><td>-27.20</td></tr><tr><td>+ accept</td><td>59.33± 3.31</td><td>54.23± 3.50</td><td>-5.10</td></tr><tr><td>+ resist</td><td>32.03± 3.65</td><td>29.10± 4.45</td><td>-2.93</td></tr><tr><td>+ PBT</td><td>54.70±2.79</td><td>52.43± 5.09</td><td>-2.27</td></tr><tr><td>Llama 3.1 70B</td><td>73.10± 0.00</td><td>40.10± 0.00</td><td>-33.00</td></tr><tr><td>+ accept</td><td>65.20± 3.25</td><td>55.70± 5.95</td><td>-9.50</td></tr><tr><td>+ resist</td><td>43.87± 27.80</td><td>43.47± 26.70</td><td>-0.40</td></tr><tr><td>+ PBT</td><td>73.17±2.53</td><td>73.40± 2.52</td><td>0.23</td></tr></table>{{< /table-caption >}}

> Table 2 presents the accuracy of different models using Laban et al. (2023)'s 'Are you sure?' prompt to measure the rate of flip-flopping, showing PBT leads to less flip-flopping.


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
{{< /gallery >}}