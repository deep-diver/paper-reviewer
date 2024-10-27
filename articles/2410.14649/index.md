---
title: "EvoPress: Towards Optimal Dynamic Model Compression via Evolutionary Search"
summary: "EvoPress: A novel evolutionary algorithm optimizes dynamic LLM compression, surpassing existing methods in accuracy and efficiency."
categories: ["AI Generated"]
tags: ["🔖 24-10-18", "🤗 24-10-23"]
showSummary: true
date: 2024-10-18
draft: false
---

### TL;DR


{{< lead >}}

Large Language Models (LLMs) are computationally expensive.  This paper introduces EvoPress, a new method for compressing LLMs more effectively.  Existing methods typically compress models uniformly, but EvoPress dynamically adjusts the compression level for different parts of the model (e.g., layers or blocks). This allows for better performance since some parts of the model are more important than others and don't need as much compression.  EvoPress uses an evolutionary search algorithm that explores different compression strategies and finds the best one.  The researchers demonstrate that EvoPress consistently outperforms other methods on several benchmark LLMs.  They also prove that their algorithm converges to an optimal solution, meaning it is guaranteed to find a good compression strategy. This is important because other similar methods often rely on assumptions that may not always be true.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.14649" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
EvoPress uses evolutionary search to optimize dynamic model compression for LLMs, achieving state-of-the-art results across various compression methods.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} EvoPress is a provably optimal and efficient method for dynamic LLM compression. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} EvoPress outperforms existing techniques across layer dropping, sparsity, and quantization. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The paper challenges the assumption of error monotonicity in LLM compression. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights





![](charts/charts_5_0.png "🔼 Figure 1: Removing twelve transformer blocks from Llama-3-8B under the constraint that only pairs of consecutive blocks can be removed. EvoPress finds the optimal configuration from the 8008 possible removal combinations in generation 6.")

> The chart displays the fast convergence of EvoPress in finding the optimal configuration for removing transformer blocks from Llama-3-8B.





{{< table-caption caption="🔽 Table 1: Depth pruning is not monotone. In this example (Llama-3-8B with Fineweb-Edu calibration), removing strictly more blocks (depicted in orange) can improve perplexity across sources. Left half of block corresponds to attention layer, right half to MLP." >}}
<table id='1' style='font-size:14px'><tr><td>Model</td><td>Configuration (Each block contains Attention + MLP)</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td rowspan="3">Llama-3-8B</td><td></td><td>5.54</td><td>8.80</td><td>7.72</td></tr><tr><td></td><td rowspan="2">188.01 24.39</td><td>147.25</td><td>70.46</td></tr><tr><td></td><td>35.53</td><td>26.24</td></tr></table>{{< /table-caption >}}

> The table shows that removing more blocks from a Llama-3-8B model does not always lead to lower perplexity, demonstrating that error monotonicity does not hold for LLMs.



### More visual insights



<details>
<summary>More on charts
</summary>


![](charts/charts_8_0.png "🔼 Figure 2: Depth pruning results, on Mistral-7B-v0.3. (Left) Relative to all prior methods, EvoPress shows significantly lower PPL gap relative to the uncompressed model, with remarkably large gaps at medium compression rates. (Right) Examining the blocks dropped, we observe that EvoPress isolates completely different profiles relative to ShortGPT (which scores by cosine similarity).")

> The chart compares the performance of EvoPress against other depth pruning methods across different sparsity levels on the Mistral-7B-v0.3 model, showing EvoPress's superior performance and unique block removal patterns.


![](charts/charts_9_0.png "🔼 Figure 5: Convergence of EvoPress when removing 8 transformer blocks (left) and 16 transformer blocks (right) of Mistral-7B-v0.3.")

> The chart displays the convergence speed of EvoPress in terms of perplexity and KL-divergence when pruning 8 and 16 transformer blocks from the Mistral-7B-v0.3 model.


![](charts/charts_26_0.png "🔼 Figure 4: Convergence of EvoPress for unstructured sparsity (left) and quantization (right) for different fitness functions.")

> The chart displays the convergence of EvoPress for unstructured sparsity and quantization using two different fitness functions (perplexity and KL-divergence).


![](charts/charts_29_0.png "🔼 Figure 5: Convergence of EvoPress when removing 8 transformer blocks (left) and 16 transformer blocks (right) of Mistral-7B-v0.3.")

> The chart displays the convergence speed of EvoPress in terms of perplexity and KL-divergence when removing 8 and 16 transformer blocks from the Mistral-7B-v0.3 model, showing a rapid convergence to near-optimal solutions within a few hours.


![](charts/charts_29_1.png "🔼 Figure 5: Convergence of EvoPress when removing 8 transformer blocks (left) and 16 transformer blocks (right) of Mistral-7B-v0.3.")

> The chart displays the convergence of EvoPress in terms of perplexity and KL-divergence over generations when removing 8 and 16 transformer blocks from the Mistral-7B-v0.3 model.


![](charts/charts_29_2.png "🔼 Figure 5: Convergence of EvoPress when removing 8 transformer blocks (left) and 16 transformer blocks (right) of Mistral-7B-v0.3.")

> The chart displays the convergence speed of EvoPress for removing 8 and 16 transformer blocks from the Mistral-7B-v0.3 model, showing the perplexity and KL divergence over generations.


![](charts/charts_30_0.png "🔼 Figure 7: Effect of removing random subsets of blocks for Llama-3-8B.")

> The chart displays the correlation between different metrics (cosine similarity, squared error, and normalized squared error) and perplexity when randomly removing subsets of blocks from Llama-3-8B, showing how these correlations change with sparsity levels.


![](charts/charts_32_0.png "🔼 Figure 8: Comparison of different block-level sparsity profiles for Llama-3.1-8B at 70% sparsity.")

> The chart compares the sparsity profiles generated by EvoPress, OWL, and uniform sparsity methods across different layers of Llama-3.1-8B model at 70% average sparsity.


