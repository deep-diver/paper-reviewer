---
title: "How Many Van Goghs Does It Take to Van Gogh? Finding the Imitation Threshold"
summary: "How many training images are needed for a text-to-image model to reliably imitate a specific concept? This paper introduces a novel method to estimate this "imitation threshold", revealing its surpris..."
categories: ["AI Generated"]
tags: ["🔖 24-10-19", "🤗 24-10-22"]
showSummary: true
date: 2024-10-19
draft: false
---

### TL;DR


{{< lead >}}

This research tackles the crucial question of how many training examples of a specific concept (e.g., Van Gogh's style or a person's face) are needed to make a text-to-image model realistically replicate that concept (the imitation threshold).  Instead of computationally intensive methods (training numerous models with varying datasets), this paper proposes MIMETIC2, an efficient approach using existing models and readily available data. Experiments across two domains (human faces and art styles) found imitation thresholds surprisingly low (200-600 images).  These findings provide new metrics to evaluate copyright violations in AI-generated art and offer guidance to model developers on minimizing privacy and copyright infringement risks.

{{< /lead >}}


{{< button href="https://arxiv.org/abs/2410.15002" target="_self" >}}
{{< icon "link" >}} &nbsp; read the paper on arXiv
{{< /button >}}

#### Why does it matter?
To provide a concise and informative summary of the research paper on imitation thresholds in text-to-image models, highlighting its key contributions and implications for researchers.
#### Key Takeaways

{{< alert "star" >}}
{{< typeit speed=10 lifeLike=true >}} A new method (MIMETIC2) efficiently estimates the minimum number of training images needed for a text-to-image model to realistically imitate a concept (the imitation threshold), without the computationally expensive process of training multiple models from scratch. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=1000 lifeLike=true >}} The imitation threshold for the studied models and datasets ranges from 200 to 600 images, significantly lower than expected and suggesting that copyright infringement concerns might be more prevalent than previously thought. {{< /typeit >}}
{{< /alert >}}

{{< alert "star" >}}
{{< typeit speed=10 startDelay=2000 lifeLike=true >}} The findings provide an empirical basis for copyright violation claims and are relevant for text-to-image model developers seeking to comply with copyright and privacy laws. {{< /typeit >}}
{{< /alert >}}

------
#### Visual Insights



