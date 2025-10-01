## Machine Learning Lifecycle

Machine Learning Lifecycle is a structured process for developing, deploying, and maintaining ML models, ensuring accuracy, reliability, and scalability.

![alt text](image.png)

By following this lifecycle, we can:

- Define objectives, scope, and success criteria for clear project direction.
- Collect diverse, sufficient datasets from reliable sources.
- Clean and preprocess data, handling issues like missing values and outliers.
- Analyze data using statistics and visualizations to uncover insights.
- Engineer features and select relevant attributes for better model performance.
- Train models, compare options, and select the best one.
- Evaluate on unseen data, optimize, and measure performance.
- Deploy models into production and monitor for drift, retraining as needed.

### Data Processing

#### Data Cleaning
- Raw Data: Initial data collected from various sources. Log files, Audio/Video files, Images, Text files, etc., Transactional data, etc.)
- Goal: Make that raw data accurate, consistent, free of errors, and usable for analysis.


##### How to Clean Data
1. Remove duplicates
2. Remove unwanted observations
3. Handle missing values
4. Manage outliers

##### Data Formatting
- Converting your input data into standard formats or structures that can be easily processed by machine learning algorithms.\
- In our case, we go through scaling, normalization, encoding categorical variables (One Hot Encoding), etc.

1. Min Max Scaling
   - Rescales features to a fixed range, usually 0 to 1.
   - Formula: X_scaled = (X - X_min) / (X_max - X_min)

2. Standardization (Z-score Normalization)
   - Centers the feature by subtracting the mean and scaling to unit variance.
   - Formula: X_standardized = (X - μ) / σ

Data Cleaning Tools:
- Python Libraries: Pandas, NumPy
- Data Cleaning Tools: OpenRefine, Trifacta