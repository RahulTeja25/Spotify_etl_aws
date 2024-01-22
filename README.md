# Spotify_etl_aws
![WhatsApp Image 2024-01-22 at 15 43 16_5f05e075](https://github.com/RahulTeja25/Spotify_etl_aws/assets/115322030/6d9cc093-1803-4417-a24e-97efa48fcaf1)


1) Data Staging in S3 Bucket:
Initiated the architecture by leveraging an S3 bucket as a staging area.
Various CSV datasets including artists, albums, and tracks were stored in this S3 bucket.

2) Visual ETL with AWS Glue:
Implemented a visual ETL process using AWS Glue, simplifying the transformation steps.
Utilized Glue to join the artist and album datasets, creating a consolidated table.
Further, integrated the joined table with the track dataset to form a comprehensive dataset.

3) Data Cleaning and Deduplication:
Performed data cleaning during the ETL process, eliminating redundant or unnecessary fields.
Applied deduplication techniques to ensure data integrity and consistency.

4) Destination Data Warehouse in S3 Bucket:
Transferred the processed and refined dataset to a destination S3 bucket designated as the data warehouse.

5) Database Creation with AWS Glue Crawler:
Leveraged AWS Glue Crawler to recognize the structure of the dataset and automatically create a database.
The database was instrumental in organizing and categorizing the data for efficient querying.

6) Querying with Amazon Athena:
Connected the database to Amazon Athena, facilitating SQL-based querying of the dataset.
Executed queries to extract specific rows of interest, enriching the dataset with relevant information.

Example queries:

Get Top-N Artists by Popularity
Track Popularity Trends
Geospatial Data for Artists

7) Results Output to S3 Bucket:
Exported the query results to an output S3 bucket, providing a structured format for further analysis.

8) QuickSight Dashboard Development:
Utilized the output S3 bucket as a data source for Amazon QuickSight.
Developed an insightful dashboard within QuickSight, allowing for intuitive visualization and analysis.

Graphs and Dashboards (in Amazon QuickSight):

Bar Chart - Average Track Popularity by Artist:
Displaying the average popularity of tracks for each artist in a bar chart.

Line Chart - Trends in Album Releases:
Visualizing trends in album releases over the years using a line chart.

Heatmap - Correlation Matrix:
Illustrating the correlation between different variables, such as track duration, release year, and popularity, in a heatmap.

Top-N Artists Pie Chart:
Creating a pie chart showcasing the distribution of top artists based on popularity.