![](charts/charts_32_1.png "🔼 Figure 9: Average sparsity per projection type for Llama-3.1-8B at 70% sparsity for EvoPress.")

> The bar chart displays the average sparsity achieved per projection type (q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj) for the Llama-3.1-8B model using EvoPress at 70% overall sparsity.


![](charts/charts_33_0.png "🔼 Figure 10: Convergence of EvoPress for 2.25 bit quantization on Llama-3.1-8B (left) and 3 bit quantization on Llama-3-8B (right).")

> The chart displays the convergence speed of EvoPress for 2.25-bit and 3-bit quantization on Llama-3.1-8B and Llama-3-8B, respectively, over generations.


![](charts/charts_33_1.png "🔼 Figure 10: Convergence of EvoPress for 2.25 bit quantization on Llama-3.1-8B (left) and 3 bit quantization on Llama-3-8B (right).")

> The chart displays the convergence speed of EvoPress for 2.25-bit and 3-bit quantization on Llama-3.1-8B and Llama-3-8B, respectively, showing the perplexity and KL-divergence values over generations.


![](charts/charts_33_2.png "🔼 Figure 11: Block-level quantization profiles for Llama-3.1-8B at 3 bit compression on average.")

> The chart displays the block-level quantization profiles for the Llama-3.1-8B model at an average compression of 3 bits, showing the bit allocation for each block.


![](charts/charts_33_3.png "🔼 Figure 9: Average sparsity per projection type for Llama-3.1-8B at 70% sparsity for EvoPress.")

> The chart visualizes the average sparsity achieved per projection type (q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj) for the Llama-3.1-8B model when applying EvoPress at a 70% overall sparsity level.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 2: Performance of various methods at 70% average sparsity. EvoPress outperforms prior methods both in terms of validation perplexity (PPL) and zero-shot accuracy." >}}
<table id='1' style='font-size:16px'><tr><td>Model</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>ArcC↑</td><td>ArcE↑</td><td>HS↑</td><td>PiQA↑</td><td>WG↑</td><td>Avg↑</td></tr><tr><td rowspan="4">Mistral-7B-v0.3</td><td>Dense</td><td>4.82</td><td>7.72</td><td>48.9</td><td>79.6</td><td>60.9</td><td>80.3</td><td>73.9</td><td>I 68.7</td></tr><tr><td>Uniform</td><td>23.08</td><td>30.03</td><td>27.1</td><td>60.9</td><td>36.1</td><td>65.9</td><td>59.4</td><td>49.9</td></tr><tr><td>OWL</td><td>17.22</td><td>21.66</td><td>27.9</td><td>62.6</td><td>38.6</td><td>67.0</td><td>63.5</td><td>51.9</td></tr><tr><td>EvoPress</td><td>14.42</td><td>16.46</td><td>31.6</td><td>64.7</td><td>41.4</td><td>69.5</td><td>61.9</td><td>53.8</td></tr><tr><td rowspan="4">Llama-3-8B</td><td>Dense</td><td>5.54</td><td>7.10</td><td>50.4</td><td>80.1</td><td>60.2</td><td>79.7</td><td>72.6</td><td>I 68.6</td></tr><tr><td>Uniform</td><td>85.84</td><td>98.35</td><td>22.7</td><td>49.9</td><td>31.4</td><td>62.1</td><td>54.4</td><td>44.1</td></tr><tr><td>OWL</td><td>48.07</td><td>52.32</td><td>27.0</td><td>54.9</td><td>36.6</td><td>65.1</td><td>58.6</td><td>48.4</td></tr><tr><td>EvoPress</td><td>28.76</td><td>33.72</td><td>28.9</td><td>56.7</td><td>38.6</td><td>68.0</td><td>61.7</td><td>50.8</td></tr><tr><td rowspan="4">Llama-3.1-8B</td><td>Dense</td><td>5.61</td><td>8.90</td><td>51.2</td><td>81.4</td><td>60.0</td><td>80.1</td><td>73.9</td><td>I 69.3</td></tr><tr><td>Uniform</td><td>68.97</td><td>103.27</td><td>22.3</td><td>49.7</td><td>31.5</td><td>61.6</td><td>55.6</td><td>44.2</td></tr><tr><td>OWL</td><td>42.29</td><td>48.65</td><td>27.4</td><td>55.8</td><td>36.5</td><td>65.7</td><td>60.7</td><td>49.2</td></tr><tr><td>EvoPress</td><td>24.32</td><td>30.58</td><td>29.1</td><td>62.4</td><td>39.5</td><td>68.9</td><td>60.3</td><td>52.0</td></tr><tr><td rowspan="4">Phi-3-Medium-14B</td><td>Dense</td><td>4.02</td><td>8.31</td><td>60.9</td><td>84.1</td><td>64.0</td><td>81.0</td><td>76.2</td><td>73.2</td></tr><tr><td>Uniform</td><td>16.66</td><td>24.73</td><td>36.9</td><td>70.6</td><td>40.0</td><td>69.4</td><td>65.8</td><td>56.5</td></tr><tr><td>OWL</td><td>15.66</td><td>23.38</td><td>35.7</td><td>69.2</td><td>39.4</td><td>68.3</td><td>64.4</td><td>55.4</td></tr><tr><td>EvoPress</td><td>13.83</td><td>19.13</td><td>41.5</td><td>73.0</td><td>43.6</td><td>71.8</td><td>69.1</td><td>59.8</td></tr></table>{{< /table-caption >}}

> Table 2 presents a comparison of different model compression methods at 70% average sparsity across multiple LLMs, showing EvoPress's superior performance in terms of perplexity and zero-shot accuracy.


