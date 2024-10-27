---
title: "LLM-based Optimization of Compound AI Systems: A Survey"
summary: "LLMs are revolutionizing compound AI optimization by efficiently generating complex parameters without gradient computation, enabling end-to-end system tuning."
categories: ["AI Generated"]
tags: ["🔖 24-10-21", "🤗 24-10-23"]
showSummary: true
date: 2024-10-21
draft: false
---

### TL;DR


{{< lead >}}

This paper surveys recent advancements in using Large Language Models (LLMs) to optimize compound AI systems.  Compound AI systems combine LLMs with other components like retrievers or code interpreters, making their behavior highly dependent on parameters like instructions or tool definitions.  Traditionally, these parameters are tuned manually, which is time-consuming and challenging.  This paper introduces a novel approach that uses an LLM as the optimizer. This is efficient because LLMs can directly generate optimized parameters, avoiding the need for computationally expensive gradient calculations. The survey categorizes optimization approaches based on the analogy of program analysis. Static analysis involves optimizing based on the system's structure without runtime execution, while dynamic analysis considers the system's runtime behavior.  The paper also explores various applications of this LLM-based optimization across different compound AI systems, including question-answering, mathematical problem-solving, and sequential decision making.  The authors emphasize the broader implications of this approach, including improved process supervision and enhanced safety in AI systems.  This method offers a way to better manage the complexity of compound AI systems, resulting in more robust and efficient AI applications.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.16392" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
This JSON contains a summary of the research paper on LLM-based optimization of compound AI systems.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} LLMs offer efficient end-to-end optimization for compound AI systems by avoiding gradient calculations. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} Static and dynamic program analysis analogies help understand how to effectively prompt LLMs for parameter optimization. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} This survey provides a framework for understanding and optimizing compound AI systems, highlighting future directions and potential impact. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: Organization of this survey. A non-exhaustive list of papers is provided.")

> The figure shows a tree-like structure that organizes the survey of LLM-based optimization of compound AI systems by workflow, optimization methods, applications, and discussions.







### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_5_0.png "🔼 Figure 2: Credit assignment: a local vs. a global approach. In backpropagation, the optimizer updates each parameter individually. In trace propagation, the prompt contains the execution trace, which allows it to generate all updated variables in a single call. Note that the loss is a textual feedback. In addition, the gradient of the instruction is not the gradient of the output, but the gradient of the instruction with respect to the gradient of the output.")

> The figure illustrates the difference between backpropagation and trace propagation in credit assignment for LLM-based optimization of compound AI systems.


![](figures/figures_5_1.png "🔼 Figure 2: Credit assignment: a local vs. a global approach. In backpropagation, the optimizer updates each parameter individually. In trace propagation, the prompt contains the execution trace, which allows it to generate all updated variables in a single call. Note that the loss is a textual feedback. In addition, the gradient of the instruction is not the gradient of the output, but the gradient of the instruction with respect to the gradient of the output.")

> The figure illustrates the difference between backpropagation and trace propagation in credit assignment for LLM-based optimization of compound AI systems.


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
{{< /gallery >}}