![](figures/figures_2_0.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in a training dataset and a model's ability to imitate that concept, showing how the imitation score increases with concept frequency and identifying the imitation threshold.





![](charts/charts_8_0.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis is the sorted image frequencies in the training dataset, and the y-axis is the imitation score (averaged over the five image generation prompts) for each concept, sorted in increasing order of frequency. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The chart displays the relationship between the frequency of concepts (human faces and art styles) in the training dataset and the model's ability to imitate them, highlighting the imitation threshold identified by the change detection algorithm.





{{< table-caption caption="🔽 Table 3: Imitation Thresholds for human face and art style imitation for the different text-to-image models and pretraining datasets we experiment with." >}}
<br><table id='8' style='font-size:14px'><tr><td>Domain</td><td>Dataset</td><td>Pretraining Data</td><td>Model</td></tr><tr><td>Human Faces</td><td>Celebrities, Politicians</td><td>LAION2B-en</td><td>SD1.1,SD1.5</td></tr><tr><td>Human Faces</td><td>Celebrities, Politicians</td><td>LAION5B</td><td>SD2.1</td></tr><tr><td>Art Style</td><td>Classical, Modern</td><td>LAION2B-en</td><td>SD1.1, SD1.5</td></tr><tr><td>Art Style</td><td>Classical, Modern</td><td>LAION5B</td><td>SD2.1</td></tr></table>{{< /table-caption >}}

> Table 3 presents the imitation thresholds for human faces and art styles, estimated using three different text-to-image models trained on two distinct pretraining datasets.



### More visual insights

<details>
<summary>More on figures
</summary>


![](figures/figures_4_0.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is 'a photorealistic close-up image of {name}'.")

> The figure shows real and generated images of celebrities with increasing numbers of training images, demonstrating the effect of concept frequency on imitation.


![](figures/figures_5_0.png "🔼 Figure 3: Overview of MIMETIC²'s methodology to estimate the imitation threshold. In Step 1, we estimate the frequency of each concept (belonging to a domain) in the pretraining data by obtaining the images that contain the concept of interest. In Step 2, we use the filtered images of each concept (obtained in Step 1) and compare them to the generated images to measure imitation (using g that receives training and generated images). We repeat this process for each concept to generate the imitation score graph, and then determine the imitation threshold with a change detection algorithm.")

> The figure illustrates the MIMETIC² methodology for estimating the imitation threshold by computing concept frequency and imitation score.


![](figures/figures_9_0.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is “a photorealistic close-up image of {name}.”")

> Figure 2 shows real and generated images of celebrities with varying numbers of training images to illustrate how the quality of generated images improves as the number of training images increases.


![](figures/figures_9_1.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is 'a photorealistic close-up image of {name}'.")

> The figure shows real and generated images of five celebrities with increasing number of training images, demonstrating the impact of training data size on imitation ability.


![](figures/figures_9_2.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is \'a photorealistic close-up image of {name}\'")

> The figure shows real and generated images of celebrities with varying numbers of training images to illustrate the effect of concept frequency on imitation.


![](figures/figures_20_0.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is ''a photorealistic close-up image of {name}''.")

> The figure shows examples of real and generated images of celebrities with increasing numbers of training images, illustrating the relationship between training data and model imitation ability.


![](figures/figures_20_2.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is 'a photorealistic close-up image of {name}'.")

> The figure shows real and generated images of celebrities with increasing numbers of training images, illustrating the concept of imitation threshold.


![](figures/figures_21_2.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in training data and a model's ability to imitate that concept, introducing the concept of an imitation threshold.


![](figures/figures_23_0.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in a training dataset and a model's ability to imitate that concept, introducing the concept of an imitation threshold.


![](figures/figures_23_1.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in training data and a model's ability to imitate it, introducing the concept of an imitation threshold.


![](figures/figures_23_2.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in training data and a model's ability to imitate that concept, introducing the concept of an imitation threshold.


![](figures/figures_23_3.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in a training dataset and a model's ability to imitate that concept, highlighting the concept of an imitation threshold.


![](figures/figures_23_4.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in a training dataset and a model's ability to imitate that concept, introducing the concept of an imitation threshold.


![](figures/figures_23_5.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is \'a photorealistic close-up image of {name}\'")

> The figure shows real and generated images of celebrities with increasing number of training images to demonstrate the imitation ability of the model.


![](figures/figures_23_6.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh’s art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in a training dataset and a model's ability to imitate that concept, showing how the imitation threshold increases with concept frequency.


![](figures/figures_23_7.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in a training dataset and a model's ability to imitate that concept, introducing the concept of an imitation threshold.


![](figures/figures_23_8.png "🔼 Figure 14: Human Face Imitation (Politicians): Similarity between the training and generated images for all politicians. The politicians with zero image counts are shaded with light gray. We show the mean and variance over the five generation prompts. The images were generated using SD1.2. The change point for human face imitation for politicians when generating images using SD1.1 is detected at 252 faces.")

> The figure shows the imitation scores for politicians as a function of the number of their images in the training dataset, with the imitation threshold detected at 252 faces.


![](figures/figures_24_0.png "🔼 Figure 15: Human Face Imitation (Politicians): Similarity between the training and generated images for all politicians. The politicians with zero image counts are shaded with light gray. We show the mean and variance over the five generation prompts. The images were generated using SD1.3. The change point for human face imitation for politicians when generating images using SD1.1 is detected at 234 faces.")

> The figure shows the imitation scores for politicians and their image counts in the training data, with the imitation threshold detected at 234 faces when using the SD1.3 model.


![](figures/figures_24_1.png "🔼 Figure 15: Human Face Imitation (Politicians): Similarity between the training and generated images for all politicians. The politicians with zero image counts are shaded with light gray. We show the mean and variance over the five generation prompts. The images were generated using SD1.3. The change point for human face imitation for politicians when generating images using SD1.1 is detected at 234 faces.")

> The figure shows the imitation score for politicians plotted against their image counts in the training data, revealing an imitation threshold of 234 faces for the SD1.3 model.


![](figures/figures_25_0.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis represents the sorted image frequencies in the training dataset, and the y-axis represents the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores for human faces and art styles as a function of their image frequencies in the training dataset, illustrating the relationship between concept prevalence and a model's ability to imitate.


![](figures/figures_26_0.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis represents the sorted image frequencies in the training dataset, and the y-axis represents the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores for human faces and art styles as a function of their image frequencies in the training dataset, with the imitation threshold identified by a change detection algorithm.


![](figures/figures_26_1.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis represents the sorted image frequencies in the training dataset, and the y-axis represents the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the relationship between a concept's frequency in the training data and the model's imitation score for human faces and art styles, indicating the imitation threshold.


![](figures/figures_26_2.png "🔼 Figure 15: Human Face Imitation (Politicians): Similarity between the training and generated images for all politicians. The politicians with zero image counts are shaded with light gray. We show the mean and variance over the five generation prompts. The images were generated using SD1.3. The change point for human face imitation for politicians when generating images using SD1.1 is detected at 234 faces.")

> The figure shows the imitation scores for politicians as a function of their image frequencies in the training dataset, with a change detection algorithm identifying the imitation threshold at 234 faces.


![](figures/figures_26_3.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis represents the sorted image frequencies in the training dataset, and the y-axis represents the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores for human faces and art styles as a function of their image frequencies in the training dataset, illustrating the concept of imitation threshold.


![](figures/figures_26_4.png "🔼 Figure 17: Human Face Imitation (Celebrities): Similarity between the training and generated images for all celebrities. The celebrities with zero image counts are shaded with light gray. We show the mean and variance over the five generation prompts. The images were generated using SD1.1. The change point for human face imitation for celebrities when generating images using SD1.1 is detected at 364 faces.")

> The figure shows the imitation score of generated images for celebrities plotted against their image frequency in the training dataset, revealing the imitation threshold at 364 faces for the SD1.1 model.


![](figures/figures_27_0.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis is the sorted image frequencies in the training dataset, and the y-axis is the imitation score (averaged over the five image generation prompts) for each concept, sorted in increasing order of frequency. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores of different concepts (celebrities and art styles) as a function of their frequencies in the training data, illustrating the concept of imitation threshold.


![](figures/figures_27_1.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis is the sorted image frequencies in the training dataset, and the y-axis is the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores of concepts in two domains (human faces and art styles) plotted against their frequency in the training data, illustrating the relationship between concept frequency and a model's ability to imitate that concept and showing the estimated imitation threshold for each.


![](figures/figures_27_2.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis represents the sorted image frequencies in the training dataset, and the y-axis represents the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores for celebrities and classical art styles as a function of their image frequency in the training data, revealing the imitation threshold for each.


![](figures/figures_27_3.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis represents the sorted image frequencies in the training dataset, and the y-axis represents the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores of concepts (celebrities and art styles) as a function of their frequency in the training data, illustrating the relationship between concept prevalence and the model's ability to imitate them, with the imitation threshold identified by a change detection algorithm.


![](figures/figures_27_4.png "🔼 Figure 5: Human Face and Art Style imitation graphs for SD1.1 using the Celebrities and Classical art style sets. The x-axis represents the sorted image frequencies in the training dataset, and the y-axis represents the imitation of the training images in the generated images, for each concept. Concepts with zero image frequencies are shaded with light gray. We show the mean imitation score and its variance over the five image generation prompts. The red vertical line indicates the imitation threshold found by the change detection algorithm, and the horizontal green line represents the average imitation scores before and after the threshold.")

> The figure shows the imitation scores for human faces and art styles as a function of the concept's image frequency in the training dataset, indicating the imitation thresholds for these concepts.


![](figures/figures_28_0.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is 'a photorealistic close-up image of {name}'.")

> The figure shows real and generated images of five celebrities with increasing numbers of training images to illustrate the concept of imitation threshold.


![](figures/figures_29_0.png "🔼 Figure 2: Examples of real celebrity images (top) and generated images from a text-to-image model (bottom) with increasing image counts from left to right (3, 273, 3K, 10K, and 90K, respectively). The prompt is “a photorealistic close-up image of {name}”.")

> The figure shows real and generated images of celebrities with increasing number of training images, illustrating the effect of training data size on model imitation.


![](figures/figures_29_1.png "🔼 Figure 1: An overview of FIT, where we seek the imitation threshold – the point at which a model was exposed to enough instances of a concept that it can reliably imitate it. The figure shows four concepts (e.g., Van Gogh's art style) that have different counts in the training data (e.g., 213K for Van Gogh). As the image count of a concept increases, the ability of the text-to-image model to imitate it increases (e.g. Piet Mondrian and Van Gogh). We propose an efficient approach, MIMETIC2, that estimates the imitation threshold without training models from scratch.")

> The figure illustrates the relationship between a concept's frequency in a training dataset and a model's ability to imitate it, showing how imitation score increases with concept frequency and introducing the proposed MIMETIC2 approach.


</details>



<details>
<summary>More on charts
</summary>


![](charts/charts_20_0.png "🔼 Figure 7: Average cosine similarity between the faces of the same people (blue colored) and of the faces of different people (red colored), measured across the reference images of the celebrities.")

> The histogram shows the distribution of average cosine similarity scores between face embeddings of the same person and different persons, used to determine the threshold for filtering images.


![](charts/charts_21_0.png "🔼 Figure 9: The first filtering step involves determining the threshold to distinguish between art and non-art images from the pretraining images, for which we compare the similarity of the image's embedding to the embedding of the text 'an artwork'.")

> The chart displays histograms showing the distribution of cosine similarity scores between image embeddings and the text embedding of 'an artwork', for both art and non-art images, used to determine the threshold for filtering non-art images from the pretraining dataset.


![](charts/charts_22_0.png "🔼 Figure 12: The second filtering step involves determining the if an art work whose caption mentions an artist actually belongs to that artist or not.")

> The histogram shows the average cosine similarity between embeddings of art images of the same artist and art images of different artists for classical and modern artists.


![](charts/charts_22_1.png "🔼 Figure 12: The second filtering step involves determining the if an art work whose caption mentions an artist actually belongs to that artist or not.")

> The figure shows the histograms of average cosine similarity between embeddings of images of the same artist and images of different artists for classical and modern artists, used to determine a threshold for filtering art images.


![](charts/charts_29_0.png "🔼 Figure 33: False-match rate (FMR) of all the face embedding models across the six demographic groups. Amazon Rekognition and InsightFace have the lowest FMR values. Moreover, these two models have lowest disparity of FMR over the demographic groups.")

> The chart displays the false-match rates of eight different face recognition models across six demographic groups, showing that Amazon Rekognition and InsightFace have the lowest false-match rates and lowest disparity across groups.


![](charts/charts_30_0.png "🔼 Figure 34: True-match rate (TMR) of all the face embedding models across the six demographic groups. Amazon Rekognition model has the highest TMR values.")

> The chart displays the true-match rate (TMR) for six demographic groups across eight different face embedding models.


</details>



<details>
<summary>More on tables
</summary>


{{< table-caption caption="🔽 Table 3: Imitation Thresholds for human face and art style imitation for the different text-to-image models and pretraining datasets we experiment with." >}}
<br><table id='11' style='font-size:14px'><tr><td>Human faces</td><td>Art style</td></tr><tr><td>A photorealistic close-up photograph of x</td><td>A painting in the style of X</td></tr><tr><td>High-resolution close-up image of X</td><td>An artwork in the style of X</td></tr><tr><td>Close-up headshot of x</td><td>A sketch in the style of X</td></tr><tr><td>X's facial close-up</td><td>A fine art piece in the style of X</td></tr><tr><td>X's face portrait</td><td>An illustration in the style of X</td></tr></table>{{< /table-caption >}}

> Table 3 presents the imitation thresholds for human faces and art styles across different text-to-image models and their respective training datasets.


{{< table-caption caption="🔽 Table 3: Imitation Thresholds for human face and art style imitation for the different text-to-image models and pretraining datasets we experiment with." >}}
<br><table id='2' style='font-size:14px'><tr><td></td><td></td><td colspan="2">Human Faces</td><td colspan="2">Art Style</td></tr><tr><td>Pretraining Dataset</td><td>Model</td><td>Celebrities</td><td>Politicians</td><td>Classical</td><td>Modern</td></tr><tr><td rowspan="2">LAION2B-en</td><td>SD1.1</td><td>364</td><td>234</td><td>112</td><td>198</td></tr><tr><td>SD1.5</td><td>364</td><td>234</td><td>112</td><td>198</td></tr><tr><td>LAION-5B</td><td>SD2.1</td><td>527</td><td>369</td><td>185</td><td>241</td></tr></table>{{< /table-caption >}}

> Table 3 presents the imitation thresholds for human faces and art styles across three different text-to-image models trained on two distinct datasets.


{{< table-caption caption="🔽 Table 4: Average difference in the imitation scores for concepts whose image counts differ by less than 10. The difference in the imitation scores are very close to 0, providing the empirical validation the distribution invariance assumption." >}}
<br><table id='6' style='font-size:16px'><tr><td>Domain</td><td>Dataset</td><td>Avg. difference in imitation score</td></tr><tr><td>Human Faces</td><td>Celebrities</td><td>0.0007</td></tr><tr><td>Human Faces</td><td>Politicians</td><td>0.0023</td></tr><tr><td>Art Style</td><td>Classical Art Style</td><td>-0.0088</td></tr><tr><td>Art Style</td><td>Modern Art Style</td><td>-0.0013</td></tr></table>{{< /table-caption >}}

> Table 4 presents the average difference in imitation scores for concepts with similar image counts, supporting the assumption of distributional invariance across concepts within the same domain.


{{< table-caption caption="🔽 Table 3: Imitation Thresholds for human face and art style imitation for the different text-to-image models and pretraining datasets we experiment with." >}}
<br><table id='2' style='font-size:18px'><tr><td>Celebrity</td><td>Face Count in 100K images</td><td>Face Count in Images with Caption Mention</td><td>Percentage of Missed Images</td><td>Number of Missed Images</td></tr><tr><td>Floyd Mayweather</td><td>1</td><td>0</td><td>0.001%</td><td>23K</td></tr><tr><td>Oprah Winfrey</td><td>2</td><td>0</td><td>0.002%</td><td>46K</td></tr><tr><td>Ronald Reagan</td><td>6</td><td>3</td><td>0.003%</td><td>69K</td></tr><tr><td>Ben Affleck</td><td>0</td><td>0</td><td>0.0%</td><td>0</td></tr><tr><td>Anne Hathaway</td><td>0</td><td>0</td><td>0.0%</td><td>0</td></tr><tr><td>Stephen King</td><td>0</td><td>0</td><td>0.0%</td><td>0</td></tr><tr><td>Johnny Depp</td><td>9</td><td>1</td><td>0.008%</td><td>184K</td></tr><tr><td>Abraham Lincoln</td><td>52</td><td>1</td><td>0.051%</td><td>1.17M</td></tr><tr><td>Kate Middleton</td><td>34</td><td>1</td><td>0.033%</td><td>759K</td></tr><tr><td>Donald Trump</td><td>16</td><td>0</td><td>0.016%</td><td>368K</td></tr></table>{{< /table-caption >}}

> Table 3 presents the imitation thresholds for human faces and art styles across different text-to-image models and their corresponding training datasets.


{{< table-caption caption="🔽 Table 6: Imitation Thresholds for politicians for all models in SD1 series and SD2.1" >}}
<br><table id='13' style='font-size:20px'><tr><td>Pretraining Dataset</td><td>Model</td><td>Human Faces : Politicians</td></tr><tr><td rowspan="5">LAION2B-en</td><td>SD1.1</td><td>234</td></tr><tr><td>SD1.2</td><td>252</td></tr><tr><td>SD1.3</td><td>234</td></tr><tr><td>SD1.4</td><td>234</td></tr><tr><td>SD1.5</td><td>234</td></tr><tr><td>LAION-5B</td><td>SD2.1</td><td>369</td></tr></table>{{< /table-caption >}}

> The table presents the imitation thresholds for politicians obtained using different versions of Stable Diffusion models, trained on LAION2B-en and LAION-5B datasets.


{{< table-caption caption="🔽 Table 3: Imitation Thresholds for human face and art style imitation for the different text-to-image models and pretraining datasets we experiment with." >}}
<br><table id='2' style='font-size:18px'><tr><td></td><td></td><td colspan="2">Human Faces</td><td colspan="2">Art Style</td></tr><tr><td>Pretraining Dataset</td><td>Model</td><td>Celebrities</td><td>Politicians</td><td>Classical Artists</td><td>Modern Artists</td></tr><tr><td rowspan="2">LAION2B-en</td><td>SD1.1</td><td>364</td><td>234</td><td>112, 391</td><td>198</td></tr><tr><td>SD1.5</td><td>364, 8571</td><td>234, 4688</td><td>112, 360</td><td>198, 4821</td></tr><tr><td>LAION-5B</td><td>SD2.1</td><td>527, 9650</td><td>369, 8666</td><td>185, 848</td><td>241, 1132</td></tr></table>{{< /table-caption >}}

> Table 3 shows the imitation thresholds for human faces and art styles across three text-to-image models trained on two different pretraining datasets.


{{< table-caption caption="🔽 Table 3: Imitation Thresholds for human face and art style imitation for the different text-to-image models and pretraining datasets we experiment with." >}}
<br><table id='5' style='font-size:18px'><tr><td>Caption Counts (LAION-2B)</td><td>Celebrities</td><td>Politicians</td><td>Classical Artists</td><td>Modern Artists</td></tr><tr><td>0</td><td>19</td><td>15</td><td>14</td><td>15</td></tr><tr><td>1-100</td><td>48</td><td>60</td><td>67</td><td>69</td></tr><tr><td>100-500</td><td>57</td><td>120</td><td>133</td><td>139</td></tr><tr><td>500-1K</td><td>52</td><td>80</td><td>62</td><td>62</td></tr><tr><td>1K-5K</td><td>151</td><td>65</td><td>63</td><td>64</td></tr><tr><td>5K-10K</td><td>19</td><td>40</td><td>39</td><td>32</td></tr><tr><td>> 10K</td><td>53</td><td>40</td><td>40</td><td>34</td></tr></table>{{< /table-caption >}}

> Table 3 presents the imitation thresholds for human faces and art styles across different text-to-image models and pretraining datasets.


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