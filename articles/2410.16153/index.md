---
title: "Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages"
summary: "PANGEA: A fully open multilingual, multimodal LLM for 39 languages, outperforming existing models in diverse cultural contexts."
categories: ["AI Generated"]
tags: ["🔖 24-10-21", "🤗 24-10-22"]
showSummary: true
date: 2024-10-21
draft: false
---

### TL;DR


{{< lead >}}

This paper introduces PANGEA, a groundbreaking multilingual and multimodal large language model (LLM). Unlike previous models primarily focused on English and Western contexts, PANGEA excels in handling 39 diverse languages and their associated cultural nuances.  Its training utilized PANGEAINS, a massive 6-million-instruction dataset, ensuring high-quality English instructions and careful machine translations.  Performance was rigorously evaluated on PANGEABENCH, a comprehensive evaluation suite covering 14 datasets across 47 languages.  PANGEA's results demonstrated significantly better performance than current open-source models in multilingual settings, especially when considering cross-cultural contexts. The researchers highlight the significance of balanced English data representation and the number of multimodal training samples, impacting performance.  Crucially, the entire project—data, code, and model—is open-sourced to promote equity and accessibility in multilingual AI development.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.16153" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
PANGEA is a fully open multilingual, multimodal large language model (LLM) trained on a massive dataset spanning 39 languages, significantly outperforming existing open-source models in multilingual settings and diverse cultural contexts. The paper introduces PANGEA, a 7B parameter multilingual, multimodal LLM trained on PANGEAINS, a 6M instruction dataset, and evaluated on PANGEABENCH, a holistic evaluation suite.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} PANGEA, a multilingual, multimodal LLM, significantly outperforms existing open-source models. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} PANGEAINS, a diverse 6M instruction dataset, is crucial for training robust multilingual, multimodal LLMs. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} PANGEABENCH, a holistic evaluation suite, offers a rigorous assessment of multilingual, multimodal LLM capabilities. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's competitive performance in English and superior performance in multilingual scenarios.





