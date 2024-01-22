# Spotify_etl_aws
![WhatsApp Image 2024-01-22 at 15 43 16_5f05e075](https://github.com/RahulTeja25/Spotify_etl_aws/assets/115322030/6d9cc093-1803-4417-a24e-97efa48fcaf1)


Data Staging in S3 Bucket:

Initiated the architecture by leveraging an S3 bucket as a staging area.
Various CSV datasets including artists, albums, and tracks were stored in this S3 bucket.
Visual ETL with AWS Glue:

Implemented a visual ETL process using AWS Glue, simplifying the transformation steps.
Utilized Glue to join the artist and album datasets, creating a consolidated table.
Further, integrated the joined table with the track dataset to form a comprehensive dataset.
Data Cleaning and Deduplication:

Performed data cleaning during the ETL process, eliminating redundant or unnecessary fields.
Applied deduplication techniques to ensure data integrity and consistency.
Destination Data Warehouse in S3 Bucket:

Transferred the processed and refined dataset to a destination S3 bucket designated as the data warehouse.
Database Creation with AWS Glue Crawler:

Leveraged AWS Glue Crawler to recognize the structure of the dataset and automatically create a database.
The database was instrumental in organizing and categorizing the data for efficient querying.
Querying with Amazon Athena:

Connected the database to Amazon Athena, facilitating SQL-based querying of the dataset.
Executed queries to extract specific rows of interest, enriching the dataset with relevant information.
Results Output to S3 Bucket:

Exported the query results to an output S3 bucket, providing a structured format for further analysis.
QuickSight Dashboard Development:

Utilized the output S3 bucket as a data source for Amazon QuickSight.
Developed an insightful dashboard within QuickSight, allowing for intuitive visualization and analysis.