{{< table-caption caption="🔽 Table 1: Depth pruning is not monotone. In this example (Llama-3-8B with Fineweb-Edu calibration), removing strictly more blocks (depicted in orange) can improve perplexity across sources. Left half of block corresponds to attention layer, right half to MLP." >}}
<table id='2' style='font-size:16px'><tr><td colspan="2">Number of Mutations</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td>min(U1, U2),</td><td>U1, U2 ~ U(1,3)</td><td>17.52</td><td>21.60</td><td>16.79</td></tr><tr><td>min(U1, U2),</td><td>U1, U2 ~ U(1, 7)</td><td>21.49</td><td>22.41</td><td>17.65</td></tr><tr><td>min(U1, U2),</td><td>U1, U2 ~ U(1, 15)</td><td>18.65</td><td>22.67</td><td>17.63</td></tr><tr><td></td><td>1</td><td>18.12</td><td>21.12</td><td>16.33</td></tr><tr><td></td><td>3</td><td>22.09</td><td>25.42</td><td>19.25</td></tr><tr><td></td><td>7</td><td>25.06</td><td>26.52</td><td>19.65</td></tr><tr><td>15</td><td></td><td>27.01</td><td>28.19</td><td>22.03</td></tr></table>{{< /table-caption >}}

> The table shows an example where removing more blocks in a Llama-3-8B model, contrary to the assumption of error monotonicity, improves perplexity across different sources.


{{< table-caption caption="🔽 Table 2: Performance of various methods at 70% average sparsity. EvoPress outperforms prior methods both in terms of validation perplexity (PPL) and zero-shot accuracy." >}}
<table id='9' style='font-size:14px'><tr><td>Offspring</td><td>Stage 1: Tokens</td><td>Stage 2: Tokens</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td>16</td><td>1024</td><td>8192</td><td>16.22</td><td>17.93</td><td>12.26</td></tr><tr><td>16</td><td>512</td><td>8192</td><td>15.87</td><td>18.28</td><td>12.38</td></tr><tr><td>16</td><td>256</td><td>8192</td><td>17.25</td><td>18.51</td><td>12.52</td></tr><tr><td>16</td><td>128</td><td>8192</td><td>16.01</td><td>18.99</td><td>12.72</td></tr><tr><td>16</td><td>64</td><td>8192</td><td>15.89</td><td>19.35</td><td>12.98</td></tr></table>{{< /table-caption >}}

> The table presents a comparison of different methods for achieving 70% average sparsity in various LLMs, showing EvoPress's superior performance in terms of perplexity and zero-shot accuracy.


{{< table-caption caption="🔽 Table 1: Depth pruning is not monotone. In this example (Llama-3-8B with Fineweb-Edu calibration), removing strictly more blocks (depicted in orange) can improve perplexity across sources. Left half of block corresponds to attention layer, right half to MLP." >}}
<table id='1' style='font-size:14px'><tr><td>Offspring</td><td>Stage 1: Tokens</td><td>Stage 2: Tokens</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td>64</td><td>512</td><td>8192</td><td>16.35</td><td>18.27</td><td>12.36</td></tr><tr><td>32</td><td>512</td><td>8192</td><td>16.65</td><td>18.22</td><td>12.44</td></tr><tr><td>16</td><td>512</td><td>8192</td><td>15.87</td><td>18.27</td><td>12.38</td></tr><tr><td>8</td><td>512</td><td>8192</td><td>16.37</td><td>18.74</td><td>12.64</td></tr><tr><td>4</td><td>512</td><td>8192</td><td>17.87</td><td>18.97</td><td>12.72</td></tr></table>{{< /table-caption >}}

> The table shows an example where removing more blocks from a Llama-3-8B model, contrary to the assumption of error monotonicity, leads to improved perplexity.


{{< table-caption caption="🔽 Table 2: Performance of various methods at 70% average sparsity. EvoPress outperforms prior methods both in terms of validation perplexity (PPL) and zero-shot accuracy." >}}
<table id='6' style='font-size:14px'><tr><td>Model</td><td># Bits</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td rowspan="6">Llama-3-8B</td><td rowspan="3">3</td><td>Uniform</td><td>12.19</td><td>15.76</td><td>11.47</td></tr><tr><td>EvoPress (PPL)</td><td>8.17</td><td>12.15</td><td>9.64</td></tr><tr><td>EvoPress (KL)</td><td>7.49</td><td>12.03</td><td>9.56</td></tr><tr><td rowspan="3">4</td><td>Uniform</td><td>6.48</td><td>9.50</td><td>8.46</td></tr><tr><td>EvoPress (PPL)</td><td>5.86</td><td>9.46</td><td>8.23</td></tr><tr><td>EvoPress (KL)</td><td>5.86</td><td>9.44</td><td>8.22</td></tr><tr><td rowspan="6">Llama-2-7B</td><td rowspan="3">3</td><td>Uniform</td><td>6.16</td><td>7.96</td><td>6.86</td></tr><tr><td>EvoPress (PPL)</td><td>5.74</td><td>7.90</td><td>6.79</td></tr><tr><td>EvoPress (KL)</td><td>5.70</td><td>7.87</td><td>6.76</td></tr><tr><td rowspan="3">4</td><td>Uniform</td><td>5.48</td><td>7.10</td><td>6.40</td></tr><tr><td>EvoPress (PPL)</td><td>5.25</td><td>7.09</td><td>6.37</td></tr><tr><td>EvoPress (KL)</td><td>5.22</td><td>7.07</td><td>6.34</td></tr><tr><td rowspan="6">Mistral-7B-v0.3</td><td rowspan="3">3</td><td>Uniform</td><td>5.54</td><td>8.57</td><td>6.96</td></tr><tr><td>EvoPress (PPL)</td><td>5.23</td><td>8.45</td><td>6.87</td></tr><tr><td>EvoPress (KL)</td><td>5.21</td><td>8.42</td><td>6.86</td></tr><tr><td rowspan="3">4</td><td>Uniform</td><td>5.10</td><td>7.87</td><td>6.50</td></tr><tr><td>EvoPress (PPL)</td><td>4.85</td><td>7.86</td><td>6.49</td></tr><tr><td>EvoPress (KL)</td><td>4.84</td><td>7.84</td><td>6.48</td></tr></table>{{< /table-caption >}}

