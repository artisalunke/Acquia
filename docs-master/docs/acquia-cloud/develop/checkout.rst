.. include:: /common/global.rst

Checking out a local copy of your code
======================================

To begin developing your |acquia-product:ac| application, make a local
copy of the application code by checking it out from its
|acquia-product:ac| code repository. Start in the location on your local
computer where you want to create your repository.

Use the following Git command to clone the entire repository to your
local directory:

``git clone [code_repository]``

where ``[code_repository]`` is the URL of the |acquia-product:ac| code
repository.

You can obtain the repository URL from either the `|acquia-product:ac|
Environments page </acquia-cloud/manage/environments#info>`__, or by
using the following method to obtain the information from the
Application information panel:

#. `Sign in to the |acquia-product:ui| <https://cloud.acquia.com/>`__,
   and then select your application.
#. On the application's page, click the **Application Info** icon.

   |Click Application info to find the repository URL|

#. In the **Application Information** panel, the repository URL is the
   value in the **URL** field. Click the **Copy** icon to copy the URL
   to your clipboard.

After you check out a copy of your code, you can make changes in the
local code repository and then `commit your code changes back to the
remote code repository </acquia-cloud/develop/update>`__ on
|acquia-product:ac|.

.. |Click Application info to find the repository URL| image:: https://cdn2.webdamdb.com/1280_cQIWvZjTvMo6.png?1526476127
   :width: 750px
   :height: 360px