![](charts/charts_1_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The chart visualizes the aggregate performance of various multimodal large language models (MLLMs) on the PANGEABENCH benchmark, comparing their performance in English and multilingual scenarios.





{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='1' style='font-size:14px'><tr><td>LAION-Multi</td><td>Heuristic Filtering</td><td>LLM Scoring</td><td>三 三 Data Generation</td><td>Instruction-Response</td></tr><tr><td>MeatLove</td><td>□ Image Size (224-4096px) □ Text Length (5-5000char) □ Aspect Ratio (0.25-3.0) □ NSFW Content (Unlikely) □ Offensive Text □ Deduplication □ CLIP Score (>0.3) □ Language Balance</td><td>□ Informativeness Rate the following alt text on a scale from 1 to 5 based on its quality in describing the image... □ Topic Classify Assign a category to the alt text based on its content. Choose from the following categories... □ Country Classify Decide if the alt textis related to a specific country's culture...</td><td>□ Recaption with Alt Text Please describe the image in detail in {language}. The image might be related to the {country}. The topic might be related to {category}. The previous short caption of the image is {text}. □ Instruction Generation Generate two instruction-response pair based on the visual content of an image. Choose two task from the list below to guide the rewriting process...</td><td>问题1: 分析图像中餐具的选择和摆设如何体现, 韩国饮食文化的特点。 (Q1:Analyze how the choicel and arrangement of tableware in the image reflect the characteristicsofKorean food culture.) 回答1: 图像中的餐具选择和摆设充分展现了韩 国饮食文化的特点。 首先, 黄铜碗碟作为韩式 料理的标志性餐具... (A1: The choice and arrangement oftableware in the image fullyhighlight the characteristics ofKoreanfood culture. First, brass bowls anddishes, as iconic tableware in Korean cuisine...) 问题2: 假设你是一位餐厅经营者, 根据图像中 的餐桌布置, 提出提升顾客用餐体验的策略。 (Q2: Suppose you arearestaurant operator. Basedon the table setting shown in the image, suggest strategies to enhance the customer dining experience.</td></tr></table>{{< /table-caption >}}

> Table 1 presents the overall performance of various multilingual multimodal LLMs on the PANGEABENCH benchmark, highlighting the superior performance of PANGEA-7B compared to existing open-source models.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_23_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a bar chart comparing the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior multilingual performance.


![](figures/figures_27_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a comparison of the aggregate performance of various multimodal LLMs on PANGEABENCH, highlighting PANGEA-7B's competitive performance in English and superior performance in multilingual scenarios.


![](figures/figures_28_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a comparison of the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's competitive performance in English and superior performance in multilingual scenarios.


![](figures/figures_29_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows that PANGEA-7B achieves comparable performance to state-of-the-art open-source models on English benchmarks but significantly outperforms them on multilingual benchmarks.


![](figures/figures_30_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a bar chart comparing the aggregate performance of various multimodal large language models (MLLMs) on a multilingual benchmark, highlighting the superior performance of the PANGEA-7B model in multilingual scenarios compared to English-centric models.


![](figures/figures_31_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a bar chart comparing the aggregate performance of various multilingual and English-centric multimodal large language models (MLLMs) on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance in multilingual scenarios.


![](figures/figures_34_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a comparison of the aggregate performance of various multilingual and multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance in multilingual scenarios.


![](figures/figures_36_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a comparison of the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's competitive performance in English and superior performance in multilingual settings.


![](figures/figures_37_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's comparable English performance and superior multilingual performance.


![](figures/figures_40_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a comparison of the aggregate performance of various multimodal LLMs on PANGEABENCH, highlighting PANGEA-7B's comparable performance to state-of-the-art open-source models in English and significantly superior performance in multilingual settings.


![](figures/figures_42_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a bar chart comparing the aggregate performance of various multilingual and English-centric multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance in multilingual settings.


![](figures/figures_43_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The figure shows a bar chart comparing the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance in multilingual settings.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_2_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The chart shows the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's competitive performance in English and its superior performance in multilingual scenarios.


![](charts/charts_10_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The chart compares the aggregate performance of various multilingual and English-centric multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance in multilingual scenarios.


![](charts/charts_10_1.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The chart compares the aggregate performance of various multilingual and English-centric multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance in multilingual settings.


![](charts/charts_10_2.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The chart visualizes the aggregate performance of various multimodal large language models (MLLMs) on the PANGEABENCH evaluation suite, highlighting PANGEA-7B's competitive performance in English and its superior performance in multilingual settings.


![](charts/charts_11_0.png "🔼 Figure 1: Overview of the aggregate performance of various multimodal LLMs on PANGEABENCH. Our PANGEA-7B demonstrates comparable performance to SoTA open-source models in English settings, while significantly outperforming them in multilingual scenarios.")

> The chart compares the aggregate performance of various multilingual and multimodal large language models (MLLMs) on the PANGEABENCH benchmark, showing PANGEA-7B's competitive performance in English and superior performance in multilingual settings.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='1' style='font-size:14px'><tr><td rowspan="3">Models</td><td rowspan="2" colspan="2">AVG (all)</td><td colspan="4">Multimodal Chat</td><td colspan="4">Cultural Understanding</td></tr><tr><td colspan="2">xChatBench</td><td colspan="2">M-LlavaBench</td><td colspan="2">CVQA</td><td colspan="2">MaRVL</td></tr><tr><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td></tr><tr><td>Gemini-1.5-Pro</td><td>67.1</td><td>62.5</td><td>67.0</td><td>54.4</td><td>103.4</td><td>106.6</td><td>75.9</td><td>75.7</td><td>76.4</td><td>72.0</td></tr><tr><td>GPT4o</td><td>68.6</td><td>64.6</td><td>71.0</td><td>64.4</td><td>104.6</td><td>100.4</td><td>79.1</td><td>79.4</td><td>81.4</td><td>82.1</td></tr><tr><td>Llava-1.5-7B</td><td>45.4</td><td>28.4</td><td>28.5</td><td>11.8</td><td>66.1</td><td>40.8</td><td>48.9</td><td>36.5</td><td>56.2</td><td>53.7</td></tr><tr><td>Llava-Next-7B</td><td>51.1</td><td>32.7</td><td>40.5</td><td>18.9</td><td>78.9</td><td>50.7</td><td>55.7</td><td>42.6</td><td>62.8</td><td>50.9</td></tr><tr><td>Phi-3.5-Vision</td><td>54.0</td><td>35.0</td><td>38.5</td><td>13.2</td><td>70.8</td><td>58.0</td><td>56.3</td><td>42.3</td><td>72.1</td><td>56.5</td></tr><tr><td>Cambrian-8B</td><td>50.9</td><td>36.4</td><td>27.5</td><td>11.3</td><td>78.4</td><td>61.8</td><td>59.7</td><td>47.5</td><td>75.4</td><td>61.8</td></tr><tr><td>Llava-OV-7B</td><td>59.5</td><td>41.3</td><td>51.0</td><td>28.5</td><td>89.7</td><td>55.3</td><td>65.2</td><td>53.7</td><td>72.7</td><td>57.5</td></tr><tr><td>Molmo-7B-D</td><td>55.4</td><td>34.1</td><td>49.5</td><td>21.1</td><td>95.9</td><td>13.8</td><td>59.4</td><td>48.3</td><td>65.3</td><td>54.9</td></tr><tr><td>Llama3.2-11B</td><td>57.2</td><td>41.9</td><td>49.0</td><td>27.8</td><td>93.9</td><td>58.2</td><td>70.2</td><td>61.4</td><td>64.5</td><td>58.1</td></tr><tr><td>PaliGemma-3B</td><td>37.3</td><td>25.8</td><td>6.0</td><td>3.5</td><td>32.1</td><td>31.9</td><td>52.9</td><td>42.9</td><td>56.5</td><td>52.2</td></tr><tr><td>PALO-7B</td><td>46.3</td><td>32.2</td><td>27.0</td><td>11.8</td><td>68.9</td><td>71.2</td><td>50.9</td><td>39.2</td><td>63.3</td><td>54.2</td></tr><tr><td>mBLIP mT0-XL</td><td>35.1</td><td>29.8</td><td>2.5</td><td>0.5</td><td>32.7</td><td>28.2</td><td>40.5</td><td>37.5</td><td>67.3</td><td>66.7</td></tr><tr><td>mBLIP BLOOMZ</td><td>36.1</td><td>30.0</td><td>4.0</td><td>1.6</td><td>43.5</td><td>41.0</td><td>44.9</td><td>36.9</td><td>62.3</td><td>58.6</td></tr><tr><td>PANGEA-7B (Ours)</td><td>59.9</td><td>52.7</td><td>46.0</td><td>35.6</td><td>84.2</td><td>89.5</td><td>64.4</td><td>57.2</td><td>87.0</td><td>79.0</td></tr><tr><td>△ over SoTA Open</td><td>+0.4</td><td>+10.8</td><td>-3.5</td><td>+7.1</td><td>-11.7</td><td>+18.3</td><td>-5.8</td><td>-4.2</td><td>+11.6</td><td>+12.3</td></tr><tr><td rowspan="3">Models</td><td colspan="2">Captioning</td><td colspan="4">Short VQA</td><td colspan="4">Multi-subject Reasoning</td></tr><tr><td colspan="2">XM100</td><td colspan="2">xGQA</td><td colspan="2">MaXM</td><td colspan="2">xMMMU</td><td colspan="2">M3Exam</td></tr><tr><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td></tr><tr><td>Gemini-1.5-Pro</td><td>27.6</td><td>19.1</td><td>54.2</td><td>48.7</td><td>56.4</td><td>63.5</td><td>65.8</td><td>57.7</td><td>77.4</td><td>64.7</td></tr><tr><td>GPT4o</td><td>27.7</td><td>19.1</td><td>55.8</td><td>51.0</td><td>60.7</td><td>65.4</td><td>69.1</td><td>58.3</td><td>68.0</td><td>61.0</td></tr><tr><td>Llava-1.5-7B</td><td>28.6</td><td>1.1</td><td>62.0</td><td>30.6</td><td>49.8</td><td>20.4</td><td>36.2</td><td>31.5</td><td>32.3</td><td>29</td></tr><tr><td>Llava-Next-7B</td><td>29.3</td><td>9.4</td><td>64.8</td><td>37.8</td><td>54.9</td><td>21.4</td><td>36.7</td><td>34.3</td><td>36.5</td><td>28.4</td></tr><tr><td>Phi-3.5-Vision</td><td>30.2</td><td>5.2</td><td>64.7</td><td>38.4</td><td>55.3</td><td>25.0</td><td>42.6</td><td>38.8</td><td>55.8</td><td>37.2</td></tr><tr><td>Cambrian-8B</td><td>20.6</td><td>9.9</td><td>64.6</td><td>39.8</td><td>55.3</td><td>28.7</td><td>41.8</td><td>33.2</td><td>34.7</td><td>33.4</td></tr><tr><td>Llava-OV-7B</td><td>30.6</td><td>7.0</td><td>64.4</td><td>48.2</td><td>54.9</td><td>34.8</td><td>46.3</td><td>41.0</td><td>60.4</td><td>45.8</td></tr><tr><td>Molmo-7B-D</td><td>22.1</td><td>9.1</td><td>51.5</td><td>43.0</td><td>52.9</td><td>37.5</td><td>44.5</td><td>40.4</td><td>57.1</td><td>39.1</td></tr><tr><td>Llama3.2-11B</td><td>27.6</td><td>4.5</td><td>55.6</td><td>45.4</td><td>55.3</td><td>43.9</td><td>46.5</td><td>41.4</td><td>51.8</td><td>36.6</td></tr><tr><td>PaliGemma-3B</td><td>18.7</td><td>0.8</td><td>59.7</td><td>30.5</td><td>47.9</td><td>19.9</td><td>26.3</td><td>25.2</td><td>36.0</td><td>25.6</td></tr><tr><td>PALO-7B</td><td>30.4</td><td>0.8</td><td>60.5</td><td>37.8</td><td>51.4</td><td>16.3</td><td>33.1</td><td>30.5</td><td>30.8</td><td>27.8</td></tr><tr><td>mBLIP mT0-XL</td><td>31.9</td><td>3.1</td><td>44.2</td><td>39.9</td><td>44.7</td><td>36.8</td><td>29.3</td><td>30.4</td><td>22.8</td><td>25</td></tr><tr><td>mBLIP BLOOMZ</td><td>22.5</td><td>10.3</td><td>43.3</td><td>36.9</td><td>44.7</td><td>24.8</td><td>29.2</td><td>30.8</td><td>30.3</td><td>29.5</td></tr><tr><td>PANGEA-7B (Ours)</td><td>30.4</td><td>14.2</td><td>64.7</td><td>60.2</td><td>55.3</td><td>53.2</td><td>45.7</td><td>43.7</td><td>61.4</td><td>42.1</td></tr><tr><td>△ over Best Open Model</td><td>-0.2</td><td>+3.9</td><td>-0.1</td><td>+12.0</td><td>0.0</td><td>+9.3</td><td>-0.8</td><td>+2.3</td><td>+1.0</td><td>-3.7</td></tr></table>{{< /table-caption >}}

> Table 1 presents the overall performance comparison of various multilingual multimodal large language models (MLLMs) on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance across various tasks and languages.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='1' style='font-size:14px'><tr><td rowspan="2">Models</td><td colspan="2">AVG (all)</td><td colspan="2">FLORES-Sub</td><td colspan="2">TyDiQA</td><td colspan="2">XStoryCloze</td><td colspan="2">MGSM</td><td colspan="2">MMMLU</td></tr><tr><td>en</td><td>mul</td><td>x→en</td><td>en→x</td><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td><td>en</td><td>mul</td></tr><tr><td>Vicuna-1.5-7B</td><td>52.1</td><td>38.7</td><td>55.6</td><td>42.4</td><td>59.7</td><td>52.7</td><td>78.1</td><td>57.4</td><td>17.6</td><td>6.4</td><td>49.5</td><td>34.7</td></tr><tr><td>Qwen2-7B-Instruct</td><td>66.6</td><td>54.5</td><td>61.8</td><td>46.0</td><td>72.2</td><td>71.2</td><td>80.3</td><td>61.9</td><td>48.8</td><td>40.4</td><td>70.1</td><td>53.1</td></tr><tr><td>Llava-1.5-7B</td><td>53.1</td><td>39.0</td><td>54.7</td><td>41.5</td><td>66.8</td><td>52.8</td><td>79.1</td><td>57.6</td><td>14.8</td><td>7.6</td><td>50.2</td><td>35.7</td></tr><tr><td>Llava-Next-7B</td><td>54.0</td><td>38.9</td><td>54.8</td><td>41.4</td><td>68.3</td><td>52.1</td><td>79.1</td><td>57.1</td><td>15.6</td><td>7.5</td><td>52.1</td><td>36.5</td></tr><tr><td>Phi-3.5-Vision</td><td>60.7</td><td>41.7</td><td>28.5</td><td>32.5</td><td>75.9</td><td>51.3</td><td>77.9</td><td>54.8</td><td>59.2</td><td>33.1</td><td>62.0</td><td>36.7</td></tr><tr><td>PALO-7B</td><td>52.0</td><td>37.5</td><td>52.9</td><td>40.4</td><td>69.4</td><td>50.8</td><td>77.4</td><td>57.2</td><td>13.6</td><td>5.8</td><td>46.7</td><td>33.4</td></tr><tr><td>PANGEA-7B (Ours)</td><td>72.8</td><td>54.3</td><td>60.7</td><td>44.9</td><td>73.7</td><td>66.0</td><td>79.1</td><td>61.2</td><td>82.0</td><td>47.4</td><td>68.4</td><td>52.2</td></tr></table>{{< /table-caption >}}

> Table 1 presents a comparison of the aggregate performance of various multimodal LLMs on the PANGEABENCH benchmark, showcasing PANGEA-7B's superior performance in multilingual scenarios.


{{< table-caption caption="🔽 Table 3: Comparison of models on the xChat dataset across different languages." >}}
<table id='3' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Spanish</td><td>Hindi</td><td>Indonesian</td><td>Japanese</td><td>Korean</td><td>Chinese</td></tr><tr><td>Gemini-1.5-Pro</td><td>71.0</td><td>65.6</td><td>66.0</td><td>62.0</td><td>65.5</td><td>68.0</td><td>66.5</td><td>65.5</td></tr><tr><td>GPT4o</td><td>67.0</td><td>65.1</td><td>66.0</td><td>64.0</td><td>65.0</td><td>66.5</td><td>67.5</td><td>61.5</td></tr><tr><td>Llava-1.5-7B</td><td>22.5</td><td>16.7</td><td>22.5</td><td>3.5</td><td>18.0</td><td>23.0</td><td>12.0</td><td>21.0</td></tr><tr><td>Llava-Next-7B</td><td>40.5</td><td>20.4</td><td>33.0</td><td>1.5</td><td>19.0</td><td>25.0</td><td>15.0</td><td>29.0</td></tr><tr><td>Phi-3.5-Vision</td><td>38.5</td><td>21.1</td><td>37.0</td><td>11.5</td><td>10.5</td><td>31.0</td><td>12.5</td><td>24.0</td></tr><tr><td>Cambrian-8B</td><td>27.5</td><td>15.8</td><td>22.5</td><td>4.0</td><td>20.0</td><td>20.0</td><td>10.5</td><td>18.0</td></tr><tr><td>Llava-OV-7B</td><td>51.0</td><td>33.1</td><td>45.5</td><td>6.5</td><td>42.0</td><td>36.5</td><td>26.0</td><td>42.0</td></tr><tr><td>Molmo-7B-D</td><td>49.5</td><td>34.7</td><td>45.0</td><td>19.5</td><td>36.5</td><td>36.0</td><td>35.0</td><td>46.0</td></tr><tr><td>Llama3.2-11B</td><td>49.0</td><td>31.3</td><td>42.5</td><td>19.5</td><td>45.0</td><td>26.0</td><td>21.0</td><td>43.0</td></tr><tr><td>PaliGemma-3B</td><td>6.0</td><td>3.8</td><td>4.5</td><td>0.5</td><td>6.5</td><td>6.5</td><td>2.0</td><td>3.0</td></tr><tr><td>PALO-7B</td><td>27.0</td><td>16.2</td><td>23.0</td><td>3.0</td><td>19.0</td><td>20.0</td><td>13.5</td><td>18.5</td></tr><tr><td>mBLIP mT0-XL</td><td>2.5</td><td>0.5</td><td>0.0</td><td>0.0</td><td>0.5</td><td>2.0</td><td>0.5</td><td>0.0</td></tr><tr><td>mBLIP BLOOMZ-7B</td><td>4.0</td><td>1.7</td><td>2.0</td><td>2.5</td><td>2.5</td><td>0.0</td><td>0.0</td><td>3.0</td></tr><tr><td>PANGEA-7B (Ours)</td><td>46.0</td><td>35.8</td><td>43.5</td><td>23.5</td><td>34.5</td><td>39.0</td><td>33.5</td><td>40.5</td></tr></table>{{< /table-caption >}}

> Table 3 presents a comparison of various models' performance on the xChat benchmark across multiple languages, including English, Spanish, Hindi, Indonesian, Japanese, Korean, and Chinese.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='7' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Arabic</td><td>Bengali</td><td>Chinese</td><td>French</td><td>Hindi</td><td>Japanese</td><td>Russian</td><td>Spanish</td><td>Urdu</td></tr><tr><td>Gemini-1.5-Pro</td><td>103.4</td><td>106.6</td><td>112.9</td><td>117.1</td><td>104.1</td><td>115.5</td><td>106.2</td><td>118.1</td><td>95.7</td><td>88.2</td><td>101.6</td></tr><tr><td>GPT4o</td><td>104.6</td><td>100.4</td><td>98.3</td><td>111.9</td><td>96.5</td><td>101.1</td><td>99.7</td><td>104.0</td><td>88.5</td><td>100.9</td><td>102.5</td></tr><tr><td>Llava-1.5-7B</td><td>66.1</td><td>40.8</td><td>26.4</td><td>11.9</td><td>50.7</td><td>63.8</td><td>23.2</td><td>70.0</td><td>46.5</td><td>59.2</td><td>15.4</td></tr><tr><td>Llava-Next-7B</td><td>78.9</td><td>50.7</td><td>24.9</td><td>11.2</td><td>72.8</td><td>91.4</td><td>18.0</td><td>70.1</td><td>71.8</td><td>82.9</td><td>13.4</td></tr><tr><td>Phi-3.5-Vision</td><td>70.8</td><td>58.0</td><td>50.1</td><td>35.1</td><td>69.2</td><td>86.0</td><td>35.9</td><td>63.0</td><td>67.6</td><td>75.6</td><td>39.3</td></tr><tr><td>Cambrian-8B</td><td>78.4</td><td>61.8</td><td>54.1</td><td>35.4</td><td>80.9</td><td>87.3</td><td>44.2</td><td>64.4</td><td>76.4</td><td>90.3</td><td>23.3</td></tr><tr><td>Llava-OV-7B</td><td>89.7</td><td>55.3</td><td>45.5</td><td>33.8</td><td>90.0</td><td>89.4</td><td>35.3</td><td>70.3</td><td>44.7</td><td>75.5</td><td>13.3</td></tr><tr><td>Molmo-7B-D</td><td>95.9</td><td>13.8</td><td>10.1</td><td>4.2</td><td>0.3</td><td>59.6</td><td>5.5</td><td>6.0</td><td>8.7</td><td>29.5</td><td>0.0</td></tr><tr><td>Llama3.2-11B</td><td>93.9</td><td>58.2</td><td>39.4</td><td>48.1</td><td>47.2</td><td>85.6</td><td>67.8</td><td>53.7</td><td>68.5</td><td>77.8</td><td>35.3</td></tr><tr><td>PaliGemma-3B</td><td>32.1</td><td>31.9</td><td>37.3</td><td>38.2</td><td>29.1</td><td>30.0</td><td>35.8</td><td>33.4</td><td>26.1</td><td>32.3</td><td>25.1</td></tr><tr><td>PALO-7B</td><td>68.9</td><td>71.2</td><td>79.1</td><td>54.6</td><td>71.5</td><td>83.9</td><td>61.9</td><td>66.6</td><td>80.9</td><td>74.4</td><td>68.2</td></tr><tr><td>mBLIP mTO-XL</td><td>32.7</td><td>28.2</td><td>33.7</td><td>26.2</td><td>3.6</td><td>39.8</td><td>26.9</td><td>26.8</td><td>34.1</td><td>36.9</td><td>26.0</td></tr><tr><td>mBLIP BLOOMZ-7B</td><td>43.5</td><td>41.0</td><td>48.1</td><td>44.1</td><td>30.6</td><td>53.3</td><td>39.1</td><td>29.8</td><td>38.1</td><td>51.5</td><td>34.0</td></tr><tr><td>PANGEA-7B (Ours)</td><td>84.2</td><td>89.5</td><td>91.0</td><td>94.9</td><td>94.4</td><td>93.8</td><td>84.9</td><td>92.8</td><td>91.2</td><td>87.4</td><td>75.5</td></tr></table>{{< /table-caption >}}

> Table 1 presents the overall performance of various multilingual multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance compared to existing open-source models.


{{< table-caption caption="🔽 Table 7: Comparison of models on the MaRVL dataset across different languages." >}}
<table id='1' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Indonesian</td><td>Swahili</td><td>Tamil</td><td>Turkish</td><td>Chinese</td></tr><tr><td>GPT4o</td><td>81.8</td><td>82.3</td><td>81.9</td><td>80.8</td><td>80.2</td><td>86.4</td><td>82.1</td></tr><tr><td>Gemini-1.5-Pro</td><td>76.4</td><td>72.0</td><td>71.2</td><td>67.8</td><td>70.0</td><td>75.4</td><td>75.8</td></tr><tr><td>Llava-1.5-7B</td><td>56.2</td><td>53.7</td><td>56.1</td><td>49.8</td><td>49.7</td><td>55.4</td><td>57.5</td></tr><tr><td>Llava-Next-7B</td><td>62.8</td><td>50.9</td><td>52.2</td><td>50.6</td><td>50.5</td><td>50.4</td><td>50.6</td></tr><tr><td>Phi-3.5-Vision</td><td>72.1</td><td>56.5</td><td>58.6</td><td>51.4</td><td>52.0</td><td>58.6</td><td>61.7</td></tr><tr><td>Cambrian-8B</td><td>75.4</td><td>61.8</td><td>64.7</td><td>53.6</td><td>56.7</td><td>65.2</td><td>68.9</td></tr><tr><td>Llava-OV-7B</td><td>72.7</td><td>57.5</td><td>60.9</td><td>51.2</td><td>51.9</td><td>63.5</td><td>60.0</td></tr><tr><td>Molmo-7B-D</td><td>65.3</td><td>54.9</td><td>61.1</td><td>49.6</td><td>49.6</td><td>52.2</td><td>62.2</td></tr><tr><td>Llama3.2-11B</td><td>64.5</td><td>58.1</td><td>62.7</td><td>52.4</td><td>54.0</td><td>61.6</td><td>59.5</td></tr><tr><td>PaliGemma-3b</td><td>56.5</td><td>52.2</td><td>53.4</td><td>49.6</td><td>50.5</td><td>56.3</td><td>51.3</td></tr><tr><td>PALO-7B</td><td>63.3</td><td>54.2</td><td>58.3</td><td>50.6</td><td>51.9</td><td>54.9</td><td>55.3</td></tr><tr><td>mBLIP mT0-XL</td><td>67.3</td><td>66.7</td><td>64.9</td><td>64.8</td><td>69.7</td><td>68.1</td><td>65.9</td></tr><tr><td>mBLIP BLOOMZ-7B</td><td>62.3</td><td>58.6</td><td>59.1</td><td>56.2</td><td>60.3</td><td>57.7</td><td>59.7</td></tr><tr><td>PANGEA-7B</td><td>87.0</td><td>79.0</td><td>81.3</td><td>75.1</td><td>69.4</td><td>84.8</td><td>84.3</td></tr></table>{{< /table-caption >}}

> Table 7 presents a comparison of various large language models' performance across different languages on the MaRVL benchmark, a dataset designed for evaluating cultural understanding in multilingual scenarios.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='1' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Arabic</td><td>Bengali</td><td>Czech</td><td>Danish</td><td>German</td><td>Greek</td></tr><tr><td>Gemini-1.5-Pro</td><td>27.6</td><td>19.1</td><td>1.7</td><td>7.5</td><td>25.9</td><td>32.8</td><td>27.6</td><td>5.0</td></tr><tr><td>GPT4o</td><td>27.7</td><td>19.1</td><td>15.8</td><td>13.5</td><td>21.1</td><td>25.3</td><td>19.3 1.9</td><td>21.1</td></tr><tr><td>Llava-1.5-7B</td><td>28.6 0.0 PALO-7B</td><td>1.1</td><td>0.0</td><td>0.0</td><td>2.1</td><td>1.0</td><td>3.1</td><td>0.0</td></tr><tr><td>Llava-Next-7B</td><td>29.3</td><td>9.4 0.0</td><td>5.6</td><td>0.1</td><td>12.1</td><td>15.7 2.0 0.9</td><td>14.4</td><td>4.2</td></tr><tr><td>Phi-3.5- Vision</td><td>30.2</td><td>5.2</td><td>0.4</td><td>2.4</td><td>16.6</td><td>16.2</td><td>0.0</td><td>20.7</td></tr><tr><td>Cambrian-8B</td><td>20.6</td><td>9.9</td><td>1.4</td><td>6.6</td><td>7.4</td><td>15.1</td><td>15.5</td><td>4.4</td></tr><tr><td>Llava-OV-7B</td><td>30.6 0.5 0.0</td><td>7.0</td><td>0.2</td><td>0.6</td><td>5.2 0.0</td><td>16.8</td><td>14.0 0.0</td><td>0.4</td></tr><tr><td>Molmo-7B-D</td><td>22.1</td><td>9.1</td><td>5.4</td><td>7.9</td><td>5.7</td><td>13.8</td><td>12.2</td><td>4.2</td></tr><tr><td>Llama3.2-11B</td><td>27.6</td><td>4.5</td><td>0.0</td><td>0.0</td><td>1.5</td><td>11.8</td><td>4.6</td><td>1.2</td></tr><tr><td>PaliGemma-3B</td><td>18.7</td><td>0.8</td><td>0.0</td><td>0.0</td><td>1.1</td><td>3.1</td><td>2.7</td><td>0.0</td></tr><tr><td>PALO-7B</td><td>30.4</td><td>0.8</td><td>0.0</td><td>0.0</td><td>2.0</td><td>1.0</td><td>2.7</td><td>0.0</td></tr><tr><td>mBLIP mT0-XL</td><td>31.9</td><td>3.1</td><td>3.2</td><td>1.6</td><td>3.7</td><td>2.1</td><td>2.9</td><td>3.1</td></tr><tr><td>mBLIP BLOOMZ</td><td>22.5</td><td>10.3</td><td>9.5</td><td>6.4</td><td>11.5</td><td>15.9</td><td>14.5</td><td>10.9</td></tr><tr><td>PANGEA-7B (Ours)</td><td>30.8</td><td>14.2</td><td>18.1</td><td>16.4</td><td>16.2</td><td>20.7</td><td>20.6</td><td>11.2</td></tr><tr><td>Models</td><td>Spanish</td><td>Persian</td><td>Finnish</td><td>Filipino</td><td>French</td><td>Hebrew</td><td>Hindi</td><td>Croatian 0.0</td></tr><tr><td>Gemini-1.5-Pro</td><td>39.5</td><td>4.2</td><td>29.0</td><td>28.7</td><td>42.4</td><td>4.3</td><td>2.2</td><td>33.8</td></tr><tr><td>GPT4o 0.0 PANGEA-7B</td><td>28.3 Models Thai Vietnamese</td><td>26.6</td><td>13.1</td><td>26.4</td><td>23.1</td><td>20.4</td><td>17.0 Llama3.2-11B</td><td>19.4</td></tr><tr><td>Llava-1.5-7B</td><td>3.7 Chinese Gemini-1.5-Pro 0.0 0.0</td><td>0.0</td><td>0.4</td><td>1.1</td><td>2.0</td><td>0.1</td><td>0.0</td><td>0.3 Ukrainian</td></tr><tr><td>Llava-Next-7B</td><td>23.6 0.2</td><td>9.4</td><td>5.5</td><td>9.3</td><td>23.0</td><td>2.7</td><td>10.2</td><td>7.5 0.0</td></tr><tr><td>Phi-3.5-Vision</td><td>20.7 0.0 5.8 0.2 3.8</td><td>0.0 1.1 0.0</td><td>1.0 BLOOMZ 14.5 14.5</td><td>1.7</td><td>21.2</td><td>0.3 5.8</td><td>0.0</td><td>0.5</td></tr><tr><td>Cambrian-8B</td><td>18.6 2.7 16.5 8.4</td><td>9.6 2.3 13.7</td><td>5.1 (Ours) 16.2 20.9 19.4</td><td>19.6 PANGEA-7B</td><td>18.3</td><td>3.8 mBLIP 3.0</td><td>6.8</td><td>7.2</td></tr><tr><td>Llava-OV-7B</td><td>24.9</td><td>3.8 21.4</td><td>1.5 18.7 mBLIP BLOOMZ (Ours)</td><td>4.2</td><td>22.0</td><td>0.0 5.8</td><td>4.4</td><td>7.2</td></tr><tr><td>Molmo-7B-D Turkish</td><td>19.8 18.6</td><td>11.3</td><td>3.1</td><td>13.0</td><td>19.8</td><td>8.3 0.0</td><td>9.4</td><td>6.9</td></tr><tr><td>Llama3.2-11B 0.9</td><td>10.2</td><td>0.0</td><td>2.4</td><td>8.4</td><td>12.0</td><td>0.0</td><td>0.2 PALO-7B</td><td>0.7</td></tr><tr><td>PaliGemma-3B</td><td>0.7 3.5</td><td>0.0</td><td>0.1</td><td>0.1 0.1</td><td>0.6</td><td>0.0</td><td>0.0 mBLIP mT0-XL</td><td>1.3</td></tr><tr><td>PALO-7B</td><td>1.5 0.4 11.8</td><td>0.0 5.5</td><td>0.4 8.2</td><td>0.9 1.0 0.0</td><td>2.1</td><td>0.0 0.6 10.1</td><td>0.0</td><td>0.2 28.1</td></tr><tr><td>mBLIP mTO-XL</td><td>8.3</td><td></td><td>1.7</td><td>2.8 PaliGemma-3B 0.9</td><td>6.4</td><td>4.0 0.0</td><td>1.8 0.3 6.3</td><td>0.9 0.6 7.4 0.1</td></tr><tr><td>mBLIP BLOOMZ</td><td>18.9</td><td>13.8</td><td>4.8</td><td>7.7</td><td>19.1 1.3</td><td>7.5 0.1</td><td>10.1 0.0</td><td>3.2</td></tr><tr><td>PANGEA-7B (Ours)</td><td>26.2 Hungarian</td><td>19.3 0.0 0.0 0.0</td><td>3.8 Llava-Next-7B</td><td>18.9</td><td>26.7 1.7</td><td>18.2</td><td>17.4</td><td>10.8</td></tr><tr><td>Models</td><td></td><td>Indonesian</td><td>Italian Phi-3.5-Vision 0.5</td><td>Japanese</td><td>Korean</td><td>Maori</td><td>Dutch 27.7</td><td>Norwegian 36.7</td></tr><tr><td>Gemini-1.5-Pro</td><td>37.2</td><td>55.4</td><td>27.6 0.4</td><td>1.2 Cambrian-8B 5.9 17.8</td><td>8.2 0.9</td><td>3.8</td><td></td><td></td></tr><tr><td>GPT4o 9.3</td><td>21.8 0.0</td><td>28.4</td><td>21.0</td><td>0.0</td><td>11.1 0.4</td><td>26.8</td><td>26.4</td><td>24.7</td></tr><tr><td>Llava-1.5-7B 0.0</td><td>3.3 9.3 17.6</td><td>0.9 14.7</td><td>4.3</td><td>0.0 0.0</td><td>0.0</td><td>0.2 9.2</td><td>2.9</td><td>3.7 16.3</td></tr><tr><td>Llava-Next-7B Phi-3.5-Vision</td><td>3.4 0.0 0.0</td><td>3.2</td><td>17.6</td><td>4.2</td><td>5.2 0.3</td><td>0.2</td><td>23.8 17.2</td><td>14.1</td></tr><tr><td>Cambrian-8B</td><td>6.6</td><td>15.7</td><td>17.5 15.5</td><td>1.6 7.2</td><td>2.0 2.2 0.0</td><td>3.2</td><td>20.3</td><td>16.0</td></tr><tr><td>Llava-OV-7B</td><td>3.6</td><td>16.4</td><td>12.8</td><td>0.6</td><td>0.0 11.3</td><td>1.7</td><td>24.7</td><td>13.9</td></tr><tr><td>Molmo-7B-D</td><td>3.5</td><td>17.2</td><td>17.8</td><td>5.2</td><td>2.4</td><td>7.5 Llava-OV-7B 0.0 0.0 0.0 0.0 2.9 0.0 0.0 0.0</td><td>15.7 GPT4o 0.0</td><td>13.8</td></tr><tr><td>Llama3.2-11B</td><td>12.7</td><td>1.2 0.8 16.9</td><td>16.0</td><td>0.0</td><td>0.0</td><td>9.3</td><td>22.0 30.9 Llava-1.5-7B</td><td>1.1</td></tr><tr><td>PaliGemma-3B</td><td>2.0</td><td>0.2</td><td>1.8</td><td>0.0</td><td>0.0</td><td>4.0</td><td>2.6</td><td>2.3</td></tr><tr><td>PALO-7B</td><td>3.4</td><td>1.1</td><td>3.2</td><td>0.0</td><td>0.0</td><td>0.1</td><td>3.5</td><td>0.7 0.0</td></tr><tr><td>mBLIP mT0-XL</td><td>2.8 0.0 2.2 0.0 0.0 0.3 0.0 4.9</td><td>6.0</td><td>2.8</td><td>0.3</td><td>2.1</td><td>1.5</td><td>3.4</td><td>3.1</td></tr><tr><td>mBLIP BLOOMZ Llama3.2-11B</td><td>11.8</td><td>16.0</td><td>16.5 0.0 0.0 0.0 0.0 PaliGemma-3B 0.5</td><td>0.0</td><td>4.5</td><td>0.1</td><td>18.2</td><td>14.5</td></tr><tr><td>PANGEA-7B (Ours)</td><td>7.7</td><td>27.9</td><td>22.9 0.0 0.2</td><td>2.1</td><td>8.1</td><td>0.7 0.2 0.0 0.0 0.1 0.0 mBLIP mT0-XL 0.0</td><td>26.6</td><td>24.9</td></tr><tr><td>Models</td><td>Polish</td><td>Portuguese</td><td>Quechua</td><td>Romanian</td><td>Russian</td><td>Swedish 3.9 2.0 7.1 0.0</td><td>Swahili</td><td>Telugu</td></tr><tr><td>Gemini-1.5-Pro</td><td>35.5</td><td>35.7</td><td>0.7</td><td>31.2</td><td>32.4</td><td>37.8 1.9</td><td>10.7</td><td>0.0 Molmo-7B-D</td></tr><tr><td>GPT4o</td><td>22.2</td><td>28.0</td><td>4.4</td><td>19.1</td><td>20.7</td><td>26.0</td><td>20.0</td><td>12.5</td></tr><tr><td>Llava-1.5-7B</td><td>0.8</td><td>2.5</td><td>0.0</td><td>1.6</td><td>0.5</td><td>2.0</td><td>0.1 2.9</td><td>0.0</td></tr><tr><td>Llava-Next-7B</td><td>13.5</td><td>21.3</td><td>0.0 0.8</td><td>11.5</td><td>13.5</td><td>16.0</td><td>3.2</td><td>0.0</td></tr><tr><td>Phi-3.5-Vision 0.0</td><td>1.0</td><td>21.0 0.5 3.7</td><td>0.4</td><td>3.2</td><td>0.7</td><td>12.5</td><td>0.4 3.7</td><td>0.0 2.3</td></tr><td>Cambrian-8B Llava-OV-7B Molmo-7B-D</td><td>9.3 7.4</td><td>17.5 24.6 16.2 3.1</td><td>0.0 0.0</td><td>13.4 6.8 11.6</td><td>11.3 5.5 12.3</td><td>17.9 15.0 2.0 14.1</td></table>{{< /table-caption >}}

> Table 1 presents a comparison of the overall performance of various multilingual multimodal large language models (MLLMs) on the PANGEABENCH benchmark, highlighting the superior performance of the PANGEA-7B model.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='1' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Bengali</td><td>German</td><td>Indonesian</td><td>Korean</td><td>Portuguese</td><td>Russian</td><td>Chinese</td></tr><tr><td>Gemini-1.5-Pro</td><td>54.2</td><td>48.7</td><td>49.4</td><td>50.2</td><td>48.6</td><td>46.4</td><td>51.2</td><td>44.8</td><td>50.2</td></tr><tr><td>GPT4o</td><td>55.8</td><td>51.0</td><td>49.4</td><td>52.6</td><td>50.4</td><td>51.0</td><td>52.2</td><td>50.0</td><td>51.4</td></tr><tr><td>Llava-1.5-7B</td><td>62.0</td><td>30.7</td><td>15.6</td><td>28.4</td><td>33.4</td><td>38.2</td><td>27.5</td><td>33.1</td><td>38.4</td></tr><tr><td>Llava-Next-7B</td><td>64.8</td><td>37.8</td><td>11.5</td><td>41.5</td><td>37.3</td><td>42.5</td><td>39.8</td><td>43.5</td><td>48.2</td></tr><tr><td>Phi-3.5-Vision</td><td>64.7</td><td>38.4</td><td>7.7</td><td>51.4</td><td>36.0</td><td>36.3</td><td>49.6</td><td>46.2</td><td>41.4</td></tr><tr><td>Cambrian-8B</td><td>64.6</td><td>39.8</td><td>32.3</td><td>44.6</td><td>36.0</td><td>43.6</td><td>41.6</td><td>44.2</td><td>36.2</td></tr><tr><td>Llava-OV-7B</td><td>64.4</td><td>48.2</td><td>41.8</td><td>49.2</td><td>48.8</td><td>45.3</td><td>52.4</td><td>54.0</td><td>45.9</td></tr><tr><td>Molmo-7B-D</td><td>51.5</td><td>43.0</td><td>25.6</td><td>45.9</td><td>44.9</td><td>44.2</td><td>46.5</td><td>45.6</td><td>48.1</td></tr><tr><td>Llama3.2-11B</td><td>55.6</td><td>45.4</td><td>42.9</td><td>46.7</td><td>46.2</td><td>44.5</td><td>46.5</td><td>44.7</td><td>46.1</td></tr><tr><td>PaliGemma-3B</td><td>59.7</td><td>30.5</td><td>13.3</td><td>44.5</td><td>21.3</td><td>22.8</td><td>34.7</td><td>35.8</td><td>41.2</td></tr><tr><td>PALO-7B</td><td>60.5</td><td>37.8</td><td>42.2</td><td>39.1</td><td>36.8</td><td>41.7</td><td>31.7</td><td>27.0</td><td>46.5</td></tr><tr><td>mBLIP mT0-XL</td><td>44.2</td><td>39.9</td><td>39.1</td><td>41.1</td><td>39.1</td><td>39.7</td><td>40.7</td><td>40.2</td><td>39.4</td></tr><tr><td>mBLIP BLOOMZ-7B</td><td>43.3</td><td>36.9</td><td>37.7</td><td>36.3</td><td>39.3</td><td>28.5</td><td>40.7</td><td>36.6</td><td>39.1</td></tr><tr><td>PANGEA-7B (Ours)</td><td>64.7</td><td>60.2</td><td>58.9</td><td>61.6</td><td>60.1</td><td>58.9</td><td>61.8</td><td>60.4</td><td>59.6</td></tr></table>{{< /table-caption >}}

> Table 1 presents a comparison of the overall performance of various multilingual multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='3' style='font-size:16px'><tr><td>Models</td><td>English</td><td>Multi</td><td>French</td><td>Hindi</td><td>Hebrew</td><td>Romanian</td><td>Thai</td><td>Chinese</td></tr><tr><td>Gemini-1.5-Pro</td><td>56.4</td><td>63.5</td><td>60.2</td><td>66.5</td><td>65.7</td><td>57.4</td><td>73.9</td><td>57.4</td></tr><tr><td>GPT4o</td><td>60.7</td><td>65.4</td><td>59.8</td><td>68.8</td><td>70.0</td><td>61.3</td><td>76.5</td><td>56.3</td></tr><tr><td>Llava-1.5-7B</td><td>49.8</td><td>20.4</td><td>32.2</td><td>17.3</td><td>12.9</td><td>15.1</td><td>17.2</td><td>27.8</td></tr><tr><td>Llava-Next-7B</td><td>54.9</td><td>21.4</td><td>33.7</td><td>16.2</td><td>10.7</td><td>15.5</td><td>18.3</td><td>33.9</td></tr><tr><td>Phi-3.5-Vision</td><td>55.3</td><td>25.0</td><td>38.3</td><td>31.9</td><td>17.5</td><td>10.9</td><td>24.3</td><td>27.4</td></tr><tr><td>Cambrian-8B</td><td>55.3</td><td>28.7</td><td>41.7</td><td>23.8</td><td>17.1</td><td>32.0</td><td>25.7</td><td>31.8</td></tr><tr><td>Llava-OV-7B</td><td>54.9</td><td>34.8</td><td>37.9</td><td>31.9</td><td>17.8</td><td>30.2</td><td>53.0</td><td>37.9</td></tr><tr><td>Molmo-7B-D</td><td>52.9</td><td>37.5</td><td>45.5</td><td>33.5</td><td>30.7</td><td>28.9</td><td>46.3</td><td>40.4</td></tr><tr><td>Llama3.2-11B</td><td>55.3</td><td>43.9</td><td>48.1</td><td>50.4</td><td>41.8</td><td>36.6</td><td>56.7</td><td>30.0</td></tr><tr><td>PaliGemma-3B</td><td>47.9</td><td>19.9</td><td>8.0</td><td>36.5</td><td>19.3</td><td>13.4</td><td>31.3</td><td>10.8</td></tr><tr><td>PALO-7B</td><td>51.4</td><td>16.3</td><td>33.7</td><td>15.8</td><td>12.1</td><td>11.3</td><td>14.6</td><td>10.5</td></tr><tr><td>mBLIP mT0-XL</td><td>44.7</td><td>36.8</td><td>36.0</td><td>42.7</td><td>28.9</td><td>30.3</td><td>56.3</td><td>26.4</td></tr><tr><td>mBLIP BLOOMZ-7B</td><td>44.7</td><td>24.8</td><td>33.0</td><td>47.3</td><td>8.9</td><td>16.9</td><td>9.7</td><td>33.2</td></tr><tr><td>PANGEA-7B (Ours)</td><td>48.6</td><td>34.3</td><td>36.4</td><td>40.4</td><td>36.4</td><td>33.1</td><td>36.2</td><td>23.1</td></tr></table>{{< /table-caption >}}

> Table 1 presents the overall performance of various multilingual multimodal LLMs on the PANGEABENCH benchmarks, highlighting the superior performance of PANGEA-7B compared to existing open-source models.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='5' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Arabic</td><td>French</td><td>Hindi</td><td>Indonesian</td><td>Japanese</td><td>Portuguese</td></tr><tr><td>Gemini-1.5-Pro (0801)</td><td>65.8</td><td>57.7</td><td>57.7</td><td>58.1</td><td>55.5</td><td>60.2</td><td>55.0</td><td>59.6</td></tr><tr><td>GPT4o (0513)</td><td>69.1</td><td>58.3</td><td>56.7</td><td>58.1</td><td>58.1</td><td>59.9</td><td>58.0</td><td>58.9</td></tr><tr><td>Llava-1.5-7B</td><td>36.2</td><td>31.5</td><td>29.5</td><td>34.9</td><td>27.5</td><td>31.6</td><td>32.0</td><td>33.7</td></tr><tr><td>Llava-Next-7B</td><td>36.7</td><td>34.3</td><td>30.5</td><td>35.6</td><td>30.9</td><td>37.0</td><td>34.9</td><td>37.0</td></tr><tr><td>Phi-3.5-Vision</td><td>42.6</td><td>38.8</td><td>35.6</td><td>44.0</td><td>30.9</td><td>36.7</td><td>37.9</td><td>47.8</td></tr><tr><td>Cambrian-8B</td><td>41.8</td><td>33.2</td><td>32.6</td><td>34.6</td><td>30.9</td><td>31.3</td><td>33.5</td><td>36.0</td></tr><tr><td>Llava-OV-7B</td><td>46.3</td><td>41.0</td><td>41.6</td><td>43.0</td><td>34.7</td><td>43.4</td><td>40.1</td><td>43.4</td></tr><tr><td>Molmo-7B-D</td><td>42.9</td><td>40.4</td><td>40.6</td><td>42.6</td><td>32.6</td><td>40.7</td><td>43.9</td><td>42.1</td></tr><tr><td>Llama3.2-11B</td><td>39.2</td><td>34.0</td><td>33.6</td><td>39.6</td><td>32.3</td><td>36.7</td><td>29.0</td><td>33.0</td></tr><tr><td>PaliGemma-3B</td><td>26.3</td><td>25.2</td><td>29.2</td><td>23.8</td><td>21.6</td><td>24.2</td><td>24.5</td><td>27.6</td></tr><tr><td>PALO-7B</td><td>33.1</td><td>30.5</td><td>30.5</td><td>33.2</td><td>28.9</td><td>34.0</td><td>27.1</td><td>33.3</td></tr><tr><td>mBLIP mT0-XL</td><td>29.3</td><td>30.4</td><td>30.2</td><td>33.2</td><td>28.2</td><td>26.9</td><td>31.6</td><td>32.3</td></tr><tr><td>mBLIP BLOOMZ-7B</td><td>29.2</td><td>30.8</td><td>28.5</td><td>33.9</td><td>27.8</td><td>33.3</td><td>31.6</td><td>29.6</td></tr><tr><td>PANGEA-7B (Ours)</td><td>45.7</td><td>43.7</td><td>42.3</td><td>45.3</td><td>41.6</td><td>46.5</td><td>40.5</td><td>46.1</td></tr></table>{{< /table-caption >}}

> Table 1 presents the overall performance of various multilingual multimodal LLMs on the PANGEABENCH benchmark, highlighting the superior performance of PANGEA-7B compared to other open-source models.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='1' style='font-size:16px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Afrikaans</td><td>Chinese</td><td>Italian</td><td>Portuguese</td><td>Thai</td><td>Vietnamese</td></tr><tr><td>Gemini-1.5-Pro</td><td>77.4</td><td>64.7</td><td>80.4</td><td>74.1</td><td>76.3</td><td>61.8</td><td>49.9</td><td>46.0</td></tr><tr><td>GPT4o</td><td>68.0</td><td>61.0</td><td>73.0</td><td>68.0</td><td>67.0</td><td>58.0</td><td>52.0</td><td>48.3</td></tr><tr><td>Llava-1.5-7B</td><td>32.3</td><td>29.0</td><td>28.2</td><td>24.3</td><td>40.1</td><td>28.2</td><td>23.7</td><td>29.3</td></tr><tr><td>Llava-Next-7B</td><td>36.5</td><td>28.4</td><td>28.2</td><td>25.4</td><td>37.8</td><td>27.0</td><td>23.7</td><td>28.4</td></tr><tr><td>Phi-3.5-Vision</td><td>55.8</td><td>37.2</td><td>44.2</td><td>40.8</td><td>51.4</td><td>40.3</td><td>25.2</td><td>21.6</td></tr><tr><td>Cambrian-8B</td><td>34.7</td><td>33.4</td><td>36.8</td><td>34.2</td><td>45.2</td><td>30.3</td><td>28.9</td><td>25.0</td></tr><tr><td>Llava-OV-7B</td><td>60.4</td><td>45.8</td><td>50.3</td><td>58.0</td><td>57.2</td><td>43.8</td><td>30.9</td><td>34.5</td></tr><tr><td>Molmo-7B-D</td><td>57.1</td><td>39.1</td><td>35.6</td><td>56.4</td><td>49.4</td><td>40.2</td><td>27.4</td><td>25.9</td></tr><tr><td>Llama3.2-11B</td><td>51.8</td><td>36.6</td><td>42.3</td><td>46.4</td><td>45.8</td><td>28.4</td><td>26.4</td><td>30.2</td></tr><tr><td>PaliGemma-3B</td><td>36.0</td><td>25.6</td><td>26.4</td><td>24.7</td><td>32.2</td><td>24.3</td><td>27.2</td><td>19.0</td></tr><tr><td>PALO-7B</td><td>30.8</td><td>27.8</td><td>31.9</td><td>22.1</td><td>36.9</td><td>32.3</td><td>22.7</td><td>20.7</td></tr><tr><td>mBLIP mT0-XL</td><td>22.8</td><td>25.0</td><td>16.0</td><td>25.6</td><td>33.7</td><td>21.2</td><td>22.4</td><td>31.0</td></tr><tr><td>mBLIP BLOOMZ-7B</td><td>30.3</td><td>29.5</td><td>28.2</td><td>29.8</td><td>37.3</td><td>28.3</td><td>22.9</td><td>30.2</td></tr><tr><td>PANGEA-7B (Ours)</td><td>61.4</td><td>42.1</td><td>52.1</td><td>49.2</td><td>54.9</td><td>43.3</td><td>32.9</td><td>19.8</td></tr></table>{{< /table-caption >}}

> Table 1 presents a comparison of the aggregate performance of various open and proprietary multimodal LLMs across different multilingual and multimodal benchmarks in PANGEABENCH.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='3' style='font-size:16px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Arabic</td><td>Bengali</td><td>Finnish</td><td>Indonesian</td><td>Korean</td><td>Russian</td><td>Swahili</td><td>Telugu</td></tr><tr><td>Vicuna-1.5-7B</td><td>59.7</td><td>52.7</td><td>32.3</td><td>68.1</td><td>63.0</td><td>72.6</td><td>58.8</td><td>57.6</td><td>51.3</td><td>18.1</td></tr><tr><td>Qwen2-7B-Instruct</td><td>72.2</td><td>71.2</td><td>67.6</td><td>75.9</td><td>67.1</td><td>78.0</td><td>64.9</td><td>67.2</td><td>75.3</td><td>73.8</td></tr><tr><td>Llava-1.5-7B</td><td>66.8</td><td>52.8</td><td>61.8</td><td>33.4</td><td>60.2</td><td>72.8</td><td>63.3</td><td>55.0</td><td>55.0</td><td>20.6</td></tr><tr><td>Llava-Next-7B</td><td>68.3</td><td>52.1</td><td>64.5</td><td>24.9</td><td>63.0</td><td>74.3</td><td>61.9</td><td>58.4</td><td>53.1</td><td>17.0</td></tr><tr><td>Phi-3.5-Vision</td><td>75.9</td><td>51.3</td><td>63.1</td><td>24.8</td><td>57.3</td><td>70.6</td><td>60.2</td><td>57.5</td><td>48.7</td><td>28.3</td></tr><tr><td>PALO-7B</td><td>69.4</td><td>50.8</td><td>60.9</td><td>46.0</td><td>61.8</td><td>70.6</td><td>56.8</td><td>56.7</td><td>42.5</td><td>10.8</td></tr><tr><td>PANGEA-7B (Ours)</td><td>73.7</td><td>66.0</td><td>55.5</td><td>65.3</td><td>66.3</td><td>74.5</td><td>69.4</td><td>60.1</td><td>76.6</td><td>60.0</td></tr></table>{{< /table-caption >}}

> Table 1 presents a comparison of the overall performance of various multilingual multimodal LLMs on the PANGEABENCH benchmark, highlighting PANGEA-7B's superior performance.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='5' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Arabic</td><td>Spanish</td><td>Basque</td><td>Hindi</td><td>Ind.</td><td>Burmese</td><td>Russian</td><td>Swahili</td><td>Telugu</td><td>Chinese</td></tr><tr><td>Vicuna-1.5-7B</td><td>78.1</td><td>57.4</td><td>52.7</td><td>69.4</td><td>50.8</td><td>54.5</td><td>61.0</td><td>48.4</td><td>66.5</td><td>52.1</td><td>54.5</td><td>63.5</td></tr><tr><td>Qwen2-7B-Instruct</td><td>80.3</td><td>61.9</td><td>64.0</td><td>71.6</td><td>51.6</td><td>59.6</td><td>68.5</td><td>50.7</td><td>72.7</td><td>53.2</td><td>55.3</td><td>72.1</td></tr><tr><td>Llava-1.5-7B</td><td>79.1</td><td>57.6</td><td>52.7</td><td>69.2</td><td>50.9</td><td>54.9</td><td>62.6</td><td>49.0</td><td>65.9</td><td>51.7</td><td>55.8</td><td>63.9</td></tr><tr><td>Llava-Next-7B</td><td>79.1</td><td>57.1</td><td>51.7</td><td>68.8</td><td>50.3</td><td>54.5</td><td>62.0</td><td>46.7</td><td>65.5</td><td>52.1</td><td>55.2</td><td>63.8</td></tr><tr><td>Phi-3.5-Vision</td><td>77.9</td><td>54.8</td><td>53.7</td><td>67.2</td><td>50.4</td><td>54.9</td><td>51.7</td><td>47.8</td><td>61.3</td><td>49.3</td><td>52.5</td><td>59.5</td></tr><tr><td>PALO-7B</td><td>77.4</td><td>57.2</td><td>56.5</td><td>68.4</td><td>49.8</td><td>58.6</td><td>58.5</td><td>47.4</td><td>65.6</td><td>51.2</td><td>53.1</td><td>62.8</td></tr><tr><td>PANGEA-7B (Ours)</td><td>79.1</td><td>61.2</td><td>60.5</td><td>67.8</td><td>50.0</td><td>61.8</td><td>66.4</td><td>48.7</td><td>69.4</td><td>58.9</td><td>60.4</td><td>68.2</td></tr></table>{{< /table-caption >}}

> Table 1 presents a comparison of the overall performance of various multilingual multimodal LLMs on the PANGEABENCH benchmark, highlighting the superior performance of PANGEA-7B.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='7' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Bengali</td><td>German</td><td>Spanish</td><td>French</td><td>Japanese</td><td>Russian</td><td>Swahili</td><td>Telugu</td><td>Thai</td><td>Chinese</td></tr><tr><td>Vicuna-1.5-7B</td><td>17.6</td><td>6.4</td><td>0.0</td><td>14.4</td><td>9.6</td><td>14.4</td><td>2.8</td><td>10.8</td><td>3.6</td><td>0.0</td><td>2.0</td><td>14.8</td></tr><tr><td>Qwen2-7B-Instruct</td><td>48.8</td><td>40.4</td><td>0.0</td><td>67.2</td><td>67.6</td><td>68.8</td><td>11.2</td><td>71.2</td><td>10.8</td><td>2.4</td><td>45.6</td><td>59.2</td></tr><tr><td>Llava-1.5-7B</td><td>14.8</td><td>7.6</td><td>0.0</td><td>15.2</td><td>10.8</td><td>18.0</td><td>2.8</td><td>11.2</td><td>0.4</td><td>0.0</td><td>1.6</td><td>15.6</td></tr><tr><td>Llava-Next-7B</td><td>15.6</td><td>7.5</td><td>0.0</td><td>13.6</td><td>13.2</td><td>16.0</td><td>1.6</td><td>12.8</td><td>2.0</td><td>0.0</td><td>1.6</td><td>14.0</td></tr><tr><td>Phi-3.5-Vision</td><td>59.2</td><td>33.1</td><td>0.0</td><td>64.0</td><td>59.6</td><td>58.0</td><td>20.0</td><td>54.0</td><td>4.0</td><td>0.0</td><td>18.8</td><td>52.4</td></tr><tr><td>PALO-7B</td><td>13.6</td><td>5.8</td><td>0.0</td><td>11.6</td><td>9.6</td><td>13.2</td><td>1.6</td><td>8.8</td><td>0.4</td><td>0.0</td><td>0.0</td><td>12.4</td></tr><tr><td>PANGEA-7B (Ours)</td><td>82.0</td><td>47.3</td><td>0.0</td><td>68.4</td><td>74.8</td><td>63.2</td><td>22.0</td><td>68.0</td><td>54.0</td><td>5.6</td><td>49.6</td><td>68.0</td></tr></table>{{< /table-caption >}}

> Table 1 presents a comparative analysis of the aggregate performance of various multilingual multimodal LLMs across different benchmarks within the PANGEABENCH evaluation suite.


{{< table-caption caption="🔽 Table 1: Overall performance on the multilingual multimodal benchmarks in PANGEABENCH. The best-performing open model on each dataset is in bold and the second best is underlined." >}}
<table id='1' style='font-size:14px'><tr><td>Models</td><td>English</td><td>Multi</td><td>Arabic</td><td>Bengali</td><td>Portuguese</td><td>Chinese</td><td>French</td><td>German</td></tr><tr><td>Vicuna-1.5-7B</td><td>49.5</td><td>34.7</td><td>30.3</td><td>28.5</td><td>39.6</td><td>36.9</td><td>40.4</td><td>39.8</td></tr><tr><td>Qwen2-7B-Instruct</td><td>70.1</td><td>53.1</td><td>51.0</td><td>43.4</td><td>60.7</td><td>63.8</td><td>61.5</td><td>57.7</td></tr><tr><td>Llava-1.5-7B</td><td>50.2</td><td>34.9</td><td>29.7</td><td>28.5</td><td>40.3</td><td>36.8</td><td>40.1</td><td>39.8</td></tr><tr><td>Llava-Next-7B</td><td>52.1</td><td>35.6</td><td>30.0</td><td>28.8</td><td>40.7</td><td>37.3</td><td>41.4</td><td>41.4</td></tr><tr><td>Phi-3.5-Vision</td><td>62.0</td><td>39.1</td><td>34.9</td><td>27.9</td><td>47.6</td><td>41.5</td><td>49.2</td><td>45.8</td></tr><tr><td>PALO-7B</td><td>46.7</td><td>32.6</td><td>30.3</td><td>29.5</td><td>36.0</td><td>34.2</td><td>36.9</td><td>35.8</td></tr><tr><td>PANGEA-7B (Ours)</td><td>68.4</td><td>52.2</td><td>49.3</td><td>44.4</td><td>58.9</td><td>60.5</td><td>58.9</td><td>56.7</td></tr><tr><td>Models</td><td>Hindi</td><td>Indonesian</td><td>Italian</td><td>Japanese</td><td>Korean</td><td>Spanish</td><td>Swahili</td><td>Yoruba</td></tr><tr><td>Vicuna-1.5-7B</td><td>29.8</td><td>36.5</td><td>39.5</td><td>35.9</td><td>34.1</td><td>40.3</td><td>27.9</td><td>26.8</td></tr><tr><td>Qwen2-7B-Instruct</td><td>45.7</td><td>57.1</td><td>60.8</td><td>58.0</td><td>54.6</td><td>61.9</td><td>36.0</td><td>31.8</td></tr><tr><td>Llava-1.5-7B</td><td>29.2</td><td>37.1</td><td>41.0</td><td>35.1</td><td>34.1</td><td>41.6</td><td>28.0</td><td>27.3</td></tr><tr><td>Llava-Next-7B</td><td>29.6</td><td>37.5</td><td>41.2</td><td>36.0</td><td>34.2</td><td>42.7</td><td>28.5</td><td>28.7</td></tr><tr><td>Phi-3.5-Vision</td><td>32.9</td><td>38.3</td><td>47.0</td><td>40.0</td><td>36.6</td><td>49.6</td><td>28.9</td><td>27.8</td></tr><tr><td>PALO-7B</td><td>29.6</td><td>33.7</td><td>36.4</td><td>32.7</td><td>30.6</td><td>37.0</td><td>26.4</td><td>27.1</td></tr><tr><td>PANGEA-7B (Ours)</td><td>45.7</td><td>55.4</td><td>58.8</td><td>55.3</td><td>52.7</td><td>59.7</td><td>42.8</td><td>31.3</td></tr></table>{{< /table-caption >}}

> Table 1 presents the overall performance comparison of different multilingual multimodal LLMs on various benchmark datasets, highlighting PANGEA-7B's superior performance.


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
<img src="paper_images/37.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/38.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/39.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/40.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/41.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/42.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/43.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/44.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/45.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/46.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/47.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/48.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/49.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/50.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/51.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
<img src="paper_images/52.png" class="grid-w50 md:grid-w33 xl:grid-w25" />
{{< /gallery >}}