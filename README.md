# AA72 Jigsaw Solution

Programmatically solving a 2000-piece jigsaw puzzle based on the shapes of edges. The puzzle features the AA72 painting by Zdzisław Beksiński. After struggling to piece it together by hand, I decided to tackle it using code instead.

# The Solution

This project employs a heuristic approach to solving the jigsaw puzzle. Here's a breakdown of the process:

0. Data Collection

I gathered a dataset of images, with each image representing a single puzzle piece. These images were captured using a smartphone camera positioned directly above the pieces, with the pieces placed on a sheet of paper held semi-steadily over a lamp for backlighting. Many pieces had rough edges due to imprecise cuts, which I manually flattened with a toothpick. Gathering data took approximately 20 hours. The dataset is available as a GitHub release.

1. Images (Image Processing)

The main objective was to extract the edges and corners of each puzzle piece. Getting decent results required tweaking parameters by trial and error. Additionally, I generated preview images with marked edges and corners for manual verification.

2. Edges

This involved segmenting each puzzle piece's edge into four distinct sides, classifying them based on their characteristics (e.g., flat, knob, hole), and standardizing their placement in a coordinate space.

3. Comparisons

The most computationally intensive phase involved comparing every edge against every other edge of each piece. This exhaustive comparison process generated a CSV file, serving as the comparison index. Edges were compared using the Iterative Closest Point (ICP) algorithm for precise edge alignment.

4. Solution

Finally, armed with the comparison index from the previous step, I embarked on solving the puzzle. I implemented three approaches, but those implementations and algorithms used are by no means perfect. Despite their imperfections, they got the job done, and now my jigsaw puzzle proudly hangs on a wall!

# Conclusions and potential improvements

While the heuristic approach served its purpose, I believe there is a lot of room for enhancing and refining the solution to make it more versatile and robust. Here are a few potential improvements that come to mind:

0. Data Collection
    - The key takeaway from this project is the importance of meticulous data collection. Using a piece of paper as a base for the backlight setup may have contributed to difficulties in fitting some pieces, as the paper tends to bend. Replacing the paper with a piece of plastic could offer better stability and accuracy. Additionally, the semi-stable frame used to hold my phone during photography may have introduced inconsistencies. Moreover, using manual camera settings instead of relying on automatic settings would have ensured greater consistency in the photos. In hindsight, paying closer attention to detail during data collection could have greatly improved the whole process.
    - It might be a good idea to get a smaller jigsaw puzzle for testing.

1. Images (Image Processing)
    - With improved data quality, I would experiment with using a smaller kernel size for the blur filter.
    - The corner selection algorithm is not reliable. Sometimes, when the knob isn't centered and the edge is noisy, the algorithm might mistakenly select noise on the knob instead of the actual corner. I considered using a neural network for image segmentation to identify the main square of the piece (eliminating knobs and holes), and then using the segmentation result to select four points covering most of it. However, this approach significantly increases complexity, so I opted to stick with the simplest idea for now.

3. Comparisons
    - To improve performance by reducing the number of comparisons, one approach could be to implement locality-sensitive hashing. With this technique, we could group similar sides together, allowing for comparisons only among those that exhibit some degree of similarity. This would not only optimize the comparison process but also speed up the jigsaw solution in step 4.
    - An alternative to using the Iterative Closest Point (ICP) algorithm could be to treat each edge as a signal and employ Fast Fourier Transform (FFT) as a feature extraction method. The score could be calculated based on FFT similarity.
    - A significantly more ambitious approach would involve developing a neural network to generate comparison scores between edges, possibly using sections of images themselves instead of just extracted edges.

4. Solution
    - The third attempt to generate a solution proves that calculating a score based on multiple edges reduces the possibility of placing the wrong piece. One potential improvement could involve clustering all the pieces into groups of four and treating these squares as primitives rather than individual puzzle pieces. With a smaller comparison index from step 3, it might be feasible to search for the best combination of such groups.
    - Several papers propose genetic algorithms or other sophisticated approaches to assembling the solution. While I opted for simplicity in this project, exploring and studying these papers could be a promising next step for further refinement.

Another consideration would be to change the approach and move away from relying solely on edges for solving the puzzle. Instead, extracting and utilizing color/pattern information could offer a new perspective. However, this new approach requires the complete rework of all three first steps.
