---
title: "Context is Key(NMF): Modelling Topical Information Dynamics in Chinese Diaspora Media"
summary: "KeyNMF, a novel topic modeling approach using transformer-based embeddings, reveals significant information dynamics in Chinese diaspora media, uncovering trends linked to major political events."
categories: ["AI Generated"]
tags: ["🔖 24-10-16", "🤗 24-10-21"]
showSummary: true
date: 2024-10-16
draft: false
---

### TL;DR


{{< lead >}}

This research introduces KeyNMF, a novel approach to topic modeling that leverages transformer-based contextual embeddings for improved accuracy and interpretability, particularly in multilingual and data-scarce environments.  It's benchmarked against other methods on Chinese datasets, demonstrating competitive performance.  The researchers then integrate KeyNMF into a pipeline for analyzing information dynamics, specifically focusing on novelty and resonance (how new and persistent information is within a system). This pipeline is applied to five Chinese news sites in the lead-up to the 2024 European parliamentary elections. The results reveal clear correlations between information dynamics and significant political events, such as the Xi Jinping's European tour and the EU parliamentary elections. The study highlights the effectiveness of KeyNMF for understanding information flows in complex media systems and lays groundwork for further research into media manipulation and political influence. The researchers released their implementation of KeyNMF as part of the Turftopic Python package, making their work reproducible and accessible to other researchers.  The findings contribute to understanding political communication in Chinese diaspora media and the impact of global events.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.12791" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
To provide a concise and informative summary of the research paper on modelling topical information dynamics in Chinese diaspora media using KeyNMF.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} KeyNMF effectively models topic dynamics in multilingual datasets, outperforming traditional methods. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Analysis of Chinese diaspora media revealed clear trends correlating information novelty and resonance with major political events. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The developed pipeline provides a valuable tool for researching information dynamics in complex cultural systems. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_8_0.png "🔼 Figure 3: The number of new articles collected at each time point for each source. An article is 'new' if it did not appear in the collected set of articles from the previous time point.")

> Figure 3 shows the number of new articles collected at each time point for five different Chinese diaspora news websites.





![](charts/charts_6_0.png "🔼 Figure 1: Sensitivity of KeyNMF to the choice of N keywords on multiple metrics and news sources.")

> The chart displays the sensitivity of KeyNMF's performance to the number of keywords used across multiple metrics and news sources.





{{< table-caption caption="🔽 Table 1 KeyNMF's performance on Chinese news data against a number of baselines. Topic descriptions were evaluated on diversity (d), internal (Cin) and external (Cex) word embedding coherence." >}}
<br><table id='2' style='font-size:14px'><tr><td></td><td colspan="3">chinanews</td><td colspan="3">ihuawen</td><td colspan="3">oushinet</td><td colspan="3">xinozhou</td><td colspan="3">yidali-huarenjie</td></tr><tr><td>Model</td><td>d</td><td>Cin</td><td>Cex</td><td>d</td><td>Cin</td><td>Cex</td><td>d</td><td>Cin</td><td>Cex</td><td>d</td><td>Cin</td><td>Cex</td><td>d</td><td>Cin</td><td>Cex</td></tr><tr><td>KeyNMF</td><td>0.93</td><td>0.29</td><td>0.63</td><td>0.91</td><td>0.17</td><td>0.64</td><td>0.84</td><td>0.23</td><td>0.58</td><td>0.85</td><td>0.26</td><td>0.55</td><td>0.88</td><td>0.52</td><td>0.57</td></tr><tr><td>S3</td><td>0.91</td><td>0.16</td><td>0.47</td><td>0.91</td><td>0.11</td><td>0.47</td><td>0.83</td><td>0.12</td><td>0.54</td><td>0.96</td><td>0.17</td><td>0.55</td><td>0.93</td><td>0.46</td><td>0.52</td></tr><tr><td>Top2Vec</td><td>0.78</td><td>0.14</td><td>0.71</td><td>0.83</td><td>0.10</td><td>0.70</td><td>0.87</td><td>0.12</td><td>0.73</td><td>0.86</td><td>0.14</td><td>0.71</td><td>0.75</td><td>0.46</td><td>0.69</td></tr><tr><td>BERTopic</td><td>0.89</td><td>0.31</td><td>0.52</td><td>0.89</td><td>0.26</td><td>0.50</td><td>0.84</td><td>0.23</td><td>0.50</td><td>0.84</td><td>0.26</td><td>0.52</td><td>0.91</td><td>0.57</td><td>0.51</td></tr><tr><td>CTMcombined</td><td>0.99</td><td>0.27</td><td>0.52</td><td>0.99</td><td>0.23</td><td>0.51</td><td>0.99</td><td>0.21</td><td>0.51</td><td>0.98</td><td>0.25</td><td>0.51</td><td>0.97</td><td>0.54</td><td>0.49</td></tr><tr><td>CTMzeroshot</td><td>0.99</td><td>0.28</td><td>0.53</td><td>0.99</td><td>0.23</td><td>0.50</td><td>0.99</td><td>0.22</td><td>0.50</td><td>1.00</td><td>0.26</td><td>0.51</td><td>0.97</td><td>0.54</td><td>0.51</td></tr><tr><td>NMF</td><td>0.74</td><td>0.27</td><td>0.57</td><td>0.60</td><td>0.18</td><td>0.53</td><td>0.64</td><td>0.18</td><td>0.54</td><td>0.66</td><td>0.18</td><td>0.56</td><td>0.71</td><td>0.49</td><td>0.54</td></tr><tr><td>LDA</td><td>0.61</td><td>0.19</td><td>0.57</td><td>0.53</td><td>0.16</td><td>0.54</td><td>0.41</td><td>0.13</td><td>0.54</td><td>0.48</td><td>0.14</td><td>0.58</td><td>0.57</td><td>0.34</td><td>0.54</td></tr></table>{{< /table-caption >}}

> Table 1 presents KeyNMF's performance against other topic modeling baselines, evaluated across multiple metrics on various Chinese news datasets.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_17_0.png "🔼 Figure 7: The distributions over time for two topics with high pseudo-probabilities before Putin’s state visit to China. These topics are generated by the 10-topic KeyNMF model for Oushinet. Note that the y-axis scale differs for each subplot.")

> Figure 7 shows the change in topic distributions over time for two topics in Oushinet news before Putin's visit to China, highlighting the shift in focus.


![](figures/figures_19_0.png "🔼 Figure 9: The distributions over time for five topics with high pseudo-probabilities during Xi Jinping's European tour. These topics are generated by the 10-topic KeyNMF models for Oushinet and Xinouzhou. Note that the y-axis scale differs for each subplot.")

> The figure shows the pseudo-probability distributions over time for five topics with high pseudo-probabilities during Xi Jinping's European tour, generated by the 10-topic KeyNMF models for Oushinet and Xinouzhou.


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
{{< /gallery >}}