> Table 2 presents a comparison of different model compression methods at 70% average sparsity, showing EvoPress's superior performance in terms of perplexity and zero-shot accuracy.


{{< table-caption caption="🔽 Table 2: Performance of various methods at 70% average sparsity. EvoPress outperforms prior methods both in terms of validation perplexity (PPL) and zero-shot accuracy." >}}
<table id='8' style='font-size:14px'><tr><td>Application</td><td>Generations</td><td>Offspring</td><td>Survivors (1)</td><td>Tokens (1)</td><td>Survivors (2)</td><td>Tokens (2)</td><td>Survivors (3)</td><td>Tokens (3)</td></tr><tr><td>Depth Pruning</td><td>k(n - k)/1.5</td><td>32</td><td>2</td><td>2048</td><td>1</td><td>32768</td><td>N/A</td><td>N/A</td></tr><tr><td>Unstr. Sparsity</td><td>400</td><td>64</td><td>8</td><td>2048</td><td>2</td><td>16384</td><td>1</td><td>65536</td></tr><tr><td>Quantization</td><td>150</td><td>128</td><td>16</td><td>2048</td><td>4</td><td>16384</td><td>1</td><td>131072</td></tr><tr><td>Super-Fast</td><td>400</td><td>16</td><td>1</td><td>512</td><td>1</td><td>8192</td><td>N/A</td><td>N/A</td></tr></table>{{< /table-caption >}}

> Table 2 presents a comparison of different methods for unstructured sparsity at 70% sparsity, showing EvoPress's superior performance in terms of perplexity and zero-shot accuracy across various LLMs.


{{< table-caption caption="🔽 Table 1: Depth pruning is not monotone. In this example (Llama-3-8B with Fineweb-Edu calibration), removing strictly more blocks (depicted in orange) can improve perplexity across sources. Left half of block corresponds to attention layer, right half to MLP." >}}
<table id='1' style='font-size:14px'><tr><td>Sparsity</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td>0%</td><td>Dense</td><td>4.82</td><td>7.72</td><td>6.41</td></tr><tr><td rowspan="6">12.5%</td><td>EvoPress</td><td>6.06</td><td>9.00</td><td>7.42</td></tr><tr><td>EvoPress (Attn.+MLP)</td><td>6.33</td><td>9.44</td><td>7.80</td></tr><tr><td>ShortGPT</td><td>7.19</td><td>10.18</td><td>8.46</td></tr><tr><td>Cosine Similarity (Window)</td><td>7.19</td><td>10.18</td><td>8.46</td></tr><tr><td>Weight Subcloning</td><td>7.19</td><td>10.18</td><td>8.46</td></tr><tr><td>Shortened Llama</td><td>6.64</td><td>9.71</td><td>7.94</td></tr><tr><td rowspan="6">25%</td><td>EvoPress</td><td>8.66</td><td>12.04</td><td>9.92</td></tr><tr><td>EvoPress (Attn.+MLP)</td><td>9.46</td><td>13.02</td><td>10.59</td></tr><tr><td>ShortGPT</td><td>43.26</td><td>40.16</td><td>29.54</td></tr><tr><td>Cosine Similarity (Window)</td><td>33.75</td><td>54.07</td><td>36.26</td></tr><tr><td>Weight Subcloning</td><td>43.26</td><td>40.16</td><td>29.54</td></tr><tr><td>Shortened Llama</td><td>14.94</td><td>19.30</td><td>14.73</td></tr><tr><td rowspan="6">37.5%</td><td>EvoPress</td><td>17.52</td><td>21.60</td><td>16.90</td></tr><tr><td>EvoPress (Attn.+MLP)</td><td>21.62</td><td>25.17</td><td>18.97</td></tr><tr><td>ShortGPT</td><td>2898.98</td><td>2722.66</td><td>981.99</td></tr><tr><td>Cosine Similarity (Window)</td><td>1034.09</td><td>2471.86</td><td>1050.56</td></tr><tr><td>Weight Subcloning</td><td>2898.98</td><td>2722.66</td><td>981.99</td></tr><tr><td>Shortened Llama</td><td>440.20</td><td>442.09</td><td>486.15</td></tr><tr><td rowspan="6">50%</td><td>EvoPress</td><td>61.75</td><td>54.15</td><td>43.23</td></tr><tr><td>EvoPress (Attn.+MLP)</td><td>108.91</td><td>99.74</td><td>69.07</td></tr><tr><td>ShortGPT</td><td>2422.72</td><td>2134.92</td><td>1083.51</td></tr><tr><td>Cosine Similarity (Window)</td><td>3411.47</td><td>1934.16</td><td>1740.91</td></tr><tr><td>Weight Subcloning</td><td>2422.72</td><td>2134.92</td><td>1083.51</td></tr><tr><td>Shortened Llama</td><td>5241.76</td><td>3595.71</td><td>1953.14</td></tr></table>{{< /table-caption >}}

> The table shows that removing more blocks from a Llama-3-8B model, as measured by perplexity, does not always lead to a decrease in performance, demonstrating that error monotonicity does not hold for LLMs.


