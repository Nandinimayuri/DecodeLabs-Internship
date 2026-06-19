Customer Segmentation using PCA and K-Means Clustering:

Project Overview:
This project focuses on identifying hidden customer groups from a retail sales dataset using unsupervised machine learning techniques.Since the dataset does not contain predefined labels,clustering techniques were used to discover patterns and group similar customers together.
The project uses Principal Component Analysis (PCA) for dimensionality reduction and K-Means Clustering for customer segmentation. The resulting clusters were then interpreted as business personas to provide useful business insights.

Objective:
i. Discover hidden patterns in retail sales data.
ii. Reduce high-dimensional data into fewer dimensions using PCA.
iii. Find the optimal number of clusters using the Elbow Method and Silhouette Score.
iv. Group similar customers using K-Means clustering.
v. Convert clusters into meaningful business personas.

Dataset:
Dataset Name: Product-Sales-Region.xlsx
The dataset contains information related to:
i. Region
ii. Product
iii. Quantity
iv. Unit Price
v. Customer Type
vi. Store Location
vii. Payment Method
viii. Discount
ix. Shipping Cost
x. Salesperson
xi. Total Price
xii. Promotion
xiii. Returns
xiv. Customer Information

Technologies Used:
i. Python
ii. Pandas
iii. NumPy
iv. Matplotlib
v. Scikit-Learn

Steps Performed:
1.Data Loading
The retail sales dataset was loaded using Pandas.
2.Data Preprocessing
i. Unnecessary date columns were removed.
ii. Categorical columns were converted into numerical format using "pd.get_dummies()".
iii. Data was standardized using "StandardScaler".
3.Principal Component Analysis (PCA)
PCA was applied to reduce the dataset into 2 principal components while preserving most of the important information.
4.Elbow Method
The Elbow Method was used to determine the possible number of clusters by analyzing WCSS values.
5.Silhouette Score
Silhouette Score was calculated for different cluster values to mathematically identify the best number of clusters.
6.K-Means Clustering
K-Means clustering was applied using the optimal number of clusters obtained from the evaluation methods.
7.Cluster Visualization
The clusters were visualized using a scatter plot based on the PCA components.
8.Business Persona Creation
The generated clusters were translated into business-friendly customer segments.
Examples:
i. Premium Customers
ii. High Value Customers
iii. Regular Customers
iv. Discount Seekers
v. Occasional Buyers

Conclusion:
This project demonstrates how unsupervised machine learning techniques can be used to analyze retail data and identify hidden customer segments.PCA helped simplify the dataset,while K-Means clustering grouped similar customers together.These insights can help businesses understand customer behavior and make better marketing and sales decisions.