# from shakti.constants import GCS_BUCKET_NAME

from google.cloud import storage
import os

from shaktiutils.utilities import name_from_path
import shakti


def gcs_file_upload(file_path, file_type):
    """Uploads a blob to the bucket."""
    # file_path = "local/path/to/file"
    # GCS_BUCKET_NAME = "bucketname"
    # https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python

    storage_client = storage.Client()

    bucket = storage_client.bucket(os.environ["GCS_BUCKET_NAME"])
    try:
        # source and destination file name are kept same
        file_name = name_from_path(file_path)
        blob = bucket.blob(file_type+"/"+file_name)
        blob.upload_from_filename(file_path)
        print("File {} has been uploaded".format(file_name))
    except NameError:
        print("Please set the environment variable {}".format("GCS_BUCKET_NAME"))


def gcs_list_files(prefix, delimiter=None):
    """Lists all the blobs in the bucket that begin with the prefix.

    This can be used to list all blobs in a "folder", e.g. "public/".

    The delimiter argument can be used to restrict the results to only the
    "files" in the given "folder". Without the delimiter, the entire tree under
    the prefix is returned. For example, given these blobs:

        a/1.txt
        a/b/2.txt

    If you just specify prefix = 'a', you'll get back:

        a/1.txt
        a/b/2.txt

    However, if you specify prefix='a' and delimiter='/', you'll get back:

        a/1.txt

    Additionally, the same request will return blobs.prefixes populated with:

        a/b/
    """
    # Note: Client.list_blobs requires at least package version 1.17.0.
    # https://cloud.google.com/storage/docs/listing-objects

    storage_client = storage.Client()
    bucket = storage_client.bucket(os.environ[GCS_BUCKET_NAME])

    files_list = storage_client.list_blobs(
        bucket, prefix=prefix, delimiter=delimiter
    )
    files_list = files_list.prefixes if delimiter else files_list
    directory = prefix
    directory += delimiter if delimiter else ""
    print("Files in {}:".format(directory))
    for file_name in files_list:
        print(" -> {}".format(file_name.name))


def gcs_download_file(source_file_path):
    """Downloads a blob from the bucket."""
    # GCS_BUCKET_NAME = "your-bucket-name"
    # source_file_path = "models/storage-object-name"
    # destination_file_name = "local/path/to/file"

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(os.environ[GCS_BUCKET_NAME])
        blob = bucket.blob(source_file_path)
        destination_file_name = "/"+source_file_path
        blob.download_to_filename(destination_file_name)

        print(
            "Blob {} downloaded to {}.".format(
                source_file_path, destination_file_name
            )
        )
    except FileNotFoundError:
        print("The file either doesn't exist in the bucket or hasn't been specified")