{{< table-caption caption="🔽 Table 10: Depth pruning of Llama-2-7B." >}}
<table id='3' style='font-size:14px'><tr><td>Sparsity</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td>0%</td><td>Dense</td><td>5.21</td><td>6.93</td><td>6.40</td></tr><tr><td rowspan="5">12.5%</td><td>EvoPress</td><td>6.42</td><td>8.60</td><td>7.54</td></tr><tr><td>ShortGPT</td><td>8.86</td><td>10.78</td><td>9.30</td></tr><tr><td>Cosine Similarity (Window)</td><td>7.53</td><td>9.82</td><td>8.51</td></tr><tr><td>Weight Subcloning</td><td>9.09</td><td>11.06</td><td>9.60</td></tr><tr><td>ShortenedLlama</td><td>7.68</td><td>10.44</td><td>8.57</td></tr><tr><td rowspan="5">25%</td><td>EvoPress</td><td>9.15</td><td>11.46</td><td>9.69</td></tr><tr><td>ShortGPT</td><td>23.41</td><td>30.30</td><td>21.16</td></tr><tr><td>Cosine Similarity (Window)</td><td>16.60</td><td>21.04</td><td>17.37</td></tr><tr><td>Weight Subcloning</td><td>23.41</td><td>30.30</td><td>21.16</td></tr><tr><td>Shortened Llama</td><td>13.86</td><td>14.08</td><td>11.81</td></tr><tr><td rowspan="5">37.5%</td><td>EvoPress</td><td>17.98</td><td>18.91</td><td>15.53</td></tr><tr><td>ShortGPT</td><td>70.94</td><td>63.51</td><td>54.07</td></tr><tr><td>Cosine Similarity (Window)</td><td>192.07</td><td>212.60</td><td>151.10</td></tr><tr><td>Weight Subcloning</td><td>70.94</td><td>63.51</td><td>54.07</td></tr><tr><td>Shortened Llama</td><td>35.37</td><td>26.07</td><td>20.37</td></tr><tr><td rowspan="5">50%</td><td>EvoPress</td><td>48.84</td><td>42.29</td><td>33.57</td></tr><tr><td>ShortGPT</td><td>226.14</td><td>171.04</td><td>180.51</td></tr><tr><td>Cosine Similarity (Window)</td><td>4570.15</td><td>2876.83</td><td>1861.06</td></tr><tr><td>Weight Subcloning</td><td>226.14</td><td>171.04</td><td>180.51</td></tr><tr><td>Shortened Llama</td><td>145.78</td><td>87.40</td><td>68.79</td></tr></table>{{< /table-caption >}}

> The table presents the results of depth pruning experiments on Llama-2-7B model, comparing the perplexity scores of various depth pruning methods at different sparsity levels.


{{< table-caption caption="🔽 Table 1: Depth pruning is not monotone. In this example (Llama-3-8B with Fineweb-Edu calibration), removing strictly more blocks (depicted in orange) can improve perplexity across sources. Left half of block corresponds to attention layer, right half to MLP." >}}
<table id='1' style='font-size:14px'><tr><td>Sparsity</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td>0%</td><td>Dense</td><td>5.54</td><td>8.80</td><td>7.62</td></tr><tr><td rowspan="5">12.5%</td><td>EvoPress</td><td>7.72</td><td>12.61</td><td>10.15</td></tr><tr><td>ShortGPT</td><td>13.21</td><td>19.56</td><td>14.25</td></tr><tr><td>Cosine Similarity (Window)</td><td>9.54</td><td>14.87</td><td>11.64</td></tr><tr><td>Weight Subcloning</td><td>13.21</td><td>19.56</td><td>14.25</td></tr><tr><td>Shortened Llama</td><td>9.42</td><td>15.09</td><td>11.57</td></tr><tr><td rowspan="5">25%</td><td>EvoPress</td><td>13.99</td><td>22.83</td><td>15.84</td></tr><tr><td>ShortGPT</td><td>5527.54</td><td>11589.93</td><td>2346.13</td></tr><tr><td>Cosine Similarity (Window)</td><td>5519.95</td><td>11629.61</td><td>2342.91</td></tr><tr><td>Weight Subcloning</td><td>5527.54</td><td>11589.93</td><td>2346.13</td></tr><tr><td>Shortened Llama</td><td>16.59</td><td>20.81</td><td>16.28</td></tr><tr><td rowspan="5">37.5%</td><td>EvoPress</td><td>27.56</td><td>35.70</td><td>26.77</td></tr><tr><td>ShortGPT</td><td>64281.36</td><td>13836.12</td><td>3789.09</td></tr><tr><td>Cosine Similarity (Window)</td><td>64627.29</td><td>13890.14</td><td>3784.72</td></tr><tr><td>Weight Subcloning</td><td>64381.36</td><td>13836.13</td><td>3789.09</td></tr><tr><td>Shortened Llama</td><td>50.20</td><td>61.56</td><td>37.40</td></tr><tr><td rowspan="5">50%</td><td>EvoPress</td><td>84.99</td><td>87.86</td><td>66.41</td></tr><tr><td>ShortGPT</td><td>1663.97</td><td>1740.04</td><td>1588.20</td></tr><tr><td>Cosine Similarity (Window)</td><td>2053.19</td><td>1116.47</td><td>694.00</td></tr><tr><td>Weight Subcloning</td><td>1663.97</td><td>1740.04</td><td>1588.20</td></tr><tr><td>Shortened Llama</td><td>724.86</td><td>666.41</td><td>210.30</td></tr></table>{{< /table-caption >}}

> The table shows that removing more blocks from a Llama-3-8B model, contrary to the assumption of error monotonicity, can sometimes lead to better perplexity.


