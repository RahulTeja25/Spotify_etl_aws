import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node album
album_node1705853887412 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://proj-spotify/stagging/albums.csv"],
        "recurse": True,
    },
    transformation_ctx="album_node1705853887412",
)

# Script generated for node artist
artist_node1705853887773 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://proj-spotify/stagging/artists.csv"],
        "recurse": True,
    },
    transformation_ctx="artist_node1705853887773",
)

# Script generated for node track
track_node1705853888032 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://proj-spotify/stagging/track.csv"]},
    transformation_ctx="track_node1705853888032",
)

# Script generated for node Join
Join_node1705854394597 = Join.apply(
    frame1=album_node1705853887412,
    frame2=artist_node1705853887773,
    keys1=["artist_id"],
    keys2=["id"],
    transformation_ctx="Join_node1705854394597",
)

# Script generated for node Join with tracks
Joinwithtracks_node1705855794170 = Join.apply(
    frame1=Join_node1705854394597,
    frame2=track_node1705853888032,
    keys1=["track_id"],
    keys2=["track_id"],
    transformation_ctx="Joinwithtracks_node1705855794170",
)

# Script generated for node Drop Fields
DropFields_node1705856635730 = DropFields.apply(
    frame=Joinwithtracks_node1705855794170,
    paths=["`.track_id`", "id"],
    transformation_ctx="DropFields_node1705856635730",
)

# Script generated for node Destination
Destination_node1705946801191 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1705856635730,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://proj-spotify/datawarehouse/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Destination_node1705946801191",
)

job.commit()