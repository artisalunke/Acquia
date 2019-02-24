.. include:: /common/global.rst

Amazon S3 file management with |acquia-product:lpm|
===================================================

|acquia-product:lpm| uses Amazon S3 storage for several purposes,
including uploading import files to the |acquia-product:cha| service and
exporting visitor information. You can use the information on this page
to help you connect to your Amazon S3 bucket to manage your
|acquia-product:lpm|-related files.


Requirements
------------

Regardless of whether you are sending files to Amazon S3 or obtaining
previously stored files, be sure to plan for the following requirements:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Component
     - Requirement
   * - **File client**
     - Because of permission restrictions that prevent you from viewing the 
       contents of the main S3 bucket, we suggest that you use a client 
       specifically designed to access Amazon S3, such as `CloudBerry Explorer <https://www.cloudberrylab.com/explorer/amazon-s3.aspx>`__ , `Cyberduck <https://cyberduck.io/>`__ , or the `AWS Command Line Interface <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html>`__.
   * - **Amazon S3 bucket credentials**
     - Available in the Profile Manager interface on **Admin > Manage Customers** by clicking your customer name. |acquia-product:lpm| displays the Customer Details webpage, which contains the following fields:

       - **AWS Access Key ID**
       - **AWS Secret Access Key**
       - **S3 Bucket URL**

Your Amazon S3 folder path will appear similar to the following, based
on where your S3 bucket is located:

-  *US* – ``lift.prod.api-file.us-east-1//INBOX``
-  *Europe* – ``lift.prod.api-file.eu-central-1//INBOX``
-  *Australia* – ``lift.prod.api-file.ap-southeast-2//INBOX``

If the default ``INBOX`` directory does not exist, you must create it.


Uploading import files
----------------------

To upload one or more files to |acquia-product:lpm| using the Amazon S3
bucket associated with your account, complete the following steps:

#. Configure your Amazon S3 client, using the **AWS Access Key ID** and
   **AWS Secret Access Key** as credentials and the **S3 Bucket URL** as
   your path.
#. Connect to the Amazon S3 bucket provided by Acquia using a local
   computer client.
#. Upload the import file that you created to your Amazon S3 path. If
   you have several import files, you can upload all of the files at the
   same time.

|acquia-product:lpm| uploads the file and lists the file on the Bulk
File Management page.

After an import file is successfully uploaded, |acquia-product:lpm|
reads each file and then moves the file to the ``ARCHIVE`` path,
renaming the file in the process to include the date and time that the
file was moved. For example, if you name your upload file
``capture.csv`` and your S3 bucket is located in the US, the new
filename will be similar to the following:

.. code-block:: none

   lift.prod.api-file.us-east-1/[account_id]/ARCHIVE/capture.csv.2014-09-24-16-55

.. _retrieve:

Retrieving your export file
---------------------------

|acquia-product:lpm| saves completed export files to an Amazon S3
directory that is associated with your account. To download your export
file, complete the following steps:

#. Connect to the Amazon S3 directory provided by Acquia using a local
   computer client. For example, the S3 folder path will be similar to
   the following, based on where your S3 directory is located:

   -  US – ``lift.prod.api-file.us-east-1//OUTBOX``
   -  Europe – ``lift.prod.api-file.eu-central-1//OUTBOX``
   -  Australia – ``lift.prod.api-file.ap-southeast-2//OUTBOX``

   If you need assistance accessing your S3 directory, `contact Acquia
   Support </support#contact>`__.

   .. note::  

      Because of permission restrictions that prevent you from viewing the
      contents of the main S3 directory, we suggest that you use a client
      specifically designed to access Amazon S3, such as `CloudBerry
      Explorer <https://www.cloudberrylab.com/explorer/amazon-s3.aspx>`__
      or `Cyberduck <https://cyberduck.io/>`__.

#. Download the export file that you requested from your Amazon S3
   directory.

Each export file includes a separate file that includes the headers for
each column of field data in the export file. Header files have the same
names as their associated export files, with ``_header`` appended to
each file name. For example, exporting the event information from
|acquia-product:lpm| would create files with names similar to the
following:

-  ``event_2014-12-27_1.csv``
-  ``event_2014-12-27_1.csv_header``

.. note::  

   The Admin > Bulk File Management webpage does not display header files.


Examining the export file
-------------------------

To ensure that other applications are able to read the export file's
data correctly, |acquia-product:lpm| adds escape characters ( ``\`` ) to
the export file. The escape characters precede certain special
characters in the file, including the following:

-  *Pipe symbol ( \| )* – ``\|``
-  *Carriage return* – ``\n``
-  *Linefeed* – ``\r``

Using escape characters ensures that there is no confusion if these
special characters are included in the content of a field, such as
**Content Title**.


Viewing your S3 bucket's top-level information
----------------------------------------------

Some users may need to access the top level of their bucket to browse
the entire structure. To do this, you must use a very specific
structure, or you will be unable to view your data:

.. code-block:: none

   s3://lift.prod.api-file.eu-central-1/EXAMPLEINC/

Be aware that the S3 URL uses a trailing slash; URLs without the
trailing slash will not work, due to Amazon restrictions for user
security.


S3 bucket file storage policy
-----------------------------

Files in the ``INBOX``, ``ARCHIVE``, and ``OUTBOX`` directories created
more than 31 days ago will be deleted by |acquia-product:cha|.