{{< table-caption caption="🔽 Table 12: Depth pruning of Llama-3.1-8B." >}}
<table id='3' style='font-size:14px'><tr><td>Sparsity</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>FW↓</td></tr><tr><td>0%</td><td>Dense</td><td>5.61</td><td>8.90</td><td>7.67</td></tr><tr><td rowspan="5">12.5%</td><td>EvoPress</td><td>7.58</td><td>12.24</td><td>10.00</td></tr><tr><td>ShortGPT</td><td>12.54</td><td>19.21</td><td>13.76</td></tr><tr><td>Cosine Similarity (Window)</td><td>12.54</td><td>19.21</td><td>13.76</td></tr><tr><td>Weight Subcloning</td><td>12.54</td><td>19.21</td><td>13.76</td></tr><tr><td>Shortened Llama</td><td>9.27</td><td>14.80</td><td>11.21</td></tr><tr><td rowspan="5">25%</td><td>EvoPress</td><td>11.59</td><td>17.84</td><td>13.96</td></tr><tr><td>ShortGPT</td><td>4278.39</td><td>6754.92</td><td>1512.39</td></tr><tr><td>Cosine Similarity (Window)</td><td>4278.39</td><td>6754.92</td><td>1512.39</td></tr><tr><td>Weight Subcloning</td><td>4278.39</td><td>6754.92</td><td>1512.39</td></tr><tr><td>Shortened Llama</td><td>20.41</td><td>20.33</td><td>16.12</td></tr><tr><td rowspan="5">37.5%</td><td>EvoPress</td><td>24.98</td><td>35.77</td><td>25.93</td></tr><tr><td>ShortGPT</td><td>123044.19</td><td>22071.51</td><td>6059.03</td></tr><tr><td>Cosine Similarity (Window)</td><td>123044.19</td><td>22071.51</td><td>6059.03</td></tr><tr><td>Weight Subcloning</td><td>123044.19</td><td>22071.51</td><td>6059.03</td></tr><tr><td>Shortened Llama</td><td>41.34</td><td>43.53</td><td>31.00</td></tr><tr><td rowspan="5">50%</td><td>EvoPress</td><td>105.84</td><td>110.69</td><td>61.25</td></tr><tr><td>ShortGPT</td><td>1630.11</td><td>1680.21</td><td>1698.64</td></tr><tr><td>Cosine Similarity (Window)</td><td>1881.54</td><td>1196.63</td><td>683.24</td></tr><tr><td>Weight Subcloning</td><td>1630.11</td><td>1680.21</td><td>1698.64</td></tr><tr><td>Shortened Llama</td><td>454.96</td><td>309.42</td><td>153.96</td></tr></table>{{< /table-caption >}}

> The table shows the perplexity results of different depth pruning methods on the Llama-3.1-8B model at various sparsity levels.


{{< table-caption caption="🔽 Table 1: Depth pruning is not monotone. In this example (Llama-3-8B with Fineweb-Edu calibration), removing strictly more blocks (depicted in orange) can improve perplexity across sources. Left half of block corresponds to attention layer, right half to MLP." >}}
<table id='1' style='font-size:16px'><tr><td>Model</td><td>Method</td><td>Removal Order (Left to Right)</td></tr><tr><td>Mistral-7B-v0.3</td><td>ShortGPT Weight Subcloning Shortened Llama</td><td>26, 25, 24, 27, 23, 22, 28, 30, 21, 29, 20, 19, 13, 17, 18, 12 26, 25, 24, 27, 23, 28, 22, 30, 21, 29, 20, 19, 13, 17, 12, 18 10, 12, 13, 11, 08, 09, 14, 15, 07, 06, 04, 27, 24, 16, 25, 05</td></tr><tr><td>Llama-2-7B</td><td>ShortGPT Weight Subcloning Shortened Llama</td><td>27, 25, 26, 28, 29, 24, 23, 22, 21, 30, 20, 19, 18, 17, 15, 14 27, 25, 28, 29, 26, 24, 23, 22, 21, 19, 30, 20, 18, 17, 14, 15 11, 12, 08, 09, 10, 06, 24, 25, 07, 14, 23, 13, 22, 21, 15, 27</td></tr><tr><td>Llama-3-8B</td><td>ShortGPT Weight Subcloning Shortened Llama</td><td>25, 26, 27, 24, 28, 23, 22, 29, 20, 21, 19, 18, 30, 17, 16, 11 25, 27, 26, 24, 28, 23, 22, 29, 20, 21, 19, 18, 30, 17, 16, 11 10, 08, 09, 11, 26, 25, 12, 22, 24, 23, 14, 13, 28, 06, 19, 21</td></tr><tr><td>Llama-3.1-8B</td><td>ShortGPT Weight Subcloning Shortened Llama</td><td>25, 26, 24, 27, 23, 28, 22, 29, 20, 21, 19, 18, 17, 30, 16, 10 25, 27, 26, 24, 28, 23, 22, 29, 20, 21, 19, 18, 30, 17, 16, 10 10, 09, 11, 08, 26, 25, 12, 24, 22, 23, 14, 28, 06, 13, 19, 21</td></tr></table>{{< /table-caption >}}

> The table shows that in large language models, removing more blocks does not always lead to lower perplexity, contradicting the assumption of error monotonicity in dynamic model compression.


