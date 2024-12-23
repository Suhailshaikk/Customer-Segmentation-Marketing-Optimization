# Mall Customer Segmentation Analysis

## Objective
To segment customers into distinct groups based on their demographic and spending patterns, enabling targeted marketing strategies.

## Dataset Overview

### Dataset File Name
`segmentation.csv`

### Dataset Size
- **Number of Rows**: 200
- **Number of Columns**: 5

### Columns
- **CustomerID**: Unique identifier for each customer.
- **Gender**: Gender of the customer (Male/Female).
- **Age**: Age of the customer.
- **Annual Income (k$)**: Annual income of the customer in thousand dollars.
- **Spending Score (1-100)**: Score assigned based on spending behavior (1 = lowest spender, 100 = highest spender).

## Steps Involved

### 1. Exploratory Data Analysis (EDA)
- Visualize the distribution of features like `Age`, `Annual Income`, and `Spending Score`.
- Analyze relationships between features (e.g., income vs. spending score).
- Identify patterns or clusters using pair plots and heatmaps.

### 2. Data Preprocessing
- Check for missing values and handle them if present.
- Encode categorical variables (e.g., `Gender`) using label encoding or one-hot encoding.
- Scale numerical features (`Age`, `Annual Income`, `Spending Score`) using standardization or normalization for clustering.

### 3. Clustering Analysis
- Use clustering algorithms like K-Means and Hierarchical Clustering.
- Determine the optimal number of clusters using methods such as the Elbow Method and Silhouette Score.
- Visualize clusters in a 2D or 3D space using PCA (Principal Component Analysis) or t-SNE.

### 4. Insights
- Identify characteristics of each customer segment (e.g., high-income high-spenders, young low-spenders).
- Provide actionable recommendations for marketing strategies based on segment characteristics.

### 5. Deployment
- Build a Streamlit web application to:
  - Upload new customer data.
  - Assign customers to segments.
  - Display cluster characteristics interactively.

## Tools and Technologies
- **Python**: For data processing and analysis.
  - Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn.
- **Clustering Algorithms**: K-Means, Hierarchical Clustering.
- **Visualization**: PCA and t-SNE for dimensionality reduction.
- **Streamlit**: For deployment.

## Results and Insights

### Clustering Analysis
- Identified **3-5 distinct customer segments** (e.g., high spenders, budget-conscious, young trendsetters).
- Key characteristics of each segment:
  - **Cluster 1**: High income, high spending score.
  - **Cluster 2**: Low income, moderate spending score.
  - **Cluster 3**: Young customers with moderate spending scores.

### Key Recommendations
- Target high spenders with premium offers and loyalty programs.
- Engage low-income customers with budget-friendly promotions.
- Create trend-based marketing campaigns for younger segments.

## Future Enhancements
- Incorporate additional customer behavior data (e.g., purchase history, online activity).
- Use advanced clustering techniques like DBSCAN for non-linear patterns.
- Perform real-time segmentation using streaming data.