{{< table-caption caption="🔽 Table 2: Performance of various methods at 70% average sparsity. EvoPress outperforms prior methods both in terms of validation perplexity (PPL) and zero-shot accuracy." >}}
<table id='1' style='font-size:14px'><tr><td>Model</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>ArcC↑</td><td>ArcE↑</td><td>HS↑</td><td>PiQA↑</td><td>WG↑</td><td>Avg↑</td></tr><tr><td rowspan="4">Mistral-7B-v0.3</td><td>Dense</td><td>4.82</td><td>7.72</td><td>48.9</td><td>79.6</td><td>60.9</td><td>80.3</td><td>73.9</td><td>68.7</td></tr><tr><td>Uniform</td><td>5.68</td><td>8.93</td><td>43.7</td><td>76.7</td><td>55.7</td><td>78.4</td><td>71.0</td><td>65.1</td></tr><tr><td>OWL</td><td>5.69</td><td>8.94</td><td>43.9</td><td>76.9</td><td>55.4</td><td>78.5</td><td>70.3</td><td>65.0</td></tr><tr><td>EvoPress</td><td>5.49</td><td>8.70</td><td>45.7</td><td>77.3</td><td>56.5</td><td>78.9</td><td>71.2</td><td>65.9</td></tr><tr><td rowspan="4">Llama-2-7B</td><td>Dense</td><td>5.12</td><td>6.93</td><td>43.4</td><td>76.3</td><td>57.1</td><td>78.1</td><td>69.0</td><td>I 64.8</td></tr><tr><td>Uniform</td><td>6.40</td><td>8.87</td><td>41.3</td><td>73.4</td><td>52.8</td><td>75.7</td><td>68.8</td><td>62.4</td></tr><tr><td>OWL</td><td>6.38</td><td>8.77</td><td>41.1</td><td>73.2</td><td>53.2</td><td>76.5</td><td>70.2</td><td>62.9</td></tr><tr><td>EvoPress</td><td>6.22</td><td>8.52</td><td>41.5</td><td>74.2</td><td>54.0</td><td>76.7</td><td>69.6</td><td>63.2</td></tr><tr><td rowspan="4">Llama-3-8B</td><td>Dense</td><td>5.54</td><td>7.10</td><td>50.4</td><td>80.1</td><td>60.2</td><td>79.7</td><td>72.6</td><td>68.6</td></tr><tr><td>Uniform</td><td>8.05</td><td>13.07</td><td>43.6</td><td>75.7</td><td>54.2</td><td>76.1</td><td>71.7</td><td>64.3</td></tr><tr><td>OWL</td><td>8.13</td><td>13.12</td><td>43.8</td><td>75.8</td><td>54.0</td><td>75.7</td><td>72.2</td><td>64.3</td></tr><tr><td>EvoPress</td><td>7.63</td><td>12.53</td><td>43.9</td><td>77.5</td><td>54.5</td><td>76.8</td><td>72.2</td><td>65.0</td></tr><tr><td rowspan="4">Llama-3.1-8B</td><td>Dense</td><td>5.61</td><td>8.90</td><td>51.2</td><td>81.4</td><td>60.0</td><td>80.1</td><td>73.9</td><td>69.3</td></tr><tr><td>Uniform</td><td>8.06</td><td>13.03</td><td>44.5</td><td>76.7</td><td>54.0</td><td>76.7</td><td>71.5</td><td>64.7</td></tr><tr><td>OWL</td><td>8.02</td><td>12.99</td><td>44.2</td><td>76.5</td><td>53.8</td><td>76.8</td><td>72.5</td><td>64.8</td></tr><tr><td>EvoPress</td><td>7.51</td><td>12.31</td><td>46.6</td><td>77.7</td><td>54.9</td><td>77.6</td><td>71.7</td><td>65.7</td></tr></table>{{< /table-caption >}}

> Table 2 presents the performance comparison of different methods for unstructured sparsity at 70% average sparsity across various LLMs, showcasing EvoPress's superior performance in terms of perplexity and zero-shot accuracy.


{{< table-caption caption="🔽 Table 2: Performance of various methods at 70% average sparsity. EvoPress outperforms prior methods both in terms of validation perplexity (PPL) and zero-shot accuracy." >}}
<table id='3' style='font-size:14px'><tr><td>Model</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td>ArcC↑</td><td>ArcE↑</td><td>HS↑</td><td>PiQA↑</td><td>WG↑</td><td>Avg↑</td></tr><tr><td rowspan="4">Mistral-7B-v0.3</td><td>Dense</td><td>4.82</td><td>7.72</td><td>48.9</td><td>79.6</td><td>60.9</td><td>80.3</td><td>73.9</td><td>68.7</td></tr><tr><td>Uniform</td><td>7.78</td><td>11.86</td><td>38.0</td><td>72.3</td><td>49.4</td><td>75.0</td><td>69.3</td><td>60.9</td></tr><tr><td>OWL</td><td>7.50</td><td>11.34</td><td>38.5</td><td>71.9</td><td>49.6</td><td>75.1</td><td>70.2</td><td>61.1</td></tr><tr><td>EvoPress</td><td>7.08</td><td>10.27</td><td>40.5</td><td>72.8</td><td>51.9</td><td>76.9</td><td>68.8</td><td>62.2</td></tr><tr><td rowspan="4">Llama-2-7B</td><td>Dense</td><td>5.12</td><td>6.93</td><td>43.4</td><td>76.3</td><td>57.1</td><td>78.1</td><td>69.0</td><td> 64.8</td></tr><tr><td>Uniform</td><td>9.3</td><td>12.37</td><td>35.8</td><td>69.5</td><td>45.9</td><td>72.4</td><td>65.9</td><td>57.9</td></tr><tr><td>OWL</td><td>8.35</td><td>11.00</td><td>36.0</td><td>69.1</td><td>47.5</td><td>73.2</td><td>66.2</td><td>58.4</td></tr><tr><td>EvoPress</td><td>8.21</td><td>10.34</td><td>37.1</td><td>70.6</td><td>49.3</td><td>74.4</td><td>67.6</td><td>59.8</td></tr><tr><td rowspan="4">Llama-3-8B</td><td>Dense</td><td>5.54</td><td>7.10</td><td>50.4</td><td>80.1</td><td>60.2</td><td>79.7</td><td>72.6</td><td>I 68.6</td></tr><tr><td>Uniform</td><td>13.86</td><td>21.43</td><td>35.2</td><td>69.7</td><td>45.6</td><td>72.2</td><td>68.0</td><td>58.2</td></tr><tr><td>OWL</td><td>12.37</td><td>18.53</td><td>38.0</td><td>70.3</td><td>47.7</td><td>72.1</td><td>68.5</td><td>59.3</td></tr><tr><td>EvoPress</td><td>11.02</td><td>16.37</td><td>39.0</td><td>71.9</td><td>48.6</td><td>74.0</td><td>69.1</td><td>60.5</td></tr><tr><td rowspan="4">Llama-3.1-8B</td><td>Dense</td><td>5.61</td><td>8.90</td><td>51.2</td><td>81.4</td><td>60.0</td><td>80.1</td><td>73.9</td><td>69.3</td></tr><tr><td>Uniform</td><td>13.43</td><td>21.46</td><td>36.4</td><td>69.7</td><td>46.2</td><td>72.3</td><td>67.7</td><td>58.5</td></tr><tr><td>OWL</td><td>12.08</td><td>18.25</td><td>38.9</td><td>71.1</td><td>47.7</td><td>73.1</td><td>68.8</td><td>59.9</td></tr><tr><td>EvoPress</td><td>10.58</td><td>15.96</td><td>40.0</td><td>72.5</td><td>49.0</td><td>74.6</td><td>69.5</td><td>61.1</td></tr></table>{{< /table-caption >}}

> Table 2 presents a comparison of different methods for achieving 70% average sparsity in LLMs, showing EvoPress's superior performance in both perplexity and zero-shot accuracy.


{{< table-caption caption="🔽 Table 2: Performance of various methods at 70% average sparsity. EvoPress outperforms prior methods both in terms of validation perplexity (PPL) and zero-shot accuracy." >}}
<table id='8' style='font-size:16px'><tr><td>Model</td><td># Bits</td><td>Method</td><td>Wiki2↓</td><td>C4↓</td><td> ArcC↑</td><td>ArcE↑</td><td>HS↑</td><td>PiQA↑</td><td>WG↑</td><td> Avg↑</td></tr><tr><td rowspan="4">Mistral-7B-v0.3</td><td rowspan="2">2.25</td><td>Best of 32</td><td>11.53</td><td>18.32</td><td>30.1</td><td>59.6</td><td>44.5</td><td>69.4</td><td>56.8</td><td>52.1</td></tr><tr><td>EvoPress</td><td>8.63</td><td>13.47</td><td>36.2</td><td>66.0</td><td>49.3</td><td>74.2</td><td>63.5</td><td>57.8</td></tr><tr><td rowspan="2">2.5</td><td>Best of 32</td><td>7.50</td><td>11.76</td><td>37.0</td><td>68.0</td><td>51.7</td><td>75.0</td><td>63.5</td><td>59.0</td></tr><tr><td>EvoPress</td><td>6.60</td><td>10.40</td><td>39.8</td><td>71.7</td><td>54.0</td><td>77.1</td><td>65.8</td><td>61.7</td></tr><tr><td rowspan="4">Llama-2-7B</td><td rowspan="2">2.25</td><td>Best of 32</td><td>13.18</td><td>18.19</td><td>24.8</td><td>50.2</td><td>40.3</td><td>66.8</td><td>56.1</td><td>47.7</td></tr><tr><td>EvoPress</td><td>9.82</td><td>9.93</td><td>29.5</td><td>61.8</td><td>46.2</td><td>70.3</td><td>59.4</td><td>53.4</td></tr><tr><td rowspan="2">2.5</td><td>Best of 32</td><td>9.42</td><td>9.01</td><td>29.1</td><td>58.6</td><td>46.9</td><td>70.1</td><td>62.6</td><td>53.5</td></tr><tr><td>EvoPress</td><td>8.03</td><td>7.33</td><td>35.3</td><td>68.4</td><td>50.8</td><td>73.9</td><td>64.2</td><td>58.5</td></tr><tr><td rowspan="4">Llama-3-8B</td><td rowspan="2">2.25</td><td>Best of 32</td><td>149.85</td><td>432.96</td><td>21.2</td><td>29.1</td><td>28.1</td><td>55.6</td><td>49.8</td><td>36.8</td></tr><tr><td>EvoPress</td><td>23.93</td><td>43.17</td><td>23.6</td><td>46.9</td><td>39.3</td><td>63.6</td><td>56.5</td><td>46.0</td></tr><tr><td rowspan="2">2.5</td><td>Best of 32</td><td>21.65</td><td>23.92</td><td>25.1</td><td>47.6</td><td>41.2</td><td>65.6</td><td>56.2</td><td>47.1</td></tr><tr><td>EvoPress</td><td>13.93</td><td>18.15</td><td>31.7</td><td>61.5</td><td>47.9</td><td>71.7</td><td>64.3</td><td>55.4</td></tr><tr><td rowspan="4">Llama-3.1-8B</td><td rowspan="2">2.25</td><td>Best of 32</td><td>259.61</td><td>181.36</td><td>20.7</td><td>31.9</td><td>30.6</td><td>57.0</td><td>51.9</td><td>38.4</td></tr><tr><td>EvoPress</td><td>22.75</td><td>33.58</td><td>26.7</td><td>48.9</td><td>40.2</td><td>63.4</td><td>55.7</td><td>47.0</td></tr><tr><td rowspan="2">2.5</td><td>Best of 32</td><td>35.33</td><td>37.09</td><td>24.1</td><td>48.4</td><td>41.7</td><td>62.7</td><td>54.5</td><td>46.3</td></tr><tr><td>EvoPress</td><td>11.73</td><td>19.03</td><td>32.2</td><td>63.3</td><td>47.5</td><td>71.8</td><td>62.3</td><td>55.4</td></tr><tr><td rowspan="4">Phi-3-Medium</td><td rowspan="2">2.25</td><td>Best of 32</td><td>14.20</td><td>18.19</td><td>28.9</td><td>46.8</td><td>40.0</td><td>61.8</td><td>53.1</td><td>46.1</td></tr><tr><td>EvoPress</td><td>10.48</td><td>14.60</td><td>36.2</td><td>62.0</td><td>46.6</td><td>66.2</td><td>55.6</td><td>53.3</td></tr><tr><td rowspan="2">2.5</td><td>Best of 32</td><td>8.26</td><td>12.65</td><td>40.5</td><td>69.3</td><td>50.3</td><td>70.9</td><td>61.9</td><td>58.6</td></tr><tr><td>EvoPress</td><td>7.12</td><td>11.23</td><td>44.1</td><td>75.9</td><td>54.1</td><td>73.5</td><td>64.6</td><td>62.4</td></tr></table>{{< /table-caption >}}

> Table 2 presents a comparison of different methods for achieving 70% sparsity in various LLMs, showing that EvoPress outperforms existing techniques in terms of both perplexity and zero-shot accuracy.


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
{{< /gallery >}}